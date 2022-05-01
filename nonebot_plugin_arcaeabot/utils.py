from ._RHelper import RHelper
from .config import config

root = RHelper()

error_code = {
    "-1": "invalid username or usercode",
    "-2": "invalid usercode",
    "-3": "user not found",
    "-4": "too many users",
    "-5": "invalid songname or songid",
    "-6": "invalid songid",
    "-7": "song not recorded",
    "-8": "too many records",
    "-9": "invalid difficulty",
    "-10": "invalid recent/overflow number",
    "-11": "allocate an arc account failed",
    "-12": "clear friend failed",
    "-13": "add friend failed",
    "-14": "this song has no beyond level",
    "-15": "not played yet",
    "-16": "user got shadowbanned",
    "-17": "querying best30 failed",
    "-18": "update service unavailable",
    "-19": "invalid partner",
    "-20": "file unavailable",
    "-21": "invalid range",
    "-22": "range of rating end smaller than its start",
    "-23": "potential is below the threshold of querying best30 (7.0)",
    "-24": "need to update arcaea, please contact maintainer",
    "-233": "internal error occurred",
}


def is_error(mode: str = "basic") -> bool:
    em = config.get_config("error_message").lower()
    m = config.get_config("more_error_message").lower()
    if em == "true":
        if m == "false" and mode == "more":
            return False
        else:
            return True
    else:
        return False


def is_float_num(str):
    s = str.split('.')
    if len(s) != 2:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
        return True
