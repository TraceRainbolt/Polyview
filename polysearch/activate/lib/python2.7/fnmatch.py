***REMOVED***Filename matching with shell patterns.

fnmatch(FILENAME, PATTERN***REMOVED*** matches according to the local convention.
fnmatchcase(FILENAME, PATTERN***REMOVED*** always takes case in account.

The functions operate by translating the pattern into a regular
expression.  They cache the compiled regular expressions for speed.

The function translate(PATTERN***REMOVED*** returns a regular expression
corresponding to PATTERN.  (It does not compile it.***REMOVED***
***REMOVED***

import re

__all__ = ["filter", "fnmatch", "fnmatchcase", "translate"***REMOVED***

_cache = {***REMOVED***
_MAXCACHE = 100

def _purge(***REMOVED***:
    ***REMOVED***Clear the pattern cache***REMOVED***
    _cache.clear(***REMOVED***

def fnmatch(name, pat***REMOVED***:
    ***REMOVED***Test whether FILENAME matches PATTERN.

    Patterns are Unix shell style:

    *       matches everything
    ?       matches any single character
    [seq***REMOVED***   matches any character in seq
    [!seq***REMOVED***  matches any char not in seq

    An initial period in FILENAME is not special.
    Both FILENAME and PATTERN are first case-normalized
    if the operating system requires it.
    If you don't want this, use fnmatchcase(FILENAME, PATTERN***REMOVED***.
    ***REMOVED***

    ***REMOVED***
    name = os.path.normcase(name***REMOVED***
    pat = os.path.normcase(pat***REMOVED***
    return fnmatchcase(name, pat***REMOVED***

def filter(names, pat***REMOVED***:
    ***REMOVED***Return the subset of the list NAMES that match PAT***REMOVED***
    ***REMOVED***,posixpath
    result=[***REMOVED***
    pat=os.path.normcase(pat***REMOVED***
    if not pat in _cache:
        res = translate(pat***REMOVED***
        if len(_cache***REMOVED*** >= _MAXCACHE:
            _cache.clear(***REMOVED***
        _cache[pat***REMOVED*** = re.compile(res***REMOVED***
    match=_cache[pat***REMOVED***.match
    if os.path is posixpath:
        # normcase on posix is NOP. Optimize it away from the loop.
        for name in names:
            if match(name***REMOVED***:
                result.append(name***REMOVED***
    else:
        for name in names:
            if match(os.path.normcase(name***REMOVED******REMOVED***:
                result.append(name***REMOVED***
    return result

def fnmatchcase(name, pat***REMOVED***:
    ***REMOVED***Test whether FILENAME matches PATTERN, including case.

    This is a version of fnmatch(***REMOVED*** which doesn't case-normalize
    its arguments.
    ***REMOVED***

    if not pat in _cache:
        res = translate(pat***REMOVED***
        if len(_cache***REMOVED*** >= _MAXCACHE:
            _cache.clear(***REMOVED***
        _cache[pat***REMOVED*** = re.compile(res***REMOVED***
    return _cache[pat***REMOVED***.match(name***REMOVED*** is not None

def translate(pat***REMOVED***:
    ***REMOVED***Translate a shell PATTERN to a regular expression.

    There is no way to quote meta-characters.
    ***REMOVED***

    i, n = 0, len(pat***REMOVED***
    res = ''
    while i < n:
        c = pat[i***REMOVED***
        i = i+1
        if c == '*':
            res = res + '.*'
        elif c == '?':
            res = res + '.'
        elif c == '[':
            j = i
            if j < n and pat[j***REMOVED*** == '!':
                j = j+1
            if j < n and pat[j***REMOVED*** == '***REMOVED***':
                j = j+1
            while j < n and pat[j***REMOVED*** != '***REMOVED***':
                j = j+1
            if j >= n:
                res = res + '\\['
            else:
                stuff = pat[i:j***REMOVED***.replace('\\','\\\\'***REMOVED***
                i = j+1
                if stuff[0***REMOVED*** == '!':
                    stuff = '^' + stuff[1:***REMOVED***
                elif stuff[0***REMOVED*** == '^':
                    stuff = '\\' + stuff
                res = '%s[%s***REMOVED***' % (res, stuff***REMOVED***
        else:
            res = res + re.escape(c***REMOVED***
    return res + '\Z(?ms***REMOVED***'
