***REMOVED*** Python 'utf-8-sig' Codec
This work similar to UTF-8 with the following changes:

* On encoding/writing a UTF-8 encoded BOM will be prepended/written as the
  first three bytes.

* On decoding/reading if the first three bytes are a UTF-8 encoded BOM, these
  bytes will be skipped.
***REMOVED***
import codecs

### Codec APIs

def encode(input, errors='strict'***REMOVED***:
    return (codecs.BOM_UTF8 + codecs.utf_8_encode(input, errors***REMOVED***[0***REMOVED***, len(input***REMOVED******REMOVED***

def decode(input, errors='strict'***REMOVED***:
    prefix = 0
    if input[:3***REMOVED*** == codecs.BOM_UTF8:
        input = input[3:***REMOVED***
        prefix = 3
    (output, consumed***REMOVED*** = codecs.utf_8_decode(input, errors, True***REMOVED***
    return (output, consumed+prefix***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        codecs.IncrementalEncoder.__init__(self, errors***REMOVED***
        self.first = 1

    def encode(self, input, final=False***REMOVED***:
        if self.first:
            self.first = 0
            return codecs.BOM_UTF8 + codecs.utf_8_encode(input, self.errors***REMOVED***[0***REMOVED***
        else:
            return codecs.utf_8_encode(input, self.errors***REMOVED***[0***REMOVED***

    def reset(self***REMOVED***:
        codecs.IncrementalEncoder.reset(self***REMOVED***
        self.first = 1

    def getstate(self***REMOVED***:
        return self.first

    def setstate(self, state***REMOVED***:
        self.first = state

class IncrementalDecoder(codecs.BufferedIncrementalDecoder***REMOVED***:
    def __init__(self, errors='strict'***REMOVED***:
        codecs.BufferedIncrementalDecoder.__init__(self, errors***REMOVED***
        self.first = True

    def _buffer_decode(self, input, errors, final***REMOVED***:
        if self.first:
            if len(input***REMOVED*** < 3:
                if codecs.BOM_UTF8.startswith(input***REMOVED***:
                    # not enough data to decide if this really is a BOM
                    # => try again on the next call
                    return (u"", 0***REMOVED***
                else:
                    self.first = None
            else:
                self.first = None
                if input[:3***REMOVED*** == codecs.BOM_UTF8:
                    (output, consumed***REMOVED*** = codecs.utf_8_decode(input[3:***REMOVED***, errors, final***REMOVED***
                    return (output, consumed+3***REMOVED***
        return codecs.utf_8_decode(input, errors, final***REMOVED***

    def reset(self***REMOVED***:
        codecs.BufferedIncrementalDecoder.reset(self***REMOVED***
        self.first = True

class StreamWriter(codecs.StreamWriter***REMOVED***:
    def reset(self***REMOVED***:
        codecs.StreamWriter.reset(self***REMOVED***
        try:
            del self.encode
        except AttributeError:
            pass

    def encode(self, input, errors='strict'***REMOVED***:
        self.encode = codecs.utf_8_encode
        return encode(input, errors***REMOVED***

class StreamReader(codecs.StreamReader***REMOVED***:
    def reset(self***REMOVED***:
        codecs.StreamReader.reset(self***REMOVED***
        try:
            del self.decode
        except AttributeError:
            pass

    def decode(self, input, errors='strict'***REMOVED***:
        if len(input***REMOVED*** < 3:
            if codecs.BOM_UTF8.startswith(input***REMOVED***:
                # not enough data to decide if this is a BOM
                # => try again on the next call
                return (u"", 0***REMOVED***
        elif input[:3***REMOVED*** == codecs.BOM_UTF8:
            self.decode = codecs.utf_8_decode
            (output, consumed***REMOVED*** = codecs.utf_8_decode(input[3:***REMOVED***,errors***REMOVED***
            return (output, consumed+3***REMOVED***
        # (else***REMOVED*** no BOM present
        self.decode = codecs.utf_8_decode
        return codecs.utf_8_decode(input, errors***REMOVED***

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='utf-8-sig',
        encode=encode,
        decode=decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
