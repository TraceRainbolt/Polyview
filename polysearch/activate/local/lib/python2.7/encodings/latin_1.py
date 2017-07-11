***REMOVED*** Python 'latin-1' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***
import codecs

### Codec APIs

class Codec(codecs.Codec***REMOVED***:

    # Note: Binding these as C functions will result in the class not
    # converting them to methods. This is intended.
    encode = codecs.latin_1_encode
    decode = codecs.latin_1_decode

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return codecs.latin_1_encode(input,self.errors***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        return codecs.latin_1_decode(input,self.errors***REMOVED***[0***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

class StreamConverter(StreamWriter,StreamReader***REMOVED***:

    encode = codecs.latin_1_decode
    decode = codecs.latin_1_encode

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='iso8859-1',
        encode=Codec.encode,
        decode=Codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
