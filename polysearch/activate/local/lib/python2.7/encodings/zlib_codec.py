***REMOVED*** Python 'zlib_codec' Codec - zlib compression encoding

    Unlike most of the other codecs which target Unicode, this codec
    will return Python string objects for both encode and decode.

    Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

***REMOVED***
import codecs
import zlib # this codec needs the optional zlib module !

### Codec APIs

def zlib_encode(input,errors='strict'***REMOVED***:

    ***REMOVED*** Encodes the object input and returns a tuple (output
        object, length consumed***REMOVED***.

        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.

    ***REMOVED***
    assert errors == 'strict'
    output = zlib.compress(input***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

def zlib_decode(input,errors='strict'***REMOVED***:

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
    output = zlib.decompress(input***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

class Codec(codecs.Codec***REMOVED***:

    def encode(self, input, errors='strict'***REMOVED***:
        return zlib_encode(input, errors***REMOVED***
    def decode(self, input, errors='strict'***REMOVED***:
        return zlib_decode(input, errors***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        assert errors == 'strict'
        self.errors = errors
        self.compressobj = zlib.compressobj(***REMOVED***

    def encode(self, input, final=False***REMOVED***:
        if final:
            c = self.compressobj.compress(input***REMOVED***
            return c + self.compressobj.flush(***REMOVED***
        else:
            return self.compressobj.compress(input***REMOVED***

    def reset(self***REMOVED***:
        self.compressobj = zlib.compressobj(***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        assert errors == 'strict'
        self.errors = errors
        self.decompressobj = zlib.decompressobj(***REMOVED***

    def decode(self, input, final=False***REMOVED***:
        if final:
            c = self.decompressobj.decompress(input***REMOVED***
            return c + self.decompressobj.flush(***REMOVED***
        else:
            return self.decompressobj.decompress(input***REMOVED***

    def reset(self***REMOVED***:
        self.decompressobj = zlib.decompressobj(***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='zlib',
        encode=zlib_encode,
        decode=zlib_decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
