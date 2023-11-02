# File: p (Python 2.7)

__doc__ = '\nCopyright (c) 2003-2007  Gustavo Niemeyer <gustavo@niemeyer.net>\n\nThis module offers extensions to the standard python 2.3+\ndatetime module.\n'
__author__ = 'Gustavo Niemeyer <gustavo@niemeyer.net>'
__license__ = 'PSF License'
import datetime
import string
import time
import sys
import os

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import relativedelta
import tz
__all__ = [
    'parse',
    'parserinfo']

class _timelex(object):
    
    def __init__(self, instream):
        if isinstance(instream, basestring):
            instream = StringIO(instream)
        self.instream = instream
        self.wordchars = 'abcdfeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdc\xdd\xde'
        self.numchars = '0123456789'
        self.whitespace = ' \t\r\n'
        self.charstack = []
        self.tokenstack = []
        self.eof = False

    
    def get_token(self):
        if self.tokenstack:
            return self.tokenstack.pop(0)
        seenletters = None
        token = None
        state = None
        wordchars = self.wordchars
        numchars = self.numchars
        whitespace = self.whitespace
        while not self.eof:
            if self.charstack:
                nextchar = self.charstack.pop(0)
            else:
                nextchar = self.instream.read(1)
                while nextchar == '\x0':
                    nextchar = self.instream.read(1)
            if not nextchar:
                self.eof = True
                break
                continue
            if not state:
                token = nextchar
                if nextchar in wordchars:
                    state = 'a'
                elif nextchar in numchars:
                    state = '0'
                elif nextchar in whitespace:
                    token = ' '
                    break
                else:
                    break
            if state == 'a':
                seenletters = True
                if nextchar in wordchars:
                    token += nextchar
                elif nextchar == '.':
                    token += nextchar
                    state = 'a.'
                else:
                    self.charstack.append(nextchar)
                    break
            if state == '0':
                if nextchar in numchars:
                    token += nextchar
                elif nextchar == '.':
                    token += nextchar
                    state = '0.'
                else:
                    self.charstack.append(nextchar)
                    break
            if state == 'a.':
                seenletters = True
                if nextchar == '.' or nextchar in wordchars:
                    token += nextchar
                elif nextchar in numchars and token[-1] == '.':
                    token += nextchar
                    state = '0.'
                else:
                    self.charstack.append(nextchar)
                    break
            if state == '0.' or nextchar == '.' or nextchar in numchars:
                token += nextchar
            elif nextchar in wordchars and token[-1] == '.':
                token += nextchar
                state = 'a.'
            else:
                self.charstack.append(nextchar)
                break
        if state in ('a.', '0.'):
            if seenletters and token.count('.') > 1 or token[-1] == '.':
                l = token.split('.')
                token = l[0]
                for tok in l[1:]:
                    self.tokenstack.append('.')
                    if tok:
                        self.tokenstack.append(tok)
                        continue
        return token

    
    def __iter__(self):
        return self

    
    def next(self):
        token = self.get_token()
        if token is None:
            raise StopIteration
        return token

    
    def split(cls, s):
        return list(cls(s))

    split = classmethod(split)


class _resultbase(object):
    
    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, None)
        

    
    def _repr(self, classname):
        l = []
        for attr in self.__slots__:
            value = getattr(self, attr)
            if value is not None:
                l.append('%s=%s' % (attr, `value`))
                continue
        return '%s(%s)' % (classname, ', '.join(l))

    
    def __repr__(self):
        return self._repr(self.__class__.__name__)



class parserinfo(object):
    JUMP = [
        ' ',
        '.',
        ',',
        ';',
        '-',
        '/',
        "'",
        'at',
        'on',
        'and',
        'ad',
        'm',
        't',
        'of',
        'st',
        'nd',
        'rd',
        'th']
    WEEKDAYS = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')]
    MONTHS = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sep', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December')]
    HMS = [
        ('h', 'hour', 'hours'),
        ('m', 'minute', 'minutes'),
        ('s', 'second', 'seconds')]
    AMPM = [
        ('am', 'a'),
        ('pm', 'p')]
    UTCZONE = [
        'UTC',
        'GMT',
        'Z']
    PERTAIN = [
        'of']
    TZOFFSET = { }
    
    def __init__(self, dayfirst = False, yearfirst = False):
        self._jump = self._convert(self.JUMP)
        self._weekdays = self._convert(self.WEEKDAYS)
        self._months = self._convert(self.MONTHS)
        self._hms = self._convert(self.HMS)
        self._ampm = self._convert(self.AMPM)
        self._utczone = self._convert(self.UTCZONE)
        self._pertain = self._convert(self.PERTAIN)
        self.dayfirst = dayfirst
        self.yearfirst = yearfirst
        self._year = time.localtime().tm_year
        self._century = (self._year // 100) * 100

    
    def _convert(self, lst):
        dct = { }
        for i in range(len(lst)):
            v = lst[i]
            if isinstance(v, tuple):
                for v in v:
                    dct[v.lower()] = i
                
            dct[v.lower()] = i
        
        return dct

    
    def jump(self, name):
        return name.lower() in self._jump

    
    def weekday(self, name):
        if len(name) >= 3:
            
            try:
                return self._weekdays[name.lower()]
            except KeyError:
                pass
            


    
    def month(self, name):
        if len(name) >= 3:
            
            try:
                return self._months[name.lower()] + 1
            except KeyError:
                pass
            


    
    def hms(self, name):
        
        try:
            return self._hms[name.lower()]
        except KeyError:
            return None


    
    def ampm(self, name):
        
        try:
            return self._ampm[name.lower()]
        except KeyError:
            return None


    
    def pertain(self, name):
        return name.lower() in self._pertain

    
    def utczone(self, name):
        return name.lower() in self._utczone

    
    def tzoffset(self, name):
        if name in self._utczone:
            return 0
        return None.TZOFFSET.get(name)

    
    def convertyear(self, year):
        if year < 100:
            year += self._century
            if abs(year - self._year) >= 50:
                if year < self._year:
                    year += 100
                else:
                    year -= 100
            
        return year

    
    def validate(self, res):
        if res.year is not None:
            res.year = self.convertyear(res.year)
        if res.tzoffset == 0 or not (res.tzname) or res.tzname == 'Z':
            res.tzname = 'UTC'
            res.tzoffset = 0
        elif res.tzoffset != 0 and res.tzname and self.utczone(res.tzname):
            res.tzoffset = 0
        return True



class parser(object):
    
    def __init__(self, info = None):
        if not info:
            pass
        self.info = parserinfo()

    
    def parse(self, timestr, default = None, ignoretz = False, tzinfos = None, **kwargs):
        if not default:
            default = datetime.datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
        res = self._parse(timestr, **None)
        if res is None:
            raise ValueError, 'unknown string format'
        repl = { }
        for attr in [
            'year',
            'month',
            'day',
            'hour',
            'minute',
            'second',
            'microsecond']:
            value = getattr(res, attr)
            if value is not None:
                repl[attr] = value
                continue
        ret = default.replace(**None)
        if res.weekday is not None and not (res.day):
            ret = ret + relativedelta.relativedelta(weekday = res.weekday)
        if not ignoretz:
            if (callable(tzinfos) or tzinfos) and res.tzname in tzinfos:
                if callable(tzinfos):
                    tzdata = tzinfos(res.tzname, res.tzoffset)
                else:
                    tzdata = tzinfos.get(res.tzname)
                if isinstance(tzdata, datetime.tzinfo):
                    tzinfo = tzdata
                elif isinstance(tzdata, basestring):
                    tzinfo = tz.tzstr(tzdata)
                elif isinstance(tzdata, int):
                    tzinfo = tz.tzoffset(res.tzname, tzdata)
                else:
                    raise ValueError, 'offset must be tzinfo subclass, tz string, or int offset'
                ret = None.replace(tzinfo = tzinfo)
            elif res.tzname and res.tzname in time.tzname:
                ret = ret.replace(tzinfo = tz.tzlocal())
            elif res.tzoffset == 0:
                ret = ret.replace(tzinfo = tz.tzutc())
            elif res.tzoffset:
                ret = ret.replace(tzinfo = tz.tzoffset(res.tzname, res.tzoffset))
            
        return ret

    
    class _result(_resultbase):
        __slots__ = [
            'year',
            'month',
            'day',
            'weekday',
            'hour',
            'minute',
            'second',
            'microsecond',
            'tzname',
            'tzoffset']

    
    def _parse(self, timestr, dayfirst = None, yearfirst = None, fuzzy = False):
        info = self.info
        if dayfirst is None:
            dayfirst = info.dayfirst
        if yearfirst is None:
            yearfirst = info.yearfirst
        res = self._result()
        l = _timelex.split(timestr)
        
        try:
            ymd = []
            mstridx = -1
            len_l = len(l)
            i = 0
            while i < len_l:
                
                try:
                    value_repr = l[i]
                    value = float(value_repr)
                except ValueError:
                    value = None

                if value is not None:
                    len_li = len(l[i])
                    i += 1
                    if len(ymd) == 3 and len_li in (2, 4):
                        if (i >= len_l or l[i] != ':') and info.hms(l[i]) is None:
                            s = l[i - 1]
                            res.hour = int(s[:2])
                            if len_li == 4:
                                res.minute = int(s[2:])
                            
                    if (len_li == 6 or len_li > 6) and l[i - 1].find('.') == 6:
                        s = l[i - 1]
                        if not ymd and l[i - 1].find('.') == -1:
                            ymd.append(info.convertyear(int(s[:2])))
                            ymd.append(int(s[2:4]))
                            ymd.append(int(s[4:]))
                        else:
                            res.hour = int(s[:2])
                            res.minute = int(s[2:4])
                            (res.second, res.microsecond) = _parsems(s[4:])
                    if len_li == 8:
                        s = l[i - 1]
                        ymd.append(int(s[:4]))
                        ymd.append(int(s[4:6]))
                        ymd.append(int(s[6:]))
                        continue
                    if len_li in (12, 14):
                        s = l[i - 1]
                        ymd.append(int(s[:4]))
                        ymd.append(int(s[4:6]))
                        ymd.append(int(s[6:8]))
                        res.hour = int(s[8:10])
                        res.minute = int(s[10:12])
                        if len_li == 14:
                            res.second = int(s[12:])
                        
                    if (i < len_l or info.hms(l[i]) is not None or i + 1 < len_l) and l[i] == ' ' and info.hms(l[i + 1]) is not None:
                        if l[i] == ' ':
                            i += 1
                        idx = info.hms(l[i])
                        while True:
                            if idx == 0:
                                res.hour = int(value)
                                if value % 1:
                                    res.minute = int(60 * (value % 1))
                                
                            elif idx == 1:
                                res.minute = int(value)
                                if value % 1:
                                    res.second = int(60 * (value % 1))
                                
                            elif idx == 2:
                                (res.second, res.microsecond) = _parsems(value_repr)
                            i += 1
                            if i >= len_l or idx == 2:
                                break
                            
                            try:
                                value_repr = l[i]
                                value = float(value_repr)
                            except ValueError:
                                break
                                continue

                            i += 1
                            idx += 1
                            if i < len_l:
                                newidx = info.hms(l[i])
                                if newidx is not None:
                                    idx = newidx
                                
                            continue
                            if i + 1 < len_l and l[i] == ':':
                                res.hour = int(value)
                                i += 1
                                value = float(l[i])
                                res.minute = int(value)
                                if value % 1:
                                    res.second = int(60 * (value % 1))
                                i += 1
                                if i < len_l and l[i] == ':':
                                    (res.second, res.microsecond) = _parsems(l[i + 1])
                                    i += 2
                                
                    if i < len_l and l[i] in ('-', '/', '.'):
                        sep = l[i]
                        ymd.append(int(value))
                        i += 1
                        if i < len_l and not info.jump(l[i]):
                            
                            try:
                                ymd.append(int(l[i]))
                            except ValueError:
                                value = info.month(l[i])
                                if value is not None:
                                    ymd.append(value)
                                    if not mstridx == -1:
                                        raise AssertionError
                                    mstridx = None(ymd) - 1
                                else:
                                    return None

                            i += 1
                            if i < len_l and l[i] == sep:
                                i += 1
                                value = info.month(l[i])
                                if value is not None:
                                    ymd.append(value)
                                    mstridx = len(ymd) - 1
                                    if not mstridx == -1:
                                        raise AssertionError
                                ymd.append(int(l[i]))
                                i += 1
                            
                        
                    if i >= len_l or info.jump(l[i]):
                        if i + 1 < len_l and info.ampm(l[i + 1]) is not None:
                            res.hour = int(value)
                            if res.hour < 12 and info.ampm(l[i + 1]) == 1:
                                res.hour += 12
                            elif res.hour == 12 and info.ampm(l[i + 1]) == 0:
                                res.hour = 0
                            i += 1
                        else:
                            ymd.append(int(value))
                        i += 1
                        continue
                    if info.ampm(l[i]) is not None:
                        res.hour = int(value)
                        if res.hour < 12 and info.ampm(l[i]) == 1:
                            res.hour += 12
                        elif res.hour == 12 and info.ampm(l[i]) == 0:
                            res.hour = 0
                        i += 1
                        continue
                    if not fuzzy:
                        return None
                    None += 1
                    continue
                value = info.weekday(l[i])
                if value is not None:
                    res.weekday = value
                    i += 1
                    continue
                value = info.month(l[i])
                if value is not None:
                    ymd.append(value)
                    if not mstridx == -1:
                        raise AssertionError
                    mstridx = None(ymd) - 1
                    i += 1
                    if i < len_l or l[i] in ('-', '/'):
                        sep = l[i]
                        i += 1
                        ymd.append(int(l[i]))
                        i += 1
                        if i < len_l and l[i] == sep:
                            i += 1
                            ymd.append(int(l[i]))
                            i += 1
                        
                    elif i + 3 < len_l:
                        if l[i] == l[i + 2]:
                            pass
                        l[i + 2] == ' '
                        if 1 and info.pertain(l[i + 1]):
                            
                            try:
                                value = int(l[i + 3])
                            except ValueError:
                                pass

                            ymd.append(info.convertyear(value))
                            i += 4
                        
                    continue
                value = info.ampm(l[i])
                if value is not None:
                    if value == 1 and res.hour < 12:
                        res.hour += 12
                    elif value == 0 and res.hour == 12:
                        res.hour = 0
                    i += 1
                    continue
                if res.hour is not None and len(l[i]) <= 5 and res.tzname is None and res.tzoffset is None:
                    for x in l[i]:
                        if x not in string.ascii_uppercase:
                            continue
                            if not [][x]:
                                res.tzname = l[i]
                                res.tzoffset = info.tzoffset(res.tzname)
                                i += 1
                                if i < len_l and l[i] in ('+', '-'):
                                    l[i] = ('+', '-')[l[i] == '+']
                                    res.tzoffset = None
                                    if info.utczone(res.tzname):
                                        res.tzname = None
                                    
                                    continue
                if res.hour is not None and l[i] in ('+', '-'):
                    signal = (-1, 1)[l[i] == '+']
                    i += 1
                    len_li = len(l[i])
                    if len_li == 4:
                        res.tzoffset = int(l[i][:2]) * 3600 + int(l[i][2:]) * 60
                    elif i + 1 < len_l and l[i + 1] == ':':
                        res.tzoffset = int(l[i]) * 3600 + int(l[i + 2]) * 60
                        i += 2
                    elif len_li <= 2:
                        res.tzoffset = int(l[i][:2]) * 3600
                    else:
                        return None
                    [] += 1
                    res.tzoffset *= signal
                    if i + 3 < len_l and info.jump(l[i]) and l[i + 1] == '(' and l[i + 3] == ')' or 3 <= len(l[i + 2]):
                        pass
                    len(l[i + 2]) <= 5
                    if 1:
                        for x in l[i + 2]:
                            if x not in string.ascii_uppercase:
                                continue
                                if not [][x]:
                                    res.tzname = l[i + 2]
                                    i += 4
                                    continue
                                    continue
                                if not info.jump(l[i]) or fuzzy:
                                    return None
                                [] += 1
                            len_ymd = len(ymd)
                            if len_ymd > 3:
                                return None
                            if ([] == 1 or mstridx != -1) and len_ymd == 2:
                                if mstridx != -1:
                                    res.month = ymd[mstridx]
                                    del ymd[mstridx]
                                if len_ymd > 1 or mstridx == -1:
                                    if ymd[0] > 31:
                                        res.year = ymd[0]
                                    else:
                                        res.day = ymd[0]
                                
                            elif len_ymd == 2:
                                if ymd[0] > 31:
                                    (res.year, res.month) = ymd
                                elif ymd[1] > 31:
                                    (res.month, res.year) = ymd
                                elif dayfirst and ymd[1] <= 12:
                                    (res.day, res.month) = ymd
                                else:
                                    (res.month, res.day) = ymd
                            if len_ymd == 3:
                                if mstridx == 0:
                                    (res.month, res.day, res.year) = ymd
                                elif mstridx == 1:
                                    if (ymd[0] > 31 or yearfirst) and ymd[2] <= 31:
                                        (res.year, res.month, res.day) = ymd
                                    else:
                                        (res.day, res.month, res.year) = ymd
                                elif mstridx == 2:
                                    if ymd[1] > 31:
                                        (res.day, res.year, res.month) = ymd
                                    else:
                                        (res.year, res.day, res.month) = ymd
                                elif (ymd[0] > 31 or yearfirst) and ymd[1] <= 12 and ymd[2] <= 31:
                                    (res.year, res.month, res.day) = ymd
                                elif (ymd[0] > 12 or dayfirst) and ymd[1] <= 12:
                                    (res.day, res.month, res.year) = ymd
                                else:
                                    (res.month, res.day, res.year) = ymd
                    else:
                        except (IndexError, ValueError, AssertionError):
                            return None

        if not info.validate(res):
            return None


DEFAULTPARSER = parser()

def parse(timestr, parserinfo = None, **kwargs):
    if parserinfo:
        return parser(parserinfo).parse(timestr, **None)
    return None.parse(timestr, **None)


class _tzparser(object):
    
    class _result(_resultbase):
        __slots__ = [
            'stdabbr',
            'stdoffset',
            'dstabbr',
            'dstoffset',
            'start',
            'end']
        
        class _attr(_resultbase):
            __slots__ = [
                'month',
                'week',
                'weekday',
                'yday',
                'jyday',
                'day',
                'time']

        
        def __repr__(self):
            return self._repr('')

        
        def __init__(self):
            _resultbase.__init__(self)
            self.start = self._attr()
            self.end = self._attr()


    
    def parse(self, tzstr):
        res = self._result()
        l = _timelex.split(tzstr)
        
        try:
            len_l = len(l)
            i = 0
            while i < len_l:
                j = i
                for x in l[j]:
                    if x in '0123456789:,-+':
                        continue
                        if not [][x]:
                            j += 1
                        if j != i:
                            if not res.stdabbr:
                                offattr = 'stdoffset'
                                res.stdabbr = ''.join(l[i:j])
                            else:
                                offattr = 'dstoffset'
                                res.dstabbr = ''.join(l[i:j])
                            i = j
                            if i < len_l:
                                if l[i] in ('+', '-') or l[i][0] in '0123456789':
                                    if l[i] in ('+', '-'):
                                        signal = (1, -1)[l[i] == '+']
                                        i += 1
                                    else:
                                        signal = -1
                                    len_li = len(l[i])
                                    if len_li == 4:
                                        setattr(res, offattr, (int(l[i][:2]) * 3600 + int(l[i][2:]) * 60) * signal)
                                    elif i + 1 < len_l and l[i + 1] == ':':
                                        setattr(res, offattr, (int(l[i]) * 3600 + int(l[i + 2]) * 60) * signal)
                                        i += 2
                                    elif len_li <= 2:
                                        setattr(res, offattr, int(l[i][:2]) * 3600 * signal)
                                    else:
                                        return None
                                    [] += 1
                            if res.dstabbr:
                                break
                            
                break
            if i < len_l:
                for j in range(i, len_l):
                    if l[j] == ';':
                        l[j] = ','
                        continue
                if not l[i] == ',':
                    raise AssertionError
                [] += 1
            if i >= len_l:
                pass
            if 8 <= l.count(','):
                pass
            l.count(',') <= 9
            if 1:
                for x in l[i:]:
                    if x != ',':
                        for y in x:
                            if y not in '0123456789':
                                continue
                                continue
                                if not [][y]:
                                    for x in (res.start, res.end):
                                        x.month = int(l[i])
                                        i += 2
                                        if l[i] == '-':
                                            value = int(l[i + 1]) * -1
                                            i += 1
                                        else:
                                            value = int(l[i])
                                        i += 2
                                        if value:
                                            x.week = value
                                            x.weekday = (int(l[i]) - 1) % 7
                                        else:
                                            x.day = int(l[i])
                                        i += 2
                                        x.time = int(l[i])
                                        i += 2
                                    
                                    if i < len_l:
                                        if l[i] in ('-', '+'):
                                            signal = (-1, 1)[l[i] == '+']
                                            i += 1
                                        else:
                                            signal = 1
                                        res.dstoffset = (res.stdoffset + int(l[i])) * signal
                                    
                                elif l.count(',') == 2 and l[i:].count('/') <= 2:
                                    for x in l[i:]:
                                        if x not in (',', '/', 'J', 'M', '.', '-', ':'):
                                            for y in x:
                                                if y not in '0123456789':
                                                    continue
                                                    continue
                                                    if not [][y]:
                                                        for x in (res.start, res.end):
                                                            if l[i] == 'J':
                                                                i += 1
                                                                x.jyday = int(l[i])
                                                            elif l[i] == 'M':
                                                                i += 1
                                                                x.month = int(l[i])
                                                                i += 1
                                                                if not l[i] in ('-', '.'):
                                                                    raise AssertionError
                                                                [] += 1
                                                                x.week = int(l[i])
                                                                if x.week == 5:
                                                                    x.week = -1
                                                                i += 1
                                                                if not l[i] in ('-', '.'):
                                                                    raise AssertionError
                                                                [] += 1
                                                                x.weekday = (int(l[i]) - 1) % 7
                                                            else:
                                                                x.yday = int(l[i]) + 1
                                                            i += 1
                                                            if i < len_l and l[i] == '/':
                                                                i += 1
                                                                len_li = len(l[i])
                                                                if len_li == 4:
                                                                    x.time = int(l[i][:2]) * 3600 + int(l[i][2:]) * 60
                                                                elif i + 1 < len_l and l[i + 1] == ':':
                                                                    x.time = int(l[i]) * 3600 + int(l[i + 2]) * 60
                                                                    i += 2
                                                                    if i + 1 < len_l and l[i + 1] == ':':
                                                                        i += 2
                                                                        x.time += int(l[i])
                                                                    
                                                                elif len_li <= 2:
                                                                    x.time = int(l[i][:2]) * 3600
                                                                else:
                                                                    return None
                                                                [] += 1
                                                            if not i == len_l and l[i] == ',':
                                                                raise AssertionError
                                                            [] += 1
                                                        
                                                        if not i >= len_l:
                                                            raise AssertionError
                                                else:
                                                    except (IndexError, ValueError, AssertionError):
                                                        []
                                                        []
                                                        1
                                                        return None

        return res


DEFAULTTZPARSER = _tzparser()

def _parsetz(tzstr):
    return DEFAULTTZPARSER.parse(tzstr)


def _parsems(value):
    '''Parse a I[.F] seconds value into (seconds, microseconds).'''
    if '.' not in value:
        return (int(value), 0)
    (i, f) = None.split('.')
    return (int(i), int(f.ljust(6, '0')[:6]))

