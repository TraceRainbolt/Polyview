#
# Secret Labs' Regular Expression Engine
#
# convert template to internal format
#
# Copyright (c***REMOVED*** 1997-2001 by Secret Labs AB.  All rights reserved.
#
# See the sre.py file for information on usage and redistribution.
#

***REMOVED***Internal support module for sre***REMOVED***

import _sre, sys
import sre_parse
from sre_constants import *

assert _sre.MAGIC == MAGIC, "SRE module mismatch"

if _sre.CODESIZE == 2:
    MAXCODE = 65535
else:
    MAXCODE = 0xFFFFFFFFL

def _identityfunction(x***REMOVED***:
    return x

_LITERAL_CODES = set([LITERAL, NOT_LITERAL***REMOVED******REMOVED***
_REPEATING_CODES = set([REPEAT, MIN_REPEAT, MAX_REPEAT***REMOVED******REMOVED***
_SUCCESS_CODES = set([SUCCESS, FAILURE***REMOVED******REMOVED***
_ASSERT_CODES = set([ASSERT, ASSERT_NOT***REMOVED******REMOVED***

def _compile(code, pattern, flags***REMOVED***:
    # internal: compile a (sub***REMOVED***pattern
    emit = code.append
    _len = len
    LITERAL_CODES = _LITERAL_CODES
    REPEATING_CODES = _REPEATING_CODES
    SUCCESS_CODES = _SUCCESS_CODES
    ASSERT_CODES = _ASSERT_CODES
    for op, av in pattern:
        if op in LITERAL_CODES:
            if flags & SRE_FLAG_IGNORECASE:
                emit(OPCODES[OP_IGNORE[op***REMOVED******REMOVED******REMOVED***
                emit(_sre.getlower(av, flags***REMOVED******REMOVED***
            else:
                emit(OPCODES[op***REMOVED******REMOVED***
                emit(av***REMOVED***
        elif op is IN:
            if flags & SRE_FLAG_IGNORECASE:
                emit(OPCODES[OP_IGNORE[op***REMOVED******REMOVED******REMOVED***
                def fixup(literal, flags=flags***REMOVED***:
                    return _sre.getlower(literal, flags***REMOVED***
            else:
                emit(OPCODES[op***REMOVED******REMOVED***
                fixup = _identityfunction
            skip = _len(code***REMOVED***; emit(0***REMOVED***
            _compile_charset(av, flags, code, fixup***REMOVED***
            code[skip***REMOVED*** = _len(code***REMOVED*** - skip
        elif op is ANY:
            if flags & SRE_FLAG_DOTALL:
                emit(OPCODES[ANY_ALL***REMOVED******REMOVED***
            else:
                emit(OPCODES[ANY***REMOVED******REMOVED***
        elif op in REPEATING_CODES:
            if flags & SRE_FLAG_TEMPLATE:
                raise error, "internal: unsupported template operator"
                emit(OPCODES[REPEAT***REMOVED******REMOVED***
                skip = _len(code***REMOVED***; emit(0***REMOVED***
                emit(av[0***REMOVED******REMOVED***
                emit(av[1***REMOVED******REMOVED***
                _compile(code, av[2***REMOVED***, flags***REMOVED***
                emit(OPCODES[SUCCESS***REMOVED******REMOVED***
                code[skip***REMOVED*** = _len(code***REMOVED*** - skip
            elif _simple(av***REMOVED*** and op is not REPEAT:
                if op is MAX_REPEAT:
                    emit(OPCODES[REPEAT_ONE***REMOVED******REMOVED***
                else:
                    emit(OPCODES[MIN_REPEAT_ONE***REMOVED******REMOVED***
                skip = _len(code***REMOVED***; emit(0***REMOVED***
                emit(av[0***REMOVED******REMOVED***
                emit(av[1***REMOVED******REMOVED***
                _compile(code, av[2***REMOVED***, flags***REMOVED***
                emit(OPCODES[SUCCESS***REMOVED******REMOVED***
                code[skip***REMOVED*** = _len(code***REMOVED*** - skip
            else:
                emit(OPCODES[REPEAT***REMOVED******REMOVED***
                skip = _len(code***REMOVED***; emit(0***REMOVED***
                emit(av[0***REMOVED******REMOVED***
                emit(av[1***REMOVED******REMOVED***
                _compile(code, av[2***REMOVED***, flags***REMOVED***
                code[skip***REMOVED*** = _len(code***REMOVED*** - skip
                if op is MAX_REPEAT:
                    emit(OPCODES[MAX_UNTIL***REMOVED******REMOVED***
                else:
                    emit(OPCODES[MIN_UNTIL***REMOVED******REMOVED***
        elif op is SUBPATTERN:
            if av[0***REMOVED***:
                emit(OPCODES[MARK***REMOVED******REMOVED***
                emit((av[0***REMOVED***-1***REMOVED****2***REMOVED***
            # _compile_info(code, av[1***REMOVED***, flags***REMOVED***
            _compile(code, av[1***REMOVED***, flags***REMOVED***
            if av[0***REMOVED***:
                emit(OPCODES[MARK***REMOVED******REMOVED***
                emit((av[0***REMOVED***-1***REMOVED****2+1***REMOVED***
        elif op in SUCCESS_CODES:
            emit(OPCODES[op***REMOVED******REMOVED***
        elif op in ASSERT_CODES:
            emit(OPCODES[op***REMOVED******REMOVED***
            skip = _len(code***REMOVED***; emit(0***REMOVED***
            if av[0***REMOVED*** >= 0:
                emit(0***REMOVED*** # look ahead
            else:
                lo, hi = av[1***REMOVED***.getwidth(***REMOVED***
                if lo != hi:
                    raise error, "look-behind requires fixed-width pattern"
                emit(lo***REMOVED*** # look behind
            _compile(code, av[1***REMOVED***, flags***REMOVED***
            emit(OPCODES[SUCCESS***REMOVED******REMOVED***
            code[skip***REMOVED*** = _len(code***REMOVED*** - skip
        elif op is CALL:
            emit(OPCODES[op***REMOVED******REMOVED***
            skip = _len(code***REMOVED***; emit(0***REMOVED***
            _compile(code, av, flags***REMOVED***
            emit(OPCODES[SUCCESS***REMOVED******REMOVED***
            code[skip***REMOVED*** = _len(code***REMOVED*** - skip
        elif op is AT:
            emit(OPCODES[op***REMOVED******REMOVED***
            if flags & SRE_FLAG_MULTILINE:
                av = AT_MULTILINE.get(av, av***REMOVED***
            if flags & SRE_FLAG_LOCALE:
                av = AT_LOCALE.get(av, av***REMOVED***
            elif flags & SRE_FLAG_UNICODE:
                av = AT_UNICODE.get(av, av***REMOVED***
            emit(ATCODES[av***REMOVED******REMOVED***
        elif op is BRANCH:
            emit(OPCODES[op***REMOVED******REMOVED***
            tail = [***REMOVED***
            tailappend = tail.append
            for av in av[1***REMOVED***:
                skip = _len(code***REMOVED***; emit(0***REMOVED***
                # _compile_info(code, av, flags***REMOVED***
                _compile(code, av, flags***REMOVED***
                emit(OPCODES[JUMP***REMOVED******REMOVED***
                tailappend(_len(code***REMOVED******REMOVED***; emit(0***REMOVED***
                code[skip***REMOVED*** = _len(code***REMOVED*** - skip
            emit(0***REMOVED*** # end of branch
            for tail in tail:
                code[tail***REMOVED*** = _len(code***REMOVED*** - tail
        elif op is CATEGORY:
            emit(OPCODES[op***REMOVED******REMOVED***
            if flags & SRE_FLAG_LOCALE:
                av = CH_LOCALE[av***REMOVED***
            elif flags & SRE_FLAG_UNICODE:
                av = CH_UNICODE[av***REMOVED***
            emit(CHCODES[av***REMOVED******REMOVED***
        elif op is GROUPREF:
            if flags & SRE_FLAG_IGNORECASE:
                emit(OPCODES[OP_IGNORE[op***REMOVED******REMOVED******REMOVED***
            else:
                emit(OPCODES[op***REMOVED******REMOVED***
            emit(av-1***REMOVED***
        elif op is GROUPREF_EXISTS:
            emit(OPCODES[op***REMOVED******REMOVED***
            emit(av[0***REMOVED***-1***REMOVED***
            skipyes = _len(code***REMOVED***; emit(0***REMOVED***
            _compile(code, av[1***REMOVED***, flags***REMOVED***
            if av[2***REMOVED***:
                emit(OPCODES[JUMP***REMOVED******REMOVED***
                skipno = _len(code***REMOVED***; emit(0***REMOVED***
                code[skipyes***REMOVED*** = _len(code***REMOVED*** - skipyes + 1
                _compile(code, av[2***REMOVED***, flags***REMOVED***
                code[skipno***REMOVED*** = _len(code***REMOVED*** - skipno
            else:
                code[skipyes***REMOVED*** = _len(code***REMOVED*** - skipyes + 1
        else:
            raise ValueError, ("unsupported operand type", op***REMOVED***

def _compile_charset(charset, flags, code, fixup=None***REMOVED***:
    # compile charset subprogram
    emit = code.append
    if fixup is None:
        fixup = _identityfunction
    for op, av in _optimize_charset(charset, fixup***REMOVED***:
        emit(OPCODES[op***REMOVED******REMOVED***
        if op is NEGATE:
            pass
        elif op is LITERAL:
            emit(fixup(av***REMOVED******REMOVED***
        elif op is RANGE:
            emit(fixup(av[0***REMOVED******REMOVED******REMOVED***
            emit(fixup(av[1***REMOVED******REMOVED******REMOVED***
        elif op is CHARSET:
            code.extend(av***REMOVED***
        elif op is BIGCHARSET:
            code.extend(av***REMOVED***
        elif op is CATEGORY:
            if flags & SRE_FLAG_LOCALE:
                emit(CHCODES[CH_LOCALE[av***REMOVED******REMOVED******REMOVED***
            elif flags & SRE_FLAG_UNICODE:
                emit(CHCODES[CH_UNICODE[av***REMOVED******REMOVED******REMOVED***
            else:
                emit(CHCODES[av***REMOVED******REMOVED***
        else:
            raise error, "internal: unsupported set operator"
    emit(OPCODES[FAILURE***REMOVED******REMOVED***

def _optimize_charset(charset, fixup***REMOVED***:
    # internal: optimize character set
    out = [***REMOVED***
    outappend = out.append
    charmap = [0***REMOVED****256
    try:
        for op, av in charset:
            if op is NEGATE:
                outappend((op, av***REMOVED******REMOVED***
            elif op is LITERAL:
                charmap[fixup(av***REMOVED******REMOVED*** = 1
            elif op is RANGE:
                for i in range(fixup(av[0***REMOVED******REMOVED***, fixup(av[1***REMOVED******REMOVED***+1***REMOVED***:
                    charmap[i***REMOVED*** = 1
            elif op is CATEGORY:
                # XXX: could append to charmap tail
                return charset # cannot compress
    except IndexError:
        # character set contains unicode characters
        return _optimize_unicode(charset, fixup***REMOVED***
    # compress character map
    i = p = n = 0
    runs = [***REMOVED***
    runsappend = runs.append
    for c in charmap:
        if c:
            if n == 0:
                p = i
            n = n + 1
        elif n:
            runsappend((p, n***REMOVED******REMOVED***
            n = 0
        i = i + 1
    if n:
        runsappend((p, n***REMOVED******REMOVED***
    if len(runs***REMOVED*** <= 2:
        # use literal/range
        for p, n in runs:
            if n == 1:
                outappend((LITERAL, p***REMOVED******REMOVED***
            else:
                outappend((RANGE, (p, p+n-1***REMOVED******REMOVED******REMOVED***
        if len(out***REMOVED*** < len(charset***REMOVED***:
            return out
    else:
        # use bitmap
        data = _mk_bitmap(charmap***REMOVED***
        outappend((CHARSET, data***REMOVED******REMOVED***
        return out
    return charset

def _mk_bitmap(bits***REMOVED***:
    data = [***REMOVED***
    dataappend = data.append
    if _sre.CODESIZE == 2:
        start = (1, 0***REMOVED***
    else:
        start = (1L, 0L***REMOVED***
    m, v = start
    for c in bits:
        if c:
            v = v + m
        m = m + m
        if m > MAXCODE:
            dataappend(v***REMOVED***
            m, v = start
    return data

# To represent a big charset, first a bitmap of all characters in the
# set is constructed. Then, this bitmap is sliced into chunks of 256
# characters, duplicate chunks are eliminated, and each chunk is
# given a number. In the compiled expression, the charset is
# represented by a 32-bit word sequence, consisting of one word for
# the number of different chunks, a sequence of 256 bytes (64 words***REMOVED***
# of chunk numbers indexed by their original chunk position, and a
# sequence of 256-bit chunks (8 words each***REMOVED***.

# Compression is normally good: in a typical charset, large ranges of
# Unicode will be either completely excluded (e.g. if only cyrillic
# letters are to be matched***REMOVED***, or completely included (e.g. if large
# subranges of Kanji match***REMOVED***. These ranges will be represented by
# chunks of all one-bits or all zero-bits.

# Matching can be also done efficiently: the more significant byte of
# the Unicode character is an index into the chunk number, and the
# less significant byte is a bit index in the chunk (just like the
# CHARSET matching***REMOVED***.

# In UCS-4 mode, the BIGCHARSET opcode still supports only subsets
# of the basic multilingual plane; an efficient representation
# for all of Unicode has not yet been developed. This means,
# in particular, that negated charsets cannot be represented as
# bigcharsets.

def _optimize_unicode(charset, fixup***REMOVED***:
    try:
        import array
    except ImportError:
        return charset
    charmap = [0***REMOVED****65536
    negate = 0
    try:
        for op, av in charset:
            if op is NEGATE:
                negate = 1
            elif op is LITERAL:
                charmap[fixup(av***REMOVED******REMOVED*** = 1
            elif op is RANGE:
                for i in xrange(fixup(av[0***REMOVED******REMOVED***, fixup(av[1***REMOVED******REMOVED***+1***REMOVED***:
                    charmap[i***REMOVED*** = 1
            elif op is CATEGORY:
                # XXX: could expand category
                return charset # cannot compress
    except IndexError:
        # non-BMP characters
        return charset
    if negate:
        if sys.maxunicode != 65535:
            # XXX: negation does not work with big charsets
            return charset
        for i in xrange(65536***REMOVED***:
            charmap[i***REMOVED*** = not charmap[i***REMOVED***
    comps = {***REMOVED***
    mapping = [0***REMOVED****256
    block = 0
    data = [***REMOVED***
    for i in xrange(256***REMOVED***:
        chunk = tuple(charmap[i*256:(i+1***REMOVED****256***REMOVED******REMOVED***
        new = comps.setdefault(chunk, block***REMOVED***
        mapping[i***REMOVED*** = new
        if new == block:
            block = block + 1
            data = data + _mk_bitmap(chunk***REMOVED***
    header = [block***REMOVED***
    if _sre.CODESIZE == 2:
        code = 'H'
    else:
        code = 'I'
    # Convert block indices to byte array of 256 bytes
    mapping = array.array('B', mapping***REMOVED***.tostring(***REMOVED***
    # Convert byte array to word array
    mapping = array.array(code, mapping***REMOVED***
    assert mapping.itemsize == _sre.CODESIZE
    header = header + mapping.tolist(***REMOVED***
    data[0:0***REMOVED*** = header
    return [(BIGCHARSET, data***REMOVED******REMOVED***

def _simple(av***REMOVED***:
    # check if av is a "simple" operator
    lo, hi = av[2***REMOVED***.getwidth(***REMOVED***
    return lo == hi == 1 and av[2***REMOVED***[0***REMOVED***[0***REMOVED*** != SUBPATTERN

def _compile_info(code, pattern, flags***REMOVED***:
    # internal: compile an info block.  in the current version,
    # this contains min/max pattern width, and an optional literal
    # prefix or a character map
    lo, hi = pattern.getwidth(***REMOVED***
    if lo == 0:
        return # not worth it
    # look for a literal prefix
    prefix = [***REMOVED***
    prefixappend = prefix.append
    prefix_skip = 0
    charset = [***REMOVED*** # not used
    charsetappend = charset.append
    if not (flags & SRE_FLAG_IGNORECASE***REMOVED***:
        # look for literal prefix
        for op, av in pattern.data:
            if op is LITERAL:
                if len(prefix***REMOVED*** == prefix_skip:
                    prefix_skip = prefix_skip + 1
                prefixappend(av***REMOVED***
            elif op is SUBPATTERN and len(av[1***REMOVED******REMOVED*** == 1:
                op, av = av[1***REMOVED***[0***REMOVED***
                if op is LITERAL:
                    prefixappend(av***REMOVED***
                else:
                    break
            else:
                break
        # if no prefix, look for charset prefix
        if not prefix and pattern.data:
            op, av = pattern.data[0***REMOVED***
            if op is SUBPATTERN and av[1***REMOVED***:
                op, av = av[1***REMOVED***[0***REMOVED***
                if op is LITERAL:
                    charsetappend((op, av***REMOVED******REMOVED***
                elif op is BRANCH:
                    c = [***REMOVED***
                    cappend = c.append
                    for p in av[1***REMOVED***:
                        if not p:
                            break
                        op, av = p[0***REMOVED***
                        if op is LITERAL:
                            cappend((op, av***REMOVED******REMOVED***
                        else:
                            break
                    else:
                        charset = c
            elif op is BRANCH:
                c = [***REMOVED***
                cappend = c.append
                for p in av[1***REMOVED***:
                    if not p:
                        break
                    op, av = p[0***REMOVED***
                    if op is LITERAL:
                        cappend((op, av***REMOVED******REMOVED***
                    else:
                        break
                else:
                    charset = c
            elif op is IN:
                charset = av
##     if prefix:
##         print "*** PREFIX", prefix, prefix_skip
##     if charset:
##         print "*** CHARSET", charset
    # add an info block
    emit = code.append
    emit(OPCODES[INFO***REMOVED******REMOVED***
    skip = len(code***REMOVED***; emit(0***REMOVED***
    # literal flag
    mask = 0
    if prefix:
        mask = SRE_INFO_PREFIX
        if len(prefix***REMOVED*** == prefix_skip == len(pattern.data***REMOVED***:
            mask = mask + SRE_INFO_LITERAL
    elif charset:
        mask = mask + SRE_INFO_CHARSET
    emit(mask***REMOVED***
    # pattern length
    if lo < MAXCODE:
        emit(lo***REMOVED***
    else:
        emit(MAXCODE***REMOVED***
        prefix = prefix[:MAXCODE***REMOVED***
    if hi < MAXCODE:
        emit(hi***REMOVED***
    else:
        emit(0***REMOVED***
    # add literal prefix
    if prefix:
        emit(len(prefix***REMOVED******REMOVED*** # length
        emit(prefix_skip***REMOVED*** # skip
        code.extend(prefix***REMOVED***
        # generate overlap table
        table = [-1***REMOVED*** + ([0***REMOVED****len(prefix***REMOVED******REMOVED***
        for i in xrange(len(prefix***REMOVED******REMOVED***:
            table[i+1***REMOVED*** = table[i***REMOVED***+1
            while table[i+1***REMOVED*** > 0 and prefix[i***REMOVED*** != prefix[table[i+1***REMOVED***-1***REMOVED***:
                table[i+1***REMOVED*** = table[table[i+1***REMOVED***-1***REMOVED***+1
        code.extend(table[1:***REMOVED******REMOVED*** # don't store first entry
    elif charset:
        _compile_charset(charset, flags, code***REMOVED***
    code[skip***REMOVED*** = len(code***REMOVED*** - skip

try:
    unicode
except NameError:
    STRING_TYPES = (type(""***REMOVED***,***REMOVED***
else:
    STRING_TYPES = (type(""***REMOVED***, type(unicode(""***REMOVED******REMOVED******REMOVED***

def isstring(obj***REMOVED***:
    for tp in STRING_TYPES:
        if isinstance(obj, tp***REMOVED***:
            return 1
    return 0

def _code(p, flags***REMOVED***:

    flags = p.pattern.flags | flags
    code = [***REMOVED***

    # compile info block
    _compile_info(code, p, flags***REMOVED***

    # compile the pattern
    _compile(code, p.data, flags***REMOVED***

    code.append(OPCODES[SUCCESS***REMOVED******REMOVED***

    return code

def compile(p, flags=0***REMOVED***:
    # internal: convert pattern list to internal format

    if isstring(p***REMOVED***:
        pattern = p
        p = sre_parse.parse(p, flags***REMOVED***
    else:
        pattern = None

    code = _code(p, flags***REMOVED***

    # print code

    # XXX: <fl> get rid of this limitation!
    if p.pattern.groups > 100:
        raise AssertionError(
            "sorry, but this version only supports 100 named groups"
            ***REMOVED***

    # map in either direction
    groupindex = p.pattern.groupdict
    indexgroup = [None***REMOVED*** * p.pattern.groups
    for k, i in groupindex.items(***REMOVED***:
        indexgroup[i***REMOVED*** = k

    return _sre.compile(
        pattern, flags | p.pattern.flags, code,
        p.pattern.groups-1,
        groupindex, indexgroup
        ***REMOVED***
