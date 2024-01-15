#!/usr/bin/env python3
'''Script is a function that
    returns an obfuscated
    log statement'''
from typing import List
import re
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''method filters values of incoming log
            records using parent class .format
            method'''
        log_message = super().format(record)
        # print(log_message)
        result = filter_datum(self.fields, self.REDACTION,
                              log_message, self.SEPARATOR)
        return(result)
