***REMOVED***Codec for quoted-printable encoding.

Like base64 and rot13, this returns Python strings, not Unicode.
***REMOVED***

import codecs, quopri
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def quopri_encode(input, errors='strict'***REMOVED***:
    ***REMOVED***Encode the input, returning a tuple (output object, length consumed***REMOVED***.

    errors defines the error handling to apply. It defaults to
    'strict' handling which is the only currently supported
    error handling for this codec.

    ***REMOVED***
    assert errors == 'strict'
    # using str(***REMOVED*** because of cStringIO's Unicode undesired Unicode behavior.
    f = StringIO(str(input***REMOVED******REMOVED***
    g = StringIO(***REMOVED***
    quopri.encode(f, g, 1***REMOVED***
    output = g.getvalue(***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

def quopri_decode(input, errors='strict'***REMOVED***:
    ***REMOVED***Decode the input, returning a tuple (output object, length consumed***REMOVED***.

    errors defines the error handling to apply. It defaults to
    'strict' handling which is the only currently supported
    error handling for this codec.

    ***REMOVED***
    assert errors == 'strict'
    f = StringIO(str(input***REMOVED******REMOVED***
    g = StringIO(***REMOVED***
    quopri.decode(f, g***REMOVED***
    output = g.getvalue(***REMOVED***
    return (output, len(input***REMOVED******REMOVED***

class Codec(codecs.Codec***REMOVED***:

    def encode(self, input,errors='strict'***REMOVED***:
        return quopri_encode(input,errors***REMOVED***
    def decode(self, input,errors='strict'***REMOVED***:
        return quopri_decode(input,errors***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return quopri_encode(input, self.errors***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        return quopri_decode(input, self.errors***REMOVED***[0***REMOVED***

class StreamWriter(Codec, codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

# encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='quopri',
        encode=quopri_encode,
        decode=quopri_decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***
