#!/usr/bin/env python3
'''Script holds various
    functions related to
    filtering and logging
    pii and pd'''
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''function returns a mysql connect
        object containing the environment
        variables of username, password, etc.'''
    # Obtain credentials from environment variables
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the MySQL database
    db = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )

    return db


def main():
    '''Function obtains a database connection
        using get_db func, then retrieves all
        rows in users table and display each
        row in a filtered format'''
    db = get_db()
    cursor = db.cursor()
    cursor.execute("select * from users;")

    PII_List = ['name=', 'email=', 'phone=',
                'ssn=', 'password=', 'ip=',
                'last_login=', 'user_agent=']
    for row in cursor:
        row_string = ''
        i = 0
        for column in row:
            row_string += PII_List[i] + str(column) + '; '
            i += 1
        log_record = logging.LogRecord("user_data", logging.INFO,
                                       None, None, row_string, None, None)
        # fields = []
        # for item in PII_FIELDS:
        #     fields.append(item)
        formatter = RedactingFormatter(PII_FIELDS)
        print(formatter.format(log_record))


main()
