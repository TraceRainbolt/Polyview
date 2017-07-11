***REMOVED***
Python 'utf-32-le' Codec
***REMOVED***
import codecs

### Codec APIs

encode = codecs.utf_32_le_encode

def decode(input, errors='strict'***REMOVED***:
    return codecs.utf_32_le_decode(input, errors, True***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return codecs.utf_32_le_encode(input, self.errors***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.BufferedIncrementalDecoder***REMOVED***:
    _buffer_decode = codecs.utf_32_le_decode

class StreamWriter(codecs.StreamWriter***REMOVED***:
    encode = codecs.utf_32_le_encode

class StreamReader(codecs.StreamReader***REMOVED***:
    decode = codecs.utf_32_le_decode

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='utf-32-le',
        encode=encode,
        decode=decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
