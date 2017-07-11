#
# big5hkscs.py: Python Unicode Codec for BIG5HKSCS
#
# Written by Hye-Shik Chang <perky@FreeBSD.org>
#

import _codecs_hk, codecs
import _multibytecodec as mbc

codec = _codecs_hk.getcodec('big5hkscs'***REMOVED***

class Codec(codecs.Codec***REMOVED***:
    encode = codec.encode
    decode = codec.decode

class IncrementalEncoder(mbc.MultibyteIncrementalEncoder,
                         codecs.IncrementalEncoder***REMOVED***:
    codec = codec

class IncrementalDecoder(mbc.MultibyteIncrementalDecoder,
                         codecs.IncrementalDecoder***REMOVED***:
    codec = codec

class StreamReader(Codec, mbc.MultibyteStreamReader, codecs.StreamReader***REMOVED***:
    codec = codec

class StreamWriter(Codec, mbc.MultibyteStreamWriter, codecs.StreamWriter***REMOVED***:
    codec = codec

def getregentry(***REMOVED***:
    return codecs.CodecInfo(
        name='big5hkscs',
        encode=Codec(***REMOVED***.encode,
        decode=Codec(***REMOVED***.decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    ***REMOVED***
