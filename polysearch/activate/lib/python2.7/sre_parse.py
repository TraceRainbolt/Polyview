#
# Secret Labs' Regular Expression Engine
#
# convert re-style regular expression to sre pattern
#
# Copyright (c***REMOVED*** 1998-2001 by Secret Labs AB.  All rights reserved.
#
# See the sre.py file for information on usage and redistribution.
#

***REMOVED***Internal support module for sre***REMOVED***

# XXX: show string offset and offending character for all errors

import sys

from sre_constants import *

SPECIAL_CHARS = ".\\[{(***REMOVED****+?^$|"
REPEAT_CHARS = "*+?{"

DIGITS = set("0123456789"***REMOVED***

OCTDIGITS = set("01234567"***REMOVED***
HEXDIGITS = set("0123456789abcdefABCDEF"***REMOVED***

WHITESPACE = set(" \t\n\r\v\f"***REMOVED***

ESCAPES = {
    r"\a": (LITERAL, ord("\a"***REMOVED******REMOVED***,
    r"\b": (LITERAL, ord("\b"***REMOVED******REMOVED***,
    r"\f": (LITERAL, ord("\f"***REMOVED******REMOVED***,
    r"\n": (LITERAL, ord("\n"***REMOVED******REMOVED***,
    r"\r": (LITERAL, ord("\r"***REMOVED******REMOVED***,
    r"\t": (LITERAL, ord("\t"***REMOVED******REMOVED***,
    r"\v": (LITERAL, ord("\v"***REMOVED******REMOVED***,
    r"\\": (LITERAL, ord("\\"***REMOVED******REMOVED***
***REMOVED***

CATEGORIES = {
    r"\A": (AT, AT_BEGINNING_STRING***REMOVED***, # start of string
    r"\b": (AT, AT_BOUNDARY***REMOVED***,
    r"\B": (AT, AT_NON_BOUNDARY***REMOVED***,
    r"\d": (IN, [(CATEGORY, CATEGORY_DIGIT***REMOVED******REMOVED******REMOVED***,
    r"\D": (IN, [(CATEGORY, CATEGORY_NOT_DIGIT***REMOVED******REMOVED******REMOVED***,
    r"\s": (IN, [(CATEGORY, CATEGORY_SPACE***REMOVED******REMOVED******REMOVED***,
    r"\S": (IN, [(CATEGORY, CATEGORY_NOT_SPACE***REMOVED******REMOVED******REMOVED***,
    r"\w": (IN, [(CATEGORY, CATEGORY_WORD***REMOVED******REMOVED******REMOVED***,
    r"\W": (IN, [(CATEGORY, CATEGORY_NOT_WORD***REMOVED******REMOVED******REMOVED***,
    r"\Z": (AT, AT_END_STRING***REMOVED***, # end of string
***REMOVED***

FLAGS = {
    # standard flags
    "i": SRE_FLAG_IGNORECASE,
    "L": SRE_FLAG_LOCALE,
    "m": SRE_FLAG_MULTILINE,
    "s": SRE_FLAG_DOTALL,
    "x": SRE_FLAG_VERBOSE,
    # extensions
    "t": SRE_FLAG_TEMPLATE,
    "u": SRE_FLAG_UNICODE,
***REMOVED***

class Pattern:
    # master pattern object.  keeps track of global attributes
    def __init__(self***REMOVED***:
        self.flags = 0
        self.open = [***REMOVED***
        self.groups = 1
        self.groupdict = {***REMOVED***
    def opengroup(self, name=None***REMOVED***:
        gid = self.groups
        self.groups = gid + 1
        if name is not None:
            ogid = self.groupdict.get(name, None***REMOVED***
            if ogid is not None:
                raise error, ("redefinition of group name %s as group %d; "
                              "was group %d" % (repr(name***REMOVED***, gid,  ogid***REMOVED******REMOVED***
            self.groupdict[name***REMOVED*** = gid
        self.open.append(gid***REMOVED***
        return gid
    def closegroup(self, gid***REMOVED***:
        self.open.remove(gid***REMOVED***
    def checkgroup(self, gid***REMOVED***:
        return gid < self.groups and gid not in self.open

class SubPattern:
    # a subpattern, in intermediate form
    def __init__(self, pattern, data=None***REMOVED***:
        self.pattern = pattern
        if data is None:
            data = [***REMOVED***
        self.data = data
        self.width = None
    def dump(self, level=0***REMOVED***:
        nl = 1
        seqtypes = type((***REMOVED******REMOVED***, type([***REMOVED******REMOVED***
        for op, av in self.data:
            print level*"  " + op,; nl = 0
            if op == "in":
                # member sublanguage
                print; nl = 1
                for op, a in av:
                    print (level+1***REMOVED****"  " + op, a
            elif op == "branch":
                print; nl = 1
                i = 0
                for a in av[1***REMOVED***:
                    if i > 0:
                        print level*"  " + "or"
                    a.dump(level+1***REMOVED***; nl = 1
                    i = i + 1
            elif type(av***REMOVED*** in seqtypes:
                for a in av:
                    if isinstance(a, SubPattern***REMOVED***:
                        if not nl: print
                        a.dump(level+1***REMOVED***; nl = 1
                    else:
                        print a, ; nl = 0
            else:
                print av, ; nl = 0
            if not nl: print
    def __repr__(self***REMOVED***:
        return repr(self.data***REMOVED***
    def __len__(self***REMOVED***:
        return len(self.data***REMOVED***
    def __delitem__(self, index***REMOVED***:
        del self.data[index***REMOVED***
    def __getitem__(self, index***REMOVED***:
        if isinstance(index, slice***REMOVED***:
            return SubPattern(self.pattern, self.data[index***REMOVED******REMOVED***
        return self.data[index***REMOVED***
    def __setitem__(self, index, code***REMOVED***:
        self.data[index***REMOVED*** = code
    def insert(self, index, code***REMOVED***:
        self.data.insert(index, code***REMOVED***
    def append(self, code***REMOVED***:
        self.data.append(code***REMOVED***
    def getwidth(self***REMOVED***:
        # determine the width (min, max***REMOVED*** for this subpattern
        if self.width:
            return self.width
        lo = hi = 0
        UNITCODES = (ANY, RANGE, IN, LITERAL, NOT_LITERAL, CATEGORY***REMOVED***
        REPEATCODES = (MIN_REPEAT, MAX_REPEAT***REMOVED***
        for op, av in self.data:
            if op is BRANCH:
                i = MAXREPEAT - 1
                j = 0
                for av in av[1***REMOVED***:
                    l, h = av.getwidth(***REMOVED***
                    i = min(i, l***REMOVED***
                    j = max(j, h***REMOVED***
                lo = lo + i
                hi = hi + j
            elif op is CALL:
                i, j = av.getwidth(***REMOVED***
                lo = lo + i
                hi = hi + j
            elif op is SUBPATTERN:
                i, j = av[1***REMOVED***.getwidth(***REMOVED***
                lo = lo + i
                hi = hi + j
            elif op in REPEATCODES:
                i, j = av[2***REMOVED***.getwidth(***REMOVED***
                lo = lo + i * av[0***REMOVED***
                hi = hi + j * av[1***REMOVED***
            elif op in UNITCODES:
                lo = lo + 1
                hi = hi + 1
            elif op == SUCCESS:
                break
        self.width = min(lo, MAXREPEAT - 1***REMOVED***, min(hi, MAXREPEAT***REMOVED***
        return self.width

class Tokenizer:
    def __init__(self, string***REMOVED***:
        self.string = string
        self.index = 0
        self.__next(***REMOVED***
    def __next(self***REMOVED***:
        if self.index >= len(self.string***REMOVED***:
            self.next = None
            return
        char = self.string[self.index***REMOVED***
        if char[0***REMOVED*** == "\\":
            try:
                c = self.string[self.index + 1***REMOVED***
            except IndexError:
                raise error, "bogus escape (end of line***REMOVED***"
            char = char + c
        self.index = self.index + len(char***REMOVED***
        self.next = char
    def match(self, char, skip=1***REMOVED***:
        if char == self.next:
            if skip:
                self.__next(***REMOVED***
            return 1
        return 0
    def get(self***REMOVED***:
        this = self.next
        self.__next(***REMOVED***
        return this
    def tell(self***REMOVED***:
        return self.index, self.next
    def seek(self, index***REMOVED***:
        self.index, self.next = index

def isident(char***REMOVED***:
    return "a" <= char <= "z" or "A" <= char <= "Z" or char == "_"

def isdigit(char***REMOVED***:
    return "0" <= char <= "9"

def isname(name***REMOVED***:
    # check that group name is a valid string
    if not isident(name[0***REMOVED******REMOVED***:
        return False
    for char in name[1:***REMOVED***:
        if not isident(char***REMOVED*** and not isdigit(char***REMOVED***:
            return False
    return True

def _class_escape(source, escape***REMOVED***:
    # handle escape code inside character class
    code = ESCAPES.get(escape***REMOVED***
    if code:
        return code
    code = CATEGORIES.get(escape***REMOVED***
    if code and code[0***REMOVED*** == IN:
        return code
    try:
        c = escape[1:2***REMOVED***
        if c == "x":
            # hexadecimal escape (exactly two digits***REMOVED***
            while source.next in HEXDIGITS and len(escape***REMOVED*** < 4:
                escape = escape + source.get(***REMOVED***
            escape = escape[2:***REMOVED***
            if len(escape***REMOVED*** != 2:
                raise error, "bogus escape: %s" % repr("\\" + escape***REMOVED***
            return LITERAL, int(escape, 16***REMOVED*** & 0xff
        elif c in OCTDIGITS:
            # octal escape (up to three digits***REMOVED***
            while source.next in OCTDIGITS and len(escape***REMOVED*** < 4:
                escape = escape + source.get(***REMOVED***
            escape = escape[1:***REMOVED***
            return LITERAL, int(escape, 8***REMOVED*** & 0xff
        elif c in DIGITS:
            raise error, "bogus escape: %s" % repr(escape***REMOVED***
        if len(escape***REMOVED*** == 2:
            return LITERAL, ord(escape[1***REMOVED******REMOVED***
    except ValueError:
        pass
    raise error, "bogus escape: %s" % repr(escape***REMOVED***

def _escape(source, escape, state***REMOVED***:
    # handle escape code in expression
    code = CATEGORIES.get(escape***REMOVED***
    if code:
        return code
    code = ESCAPES.get(escape***REMOVED***
    if code:
        return code
    try:
        c = escape[1:2***REMOVED***
        if c == "x":
            # hexadecimal escape
            while source.next in HEXDIGITS and len(escape***REMOVED*** < 4:
                escape = escape + source.get(***REMOVED***
            if len(escape***REMOVED*** != 4:
                raise ValueError
            return LITERAL, int(escape[2:***REMOVED***, 16***REMOVED*** & 0xff
        elif c == "0":
            # octal escape
            while source.next in OCTDIGITS and len(escape***REMOVED*** < 4:
                escape = escape + source.get(***REMOVED***
            return LITERAL, int(escape[1:***REMOVED***, 8***REMOVED*** & 0xff
        elif c in DIGITS:
            # octal escape *or* decimal group reference (sigh***REMOVED***
            if source.next in DIGITS:
                escape = escape + source.get(***REMOVED***
                if (escape[1***REMOVED*** in OCTDIGITS and escape[2***REMOVED*** in OCTDIGITS and
                    source.next in OCTDIGITS***REMOVED***:
                    # got three octal digits; this is an octal escape
                    escape = escape + source.get(***REMOVED***
                    return LITERAL, int(escape[1:***REMOVED***, 8***REMOVED*** & 0xff
            # not an octal escape, so this is a group reference
            group = int(escape[1:***REMOVED******REMOVED***
            if group < state.groups:
                if not state.checkgroup(group***REMOVED***:
                    raise error, "cannot refer to open group"
                return GROUPREF, group
            raise ValueError
        if len(escape***REMOVED*** == 2:
            return LITERAL, ord(escape[1***REMOVED******REMOVED***
    except ValueError:
        pass
    raise error, "bogus escape: %s" % repr(escape***REMOVED***

def _parse_sub(source, state, nested=1***REMOVED***:
    # parse an alternation: a|b|c

    items = [***REMOVED***
    itemsappend = items.append
    sourcematch = source.match
    while 1:
        itemsappend(_parse(source, state***REMOVED******REMOVED***
        if sourcematch("|"***REMOVED***:
            continue
        if not nested:
            break
        if not source.next or sourcematch("***REMOVED***", 0***REMOVED***:
            break
        else:
            raise error, "pattern not properly closed"

    if len(items***REMOVED*** == 1:
        return items[0***REMOVED***

    subpattern = SubPattern(state***REMOVED***
    subpatternappend = subpattern.append

    # check if all items share a common prefix
    while 1:
        prefix = None
        for item in items:
            if not item:
                break
            if prefix is None:
                prefix = item[0***REMOVED***
            elif item[0***REMOVED*** != prefix:
                break
        else:
            # all subitems start with a common "prefix".
            # move it out of the branch
            for item in items:
                del item[0***REMOVED***
            subpatternappend(prefix***REMOVED***
            continue # check next one
        break

    # check if the branch can be replaced by a character set
    for item in items:
        if len(item***REMOVED*** != 1 or item[0***REMOVED***[0***REMOVED*** != LITERAL:
            break
    else:
        # we can store this as a character set instead of a
        # branch (the compiler may optimize this even more***REMOVED***
        set = [***REMOVED***
        setappend = set.append
        for item in items:
            setappend(item[0***REMOVED******REMOVED***
        subpatternappend((IN, set***REMOVED******REMOVED***
        return subpattern

    subpattern.append((BRANCH, (None, items***REMOVED******REMOVED******REMOVED***
    return subpattern

def _parse_sub_cond(source, state, condgroup***REMOVED***:
    item_yes = _parse(source, state***REMOVED***
    if source.match("|"***REMOVED***:
        item_no = _parse(source, state***REMOVED***
        if source.match("|"***REMOVED***:
            raise error, "conditional backref with more than two branches"
    else:
        item_no = None
    if source.next and not source.match("***REMOVED***", 0***REMOVED***:
        raise error, "pattern not properly closed"
    subpattern = SubPattern(state***REMOVED***
    subpattern.append((GROUPREF_EXISTS, (condgroup, item_yes, item_no***REMOVED******REMOVED******REMOVED***
    return subpattern

_PATTERNENDERS = set("|***REMOVED***"***REMOVED***
_ASSERTCHARS = set("=!<"***REMOVED***
_LOOKBEHINDASSERTCHARS = set("=!"***REMOVED***
_REPEATCODES = set([MIN_REPEAT, MAX_REPEAT***REMOVED******REMOVED***

def _parse(source, state***REMOVED***:
    # parse a simple pattern
    subpattern = SubPattern(state***REMOVED***

    # precompute constants into local variables
    subpatternappend = subpattern.append
    sourceget = source.get
    sourcematch = source.match
    _len = len
    PATTERNENDERS = _PATTERNENDERS
    ASSERTCHARS = _ASSERTCHARS
    LOOKBEHINDASSERTCHARS = _LOOKBEHINDASSERTCHARS
    REPEATCODES = _REPEATCODES

    while 1:

        if source.next in PATTERNENDERS:
            break # end of subpattern
        this = sourceget(***REMOVED***
        if this is None:
            break # end of pattern

        if state.flags & SRE_FLAG_VERBOSE:
            # skip whitespace and comments
            if this in WHITESPACE:
                continue
            if this == "#":
                while 1:
                    this = sourceget(***REMOVED***
                    if this in (None, "\n"***REMOVED***:
                        break
                continue

        if this and this[0***REMOVED*** not in SPECIAL_CHARS:
            subpatternappend((LITERAL, ord(this***REMOVED******REMOVED******REMOVED***

        elif this == "[":
            # character set
            set = [***REMOVED***
            setappend = set.append
##          if sourcematch(":"***REMOVED***:
##              pass # handle character classes
            if sourcematch("^"***REMOVED***:
                setappend((NEGATE, None***REMOVED******REMOVED***
            # check remaining characters
            start = set[:***REMOVED***
            while 1:
                this = sourceget(***REMOVED***
                if this == "***REMOVED***" and set != start:
                    break
                elif this and this[0***REMOVED*** == "\\":
                    code1 = _class_escape(source, this***REMOVED***
                elif this:
                    code1 = LITERAL, ord(this***REMOVED***
                else:
                    raise error, "unexpected end of regular expression"
                if sourcematch("-"***REMOVED***:
                    # potential range
                    this = sourceget(***REMOVED***
                    if this == "***REMOVED***":
                        if code1[0***REMOVED*** is IN:
                            code1 = code1[1***REMOVED***[0***REMOVED***
                        setappend(code1***REMOVED***
                        setappend((LITERAL, ord("-"***REMOVED******REMOVED******REMOVED***
                        break
                    elif this:
                        if this[0***REMOVED*** == "\\":
                            code2 = _class_escape(source, this***REMOVED***
                        else:
                            code2 = LITERAL, ord(this***REMOVED***
                        if code1[0***REMOVED*** != LITERAL or code2[0***REMOVED*** != LITERAL:
                            raise error, "bad character range"
                        lo = code1[1***REMOVED***
                        hi = code2[1***REMOVED***
                        if hi < lo:
                            raise error, "bad character range"
                        setappend((RANGE, (lo, hi***REMOVED******REMOVED******REMOVED***
                    else:
                        raise error, "unexpected end of regular expression"
                else:
                    if code1[0***REMOVED*** is IN:
                        code1 = code1[1***REMOVED***[0***REMOVED***
                    setappend(code1***REMOVED***

            # XXX: <fl> should move set optimization to compiler!
            if _len(set***REMOVED***==1 and set[0***REMOVED***[0***REMOVED*** is LITERAL:
                subpatternappend(set[0***REMOVED******REMOVED*** # optimization
            elif _len(set***REMOVED***==2 and set[0***REMOVED***[0***REMOVED*** is NEGATE and set[1***REMOVED***[0***REMOVED*** is LITERAL:
                subpatternappend((NOT_LITERAL, set[1***REMOVED***[1***REMOVED******REMOVED******REMOVED*** # optimization
            else:
                # XXX: <fl> should add charmap optimization here
                subpatternappend((IN, set***REMOVED******REMOVED***

        elif this and this[0***REMOVED*** in REPEAT_CHARS:
            # repeat previous item
            if this == "?":
                min, max = 0, 1
            elif this == "*":
                min, max = 0, MAXREPEAT

            elif this == "+":
                min, max = 1, MAXREPEAT
            elif this == "{":
                if source.next == "***REMOVED***":
                    subpatternappend((LITERAL, ord(this***REMOVED******REMOVED******REMOVED***
                    continue
                here = source.tell(***REMOVED***
                min, max = 0, MAXREPEAT
                lo = hi = ""
                while source.next in DIGITS:
                    lo = lo + source.get(***REMOVED***
                if sourcematch(","***REMOVED***:
                    while source.next in DIGITS:
                        hi = hi + sourceget(***REMOVED***
                else:
                    hi = lo
                if not sourcematch("***REMOVED***"***REMOVED***:
                    subpatternappend((LITERAL, ord(this***REMOVED******REMOVED******REMOVED***
                    source.seek(here***REMOVED***
                    continue
                if lo:
                    min = int(lo***REMOVED***
                    if min >= MAXREPEAT:
                        raise OverflowError("the repetition number is too large"***REMOVED***
                if hi:
                    max = int(hi***REMOVED***
                    if max >= MAXREPEAT:
                        raise OverflowError("the repetition number is too large"***REMOVED***
                    if max < min:
                        raise error("bad repeat interval"***REMOVED***
            else:
                raise error, "not supported"
            # figure out which item to repeat
            if subpattern:
                item = subpattern[-1:***REMOVED***
            else:
                item = None
            if not item or (_len(item***REMOVED*** == 1 and item[0***REMOVED***[0***REMOVED*** == AT***REMOVED***:
                raise error, "nothing to repeat"
            if item[0***REMOVED***[0***REMOVED*** in REPEATCODES:
                raise error, "multiple repeat"
            if sourcematch("?"***REMOVED***:
                subpattern[-1***REMOVED*** = (MIN_REPEAT, (min, max, item***REMOVED******REMOVED***
            else:
                subpattern[-1***REMOVED*** = (MAX_REPEAT, (min, max, item***REMOVED******REMOVED***

        elif this == ".":
            subpatternappend((ANY, None***REMOVED******REMOVED***

        elif this == "(":
            group = 1
            name = None
            condgroup = None
            if sourcematch("?"***REMOVED***:
                group = 0
                # options
                if sourcematch("P"***REMOVED***:
                    # python extensions
                    if sourcematch("<"***REMOVED***:
                        # named group: skip forward to end of name
                        name = ""
                        while 1:
                            char = sourceget(***REMOVED***
                            if char is None:
                                raise error, "unterminated name"
                            if char == ">":
                                break
                            name = name + char
                        group = 1
                        if not name:
                            raise error("missing group name"***REMOVED***
                        if not isname(name***REMOVED***:
                            raise error("bad character in group name %r" %
                                        name***REMOVED***
                    elif sourcematch("="***REMOVED***:
                        # named backreference
                        name = ""
                        while 1:
                            char = sourceget(***REMOVED***
                            if char is None:
                                raise error, "unterminated name"
                            if char == "***REMOVED***":
                                break
                            name = name + char
                        if not name:
                            raise error("missing group name"***REMOVED***
                        if not isname(name***REMOVED***:
                            raise error("bad character in backref group name "
                                        "%r" % name***REMOVED***
                        gid = state.groupdict.get(name***REMOVED***
                        if gid is None:
                            raise error, "unknown group name"
                        subpatternappend((GROUPREF, gid***REMOVED******REMOVED***
                        continue
                    else:
                        char = sourceget(***REMOVED***
                        if char is None:
                            raise error, "unexpected end of pattern"
                        raise error, "unknown specifier: ?P%s" % char
                elif sourcematch(":"***REMOVED***:
                    # non-capturing group
                    group = 2
                elif sourcematch("#"***REMOVED***:
                    # comment
                    while 1:
                        if source.next is None or source.next == "***REMOVED***":
                            break
                        sourceget(***REMOVED***
                    if not sourcematch("***REMOVED***"***REMOVED***:
                        raise error, "unbalanced parenthesis"
                    continue
                elif source.next in ASSERTCHARS:
                    # lookahead assertions
                    char = sourceget(***REMOVED***
                    dir = 1
                    if char == "<":
                        if source.next not in LOOKBEHINDASSERTCHARS:
                            raise error, "syntax error"
                        dir = -1 # lookbehind
                        char = sourceget(***REMOVED***
                    p = _parse_sub(source, state***REMOVED***
                    if not sourcematch("***REMOVED***"***REMOVED***:
                        raise error, "unbalanced parenthesis"
                    if char == "=":
                        subpatternappend((ASSERT, (dir, p***REMOVED******REMOVED******REMOVED***
                    else:
                        subpatternappend((ASSERT_NOT, (dir, p***REMOVED******REMOVED******REMOVED***
                    continue
                elif sourcematch("("***REMOVED***:
                    # conditional backreference group
                    condname = ""
                    while 1:
                        char = sourceget(***REMOVED***
                        if char is None:
                            raise error, "unterminated name"
                        if char == "***REMOVED***":
                            break
                        condname = condname + char
                    group = 2
                    if not condname:
                        raise error("missing group name"***REMOVED***
                    if isname(condname***REMOVED***:
                        condgroup = state.groupdict.get(condname***REMOVED***
                        if condgroup is None:
                            raise error, "unknown group name"
                    else:
                        try:
                            condgroup = int(condname***REMOVED***
                        except ValueError:
                            raise error, "bad character in group name"
                else:
                    # flags
                    if not source.next in FLAGS:
                        raise error, "unexpected end of pattern"
                    while source.next in FLAGS:
                        state.flags = state.flags | FLAGS[sourceget(***REMOVED******REMOVED***
            if group:
                # parse group contents
                if group == 2:
                    # anonymous group
                    group = None
                else:
                    group = state.opengroup(name***REMOVED***
                if condgroup:
                    p = _parse_sub_cond(source, state, condgroup***REMOVED***
                else:
                    p = _parse_sub(source, state***REMOVED***
                if not sourcematch("***REMOVED***"***REMOVED***:
                    raise error, "unbalanced parenthesis"
                if group is not None:
                    state.closegroup(group***REMOVED***
                subpatternappend((SUBPATTERN, (group, p***REMOVED******REMOVED******REMOVED***
            else:
                while 1:
                    char = sourceget(***REMOVED***
                    if char is None:
                        raise error, "unexpected end of pattern"
                    if char == "***REMOVED***":
                        break
                    raise error, "unknown extension"

        elif this == "^":
            subpatternappend((AT, AT_BEGINNING***REMOVED******REMOVED***

        elif this == "$":
            subpattern.append((AT, AT_END***REMOVED******REMOVED***

        elif this and this[0***REMOVED*** == "\\":
            code = _escape(source, this, state***REMOVED***
            subpatternappend(code***REMOVED***

        else:
            raise error, "parser error"

    return subpattern

def parse(str, flags=0, pattern=None***REMOVED***:
    # parse 're' pattern into list of (opcode, argument***REMOVED*** tuples

    source = Tokenizer(str***REMOVED***

    if pattern is None:
        pattern = Pattern(***REMOVED***
    pattern.flags = flags
    pattern.str = str

    p = _parse_sub(source, pattern, 0***REMOVED***

    tail = source.get(***REMOVED***
    if tail == "***REMOVED***":
        raise error, "unbalanced parenthesis"
    elif tail:
        raise error, "bogus characters at end of regular expression"

    if flags & SRE_FLAG_DEBUG:
        p.dump(***REMOVED***

    if not (flags & SRE_FLAG_VERBOSE***REMOVED*** and p.pattern.flags & SRE_FLAG_VERBOSE:
        # the VERBOSE flag was switched on inside the pattern.  to be
        # on the safe side, we'll parse the whole thing again...
        return parse(str, p.pattern.flags***REMOVED***

    return p

def parse_template(source, pattern***REMOVED***:
    # parse 're' replacement string into list of literals and
    # group references
    s = Tokenizer(source***REMOVED***
    sget = s.get
    p = [***REMOVED***
    a = p.append
    def literal(literal, p=p, pappend=a***REMOVED***:
        if p and p[-1***REMOVED***[0***REMOVED*** is LITERAL:
            p[-1***REMOVED*** = LITERAL, p[-1***REMOVED***[1***REMOVED*** + literal
        else:
            pappend((LITERAL, literal***REMOVED******REMOVED***
    sep = source[:0***REMOVED***
    if type(sep***REMOVED*** is type(""***REMOVED***:
        makechar = chr
    else:
        makechar = unichr
    while 1:
        this = sget(***REMOVED***
        if this is None:
            break # end of replacement string
        if this and this[0***REMOVED*** == "\\":
            # group
            c = this[1:2***REMOVED***
            if c == "g":
                name = ""
                if s.match("<"***REMOVED***:
                    while 1:
                        char = sget(***REMOVED***
                        if char is None:
                            raise error, "unterminated group name"
                        if char == ">":
                            break
                        name = name + char
                if not name:
                    raise error, "missing group name"
                try:
                    index = int(name***REMOVED***
                    if index < 0:
                        raise error, "negative group number"
                except ValueError:
                    if not isname(name***REMOVED***:
                        raise error, "bad character in group name"
                    try:
                        index = pattern.groupindex[name***REMOVED***
                    except KeyError:
                        raise IndexError, "unknown group name"
                a((MARK, index***REMOVED******REMOVED***
            elif c == "0":
                if s.next in OCTDIGITS:
                    this = this + sget(***REMOVED***
                    if s.next in OCTDIGITS:
                        this = this + sget(***REMOVED***
                literal(makechar(int(this[1:***REMOVED***, 8***REMOVED*** & 0xff***REMOVED******REMOVED***
            elif c in DIGITS:
                isoctal = False
                if s.next in DIGITS:
                    this = this + sget(***REMOVED***
                    if (c in OCTDIGITS and this[2***REMOVED*** in OCTDIGITS and
                        s.next in OCTDIGITS***REMOVED***:
                        this = this + sget(***REMOVED***
                        isoctal = True
                        literal(makechar(int(this[1:***REMOVED***, 8***REMOVED*** & 0xff***REMOVED******REMOVED***
                if not isoctal:
                    a((MARK, int(this[1:***REMOVED******REMOVED******REMOVED******REMOVED***
            else:
                try:
                    this = makechar(ESCAPES[this***REMOVED***[1***REMOVED******REMOVED***
                except KeyError:
                    pass
                literal(this***REMOVED***
        else:
            literal(this***REMOVED***
    # convert template to groups and literals lists
    i = 0
    groups = [***REMOVED***
    groupsappend = groups.append
    literals = [None***REMOVED*** * len(p***REMOVED***
    for c, s in p:
        if c is MARK:
            groupsappend((i, s***REMOVED******REMOVED***
            # literal[i***REMOVED*** is already None
        else:
            literals[i***REMOVED*** = s
        i = i + 1
    return groups, literals

def expand_template(template, match***REMOVED***:
    g = match.group
    sep = match.string[:0***REMOVED***
    groups, literals = template
    literals = literals[:***REMOVED***
    try:
        for index, group in groups:
            literals[index***REMOVED*** = s = g(group***REMOVED***
            if s is None:
                raise error, "unmatched group"
    except IndexError:
        raise error, "invalid group reference"
    return sep.join(literals***REMOVED***
