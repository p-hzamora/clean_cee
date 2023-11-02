# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: sqlite3\dbapi2.pyc
# Compiled at: 2011-03-08 09:43:22
import datetime, time
from _sqlite3 import *
paramstyle = 'qmark'
threadsafety = 1
apilevel = '2.0'
Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime

def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])


def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])


def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])


version_info = tuple([ int(x) for x in version.split('.') ])
sqlite_version_info = tuple([ int(x) for x in sqlite_version.split('.') ])
Binary = buffer

def register_adapters_and_converters():

    def adapt_date(val):
        return val.isoformat()

    def adapt_datetime(val):
        return val.isoformat(' ')

    def convert_date(val):
        return datetime.date(*map(int, val.split('-')))

    def convert_timestamp(val):
        datepart, timepart = val.split(' ')
        year, month, day = map(int, datepart.split('-'))
        timepart_full = timepart.split('.')
        hours, minutes, seconds = map(int, timepart_full[0].split(':'))
        if len(timepart_full) == 2:
            microseconds = int(timepart_full[1])
        else:
            microseconds = 0
        val = datetime.datetime(year, month, day, hours, minutes, seconds, microseconds)
        return val

    register_adapter(datetime.date, adapt_date)
    register_adapter(datetime.datetime, adapt_datetime)
    register_converter('date', convert_date)
    register_converter('timestamp', convert_timestamp)


register_adapters_and_converters()
del register_adapters_and_converters