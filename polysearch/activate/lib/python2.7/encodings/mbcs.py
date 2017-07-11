***REMOVED*** Python 'mbcs' Codec for Windows


Cloned by Mark Hammond (mhammond@skippinet.com.au***REMOVED*** from ascii.py,
which was written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***
# Import them explicitly to cause an ImportError
# on non-Windows systems
from codecs import mbcs_encode, mbcs_decode
# for IncrementalDecoder, IncrementalEncoder, ...
import codecs

### Codec APIs

encode = mbcs_encode

def decode(input, errors='strict'***REMOVED***:
    return mbcs_decode(input, errors, True***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return mbcs_encode(input, self.errors***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.BufferedIncrementalDecoder***REMOVED***:
    _buffer_decode = mbcs_decode

class StreamWriter(codecs.StreamWriter***REMOVED***:
    encode = mbcs_encode

class StreamReader(codecs.StreamReader***REMOVED***:
    decode = mbcs_decode

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='mbcs',
        encode=encode,
        decode=decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
