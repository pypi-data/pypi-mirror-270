###############################################################################
#
# (C) Copyright 2023 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
from everysk.core.fields import ListField, DictField

## HTTP Settings
HTTP_SUCCESS_STATUS_CODES = ListField(default=[200, 201, 202, 303], readonly=True)
HTTP_DEFAULT_HEADERS = DictField(
    default={
        'Accept-Encoding': 'gzip, deflate;q=0.9',
        'Accept-Language': 'en-US, en;q=0.9, pt-BR;q=0.8, pt;q=0.7',
        'Cache-control': 'no-cache',
        'Connection': 'close', # Remove on HTTP/2 requests
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    },
    readonly=True
)
