***REMOVED*** codecs -- Python Codec Registry, API and helpers.


Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***#"

import __builtin__, sys

### Registry and builtin stateless codec functions

try:
    from _codecs import *
except ImportError, why:
    raise SystemError('Failed to load the builtin codecs: %s' % why***REMOVED***

__all__ = ["register", "lookup", "open", "EncodedFile", "BOM", "BOM_BE",
           "BOM_LE", "BOM32_BE", "BOM32_LE", "BOM64_BE", "BOM64_LE",
           "BOM_UTF8", "BOM_UTF16", "BOM_UTF16_LE", "BOM_UTF16_BE",
           "BOM_UTF32", "BOM_UTF32_LE", "BOM_UTF32_BE",
           "strict_errors", "ignore_errors", "replace_errors",
           "xmlcharrefreplace_errors",
           "register_error", "lookup_error"***REMOVED***

### Constants

#
# Byte Order Mark (BOM = ZERO WIDTH NO-BREAK SPACE = U+FEFF***REMOVED***
# and its possible byte string values
# for UTF8/UTF16/UTF32 output and little/big endian machines
#

# UTF-8
BOM_UTF8 = '\xef\xbb\xbf'

# UTF-16, little endian
BOM_LE = BOM_UTF16_LE = '\xff\xfe'

# UTF-16, big endian
BOM_BE = BOM_UTF16_BE = '\xfe\xff'

# UTF-32, little endian
BOM_UTF32_LE = '\xff\xfe\x00\x00'

# UTF-32, big endian
BOM_UTF32_BE = '\x00\x00\xfe\xff'

if sys.byteorder == 'little':

    # UTF-16, native endianness
    BOM = BOM_UTF16 = BOM_UTF16_LE

    # UTF-32, native endianness
    BOM_UTF32 = BOM_UTF32_LE

else:

    # UTF-16, native endianness
    BOM = BOM_UTF16 = BOM_UTF16_BE

    # UTF-32, native endianness
    BOM_UTF32 = BOM_UTF32_BE

# Old broken names (don't use in new code***REMOVED***
BOM32_LE = BOM_UTF16_LE
BOM32_BE = BOM_UTF16_BE
BOM64_LE = BOM_UTF32_LE
BOM64_BE = BOM_UTF32_BE


### Codec base classes (defining the API***REMOVED***

class CodecInfo(tuple***REMOVED***:

    def __new__(cls, encode, decode, streamreader=None, streamwriter=None,
        incrementalencoder=None, incrementaldecoder=None, name=None***REMOVED***:
        self = tuple.__new__(cls, (encode, decode, streamreader, streamwriter***REMOVED******REMOVED***
        self.name = name
        self.encode = encode
        self.decode = decode
        self.incrementalencoder = incrementalencoder
        self.incrementaldecoder = incrementaldecoder
        self.streamwriter = streamwriter
        self.streamreader = streamreader
        return self

    def __repr__(self***REMOVED***:
        return "<%s.%s object for encoding %s at 0x%x>" % (self.__class__.__module__, self.__class__.__name__, self.name, id(self***REMOVED******REMOVED***

class Codec:

    ***REMOVED*** Defines the interface for stateless encoders/decoders.

        The .encode(***REMOVED***/.decode(***REMOVED*** methods may use different error
        handling schemes by providing the errors argument. These
        string values are predefined:

         'strict' - raise a ValueError error (or a subclass***REMOVED***
         'ignore' - ignore the character and continue with the next
         'replace' - replace with a suitable replacement character;
                    Python will use the official U+FFFD REPLACEMENT
                    CHARACTER for the builtin Unicode codecs on
                    decoding and '?' on encoding.
         'xmlcharrefreplace' - Replace with the appropriate XML
                               character reference (only for encoding***REMOVED***.
         'backslashreplace'  - Replace with backslashed escape sequences
                               (only for encoding***REMOVED***.

        The set of allowed values can be extended via register_error.

    ***REMOVED***
    def encode(self, input, errors='strict'***REMOVED***:

        ***REMOVED*** Encodes the object input and returns a tuple (output
            object, length consumed***REMOVED***.

            errors defines the error handling to apply. It defaults to
            'strict' handling.

            The method may not store state in the Codec instance. Use
            StreamCodec for codecs which have to keep state in order to
            make encoding/decoding efficient.

            The encoder must be able to handle zero length input and
            return an empty object of the output object type in this
            situation.

        ***REMOVED***
        raise NotImplementedError

    def decode(self, input, errors='strict'***REMOVED***:

        ***REMOVED*** Decodes the object input and returns a tuple (output
            object, length consumed***REMOVED***.

            input must be an object which provides the bf_getreadbuf
            buffer slot. Python strings, buffer objects and memory
            mapped files are examples of objects providing this slot.

            errors defines the error handling to apply. It defaults to
            'strict' handling.

            The method may not store state in the Codec instance. Use
            StreamCodec for codecs which have to keep state in order to
            make encoding/decoding efficient.

            The decoder must be able to handle zero length input and
            return an empty object of the output object type in this
            situation.

        ***REMOVED***
        raise NotImplementedError

class IncrementalEncoder(object***REMOVED***:
    ***REMOVED***
    An IncrementalEncoder encodes an input in multiple steps. The input can be
    passed piece by piece to the encode(***REMOVED*** method. The IncrementalEncoder remembers
    the state of the Encoding process between calls to encode(***REMOVED***.
    ***REMOVED***
    def __init__(self, errors='strict'***REMOVED***:
        ***REMOVED***
        Creates an IncrementalEncoder instance.

        The IncrementalEncoder may use different error handling schemes by
        providing the errors keyword argument. See the module docstring
        for a list of possible values.
        ***REMOVED***
        self.errors = errors
        self.buffer = ""

    def encode(self, input, final=False***REMOVED***:
        ***REMOVED***
        Encodes input and returns the resulting object.
        ***REMOVED***
        raise NotImplementedError

    def reset(self***REMOVED***:
        ***REMOVED***
        Resets the encoder to the initial state.
        ***REMOVED***

    def getstate(self***REMOVED***:
        ***REMOVED***
        Return the current state of the encoder.
        ***REMOVED***
        return 0

    def setstate(self, state***REMOVED***:
        ***REMOVED***
        Set the current state of the encoder. state must have been
        returned by getstate(***REMOVED***.
        ***REMOVED***

class BufferedIncrementalEncoder(IncrementalEncoder***REMOVED***:
    ***REMOVED***
    This subclass of IncrementalEncoder can be used as the baseclass for an
    incremental encoder if the encoder must keep some of the output in a
    buffer between calls to encode(***REMOVED***.
    ***REMOVED***
    def __init__(self, errors='strict'***REMOVED***:
        IncrementalEncoder.__init__(self, errors***REMOVED***
        self.buffer = "" # unencoded input that is kept between calls to encode(***REMOVED***

    def _buffer_encode(self, input, errors, final***REMOVED***:
        # Overwrite this method in subclasses: It must encode input
        # and return an (output, length consumed***REMOVED*** tuple
        raise NotImplementedError

    def encode(self, input, final=False***REMOVED***:
        # encode input (taking the buffer into account***REMOVED***
        data = self.buffer + input
        (result, consumed***REMOVED*** = self._buffer_encode(data, self.errors, final***REMOVED***
        # keep unencoded input until the next call
        self.buffer = data[consumed:***REMOVED***
        return result

    def reset(self***REMOVED***:
        IncrementalEncoder.reset(self***REMOVED***
        self.buffer = ""

    def getstate(self***REMOVED***:
        return self.buffer or 0

    def setstate(self, state***REMOVED***:
        self.buffer = state or ""

class IncrementalDecoder(object***REMOVED***:
    ***REMOVED***
    An IncrementalDecoder decodes an input in multiple steps. The input can be
    passed piece by piece to the decode(***REMOVED*** method. The IncrementalDecoder
    remembers the state of the decoding process between calls to decode(***REMOVED***.
    ***REMOVED***
    def __init__(self, errors='strict'***REMOVED***:
        ***REMOVED***
        Creates a IncrementalDecoder instance.

        The IncrementalDecoder may use different error handling schemes by
        providing the errors keyword argument. See the module docstring
        for a list of possible values.
        ***REMOVED***
        self.errors = errors

    def decode(self, input, final=False***REMOVED***:
        ***REMOVED***
        Decodes input and returns the resulting object.
        ***REMOVED***
        raise NotImplementedError

    def reset(self***REMOVED***:
        ***REMOVED***
        Resets the decoder to the initial state.
        ***REMOVED***

    def getstate(self***REMOVED***:
        ***REMOVED***
        Return the current state of the decoder.

        This must be a (buffered_input, additional_state_info***REMOVED*** tuple.
        buffered_input must be a bytes object containing bytes that
        were passed to decode(***REMOVED*** that have not yet been converted.
        additional_state_info must be a non-negative integer
        representing the state of the decoder WITHOUT yet having
        processed the contents of buffered_input.  In the initial state
        and after reset(***REMOVED***, getstate(***REMOVED*** must return (b"", 0***REMOVED***.
        ***REMOVED***
        return (b"", 0***REMOVED***

    def setstate(self, state***REMOVED***:
        ***REMOVED***
        Set the current state of the decoder.

        state must have been returned by getstate(***REMOVED***.  The effect of
        setstate((b"", 0***REMOVED******REMOVED*** must be equivalent to reset(***REMOVED***.
        ***REMOVED***

class BufferedIncrementalDecoder(IncrementalDecoder***REMOVED***:
    ***REMOVED***
    This subclass of IncrementalDecoder can be used as the baseclass for an
    incremental decoder if the decoder must be able to handle incomplete byte
    sequences.
    ***REMOVED***
    def __init__(self, errors='strict'***REMOVED***:
        IncrementalDecoder.__init__(self, errors***REMOVED***
        self.buffer = "" # undecoded input that is kept between calls to decode(***REMOVED***

    def _buffer_decode(self, input, errors, final***REMOVED***:
        # Overwrite this method in subclasses: It must decode input
        # and return an (output, length consumed***REMOVED*** tuple
        raise NotImplementedError

    def decode(self, input, final=False***REMOVED***:
        # decode input (taking the buffer into account***REMOVED***
        data = self.buffer + input
        (result, consumed***REMOVED*** = self._buffer_decode(data, self.errors, final***REMOVED***
        # keep undecoded input until the next call
        self.buffer = data[consumed:***REMOVED***
        return result

    def reset(self***REMOVED***:
        IncrementalDecoder.reset(self***REMOVED***
        self.buffer = ""

    def getstate(self***REMOVED***:
        # additional state info is always 0
        return (self.buffer, 0***REMOVED***

    def setstate(self, state***REMOVED***:
        # ignore additional state info
        self.buffer = state[0***REMOVED***

#
# The StreamWriter and StreamReader class provide generic working
# interfaces which can be used to implement new encoding submodules
# very easily. See encodings/utf_8.py for an example on how this is
# done.
#

class StreamWriter(Codec***REMOVED***:

    def __init__(self, stream, errors='strict'***REMOVED***:

        ***REMOVED*** Creates a StreamWriter instance.

            stream must be a file-like object open for writing
            (binary***REMOVED*** data.

            The StreamWriter may use different error handling
            schemes by providing the errors keyword argument. These
            parameters are predefined:

             'strict' - raise a ValueError (or a subclass***REMOVED***
             'ignore' - ignore the character and continue with the next
             'replace'- replace with a suitable replacement character
             'xmlcharrefreplace' - Replace with the appropriate XML
                                   character reference.
             'backslashreplace'  - Replace with backslashed escape
                                   sequences (only for encoding***REMOVED***.

            The set of allowed parameter values can be extended via
            register_error.
        ***REMOVED***
        self.stream = stream
        self.errors = errors

    def write(self, object***REMOVED***:

        ***REMOVED*** Writes the object's contents encoded to self.stream.
        ***REMOVED***
        data, consumed = self.encode(object, self.errors***REMOVED***
        self.stream.write(data***REMOVED***

    def writelines(self, list***REMOVED***:

        ***REMOVED*** Writes the concatenated list of strings to the stream
            using .write(***REMOVED***.
        ***REMOVED***
        self.write(''.join(list***REMOVED******REMOVED***

    def reset(self***REMOVED***:

        ***REMOVED*** Flushes and resets the codec buffers used for keeping state.

            Calling this method should ensure that the data on the
            output is put into a clean state, that allows appending
            of new fresh data without having to rescan the whole
            stream to recover state.

        ***REMOVED***
        pass

    def seek(self, offset, whence=0***REMOVED***:
        self.stream.seek(offset, whence***REMOVED***
        if whence == 0 and offset == 0:
            self.reset(***REMOVED***

    def __getattr__(self, name,
                    getattr=getattr***REMOVED***:

        ***REMOVED*** Inherit all other methods from the underlying stream.
        ***REMOVED***
        return getattr(self.stream, name***REMOVED***

    def __enter__(self***REMOVED***:
        return self

    def __exit__(self, type, value, tb***REMOVED***:
        self.stream.close(***REMOVED***

###

class StreamReader(Codec***REMOVED***:

    def __init__(self, stream, errors='strict'***REMOVED***:

        ***REMOVED*** Creates a StreamReader instance.

            stream must be a file-like object open for reading
            (binary***REMOVED*** data.

            The StreamReader may use different error handling
            schemes by providing the errors keyword argument. These
            parameters are predefined:

             'strict' - raise a ValueError (or a subclass***REMOVED***
             'ignore' - ignore the character and continue with the next
             'replace'- replace with a suitable replacement character;

            The set of allowed parameter values can be extended via
            register_error.
        ***REMOVED***
        self.stream = stream
        self.errors = errors
        self.bytebuffer = ""
        # For str->str decoding this will stay a str
        # For str->unicode decoding the first read will promote it to unicode
        self.charbuffer = ""
        self.linebuffer = None

    def decode(self, input, errors='strict'***REMOVED***:
        raise NotImplementedError

    def read(self, size=-1, chars=-1, firstline=False***REMOVED***:

        ***REMOVED*** Decodes data from the stream self.stream and returns the
            resulting object.

            chars indicates the number of characters to read from the
            stream. read(***REMOVED*** will never return more than chars
            characters, but it might return less, if there are not enough
            characters available.

            size indicates the approximate maximum number of bytes to
            read from the stream for decoding purposes. The decoder
            can modify this setting as appropriate. The default value
            -1 indicates to read and decode as much as possible.  size
            is intended to prevent having to decode huge files in one
            step.

            If firstline is true, and a UnicodeDecodeError happens
            after the first line terminator in the input only the first line
            will be returned, the rest of the input will be kept until the
            next call to read(***REMOVED***.

            The method should use a greedy read strategy meaning that
            it should read as much data as is allowed within the
            definition of the encoding and the given size, e.g.  if
            optional encoding endings or state markers are available
            on the stream, these should be read too.
        ***REMOVED***
        # If we have lines cached, first merge them back into characters
        if self.linebuffer:
            self.charbuffer = "".join(self.linebuffer***REMOVED***
            self.linebuffer = None

        # read until we get the required number of characters (if available***REMOVED***
        while True:
            # can the request be satisfied from the character buffer?
            if chars >= 0:
                if len(self.charbuffer***REMOVED*** >= chars:
                    break
            elif size >= 0:
                if len(self.charbuffer***REMOVED*** >= size:
                    break
            # we need more data
            if size < 0:
                newdata = self.stream.read(***REMOVED***
            else:
                newdata = self.stream.read(size***REMOVED***
            # decode bytes (those remaining from the last call included***REMOVED***
            data = self.bytebuffer + newdata
            try:
                newchars, decodedbytes = self.decode(data, self.errors***REMOVED***
            except UnicodeDecodeError, exc:
                if firstline:
                    newchars, decodedbytes = self.decode(data[:exc.start***REMOVED***, self.errors***REMOVED***
                    lines = newchars.splitlines(True***REMOVED***
                    if len(lines***REMOVED***<=1:
                        raise
                else:
                    raise
            # keep undecoded bytes until the next call
            self.bytebuffer = data[decodedbytes:***REMOVED***
            # put new characters in the character buffer
            self.charbuffer += newchars
            # there was no data available
            if not newdata:
                break
        if chars < 0:
            # Return everything we've got
            result = self.charbuffer
            self.charbuffer = ""
        else:
            # Return the first chars characters
            result = self.charbuffer[:chars***REMOVED***
            self.charbuffer = self.charbuffer[chars:***REMOVED***
        return result

    def readline(self, size=None, keepends=True***REMOVED***:

        ***REMOVED*** Read one line from the input stream and return the
            decoded data.

            size, if given, is passed as size argument to the
            read(***REMOVED*** method.

        ***REMOVED***
        # If we have lines cached from an earlier read, return
        # them unconditionally
        if self.linebuffer:
            line = self.linebuffer[0***REMOVED***
            del self.linebuffer[0***REMOVED***
            if len(self.linebuffer***REMOVED*** == 1:
                # revert to charbuffer mode; we might need more data
                # next time
                self.charbuffer = self.linebuffer[0***REMOVED***
                self.linebuffer = None
            if not keepends:
                line = line.splitlines(False***REMOVED***[0***REMOVED***
            return line

        readsize = size or 72
        line = ""
        # If size is given, we call read(***REMOVED*** only once
        while True:
            data = self.read(readsize, firstline=True***REMOVED***
            if data:
                # If we're at a "\r" read one extra character (which might
                # be a "\n"***REMOVED*** to get a proper line ending. If the stream is
                # temporarily exhausted we return the wrong line ending.
                if data.endswith("\r"***REMOVED***:
                    data += self.read(size=1, chars=1***REMOVED***

            line += data
            lines = line.splitlines(True***REMOVED***
            if lines:
                if len(lines***REMOVED*** > 1:
                    # More than one line result; the first line is a full line
                    # to return
                    line = lines[0***REMOVED***
                    del lines[0***REMOVED***
                    if len(lines***REMOVED*** > 1:
                        # cache the remaining lines
                        lines[-1***REMOVED*** += self.charbuffer
                        self.linebuffer = lines
                        self.charbuffer = None
                    else:
                        # only one remaining line, put it back into charbuffer
                        self.charbuffer = lines[0***REMOVED*** + self.charbuffer
                    if not keepends:
                        line = line.splitlines(False***REMOVED***[0***REMOVED***
                    break
                line0withend = lines[0***REMOVED***
                line0withoutend = lines[0***REMOVED***.splitlines(False***REMOVED***[0***REMOVED***
                if line0withend != line0withoutend: # We really have a line end
                    # Put the rest back together and keep it until the next call
                    self.charbuffer = "".join(lines[1:***REMOVED******REMOVED*** + self.charbuffer
                    if keepends:
                        line = line0withend
                    else:
                        line = line0withoutend
                    break
            # we didn't get anything or this was our only try
            if not data or size is not None:
                if line and not keepends:
                    line = line.splitlines(False***REMOVED***[0***REMOVED***
                break
            if readsize<8000:
                readsize *= 2
        return line

    def readlines(self, sizehint=None, keepends=True***REMOVED***:

        ***REMOVED*** Read all lines available on the input stream
            and return them as list of lines.

            Line breaks are implemented using the codec's decoder
            method and are included in the list entries.

            sizehint, if given, is ignored since there is no efficient
            way to finding the true end-of-line.

        ***REMOVED***
        data = self.read(***REMOVED***
        return data.splitlines(keepends***REMOVED***

    def reset(self***REMOVED***:

        ***REMOVED*** Resets the codec buffers used for keeping state.

            Note that no stream repositioning should take place.
            This method is primarily intended to be able to recover
            from decoding errors.

        ***REMOVED***
        self.bytebuffer = ""
        self.charbuffer = u""
        self.linebuffer = None

    def seek(self, offset, whence=0***REMOVED***:
        ***REMOVED*** Set the input stream's current position.

            Resets the codec buffers used for keeping state.
        ***REMOVED***
        self.stream.seek(offset, whence***REMOVED***
        self.reset(***REMOVED***

    def next(self***REMOVED***:

        ***REMOVED*** Return the next decoded line from the input stream.***REMOVED***
        line = self.readline(***REMOVED***
        if line:
            return line
        raise StopIteration

    def __iter__(self***REMOVED***:
        return self

    def __getattr__(self, name,
                    getattr=getattr***REMOVED***:

        ***REMOVED*** Inherit all other methods from the underlying stream.
        ***REMOVED***
        return getattr(self.stream, name***REMOVED***

    def __enter__(self***REMOVED***:
        return self

    def __exit__(self, type, value, tb***REMOVED***:
        self.stream.close(***REMOVED***

###

class StreamReaderWriter:

    ***REMOVED*** StreamReaderWriter instances allow wrapping streams which
        work in both read and write modes.

        The design is such that one can use the factory functions
        returned by the codec.lookup(***REMOVED*** function to construct the
        instance.

    ***REMOVED***
    # Optional attributes set by the file wrappers below
    encoding = 'unknown'

    def __init__(self, stream, Reader, Writer, errors='strict'***REMOVED***:

        ***REMOVED*** Creates a StreamReaderWriter instance.

            stream must be a Stream-like object.

            Reader, Writer must be factory functions or classes
            providing the StreamReader, StreamWriter interface resp.

            Error handling is done in the same way as defined for the
            StreamWriter/Readers.

        ***REMOVED***
        self.stream = stream
        self.reader = Reader(stream, errors***REMOVED***
        self.writer = Writer(stream, errors***REMOVED***
        self.errors = errors

    def read(self, size=-1***REMOVED***:

        return self.reader.read(size***REMOVED***

    def readline(self, size=None***REMOVED***:

        return self.reader.readline(size***REMOVED***

    def readlines(self, sizehint=None***REMOVED***:

        return self.reader.readlines(sizehint***REMOVED***

    def next(self***REMOVED***:

        ***REMOVED*** Return the next decoded line from the input stream.***REMOVED***
        return self.reader.next(***REMOVED***

    def __iter__(self***REMOVED***:
        return self

    def write(self, data***REMOVED***:

        return self.writer.write(data***REMOVED***

    def writelines(self, list***REMOVED***:

        return self.writer.writelines(list***REMOVED***

    def reset(self***REMOVED***:

        self.reader.reset(***REMOVED***
        self.writer.reset(***REMOVED***

    def seek(self, offset, whence=0***REMOVED***:
        self.stream.seek(offset, whence***REMOVED***
        self.reader.reset(***REMOVED***
        if whence == 0 and offset == 0:
            self.writer.reset(***REMOVED***

    def __getattr__(self, name,
                    getattr=getattr***REMOVED***:

        ***REMOVED*** Inherit all other methods from the underlying stream.
        ***REMOVED***
        return getattr(self.stream, name***REMOVED***

    # these are needed to make "with codecs.open(...***REMOVED***" work properly

    def __enter__(self***REMOVED***:
        return self

    def __exit__(self, type, value, tb***REMOVED***:
        self.stream.close(***REMOVED***

###

class StreamRecoder:

    ***REMOVED*** StreamRecoder instances provide a frontend - backend
        view of encoding data.

        They use the complete set of APIs returned by the
        codecs.lookup(***REMOVED*** function to implement their task.

        Data written to the stream is first decoded into an
        intermediate format (which is dependent on the given codec
        combination***REMOVED*** and then written to the stream using an instance
        of the provided Writer class.

        In the other direction, data is read from the stream using a
        Reader instance and then return encoded data to the caller.

    ***REMOVED***
    # Optional attributes set by the file wrappers below
    data_encoding = 'unknown'
    file_encoding = 'unknown'

    def __init__(self, stream, encode, decode, Reader, Writer,
                 errors='strict'***REMOVED***:

        ***REMOVED*** Creates a StreamRecoder instance which implements a two-way
            conversion: encode and decode work on the frontend (the
            input to .read(***REMOVED*** and output of .write(***REMOVED******REMOVED*** while
            Reader and Writer work on the backend (reading and
            writing to the stream***REMOVED***.

            You can use these objects to do transparent direct
            recodings from e.g. latin-1 to utf-8 and back.

            stream must be a file-like object.

            encode, decode must adhere to the Codec interface, Reader,
            Writer must be factory functions or classes providing the
            StreamReader, StreamWriter interface resp.

            encode and decode are needed for the frontend translation,
            Reader and Writer for the backend translation. Unicode is
            used as intermediate encoding.

            Error handling is done in the same way as defined for the
            StreamWriter/Readers.

        ***REMOVED***
        self.stream = stream
        self.encode = encode
        self.decode = decode
        self.reader = Reader(stream, errors***REMOVED***
        self.writer = Writer(stream, errors***REMOVED***
        self.errors = errors

    def read(self, size=-1***REMOVED***:

        data = self.reader.read(size***REMOVED***
        data, bytesencoded = self.encode(data, self.errors***REMOVED***
        return data

    def readline(self, size=None***REMOVED***:

        if size is None:
            data = self.reader.readline(***REMOVED***
        else:
            data = self.reader.readline(size***REMOVED***
        data, bytesencoded = self.encode(data, self.errors***REMOVED***
        return data

    def readlines(self, sizehint=None***REMOVED***:

        data = self.reader.read(***REMOVED***
        data, bytesencoded = self.encode(data, self.errors***REMOVED***
        return data.splitlines(1***REMOVED***

    def next(self***REMOVED***:

        ***REMOVED*** Return the next decoded line from the input stream.***REMOVED***
        data = self.reader.next(***REMOVED***
        data, bytesencoded = self.encode(data, self.errors***REMOVED***
        return data

    def __iter__(self***REMOVED***:
        return self

    def write(self, data***REMOVED***:

        data, bytesdecoded = self.decode(data, self.errors***REMOVED***
        return self.writer.write(data***REMOVED***

    def writelines(self, list***REMOVED***:

        data = ''.join(list***REMOVED***
        data, bytesdecoded = self.decode(data, self.errors***REMOVED***
        return self.writer.write(data***REMOVED***

    def reset(self***REMOVED***:

        self.reader.reset(***REMOVED***
        self.writer.reset(***REMOVED***

    def __getattr__(self, name,
                    getattr=getattr***REMOVED***:

        ***REMOVED*** Inherit all other methods from the underlying stream.
        ***REMOVED***
        return getattr(self.stream, name***REMOVED***

    def __enter__(self***REMOVED***:
        return self

    def __exit__(self, type, value, tb***REMOVED***:
        self.stream.close(***REMOVED***

### Shortcuts

def open(filename, mode='rb', encoding=None, errors='strict', buffering=1***REMOVED***:

    ***REMOVED*** Open an encoded file using the given mode and return
        a wrapped version providing transparent encoding/decoding.

        Note: The wrapped version will only accept the object format
        defined by the codecs, i.e. Unicode objects for most builtin
        codecs. Output is also codec dependent and will usually be
        Unicode as well.

        Files are always opened in binary mode, even if no binary mode
        was specified. This is done to avoid data loss due to encodings
        using 8-bit values. The default file mode is 'rb' meaning to
        open the file in binary read mode.

        encoding specifies the encoding which is to be used for the
        file.

        errors may be given to define the error handling. It defaults
        to 'strict' which causes ValueErrors to be raised in case an
        encoding error occurs.

        buffering has the same meaning as for the builtin open(***REMOVED*** API.
        It defaults to line buffered.

        The returned wrapped file object provides an extra attribute
        .encoding which allows querying the used encoding. This
        attribute is only available if an encoding was specified as
        parameter.

    ***REMOVED***
    if encoding is not None:
        if 'U' in mode:
            # No automatic conversion of '\n' is done on reading and writing
            mode = mode.strip(***REMOVED***.replace('U', ''***REMOVED***
            if mode[:1***REMOVED*** not in set('rwa'***REMOVED***:
                mode = 'r' + mode
        if 'b' not in mode:
            # Force opening of the file in binary mode
            mode = mode + 'b'
    file = __builtin__.open(filename, mode, buffering***REMOVED***
    if encoding is None:
        return file
    info = lookup(encoding***REMOVED***
    srw = StreamReaderWriter(file, info.streamreader, info.streamwriter, errors***REMOVED***
    # Add attributes to simplify introspection
    srw.encoding = encoding
    return srw

def EncodedFile(file, data_encoding, file_encoding=None, errors='strict'***REMOVED***:

    ***REMOVED*** Return a wrapped version of file which provides transparent
        encoding translation.

        Strings written to the wrapped file are interpreted according
        to the given data_encoding and then written to the original
        file as string using file_encoding. The intermediate encoding
        will usually be Unicode but depends on the specified codecs.

        Strings are read from the file using file_encoding and then
        passed back to the caller as string using data_encoding.

        If file_encoding is not given, it defaults to data_encoding.

        errors may be given to define the error handling. It defaults
        to 'strict' which causes ValueErrors to be raised in case an
        encoding error occurs.

        The returned wrapped file object provides two extra attributes
        .data_encoding and .file_encoding which reflect the given
        parameters of the same name. The attributes can be used for
        introspection by Python programs.

    ***REMOVED***
    if file_encoding is None:
        file_encoding = data_encoding
    data_info = lookup(data_encoding***REMOVED***
    file_info = lookup(file_encoding***REMOVED***
    sr = StreamRecoder(file, data_info.encode, data_info.decode,
                       file_info.streamreader, file_info.streamwriter, errors***REMOVED***
    # Add attributes to simplify introspection
    sr.data_encoding = data_encoding
    sr.file_encoding = file_encoding
    return sr

### Helpers for codec lookup

def getencoder(encoding***REMOVED***:

    ***REMOVED*** Lookup up the codec for the given encoding and return
        its encoder function.

        Raises a LookupError in case the encoding cannot be found.

    ***REMOVED***
    return lookup(encoding***REMOVED***.encode

def getdecoder(encoding***REMOVED***:

    ***REMOVED*** Lookup up the codec for the given encoding and return
        its decoder function.

        Raises a LookupError in case the encoding cannot be found.

    ***REMOVED***
    return lookup(encoding***REMOVED***.decode

def getincrementalencoder(encoding***REMOVED***:

    ***REMOVED*** Lookup up the codec for the given encoding and return
        its IncrementalEncoder class or factory function.

        Raises a LookupError in case the encoding cannot be found
        or the codecs doesn't provide an incremental encoder.

    ***REMOVED***
    encoder = lookup(encoding***REMOVED***.incrementalencoder
    if encoder is None:
        raise LookupError(encoding***REMOVED***
    return encoder

def getincrementaldecoder(encoding***REMOVED***:

    ***REMOVED*** Lookup up the codec for the given encoding and return
        its IncrementalDecoder class or factory function.

        Raises a LookupError in case the encoding cannot be found
        or the codecs doesn't provide an incremental decoder.

    ***REMOVED***
    decoder = lookup(encoding***REMOVED***.incrementaldecoder
    if decoder is None:
        raise LookupError(encoding***REMOVED***
    return decoder

def getreader(encoding***REMOVED***:

    ***REMOVED*** Lookup up the codec for the given encoding and return
        its StreamReader class or factory function.

        Raises a LookupError in case the encoding cannot be found.

    ***REMOVED***
    return lookup(encoding***REMOVED***.streamreader

def getwriter(encoding***REMOVED***:

    ***REMOVED*** Lookup up the codec for the given encoding and return
        its StreamWriter class or factory function.

        Raises a LookupError in case the encoding cannot be found.

    ***REMOVED***
    return lookup(encoding***REMOVED***.streamwriter

def iterencode(iterator, encoding, errors='strict', **kwargs***REMOVED***:
    ***REMOVED***
    Encoding iterator.

    Encodes the input strings from the iterator using a IncrementalEncoder.

    errors and kwargs are passed through to the IncrementalEncoder
    constructor.
    ***REMOVED***
    encoder = getincrementalencoder(encoding***REMOVED***(errors, **kwargs***REMOVED***
    for input in iterator:
        output = encoder.encode(input***REMOVED***
        if output:
            yield output
    output = encoder.encode("", True***REMOVED***
    if output:
        yield output

def iterdecode(iterator, encoding, errors='strict', **kwargs***REMOVED***:
    ***REMOVED***
    Decoding iterator.

    Decodes the input strings from the iterator using a IncrementalDecoder.

    errors and kwargs are passed through to the IncrementalDecoder
    constructor.
    ***REMOVED***
    decoder = getincrementaldecoder(encoding***REMOVED***(errors, **kwargs***REMOVED***
    for input in iterator:
        output = decoder.decode(input***REMOVED***
        if output:
            yield output
    output = decoder.decode("", True***REMOVED***
    if output:
        yield output

### Helpers for charmap-based codecs

def make_identity_dict(rng***REMOVED***:

    ***REMOVED*** make_identity_dict(rng***REMOVED*** -> dict

        Return a dictionary where elements of the rng sequence are
        mapped to themselves.

    ***REMOVED***
    res = {***REMOVED***
    for i in rng:
        res[i***REMOVED***=i
    return res

def make_encoding_map(decoding_map***REMOVED***:

    ***REMOVED*** Creates an encoding map from a decoding map.

        If a target mapping in the decoding map occurs multiple
        times, then that target is mapped to None (undefined mapping***REMOVED***,
        causing an exception when encountered by the charmap codec
        during translation.

        One example where this happens is cp875.py which decodes
        multiple character to \u001a.

    ***REMOVED***
    m = {***REMOVED***
    for k,v in decoding_map.items(***REMOVED***:
        if not v in m:
            m[v***REMOVED*** = k
        else:
            m[v***REMOVED*** = None
    return m

### error handlers

try:
    strict_errors = lookup_error("strict"***REMOVED***
    ignore_errors = lookup_error("ignore"***REMOVED***
    replace_errors = lookup_error("replace"***REMOVED***
    xmlcharrefreplace_errors = lookup_error("xmlcharrefreplace"***REMOVED***
    backslashreplace_errors = lookup_error("backslashreplace"***REMOVED***
except LookupError:
    # In --disable-unicode builds, these error handler are missing
    strict_errors = None
    ignore_errors = None
    replace_errors = None
    xmlcharrefreplace_errors = None
    backslashreplace_errors = None

# Tell modulefinder that using codecs probably needs the encodings
# package
_false = 0
if _false:
    import encodings

### Tests

if __name__ == '__main__':

    # Make stdout translate Latin-1 output into UTF-8 output
    sys.stdout = EncodedFile(sys.stdout, 'latin-1', 'utf-8'***REMOVED***

    # Have stdin translate Latin-1 input into UTF-8 input
    sys.stdin = EncodedFile(sys.stdin, 'utf-8', 'latin-1'***REMOVED***
