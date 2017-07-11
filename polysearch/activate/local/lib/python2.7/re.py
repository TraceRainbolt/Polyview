#
# Secret Labs' Regular Expression Engine
#
# re-compatible interface for the sre matching engine
#
# Copyright (c***REMOVED*** 1998-2001 by Secret Labs AB.  All rights reserved.
#
# This version of the SRE library can be redistributed under CNRI's
# Python 1.6 license.  For any other use, please contact Secret Labs
# AB (info@pythonware.com***REMOVED***.
#
# Portions of this engine have been developed in cooperation with
# CNRI.  Hewlett-Packard provided funding for 1.6 integration and
# other compatibility work.
#

r***REMOVED***Support for regular expressions (RE***REMOVED***.

This module provides regular expression matching operations similar to
those found in Perl.  It supports both 8-bit and Unicode strings; both
the pattern and the strings being processed can contain null bytes and
characters outside the US ASCII range.

Regular expressions can contain both special and ordinary characters.
Most ordinary characters, like "A", "a", or "0", are the simplest
regular expressions; they simply match themselves.  You can
concatenate ordinary characters, so last matches the string 'last'.

The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy***REMOVED*** repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy***REMOVED*** repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy***REMOVED*** of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
***REMOVED***m,n***REMOVED***    Matches from m to n repetitions of the preceding RE.
***REMOVED***m,n***REMOVED***?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    [***REMOVED***       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...***REMOVED***    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?iLmsux***REMOVED*** Set the I, L, M, S, U, or X flag for the RE (see below***REMOVED***.
    (?:...***REMOVED***  Non-grouping version of regular parentheses.
    (?P<name>...***REMOVED*** The substring matched by the group is accessible by name.
    (?P=name***REMOVED***     Matches the text matched earlier by the group named name.
    (?#...***REMOVED***  A comment; ignored.
    (?=...***REMOVED***  Matches if ... matches next, but doesn't consume the string.
    (?!...***REMOVED***  Matches if ... doesn't match next.
    (?<=...***REMOVED*** Matches if preceded by ... (must be fixed length***REMOVED***.
    (?<!...***REMOVED*** Matches if not preceded by ... (must be fixed length***REMOVED***.
    (?(id/name***REMOVED***yes|no***REMOVED*** Matches yes pattern if the group with id/name matched,
                       the (optional***REMOVED*** no pattern otherwise.

The special sequences consist of "\\" and a character from the list
below.  If the ordinary character is not on the list, then the
resulting RE will match the second character.
    \number  Matches the contents of the group of the same number.
    \A       Matches only at the start of the string.
    \Z       Matches only at the end of the string.
    \b       Matches the empty string, but only at the start or end of a word.
    \B       Matches the empty string, but not at the start or end of a word.
    \d       Matches any decimal digit; equivalent to the set [0-9***REMOVED***.
    \D       Matches any non-digit character; equivalent to the set [^0-9***REMOVED***.
    \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v***REMOVED***.
    \S       Matches any non-whitespace character; equiv. to [^ \t\n\r\f\v***REMOVED***.
    \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_***REMOVED***.
             With LOCALE, it will match the set [0-9_***REMOVED*** plus characters defined
             as letters for the current locale.
    \W       Matches the complement of \w.
    \\       Matches a literal backslash.

This module exports the following functions:
    match    Match a regular expression pattern to the beginning of a string.
    search   Search a string for the presence of a pattern.
    sub      Substitute occurrences of a pattern found in a string.
    subn     Same as sub, but also return the number of substitutions made.
    split    Split a string by the occurrences of a pattern.
    findall  Find all occurrences of a pattern in a string.
    finditer Return an iterator yielding a match object for each match.
    compile  Compile a pattern into a RegexObject.
    purge    Clear the regular expression cache.
    escape   Backslash all non-alphanumerics in a string.

Some of the functions in this module takes flags as optional parameters:
    I  IGNORECASE  Perform case-insensitive matching.
    L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
    M  MULTILINE   "^" matches the beginning of lines (after a newline***REMOVED***
                   as well as the string.
                   "$" matches the end of lines (before a newline***REMOVED*** as well
                   as the end of the string.
    S  DOTALL      "." matches any character at all, including the newline.
    X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    U  UNICODE     Make \w, \W, \b, \B, dependent on the Unicode locale.

This module also defines an exception 'error'.

***REMOVED***

import sys
import sre_compile
import sre_parse

# public symbols
__all__ = [ "match", "search", "sub", "subn", "split", "findall",
    "compile", "purge", "template", "escape", "I", "L", "M", "S", "X",
    "U", "IGNORECASE", "LOCALE", "MULTILINE", "DOTALL", "VERBOSE",
    "UNICODE", "error" ***REMOVED***

__version__ = "2.2.1"

# flags
I = IGNORECASE = sre_compile.SRE_FLAG_IGNORECASE # ignore case
L = LOCALE = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
U = UNICODE = sre_compile.SRE_FLAG_UNICODE # assume unicode locale
M = MULTILINE = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
S = DOTALL = sre_compile.SRE_FLAG_DOTALL # make dot match newline
X = VERBOSE = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments

# sre extensions (experimental, don't rely on these***REMOVED***
T = TEMPLATE = sre_compile.SRE_FLAG_TEMPLATE # disable backtracking
DEBUG = sre_compile.SRE_FLAG_DEBUG # dump pattern after compilation

# sre exception
error = sre_compile.error

# --------------------------------------------------------------------
# public interface

def match(pattern, string, flags=0***REMOVED***:
    ***REMOVED***Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found.***REMOVED***
    return _compile(pattern, flags***REMOVED***.match(string***REMOVED***

def search(pattern, string, flags=0***REMOVED***:
    ***REMOVED***Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found.***REMOVED***
    return _compile(pattern, flags***REMOVED***.search(string***REMOVED***

def sub(pattern, repl, string, count=0, flags=0***REMOVED***:
    ***REMOVED***Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used.***REMOVED***
    return _compile(pattern, flags***REMOVED***.sub(repl, string, count***REMOVED***

def subn(pattern, repl, string, count=0, flags=0***REMOVED***:
    ***REMOVED***Return a 2-tuple containing (new_string, number***REMOVED***.
    new_string is the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in the source
    string by the replacement repl.  number is the number of
    substitutions that were made. repl can be either a string or a
    callable; if a string, backslash escapes in it are processed.
    If it is a callable, it's passed the match object and must
    return a replacement string to be used.***REMOVED***
    return _compile(pattern, flags***REMOVED***.subn(repl, string, count***REMOVED***

def split(pattern, string, maxsplit=0, flags=0***REMOVED***:
    ***REMOVED***Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.***REMOVED***
    return _compile(pattern, flags***REMOVED***.split(string, maxsplit***REMOVED***

def findall(pattern, string, flags=0***REMOVED***:
    ***REMOVED***Return a list of all non-overlapping matches in the string.

    If one or more groups are present in the pattern, return a
    list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result.***REMOVED***
    return _compile(pattern, flags***REMOVED***.findall(string***REMOVED***

if sys.hexversion >= 0x02020000:
    __all__.append("finditer"***REMOVED***
    def finditer(pattern, string, flags=0***REMOVED***:
        ***REMOVED***Return an iterator over all non-overlapping matches in the
        string.  For each match, the iterator returns a match object.

        Empty matches are included in the result.***REMOVED***
        return _compile(pattern, flags***REMOVED***.finditer(string***REMOVED***

def compile(pattern, flags=0***REMOVED***:
    "Compile a regular expression pattern, returning a pattern object."
    return _compile(pattern, flags***REMOVED***

def purge(***REMOVED***:
    "Clear the regular expression cache"
    _cache.clear(***REMOVED***
    _cache_repl.clear(***REMOVED***

def template(pattern, flags=0***REMOVED***:
    "Compile a template pattern, returning a pattern object"
    return _compile(pattern, flags|T***REMOVED***

_alphanum = frozenset(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"***REMOVED***

def escape(pattern***REMOVED***:
    "Escape all non-alphanumeric characters in pattern."
    s = list(pattern***REMOVED***
    alphanum = _alphanum
    for i, c in enumerate(pattern***REMOVED***:
        if c not in alphanum:
            if c == "\000":
                s[i***REMOVED*** = "\\000"
            else:
                s[i***REMOVED*** = "\\" + c
    return pattern[:0***REMOVED***.join(s***REMOVED***

# --------------------------------------------------------------------
# internals

_cache = {***REMOVED***
_cache_repl = {***REMOVED***

_pattern_type = type(sre_compile.compile("", 0***REMOVED******REMOVED***

_MAXCACHE = 100

def _compile(*key***REMOVED***:
    # internal: compile pattern
    pattern, flags = key
    bypass_cache = flags & DEBUG
    if not bypass_cache:
        cachekey = (type(key[0***REMOVED******REMOVED***,***REMOVED*** + key
        p = _cache.get(cachekey***REMOVED***
        if p is not None:
            return p
    if isinstance(pattern, _pattern_type***REMOVED***:
        if flags:
            raise ValueError('Cannot process flags argument with a compiled pattern'***REMOVED***
        return pattern
    if not sre_compile.isstring(pattern***REMOVED***:
        raise TypeError, "first argument must be string or compiled pattern"
    try:
        p = sre_compile.compile(pattern, flags***REMOVED***
    except error, v:
        raise error, v # invalid expression
    if not bypass_cache:
        if len(_cache***REMOVED*** >= _MAXCACHE:
            _cache.clear(***REMOVED***
        _cache[cachekey***REMOVED*** = p
    return p

def _compile_repl(*key***REMOVED***:
    # internal: compile replacement pattern
    p = _cache_repl.get(key***REMOVED***
    if p is not None:
        return p
    repl, pattern = key
    try:
        p = sre_parse.parse_template(repl, pattern***REMOVED***
    except error, v:
        raise error, v # invalid expression
    if len(_cache_repl***REMOVED*** >= _MAXCACHE:
        _cache_repl.clear(***REMOVED***
    _cache_repl[key***REMOVED*** = p
    return p

def _expand(pattern, match, template***REMOVED***:
    # internal: match.expand implementation hook
    template = sre_parse.parse_template(template, pattern***REMOVED***
    return sre_parse.expand_template(template, match***REMOVED***

def _subx(pattern, template***REMOVED***:
    # internal: pattern.sub/subn implementation helper
    template = _compile_repl(template, pattern***REMOVED***
    if not template[0***REMOVED*** and len(template[1***REMOVED******REMOVED*** == 1:
        # literal replacement
        return template[1***REMOVED***[0***REMOVED***
    def filter(match, template=template***REMOVED***:
        return sre_parse.expand_template(template, match***REMOVED***
    return filter

# register myself for pickling

import copy_reg

def _pickle(p***REMOVED***:
    return _compile, (p.pattern, p.flags***REMOVED***

copy_reg.pickle(_pattern_type, _pickle, _compile***REMOVED***

# --------------------------------------------------------------------
# experimental stuff (see python-dev discussions for details***REMOVED***

class Scanner:
    def __init__(self, lexicon, flags=0***REMOVED***:
        from sre_constants import BRANCH, SUBPATTERN
        self.lexicon = lexicon
        # combine phrases into a compound pattern
        p = [***REMOVED***
        s = sre_parse.Pattern(***REMOVED***
        s.flags = flags
        for phrase, action in lexicon:
            p.append(sre_parse.SubPattern(s, [
                (SUBPATTERN, (len(p***REMOVED***+1, sre_parse.parse(phrase, flags***REMOVED******REMOVED******REMOVED***,
                ***REMOVED******REMOVED******REMOVED***
        s.groups = len(p***REMOVED***+1
        p = sre_parse.SubPattern(s, [(BRANCH, (None, p***REMOVED******REMOVED******REMOVED******REMOVED***
        self.scanner = sre_compile.compile(p***REMOVED***
    def scan(self, string***REMOVED***:
        result = [***REMOVED***
        append = result.append
        match = self.scanner.scanner(string***REMOVED***.match
        i = 0
        while 1:
            m = match(***REMOVED***
            if not m:
                break
            j = m.end(***REMOVED***
            if i == j:
                break
            action = self.lexicon[m.lastindex-1***REMOVED***[1***REMOVED***
            if hasattr(action, '__call__'***REMOVED***:
                self.match = m
                action = action(self, m.group(***REMOVED******REMOVED***
            if action is not None:
                append(action***REMOVED***
            i = j
        return result, string[i:***REMOVED***
