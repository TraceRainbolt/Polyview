***REMOVED*** Python 'bz2_codec' Codec - bz2 compression encoding

    Unlike most of the other codecs which target Unicode, this codec
    will return Python string objects for both encode and decode.

    Adapted by Raymond Hettinger from zlib_codec.py which was written
    by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

***REMOVED***
import codecs
import bz2 # this codec needs the optional bz2 module !

### Codec APIs

def bz2_encode(input,errors='strict'***REMOVED***:

    ***REMOVED*** Encodes the object input and returns a tuple (output
        object, length consumed***REMOVED***.

        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.

    ***REMOVED***
    assert errors == 'strict'
    output = bz2.compress(input***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

def bz2_decode(input,errors='strict'***REMOVED***:

    ***REMOVED*** Decodes the object input and returns a tuple (output
        object, length consumed***REMOVED***.

        input must be an object which provides the bf_getreadbuf
        buffer slot. Python strings, buffer objects and memory
        mapped files are examples of objects providing this slot.

        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.

    ***REMOVED***
    assert errors == 'strict'
    output = bz2.decompress(input***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

class Codec(codecs.Codec***REMOVED***:

    def encode(self, input, errors='strict'***REMOVED***:
        return bz2_encode(input, errors***REMOVED***
    def decode(self, input, errors='strict'***REMOVED***:
        return bz2_decode(input, errors***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        assert errors == 'strict'
        self.errors = errors
        self.compressobj = bz2.BZ2Compressor(***REMOVED***

    def encode(self, input, final=False***REMOVED***:
        if final:
            c = self.compressobj.compress(input***REMOVED***
            return c + self.compressobj.flush(***REMOVED***
        else:
            return self.compressobj.compress(input***REMOVED***

    def reset(self***REMOVED***:
        self.compressobj = bz2.BZ2Compressor(***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        assert errors == 'strict'
        self.errors = errors
        self.decompressobj = bz2.BZ2Decompressor(***REMOVED***

    def decode(self, input, final=False***REMOVED***:
        try:
            return self.decompressobj.decompress(input***REMOVED***
        except EOFError:
            return ''

    def reset(self***REMOVED***:
        self.decompressobj = bz2.BZ2Decompressor(***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name="bz2",
        encode=bz2_encode,
        decode=bz2_decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
