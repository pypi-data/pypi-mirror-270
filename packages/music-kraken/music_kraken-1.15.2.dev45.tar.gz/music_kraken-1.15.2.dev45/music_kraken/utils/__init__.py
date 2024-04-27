from datetime import datetime
from pathlib import Path
import json
import logging
import inspect

from .shared import DEBUG, DEBUG_LOGGING, DEBUG_DUMP, DEBUG_TRACE, DEBUG_OBJECT_TRACE, DEBUG_OBJECT_TRACE_CALLSTACK
from .config import config, read_config, write_config
from .enums.colors import BColors
from .path_manager import LOCATIONS

"""
IO functions
"""

def _apply_color(msg: str, color: BColors) -> str:
    if color is BColors.ENDC:
        return msg
    return color.value + msg + BColors.ENDC.value


def output(msg: str, color: BColors = BColors.ENDC):
    print(_apply_color(msg, color))


def user_input(msg: str, color: BColors = BColors.ENDC):
    return input(_apply_color(msg, color)).strip()


def dump_to_file(file_name: str, payload: str, is_json: bool = False, exit_after_dump: bool = False):
    if not DEBUG_DUMP:
        return

    path = Path(LOCATIONS.TEMP_DIRECTORY, file_name)
    logging.warning(f"dumping {file_name} to: \"{path}\"")

    if is_json and isinstance(payload, str):
        payload = json.loads(payload)

    if isinstance(payload, dict):
        payload = json.dumps(payload, indent=4)

    with path.open("w") as f:
        f.write(payload)

    if exit_after_dump:
        exit()


def trace(msg: str):
    if not DEBUG_TRACE:
        return

    output(BColors.OKBLUE.value + "trace: " + BColors.ENDC.value + msg)

def request_trace(msg: str):
    if not DEBUG_TRACE:
        return

    output(BColors.OKGREEN.value + "request: " + BColors.ENDC.value + msg)

def object_trace(obj):
    if not DEBUG_OBJECT_TRACE:
        return

    appendix =  f" called by [{' | '.join(f'{s.function} {Path(s.filename).name}:{str(s.lineno)}' for s in inspect.stack()[1:5])}]" if DEBUG_OBJECT_TRACE_CALLSTACK else ""
    output("object: " + str(obj) + appendix)


"""
misc functions
"""

def get_current_millis() -> int:
    dt = datetime.now()
    return int(dt.microsecond / 1_000)


def get_unix_time() -> int:
    return int(datetime.now().timestamp())