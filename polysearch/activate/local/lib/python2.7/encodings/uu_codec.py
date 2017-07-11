***REMOVED*** Python 'uu_codec' Codec - UU content transfer encoding

    Unlike most of the other codecs which target Unicode, this codec
    will return Python string objects for both encode and decode.

    Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***. Some details were
    adapted from uu.py which was written by Lance Ellinghouse and
    modified by Jack Jansen and Fredrik Lundh.

***REMOVED***
import codecs, binascii

### Codec APIs

def uu_encode(input,errors='strict',filename='<data>',mode=0666***REMOVED***:

    ***REMOVED*** Encodes the object input and returns a tuple (output
        object, length consumed***REMOVED***.

        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.

    ***REMOVED***
    assert errors == 'strict'
    from cStringIO import StringIO
    from binascii import b2a_uu
    # using str(***REMOVED*** because of cStringIO's Unicode undesired Unicode behavior.
    infile = StringIO(str(input***REMOVED******REMOVED***
    outfile = StringIO(***REMOVED***
    read = infile.read
    write = outfile.write

    # Encode
    write('begin %o %s\n' % (mode & 0777, filename***REMOVED******REMOVED***
    chunk = read(45***REMOVED***
    while chunk:
        write(b2a_uu(chunk***REMOVED******REMOVED***
        chunk = read(45***REMOVED***
    write(' \nend\n'***REMOVED***

    return (outfile.getvalue(***REMOVED***, len(input***REMOVED******REMOVED***

def uu_decode(input,errors='strict'***REMOVED***:

    ***REMOVED*** Decodes the object input and returns a tuple (output
        object, length consumed***REMOVED***.

        input must be an object which provides the bf_getreadbuf
        buffer slot. Python strings, buffer objects and memory
        mapped files are examples of objects providing this slot.

        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.

        Note: filename and file mode information in the input data is
        ignored.

    ***REMOVED***
    assert errors == 'strict'
    from cStringIO import StringIO
    from binascii import a2b_uu
    infile = StringIO(str(input***REMOVED******REMOVED***
    outfile = StringIO(***REMOVED***
    readline = infile.readline
    write = outfile.write

    # Find start of encoded data
    while 1:
        s = readline(***REMOVED***
        if not s:
            raise ValueError, 'Missing "begin" line in input data'
        if s[:5***REMOVED*** == 'begin':
            break

    # Decode
    while 1:
        s = readline(***REMOVED***
        if not s or \
           s == 'end\n':
            break
        try:
            data = a2b_uu(s***REMOVED***
        except binascii.Error, v:
            # Workaround for broken uuencoders by /Fredrik Lundh
            nbytes = (((ord(s[0***REMOVED******REMOVED***-32***REMOVED*** & 63***REMOVED*** * 4 + 5***REMOVED*** / 3
            data = a2b_uu(s[:nbytes***REMOVED******REMOVED***
            #sys.stderr.write("Warning: %s\n" % str(v***REMOVED******REMOVED***
        write(data***REMOVED***
    if not s:
        raise ValueError, 'Truncated input data'

    return (outfile.getvalue(***REMOVED***, len(input***REMOVED******REMOVED***

class Codec(codecs.Codec***REMOVED***:

    def encode(self,input,errors='strict'***REMOVED***:
        return uu_encode(input,errors***REMOVED***

    def decode(self,input,errors='strict'***REMOVED***:
        return uu_decode(input,errors***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return uu_encode(input, self.errors***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        return uu_decode(input, self.errors***REMOVED***[0***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='uu',
        encode=uu_encode,
        decode=uu_decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
