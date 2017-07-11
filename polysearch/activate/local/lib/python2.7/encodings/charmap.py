***REMOVED*** Generic Python Character Mapping Codec.

    Use this codec directly rather than through the automatic
    conversion mechanisms supplied by unicode(***REMOVED*** and .encode(***REMOVED***.


Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***#"

import codecs

### Codec APIs

class Codec(codecs.Codec***REMOVED***:

    # Note: Binding these as C functions will result in the class not
    # converting them to methods. This is intended.
    encode = codecs.charmap_encode
    decode = codecs.charmap_decode

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def __init__(self, errors='strict', mapping=None***REMOVED***:
        codecs.IncrementalEncoder.__init__(self, errors***REMOVED***
        self.mapping = mapping

    def encode(self, input, final=False***REMOVED***:
        return codecs.charmap_encode(input, self.errors, self.mapping***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def __init__(self, errors='strict', mapping=None***REMOVED***:
        codecs.IncrementalDecoder.__init__(self, errors***REMOVED***
        self.mapping = mapping

    def decode(self, input, final=False***REMOVED***:
        return codecs.charmap_decode(input, self.errors, self.mapping***REMOVED***[0***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:

    def __init__(self,stream,errors='strict',mapping=None***REMOVED***:
        codecs.StreamWriter.__init__(self,stream,errors***REMOVED***
        self.mapping = mapping

    def encode(self,input,errors='strict'***REMOVED***:
        return Codec.encode(input,errors,self.mapping***REMOVED***

class StreamReader(Codec,codecs.StreamReader***REMOVED***:

    def __init__(self,stream,errors='strict',mapping=None***REMOVED***:
        codecs.StreamReader.__init__(self,stream,errors***REMOVED***
        self.mapping = mapping

    def decode(self,input,errors='strict'***REMOVED***:
        return Codec.decode(input,errors,self.mapping***REMOVED***

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='charmap',
        encode=Codec.encode,
        decode=Codec.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
