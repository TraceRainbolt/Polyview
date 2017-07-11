#! /usr/bin/python2.7
***REMOVED*** Python Character Mapping Codec for ROT13.

    See http://ucsub.colorado.edu/~kominek/rot13/ for details.

    Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

***REMOVED***#"

import codecs

### Codec APIs

class Codec(codecs.Codec***REMOVED***:

    def encode(self,input,errors='strict'***REMOVED***:
        return codecs.charmap_encode(input,errors,encoding_map***REMOVED***

    def decode(self,input,errors='strict'***REMOVED***:
        return codecs.charmap_decode(input,errors,decoding_map***REMOVED***

class IncrementalEncoder(codecs.IncrementalEncoder***REMOVED***:
    def encode(self, input, final=False***REMOVED***:
        return codecs.charmap_encode(input,self.errors,encoding_map***REMOVED***[0***REMOVED***

class IncrementalDecoder(codecs.IncrementalDecoder***REMOVED***:
    def decode(self, input, final=False***REMOVED***:
        return codecs.charmap_decode(input,self.errors,decoding_map***REMOVED***[0***REMOVED***

class StreamWriter(Codec,codecs.StreamWriter***REMOVED***:
    pass

class StreamReader(Codec,codecs.StreamReader***REMOVED***:
    pass

### encodings module API

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='rot-13',
        encode=Codec(***REMOVED***.encode,
        decode=Codec(***REMOVED***.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    ***REMOVED***

### Decoding Map

decoding_map = codecs.make_identity_dict(range(256***REMOVED******REMOVED***
decoding_map.update({
   0x0041: 0x004e,
   0x0042: 0x004f,
   0x0043: 0x0050,
   0x0044: 0x0051,
   0x0045: 0x0052,
   0x0046: 0x0053,
   0x0047: 0x0054,
   0x0048: 0x0055,
   0x0049: 0x0056,
   0x004a: 0x0057,
   0x004b: 0x0058,
   0x004c: 0x0059,
   0x004d: 0x005a,
   0x004e: 0x0041,
   0x004f: 0x0042,
   0x0050: 0x0043,
   0x0051: 0x0044,
   0x0052: 0x0045,
   0x0053: 0x0046,
   0x0054: 0x0047,
   0x0055: 0x0048,
   0x0056: 0x0049,
   0x0057: 0x004a,
   0x0058: 0x004b,
   0x0059: 0x004c,
   0x005a: 0x004d,
   0x0061: 0x006e,
   0x0062: 0x006f,
   0x0063: 0x0070,
   0x0064: 0x0071,
   0x0065: 0x0072,
   0x0066: 0x0073,
   0x0067: 0x0074,
   0x0068: 0x0075,
   0x0069: 0x0076,
   0x006a: 0x0077,
   0x006b: 0x0078,
   0x006c: 0x0079,
   0x006d: 0x007a,
   0x006e: 0x0061,
   0x006f: 0x0062,
   0x0070: 0x0063,
   0x0071: 0x0064,
   0x0072: 0x0065,
   0x0073: 0x0066,
   0x0074: 0x0067,
   0x0075: 0x0068,
   0x0076: 0x0069,
   0x0077: 0x006a,
   0x0078: 0x006b,
   0x0079: 0x006c,
   0x007a: 0x006d,
***REMOVED******REMOVED***

### Encoding Map

encoding_map = codecs.make_encoding_map(decoding_map***REMOVED***

### Filter API

def rot13(infile, outfile***REMOVED***:
    outfile.write(infile.read(***REMOVED***.encode('rot-13'***REMOVED******REMOVED***

if __name__ == '__main__':
    import sys
    rot13(sys.stdin, sys.stdout***REMOVED***
