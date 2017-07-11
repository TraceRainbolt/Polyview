# -*- coding: iso-8859-1 -*-
***REMOVED*** Codec for the Punicode encoding, as specified in RFC 3492

Written by Martin v. Löwis.
***REMOVED***

import codecs

##################### Encoding #####################################

def segregate(str***REMOVED***:
    ***REMOVED***3.1 Basic code point segregation***REMOVED***
    base = [***REMOVED***
    extended = {***REMOVED***
    for c in str:
        if ord(c***REMOVED*** < 128:
            base.append(c***REMOVED***
        else:
            extended[c***REMOVED*** = 1
    extended = extended.keys(***REMOVED***
    extended.sort(***REMOVED***
    return "".join(base***REMOVED***.encode("ascii"***REMOVED***,extended

def selective_len(str, max***REMOVED***:
    ***REMOVED***Return the length of str, considering only characters below max.***REMOVED***
    res = 0
    for c in str:
        if ord(c***REMOVED*** < max:
            res += 1
    return res

def selective_find(str, char, index, pos***REMOVED***:
    ***REMOVED***Return a pair (index, pos***REMOVED***, indicating the next occurrence of
    char in str. index is the position of the character considering
    only ordinals up to and including char, and pos is the position in
    the full string. index/pos is the starting position in the full
    string.***REMOVED***

    l = len(str***REMOVED***
    while 1:
        pos += 1
        if pos == l:
            return (-1, -1***REMOVED***
        c = str[pos***REMOVED***
        if c == char:
            return index+1, pos
        elif c < char:
            index += 1

def insertion_unsort(str, extended***REMOVED***:
    ***REMOVED***3.2 Insertion unsort coding***REMOVED***
    oldchar = 0x80
    result = [***REMOVED***
    oldindex = -1
    for c in extended:
        index = pos = -1
        char = ord(c***REMOVED***
        curlen = selective_len(str, char***REMOVED***
        delta = (curlen+1***REMOVED*** * (char - oldchar***REMOVED***
        while 1:
            index,pos = selective_find(str,c,index,pos***REMOVED***
            if index == -1:
                break
            delta += index - oldindex
            result.append(delta-1***REMOVED***
            oldindex = index
            delta = 0
        oldchar = char

    return result

def T(j, bias***REMOVED***:
    # Punycode parameters: tmin = 1, tmax = 26, base = 36
    res = 36 * (j + 1***REMOVED*** - bias
    if res < 1: return 1
    if res > 26: return 26
    return res

digits = "abcdefghijklmnopqrstuvwxyz0123456789"
def generate_generalized_integer(N, bias***REMOVED***:
    ***REMOVED***3.3 Generalized variable-length integers***REMOVED***
    result = [***REMOVED***
    j = 0
    while 1:
        t = T(j, bias***REMOVED***
        if N < t:
            result.append(digits[N***REMOVED******REMOVED***
            return result
        result.append(digits[t + ((N - t***REMOVED*** % (36 - t***REMOVED******REMOVED******REMOVED******REMOVED***
        N = (N - t***REMOVED*** // (36 - t***REMOVED***
        j += 1

def adapt(delta, first, numchars***REMOVED***:
    if first:
        delta //= 700
    else:
        delta //= 2
    delta += delta // numchars
    # ((base - tmin***REMOVED*** * tmax***REMOVED*** // 2 == 455
    divisions = 0
    while delta > 455:
        delta = delta // 35 # base - tmin
        divisions += 36
    bias = divisions + (36 * delta // (delta + 38***REMOVED******REMOVED***
    return bias


def generate_integers(baselen, deltas***REMOVED***:
    ***REMOVED***3.4 Bias adaptation***REMOVED***
    # Punycode parameters: initial bias = 72, damp = 700, skew = 38
    result = [***REMOVED***
    bias = 72
    for points, delta in enumerate(deltas***REMOVED***:
        s = generate_generalized_integer(delta, bias***REMOVED***
        result.extend(s***REMOVED***
        bias = adapt(delta, points==0, baselen+points+1***REMOVED***
    return "".join(result***REMOVED***

def punycode_encode(text***REMOVED***:
    base, extended = segregate(text***REMOVED***
    base = base.encode("ascii"***REMOVED***
    deltas = insertion_unsort(text, extended***REMOVED***
    extended = generate_integers(len(base***REMOVED***, deltas***REMOVED***
    if base:
        return base + "-" + extended
    return extended

##################### Decoding #####################################

def decode_generalized_number(extended, extpos, bias, errors***REMOVED***:
    ***REMOVED***3.3 Generalized variable-length integers***REMOVED***
    result = 0
    w = 1
    j = 0
    while 1:
        try:
            char = ord(extended[extpos***REMOVED******REMOVED***
        except IndexError:
            if errors == "strict":
                raise UnicodeError, "incomplete punicode string"
            return extpos + 1, None
        extpos += 1
        if 0x41 <= char <= 0x5A: # A-Z
            digit = char - 0x41
        elif 0x30 <= char <= 0x39:
            digit = char - 22 # 0x30-26
        elif errors == "strict":
            raise UnicodeError("Invalid extended code point '%s'"
                               % extended[extpos***REMOVED******REMOVED***
        else:
            return extpos, None
        t = T(j, bias***REMOVED***
        result += digit * w
        if digit < t:
            return extpos, result
        w = w * (36 - t***REMOVED***
        j += 1


def insertion_sort(base, extended, errors***REMOVED***:
    ***REMOVED***3.2 Insertion unsort coding***REMOVED***
    char = 0x80
    pos = -1
    bias = 72
    extpos = 0
    while extpos < len(extended***REMOVED***:
        newpos, delta = decode_generalized_number(extended, extpos,
                                                  bias, errors***REMOVED***
        if delta is None:
            # There was an error in decoding. We can't continue because
            # synchronization is lost.
            return base
        pos += delta+1
        char += pos // (len(base***REMOVED*** + 1***REMOVED***
        if char > 0x10FFFF:
            if errors == "strict":
                raise UnicodeError, ("Invalid character U+%x" % char***REMOVED***
            char = ord('?'***REMOVED***
        pos = pos % (len(base***REMOVED*** + 1***REMOVED***
        base = base[:pos***REMOVED*** + unichr(char***REMOVED*** + base[pos:***REMOVED***
        bias = adapt(delta, (extpos == 0***REMOVED***, len(base***REMOVED******REMOVED***
        extpos = newpos
    return base

def punycode_decode(text, errors***REMOVED***:
    pos = text.rfind("-"***REMOVED***
    if pos == -1:
        base = ""
        extended = text
    else:
        base = text[:pos***REMOVED***
        extended = text[pos+1:***REMOVED***
    base = unicode(base, "ascii", errors***REMOVED***
    extended = extended.upper(***REMOVED***
    return insertion_sort(base, extended, errors***REMOVED***

### Codec APIs

class Codec(codecs.Codec***REMOVED***:

    def encode(self,input,errors='strict'***REMOVED***:
        res = punycode_encode(input***REMOVED***
        return res, len(input***REMOVED***

    def decode(self,input,errors='strict'***REMOVED***:
        if errors not in ('strict', 'replace', 'ignore'***REMOVED***:
            raise UnicodeError, "Unsupported error handling "+errors
        res = punycode_decode(input, errors***REMOVED***
        return res, len(input***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return punycode_encode(input***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        if self.errors not in ('strict', 'replace', 'ignore'***REMOVED***:
            raise UnicodeError, "Unsupported error handling "+self.errors
        return punycode_decode(input, self.errors***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='punycode',
        encode=Codec(***REMOVED***.encode,
        decode=Codec(***REMOVED***.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
