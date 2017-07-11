***REMOVED*** Python 'undefined' Codec

    This codec will always raise a ValueError exception when being
    used. It is intended for use by the site.py file to switch off
    automatic string to Unicode coercion.

Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***
import codecs

### Codec APIs

class Codec(codecs.Codec***REMOVED***:

    def encode(self,input,errors='strict'***REMOVED***:
        raise UnicodeError("undefined encoding"***REMOVED***

    def decode(self,input,errors='strict'***REMOVED***:
        raise UnicodeError("undefined encoding"***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        raise UnicodeError("undefined encoding"***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        raise UnicodeError("undefined encoding"***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='undefined',
        encode=Codec(***REMOVED***.encode,
        decode=Codec(***REMOVED***.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
