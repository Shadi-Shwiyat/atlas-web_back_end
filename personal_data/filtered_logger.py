#!/usr/bin/env python3
'''Script holds various
    functions related to
    filtering and logging
    pii and pd'''
from typing import List
import re
import logging

PII_FIELDS = ('phone', 'password', 'email', 'ssn', 'name')


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


def get_logger() -> logging.Logger:
    '''Function returns a
        logging.logger object named
        user_data and only logs up to
        logging.INFO level'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
