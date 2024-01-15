#!/usr/bin/env python3
'''Script is a function that
    returns an obfuscated
    log statement'''
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Function returns a string as
        a representation of log data, in
        which certian fields(which are
        passed in) are obfuscated with
        the redaction(also passed in)'''
    for field in fields:
        pattern = re.compile(rf'({field}=).*?{separator}')
        replacement = rf'\1{redaction}{separator}'
        message = re.sub(pattern, replacement, message)
    return(message)
