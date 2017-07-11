# This module implements the RFCs 3490 (IDNA***REMOVED*** and 3491 (Nameprep***REMOVED***

import stringprep, re, codecs
from unicodedata import ucd_3_2_0 as unicodedata

# IDNA section 3.1
dots = re.compile(u"[\u002E\u3002\uFF0E\uFF61***REMOVED***"***REMOVED***

# IDNA section 5
ace_prefix = "xn--"
uace_prefix = unicode(ace_prefix, "ascii"***REMOVED***

# This assumes query strings, so AllowUnassigned is true
def nameprep(label***REMOVED***:
    # Map
    newlabel = [***REMOVED***
    for c in label:
        if stringprep.in_table_b1(c***REMOVED***:
            # Map to nothing
            continue
        newlabel.append(stringprep.map_table_b2(c***REMOVED******REMOVED***
    label = u"".join(newlabel***REMOVED***

    # Normalize
    label = unicodedata.normalize("NFKC", label***REMOVED***

    # Prohibit
    for c in label:
        if stringprep.in_table_c12(c***REMOVED*** or \
           stringprep.in_table_c22(c***REMOVED*** or \
           stringprep.in_table_c3(c***REMOVED*** or \
           stringprep.in_table_c4(c***REMOVED*** or \
           stringprep.in_table_c5(c***REMOVED*** or \
           stringprep.in_table_c6(c***REMOVED*** or \
           stringprep.in_table_c7(c***REMOVED*** or \
           stringprep.in_table_c8(c***REMOVED*** or \
           stringprep.in_table_c9(c***REMOVED***:
            raise UnicodeError("Invalid character %r" % c***REMOVED***

    # Check bidi
    RandAL = map(stringprep.in_table_d1, label***REMOVED***
    for c in RandAL:
        if c:
            # There is a RandAL char in the string. Must perform further
            # tests:
            # 1***REMOVED*** The characters in section 5.8 MUST be prohibited.
            # This is table C.8, which was already checked
            # 2***REMOVED*** If a string contains any RandALCat character, the string
            # MUST NOT contain any LCat character.
            if filter(stringprep.in_table_d2, label***REMOVED***:
                raise UnicodeError("Violation of BIDI requirement 2"***REMOVED***

            # 3***REMOVED*** If a string contains any RandALCat character, a
            # RandALCat character MUST be the first character of the
            # string, and a RandALCat character MUST be the last
            # character of the string.
            if not RandAL[0***REMOVED*** or not RandAL[-1***REMOVED***:
                raise UnicodeError("Violation of BIDI requirement 3"***REMOVED***

    return label

def ToASCII(label***REMOVED***:
    try:
        # Step 1: try ASCII
        label = label.encode("ascii"***REMOVED***
    except UnicodeError:
        pass
    else:
        # Skip to step 3: UseSTD3ASCIIRules is false, so
        # Skip to step 8.
        if 0 < len(label***REMOVED*** < 64:
            return label
        raise UnicodeError("label empty or too long"***REMOVED***

    # Step 2: nameprep
    label = nameprep(label***REMOVED***

    # Step 3: UseSTD3ASCIIRules is false
    # Step 4: try ASCII
    try:
        label = label.encode("ascii"***REMOVED***
    except UnicodeError:
        pass
    else:
        # Skip to step 8.
        if 0 < len(label***REMOVED*** < 64:
            return label
        raise UnicodeError("label empty or too long"***REMOVED***

    # Step 5: Check ACE prefix
    if label.startswith(uace_prefix***REMOVED***:
        raise UnicodeError("Label starts with ACE prefix"***REMOVED***

    # Step 6: Encode with PUNYCODE
    label = label.encode("punycode"***REMOVED***

    # Step 7: Prepend ACE prefix
    label = ace_prefix + label

    # Step 8: Check size
    if 0 < len(label***REMOVED*** < 64:
        return label
    raise UnicodeError("label empty or too long"***REMOVED***

def ToUnicode(label***REMOVED***:
    # Step 1: Check for ASCII
    if isinstance(label, str***REMOVED***:
        pure_ascii = True
    else:
        try:
            label = label.encode("ascii"***REMOVED***
            pure_ascii = True
        except UnicodeError:
            pure_ascii = False
    if not pure_ascii:
        # Step 2: Perform nameprep
        label = nameprep(label***REMOVED***
        # It doesn't say this, but apparently, it should be ASCII now
        try:
            label = label.encode("ascii"***REMOVED***
        except UnicodeError:
            raise UnicodeError("Invalid character in IDN label"***REMOVED***
    # Step 3: Check for ACE prefix
    if not label.startswith(ace_prefix***REMOVED***:
        return unicode(label, "ascii"***REMOVED***

    # Step 4: Remove ACE prefix
    label1 = label[len(ace_prefix***REMOVED***:***REMOVED***

    # Step 5: Decode using PUNYCODE
    result = label1.decode("punycode"***REMOVED***

    # Step 6: Apply ToASCII
    label2 = ToASCII(result***REMOVED***

    # Step 7: Compare the result of step 6 with the one of step 3
    # label2 will already be in lower case.
    if label.lower(***REMOVED*** != label2:
        raise UnicodeError("IDNA does not round-trip", label, label2***REMOVED***

    # Step 8: return the result of step 5
    return result

### Codec APIs

class Codec(codecs.Codec***REMOVED***:
    def encode(self,input,errors='strict'***REMOVED***:

        if errors != 'strict':
            # IDNA is quite clear that implementations must be strict
            raise UnicodeError("unsupported error handling "+errors***REMOVED***

        if not input:
            return "", 0

        result = [***REMOVED***
        labels = dots.split(input***REMOVED***
        if labels and len(labels[-1***REMOVED******REMOVED***==0:
            trailing_dot = '.'
            del labels[-1***REMOVED***
        else:
            trailing_dot = ''
        for label in labels:
            result.append(ToASCII(label***REMOVED******REMOVED***
        # Join with U+002E
        return ".".join(result***REMOVED***+trailing_dot, len(input***REMOVED***

    def decode(self,input,errors='strict'***REMOVED***:

        if errors != 'strict':
            raise UnicodeError("Unsupported error handling "+errors***REMOVED***

        if not input:
            return u"", 0

        # IDNA allows decoding to operate on Unicode strings, too.
        if isinstance(input, unicode***REMOVED***:
            labels = dots.split(input***REMOVED***
        else:
            # Must be ASCII string
            input = str(input***REMOVED***
            unicode(input, "ascii"***REMOVED***
            labels = input.split("."***REMOVED***

        if labels and len(labels[-1***REMOVED******REMOVED*** == 0:
            trailing_dot = u'.'
            del labels[-1***REMOVED***
        else:
            trailing_dot = u''

        result = [***REMOVED***
        for label in labels:
            result.append(ToUnicode(label***REMOVED******REMOVED***

        return u".".join(result***REMOVED***+trailing_dot, len(input***REMOVED***

class IncrementalEncoder(codecs.BufferedIncrementalEncoder***REMOVED***:
    def _buffer_encode(self, input, errors, final***REMOVED***:
        if errors != 'strict':
            # IDNA is quite clear that implementations must be strict
            raise UnicodeError("unsupported error handling "+errors***REMOVED***

        if not input:
            return ("", 0***REMOVED***

        labels = dots.split(input***REMOVED***
        trailing_dot = u''
        if labels:
            if not labels[-1***REMOVED***:
                trailing_dot = '.'
                del labels[-1***REMOVED***
            elif not final:
                # Keep potentially unfinished label until the next call
                del labels[-1***REMOVED***
                if labels:
                    trailing_dot = '.'

        result = [***REMOVED***
        size = 0
        for label in labels:
            result.append(ToASCII(label***REMOVED******REMOVED***
            if size:
                size += 1
            size += len(label***REMOVED***

        # Join with U+002E
        result = ".".join(result***REMOVED*** + trailing_dot
        size += len(trailing_dot***REMOVED***
        return (result, size***REMOVED***

class IncrementalDecoder(codecs.BufferedIncrementalDecoder***REMOVED***:
    def _buffer_decode(self, input, errors, final***REMOVED***:
        if errors != 'strict':
            raise UnicodeError("Unsupported error handling "+errors***REMOVED***

        if not input:
            return (u"", 0***REMOVED***

        # IDNA allows decoding to operate on Unicode strings, too.
        if isinstance(input, unicode***REMOVED***:
            labels = dots.split(input***REMOVED***
        else:
            # Must be ASCII string
            input = str(input***REMOVED***
            unicode(input, "ascii"***REMOVED***
            labels = input.split("."***REMOVED***

        trailing_dot = u''
        if labels:
            if not labels[-1***REMOVED***:
                trailing_dot = u'.'
                del labels[-1***REMOVED***
            elif not final:
                # Keep potentially unfinished label until the next call
                del labels[-1***REMOVED***
                if labels:
                    trailing_dot = u'.'

        result = [***REMOVED***
        size = 0
        for label in labels:
            result.append(ToUnicode(label***REMOVED******REMOVED***
            if size:
                size += 1
            size += len(label***REMOVED***

        result = u".".join(result***REMOVED*** + trailing_dot
        size += len(trailing_dot***REMOVED***
        return (result, size***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='idna',
        encode=Codec(***REMOVED***.encode,
        decode=Codec(***REMOVED***.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
