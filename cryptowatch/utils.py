import os
import logging


cw_logger = logging.getLogger("cryptowatch")

cw_handler = logging.StreamHandler()
cw_handler.setLevel(logging.INFO)

cw_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
cw_handler.setFormatter(cw_format)

cw_logger.addHandler(cw_handler)


def log(msg, is_warning=False, is_error=False, is_debug=False):
    if is_debug:
        cw_logger.debug(msg)
    elif is_error:
        cw_logger.error(msg)
    elif is_warning:
        cw_logger.warning(msg)
    else:
        cw_logger.info(msg)


def translate_periods(periods):

    mapping = {
        "1m": "60",
        "3m": "180",
        "5m": "300",
        "15m": "900",
        "30m": "1800",
        "1h": "3600",
        "2h": "7200",
        "4h": "14400",
        "6h": "21600",
        "12h": "43200",
        "1d": "86400",
        "3d": "259200",
        "1w": "604800",
    }
    sec_periods = []
    for p in periods:
        sec_periods.append(mapping.get(str(p).lower()))
    return sec_periods
