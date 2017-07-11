***REMOVED*** Python 'utf-16' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***
import codecs, sys

### Codec APIs

encode = codecs.utf_16_encode

def decode(input, errors='strict'***REMOVED***:
    return codecs.utf_16_decode(input, errors, True***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        codecs.IncrementalEncoder.__init__(self, errors***REMOVED***
        self.encoder = None

    def encode(self, input, final=False***REMOVED***:
        if self.encoder is None:
            result = codecs.utf_16_encode(input, self.errors***REMOVED***[0***REMOVED***
            if sys.byteorder == 'little':
                self.encoder = codecs.utf_16_le_encode
            else:
                self.encoder = codecs.utf_16_be_encode
            return result
        return self.encoder(input, self.errors***REMOVED***[0***REMOVED***

    def reset(self***REMOVED***:
        codecs.IncrementalEncoder.reset(self***REMOVED***
        self.encoder = None

    def getstate(self***REMOVED***:
        # state info we return to the caller:
        # 0: stream is in natural order for this platform
        # 2: endianness hasn't been determined yet
        # (we're never writing in unnatural order***REMOVED***
        return (2 if self.encoder is None else 0***REMOVED***

    def setstate(self, state***REMOVED***:
        if state:
            self.encoder = None
        else:
            if sys.byteorder == 'little':
                self.encoder = codecs.utf_16_le_encode
            else:
                self.encoder = codecs.utf_16_be_encode

class IncrementalDecoder(codecs.BufferedIncrementalDecoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        codecs.BufferedIncrementalDecoder.__init__(self, errors***REMOVED***
        self.decoder = None

    def _buffer_decode(self, input, errors, final***REMOVED***:
        if self.decoder is None:
            (output, consumed, byteorder***REMOVED*** = \
                codecs.utf_16_ex_decode(input, errors, 0, final***REMOVED***
            if byteorder == -1:
                self.decoder = codecs.utf_16_le_decode
            elif byteorder == 1:
                self.decoder = codecs.utf_16_be_decode
            elif consumed >= 2:
                raise UnicodeError("UTF-16 stream does not start with BOM"***REMOVED***
            return (output, consumed***REMOVED***
        return self.decoder(input, self.errors, final***REMOVED***

    def reset(self***REMOVED***:
        codecs.BufferedIncrementalDecoder.reset(self***REMOVED***
        self.decoder = None

class StreamWriter(codecs.StreamWriter***REMOVED***:
    def __init__(self, stream, errors='strict'***REMOVED***:
        codecs.StreamWriter.__init__(self, stream, errors***REMOVED***
        self.encoder = None

    def reset(self***REMOVED***:
        codecs.StreamWriter.reset(self***REMOVED***
        self.encoder = None

    def encode(self, input, errors='strict'***REMOVED***:
        if self.encoder is None:
            result = codecs.utf_16_encode(input, errors***REMOVED***
            if sys.byteorder == 'little':
                self.encoder = codecs.utf_16_le_encode
            else:
                self.encoder = codecs.utf_16_be_encode
            return result
        else:
            return self.encoder(input, errors***REMOVED***

class StreamReader(codecs.StreamReader***REMOVED***:

    def reset(self***REMOVED***:
        codecs.StreamReader.reset(self***REMOVED***
        try:
            del self.decode
        except AttributeError:
            pass

    def decode(self, input, errors='strict'***REMOVED***:
        (object, consumed, byteorder***REMOVED*** = \
            codecs.utf_16_ex_decode(input, errors, 0, False***REMOVED***
        if byteorder == -1:
            self.decode = codecs.utf_16_le_decode
        elif byteorder == 1:
            self.decode = codecs.utf_16_be_decode
        elif consumed>=2:
            raise UnicodeError,"UTF-16 stream does not start with BOM"
        return (object, consumed***REMOVED***

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='utf-16',
        encode=encode,
        decode=decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
