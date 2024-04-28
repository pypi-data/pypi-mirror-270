"""Script containing configurations for the openadapt application.

Usage:

    from openadapt import config
    ...
    config.<setting>
    ...

"""

import multiprocessing
import os
import pathlib
import shutil

from dotenv import load_dotenv
from loguru import logger
import git
import sentry_sdk

_DEFAULTS = {
    "GOOGLE_API_KEY": "<set in .env>",
    "SOM_SERVER_URL": "<set in .env>",
    "REPLICATE_API_TOKEN": "<set your api key in .env>",
    "DEFAULT_ADAPTER": (
        "openai",
        "anthropic",
        "google",
    )[0],
    "DEFAULT_SEGMENTATION_ADAPTER": ("som", "replicate", "ultralytics")[-1],
    "ANTHROPIC_API_KEY": "<set your api key in .env>",
    "CACHE_DIR_PATH": ".cache",
    "CACHE_ENABLED": True,
    "CACHE_VERBOSITY": 0,
    "DB_ECHO": False,
    "DB_FNAME": "openadapt.db",
    "ERROR_REPORTING_ENABLED": True,
    "ERROR_REPORTING_DSN": (
        "https://dcf5d7889a3b4b47ae12a3af9ffcbeb7@app.glitchtip.com/3798"
    ),
    "ERROR_REPORTING_BRANCH": "main",
    "OPENAI_API_KEY": "<set your api key in .env>",
    # "OPENAI_MODEL_NAME": "gpt-4",
    "OPENAI_MODEL_NAME": "gpt-3.5-turbo",
    "RECORD_WINDOW_DATA": False,
    # may incur significant performance penalty
    "RECORD_READ_ACTIVE_ELEMENT_STATE": False,
    # TODO: remove?
    "REPLAY_STRIP_ELEMENT_STATE": True,
    # IGNORES WARNINGS (PICKLING, ETC.)
    # TODO: ignore warnings by default on GUI
    "IGNORE_WARNINGS": False,
    "MAX_NUM_WARNINGS_PER_SECOND": 5,
    "WARNING_SUPPRESSION_PERIOD": 1,
    "MESSAGES_TO_FILTER": ["Cannot pickle Objective-C objects"],
    # ACTION EVENT CONFIGURATIONS
    "ACTION_TEXT_SEP": "-",
    "ACTION_TEXT_NAME_PREFIX": "<",
    "ACTION_TEXT_NAME_SUFFIX": ">",
    # PERFORMANCE PLOTTING CONFIGURATION
    "PLOT_PERFORMANCE": True,
    # CAPTURE CONFIGURATION
    "CAPTURE_DIR_PATH": "captures",
    # APP CONFIGURATIONS
    "APP_DARK_MODE": False,
    # SCRUBBING CONFIGURATIONS
    "SCRUB_ENABLED": False,
    "SCRUB_CHAR": "*",
    "SCRUB_LANGUAGE": "en",
    # TODO support lists in getenv_fallback
    "SCRUB_FILL_COLOR": 0x0000FF,  # BGR format
    "SCRUB_CONFIG_TRF": {
        "nlp_engine_name": "spacy",
        "models": [{"lang_code": "en", "model_name": "en_core_web_trf"}],
    },
    "SCRUB_PRESIDIO_IGNORE_ENTITIES": [
        # 'US_PASSPORT',
        # 'US_DRIVER_LICENSE',
        # 'CRYPTO',
        # 'UK_NHS',
        # 'PERSON',
        # 'CREDIT_CARD',
        # 'US_BANK_NUMBER',
        # 'PHONE_NUMBER',
        # 'US_ITIN',
        # 'AU_ABN',
        # 'DATE_TIME',
        # 'NRP',
        # 'SG_NRIC_FIN',
        # 'AU_ACN',
        # 'IP_ADDRESS',
        # 'EMAIL_ADDRESS',
        # 'URL',
        # 'IBAN_CODE',
        # 'AU_TFN',
        # 'LOCATION',
        # 'AU_MEDICARE',
        # 'US_SSN',
        # 'MEDICAL_LICENSE'
    ],
    "SCRUB_KEYS_HTML": [
        "text",
        "canonical_text",
        "title",
        "state",
        "task_description",
        "key_char",
        "canonical_key_char",
        "key_vk",
        "children",
    ],
    # VISUALIZATION CONFIGURATIONS
    "VISUALIZE_DARK_MODE": False,
    "VISUALIZE_RUN_NATIVELY": True,
    "VISUALIZE_DENSE_TREES": True,
    "VISUALIZE_ANIMATIONS": True,
    "VISUALIZE_EXPAND_ALL": False,  # not recommended for large trees
    "VISUALIZE_MAX_TABLE_CHILDREN": 10,
    # Calculate and save the difference between 2 neighboring screenshots
    "SAVE_SCREENSHOT_DIFF": False,
    "SPACY_MODEL_NAME": "en_core_web_trf",
    "PRIVATE_AI_API_KEY": "<set your api key in .env>",
    "RECORD_VIDEO": False,
    "RECORD_IMAGES": True,
    "VIDEO_PIXEL_FORMAT": "rgb24",
    "DASHBOARD_CLIENT_PORT": 3000,
    "DASHBOARD_SERVER_PORT": 8000,
}

# each string in STOP_STRS should only contain strings
# that don't contain special characters
STOP_STRS = [
    "oa.stop",
    # TODO:
    # "<ctrl>+c,<ctrl>+c,<ctrl>+c"
]
# each list in SPECIAL_CHAR_STOP_SEQUENCES should contain sequences
# containing special chars, separated by keys
SPECIAL_CHAR_STOP_SEQUENCES = [["ctrl", "ctrl", "ctrl"]]
# sequences that when typed, will stop the recording of ActionEvents in record.py
STOP_SEQUENCES = [
    list(stop_str) for stop_str in STOP_STRS
] + SPECIAL_CHAR_STOP_SEQUENCES

ENV_FILE_PATH = pathlib.Path(__file__).parent.parent / ".env"
ENV_EXAMPLE_FILE_PATH = pathlib.Path(__file__).parent.parent / ".env.example"

# Create .env file if it doesn't exist
if not os.path.isfile(ENV_FILE_PATH):
    shutil.copy(ENV_EXAMPLE_FILE_PATH, ENV_FILE_PATH)


def getenv_fallback(var_name: str) -> str:
    """Get the value of an environment variable or fallback to the default value.

    Args:
        var_name (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable or the default value if not found.

    Raises:
        ValueError: If the environment variable is not defined.
    """
    rval = os.getenv(var_name) or _DEFAULTS.get(var_name)
    if type(rval) is str and rval.lower() in (
        "true",
        "false",
        "1",
        "0",
    ):
        rval = rval.lower() == "true" or rval == "1"
    if type(rval) is str and rval.isnumeric():
        rval = int(rval)
    if rval is None:
        raise ValueError(f"{var_name=} not defined")
    return rval


def persist_env(var_name: str, val: str, env_file_path: str = ENV_FILE_PATH) -> None:
    """Persist an environment variable to a .env file.

    Args:
        var_name (str): The name of the environment variable.
        val (str): The value of the environment variable.
        env_file_path (str, optional): The path to the .env file (default: ".env").
    """
    if not os.path.exists(env_file_path):
        with open(env_file_path, "w") as f:
            f.write(f"{var_name}={val}")
    else:
        # find and replace
        with open(env_file_path, "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(f"{var_name}="):
                lines[i] = f"{var_name}={val}\n"
                break
        else:
            # we didn't find the variable in the file, so append it
            if lines[-1][-1] != "\n":
                lines.append("\n")
            lines.append(f"{var_name}={val}")
        with open(env_file_path, "w") as f:
            f.writelines(lines)


load_dotenv()

for key in _DEFAULTS:
    val = getenv_fallback(key)
    locals()[key] = val

ROOT_DIRPATH = pathlib.Path(__file__).parent.parent.resolve()
DATA_DIRECTORY_PATH = ROOT_DIRPATH / "data"
RECORDING_DIRECTORY_PATH = DATA_DIRECTORY_PATH / "recordings"
# TODO: clarify why this is necessary (see share.py)
if DB_FNAME == "openadapt.db":  # noqa
    DB_FPATH = ROOT_DIRPATH / DB_FNAME  # noqa
else:
    DB_FPATH = RECORDING_DIRECTORY_PATH / DB_FNAME  # noqa
DB_URL = f"sqlite:///{DB_FPATH}"
DIRNAME_PERFORMANCE_PLOTS = "performance"


def set_db_url(db_fname: str) -> None:
    """Set the database URL based on the given database file name.

    Args:
        db_fname (str): The database file name.
    """
    # TODO: pass these in as parameters, whose default values are the globals
    global DB_FNAME, DB_FPATH, DB_URL
    DB_FNAME = db_fname
    if DB_FNAME == "openadapt.db":  # noqa
        DB_FPATH = ROOT_DIRPATH / DB_FNAME  # noqa
    else:
        DB_FPATH = RECORDING_DIRECTORY_PATH / DB_FNAME  # noqa
    DB_URL = f"sqlite:///{DB_FPATH}"
    logger.info(f"{DB_URL=}")


def obfuscate(val: str, pct_reveal: float = 0.1, char: str = "*") -> str:
    """Obfuscates a value by replacing a portion of characters.

    Args:
        val (str): The value to obfuscate.
        pct_reveal (float, optional): Percentage of characters to reveal (default: 0.1).
        char (str, optional): Obfuscation character (default: "*").

    Returns:
        str: Obfuscated value with a portion of characters replaced.

    Raises:
        AssertionError: If length of obfuscated value does not match original value.
    """
    num_reveal = int(len(val) * pct_reveal)
    num_obfuscate = len(val) - num_reveal
    obfuscated = char * num_obfuscate
    revealed = val[-num_reveal:]
    rval = f"{obfuscated}{revealed}"
    assert len(rval) == len(val), (val, rval)
    return rval


_OBFUSCATE_KEY_PARTS = ("KEY", "PASSWORD", "TOKEN")
if multiprocessing.current_process().name == "MainProcess":
    for key, val in dict(locals()).items():
        if not key.startswith("_") and key.isupper():
            parts = key.split("_")
            if (
                any([part in parts for part in _OBFUSCATE_KEY_PARTS])
                and val != _DEFAULTS[key]
            ):
                val = obfuscate(val)
            logger.info(f"{key}={val}")

    if ERROR_REPORTING_ENABLED:  # type: ignore # noqa
        active_branch_name = git.Repo(ROOT_DIRPATH).active_branch.name
        logger.info(f"{active_branch_name=}")
        is_reporting_branch = active_branch_name == ERROR_REPORTING_BRANCH  # type: ignore # noqa
        logger.info(f"{is_reporting_branch=}")
        if is_reporting_branch:
            sentry_sdk.init(
                dsn=ERROR_REPORTING_DSN,  # type: ignore # noqa
                traces_sample_rate=1.0,
            )
