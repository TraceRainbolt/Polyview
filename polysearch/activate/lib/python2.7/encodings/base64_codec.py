***REMOVED*** Python 'base64_codec' Codec - base64 content transfer encoding

    Unlike most of the other codecs which target Unicode, this codec
    will return Python string objects for both encode and decode.

    Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

***REMOVED***
import codecs, base64

### Codec APIs

def base64_encode(input,errors='strict'***REMOVED***:

    ***REMOVED*** Encodes the object input and returns a tuple (output
        object, length consumed***REMOVED***.

        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.

    ***REMOVED***
    assert errors == 'strict'
    output = base64.encodestring(input***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

def base64_decode(input,errors='strict'***REMOVED***:

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
    output = base64.decodestring(input***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

class Codec(codecs.Codec***REMOVED***:

    def encode(self, input,errors='strict'***REMOVED***:
        return base64_encode(input,errors***REMOVED***
    def decode(self, input,errors='strict'***REMOVED***:
        return base64_decode(input,errors***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        assert self.errors == 'strict'
        return base64.encodestring(input***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        assert self.errors == 'strict'
        return base64.decodestring(input***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='base64',
        encode=base64_encode,
        decode=base64_decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
