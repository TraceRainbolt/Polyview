***REMOVED***
Python 'utf-32' Codec
***REMOVED***
import codecs, sys

### Codec APIs

encode = codecs.utf_32_encode

def decode(input, errors='strict'***REMOVED***:
    return codecs.utf_32_decode(input, errors, True***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        codecs.IncrementalEncoder.__init__(self, errors***REMOVED***
        self.encoder = None

    def encode(self, input, final=False***REMOVED***:
        if self.encoder is None:
            result = codecs.utf_32_encode(input, self.errors***REMOVED***[0***REMOVED***
            if sys.byteorder == 'little':
                self.encoder = codecs.utf_32_le_encode
            else:
                self.encoder = codecs.utf_32_be_encode
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
                self.encoder = codecs.utf_32_le_encode
            else:
                self.encoder = codecs.utf_32_be_encode

class IncrementalDecoder(codecs.BufferedIncrementalDecoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        codecs.BufferedIncrementalDecoder.__init__(self, errors***REMOVED***
        self.decoder = None

    def _buffer_decode(self, input, errors, final***REMOVED***:
        if self.decoder is None:
            (output, consumed, byteorder***REMOVED*** = \
                codecs.utf_32_ex_decode(input, errors, 0, final***REMOVED***
            if byteorder == -1:
                self.decoder = codecs.utf_32_le_decode
            elif byteorder == 1:
                self.decoder = codecs.utf_32_be_decode
            elif consumed >= 4:
                raise UnicodeError("UTF-32 stream does not start with BOM"***REMOVED***
            return (output, consumed***REMOVED***
        return self.decoder(input, self.errors, final***REMOVED***

    def reset(self***REMOVED***:
        codecs.BufferedIncrementalDecoder.reset(self***REMOVED***
        self.decoder = None

    def getstate(self***REMOVED***:
        # additonal state info from the base class must be None here,
        # as it isn't passed along to the caller
        state = codecs.BufferedIncrementalDecoder.getstate(self***REMOVED***[0***REMOVED***
        # additional state info we pass to the caller:
        # 0: stream is in natural order for this platform
        # 1: stream is in unnatural order
        # 2: endianness hasn't been determined yet
        if self.decoder is None:
            return (state, 2***REMOVED***
        addstate = int((sys.byteorder == "big"***REMOVED*** !=
                       (self.decoder is codecs.utf_32_be_decode***REMOVED******REMOVED***
        return (state, addstate***REMOVED***

    def setstate(self, state***REMOVED***:
        # state[1***REMOVED*** will be ignored by BufferedIncrementalDecoder.setstate(***REMOVED***
        codecs.BufferedIncrementalDecoder.setstate(self, state***REMOVED***
        state = state[1***REMOVED***
        if state == 0:
            self.decoder = (codecs.utf_32_be_decode
                            if sys.byteorder == "big"
                            else codecs.utf_32_le_decode***REMOVED***
        elif state == 1:
            self.decoder = (codecs.utf_32_le_decode
                            if sys.byteorder == "big"
                            else codecs.utf_32_be_decode***REMOVED***
        else:
            self.decoder = None

class StreamWriter(codecs.StreamWriter***REMOVED***:
    def __init__(self, stream, errors='strict'***REMOVED***:
        self.encoder = None
        codecs.StreamWriter.__init__(self, stream, errors***REMOVED***

    def reset(self***REMOVED***:
        codecs.StreamWriter.reset(self***REMOVED***
        self.encoder = None

    def encode(self, input, errors='strict'***REMOVED***:
        if self.encoder is None:
            result = codecs.utf_32_encode(input, errors***REMOVED***
            if sys.byteorder == 'little':
                self.encoder = codecs.utf_32_le_encode
            else:
                self.encoder = codecs.utf_32_be_encode
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
            codecs.utf_32_ex_decode(input, errors, 0, False***REMOVED***
        if byteorder == -1:
            self.decode = codecs.utf_32_le_decode
        elif byteorder == 1:
            self.decode = codecs.utf_32_be_decode
        elif consumed>=4:
            raise UnicodeError,"UTF-32 stream does not start with BOM"
        return (object, consumed***REMOVED***

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='utf-32',
        encode=encode,
        decode=decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
