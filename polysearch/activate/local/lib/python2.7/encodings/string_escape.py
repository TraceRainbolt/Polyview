# -*- coding: iso-8859-1 -*-
***REMOVED*** Python 'escape' Codec


Written by Martin v. Löwis (martin@v.loewis.de***REMOVED***.

***REMOVED***
import codecs

class Codec(codecs.Codec***REMOVED***:

    encode = codecs.escape_encode
    decode = codecs.escape_decode

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return codecs.escape_encode(input, self.errors***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        return codecs.escape_decode(input, self.errors***REMOVED***[0***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='string-escape',
        encode=Codec.encode,
        decode=Codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
