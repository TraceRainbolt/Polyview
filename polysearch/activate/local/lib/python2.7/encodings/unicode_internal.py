***REMOVED*** Python 'unicode-internal' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***
import codecs

### Codec APIs

class Codec(codecs.Codec***REMOVED***:

    # Note: Binding these as C functions will result in the class not
    # converting them to methods. This is intended.
    encode = codecs.unicode_internal_encode
    decode = codecs.unicode_internal_decode

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return codecs.unicode_internal_encode(input, self.errors***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        return codecs.unicode_internal_decode(input, self.errors***REMOVED***[0***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='unicode-internal',
        encode=Codec.encode,
        decode=Codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
