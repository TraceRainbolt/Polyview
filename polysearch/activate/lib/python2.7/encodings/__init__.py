***REMOVED*** Standard "encodings" Package

    Standard Python encoding modules are stored in this package
    directory.

    Codec modules must have names corresponding to normalized encoding
    names as defined in the normalize_encoding(***REMOVED*** function below, e.g.
    'utf-8' must be implemented by the module 'utf_8.py'.

    Each codec module must export the following interface:

    * getregentry(***REMOVED*** -> codecs.CodecInfo object
    The getregentry(***REMOVED*** API must a CodecInfo object with encoder, decoder,
    incrementalencoder, incrementaldecoder, streamwriter and streamreader
    atttributes which adhere to the Python Codec Interface Standard.

    In addition, a module may optionally also define the following
    APIs which are then used by the package's codec search function:

    * getaliases(***REMOVED*** -> sequence of encoding name strings to use as aliases

    Alias names returned by getaliases(***REMOVED*** must be normalized encoding
    names as defined by normalize_encoding(***REMOVED***.

Written by Marc-Andre Lemburg (mal@lemburg.com***REMOVED***.

(c***REMOVED*** Copyright CNRI, All Rights Reserved. NO WARRANTY.

***REMOVED***#"

import codecs
from encodings import aliases
import __builtin__

_cache = {***REMOVED***
_unknown = '--unknown--'
_import_tail = ['*'***REMOVED***
_norm_encoding_map = ('                                              . '
                      '0123456789       ABCDEFGHIJKLMNOPQRSTUVWXYZ     '
                      ' abcdefghijklmnopqrstuvwxyz                     '
                      '                                                '
                      '                                                '
                      '                '***REMOVED***
_aliases = aliases.aliases

class CodecRegistryError(LookupError, SystemError***REMOVED***:
    pass

def normalize_encoding(encoding***REMOVED***:

    ***REMOVED*** Normalize an encoding name.

        Normalization works as follows: all non-alphanumeric
        characters except the dot used for Python package names are
        collapsed and replaced with a single underscore, e.g. '  -;#'
        becomes '_'. Leading and trailing underscores are removed.

        Note that encoding names should be ASCII only; if they do use
        non-ASCII characters, these must be Latin-1 compatible.

    ***REMOVED***
    # Make sure we have an 8-bit string, because .translate(***REMOVED*** works
    # differently for Unicode strings.
    if hasattr(__builtin__, "unicode"***REMOVED*** and isinstance(encoding, unicode***REMOVED***:
        # Note that .encode('latin-1'***REMOVED*** does *not* use the codec
        # registry, so this call doesn't recurse. (See unicodeobject.c
        # PyUnicode_AsEncodedString(***REMOVED*** for details***REMOVED***
        encoding = encoding.encode('latin-1'***REMOVED***
    return '_'.join(encoding.translate(_norm_encoding_map***REMOVED***.split(***REMOVED******REMOVED***

def search_function(encoding***REMOVED***:

    # Cache lookup
    entry = _cache.get(encoding, _unknown***REMOVED***
    if entry is not _unknown:
        return entry

    # Import the module:
    #
    # First try to find an alias for the normalized encoding
    # name and lookup the module using the aliased name, then try to
    # lookup the module using the standard import scheme, i.e. first
    # try in the encodings package, then at top-level.
    #
    norm_encoding = normalize_encoding(encoding***REMOVED***
    aliased_encoding = _aliases.get(norm_encoding***REMOVED*** or \
                       _aliases.get(norm_encoding.replace('.', '_'***REMOVED******REMOVED***
    if aliased_encoding is not None:
        modnames = [aliased_encoding,
                    norm_encoding***REMOVED***
    else:
        modnames = [norm_encoding***REMOVED***
    for modname in modnames:
        if not modname or '.' in modname:
            continue
        try:
            # Import is absolute to prevent the possibly malicious import of a
            # module with side-effects that is not in the 'encodings' package.
            mod = __import__('encodings.' + modname, fromlist=_import_tail,
                             level=0***REMOVED***
        except ImportError:
            pass
        else:
            break
    else:
        mod = None

    try:
        getregentry = mod.getregentry
    except AttributeError:
        # Not a codec module
        mod = None

    if mod is None:
        # Cache misses
        _cache[encoding***REMOVED*** = None
        return None

    # Now ask the module for the registry entry
    entry = getregentry(***REMOVED***
    if not isinstance(entry, codecs.CodecInfo***REMOVED***:
        if not 4 <= len(entry***REMOVED*** <= 7:
            raise CodecRegistryError,\
                 'module "%s" (%s***REMOVED*** failed to register' % \
                  (mod.__name__, mod.__file__***REMOVED***
        if not hasattr(entry[0***REMOVED***, '__call__'***REMOVED*** or \
           not hasattr(entry[1***REMOVED***, '__call__'***REMOVED*** or \
           (entry[2***REMOVED*** is not None and not hasattr(entry[2***REMOVED***, '__call__'***REMOVED******REMOVED*** or \
           (entry[3***REMOVED*** is not None and not hasattr(entry[3***REMOVED***, '__call__'***REMOVED******REMOVED*** or \
           (len(entry***REMOVED*** > 4 and entry[4***REMOVED*** is not None and not hasattr(entry[4***REMOVED***, '__call__'***REMOVED******REMOVED*** or \
           (len(entry***REMOVED*** > 5 and entry[5***REMOVED*** is not None and not hasattr(entry[5***REMOVED***, '__call__'***REMOVED******REMOVED***:
            raise CodecRegistryError,\
                'incompatible codecs in module "%s" (%s***REMOVED***' % \
                (mod.__name__, mod.__file__***REMOVED***
        if len(entry***REMOVED***<7 or entry[6***REMOVED*** is None:
            entry += (None,***REMOVED****(6-len(entry***REMOVED******REMOVED*** + (mod.__name__.split(".", 1***REMOVED***[1***REMOVED***,***REMOVED***
        entry = codecs.CodecInfo(*entry***REMOVED***

    # Cache the codec registry entry
    _cache[encoding***REMOVED*** = entry

    # Register its aliases (without overwriting previously registered
    # aliases***REMOVED***
    try:
        codecaliases = mod.getaliases(***REMOVED***
    except AttributeError:
        pass
    else:
        for alias in codecaliases:
            if alias not in _aliases:
                _aliases[alias***REMOVED*** = modname

    # Return the registry entry
    return entry

# Register the search_function in the Python codec registry
codecs.register(search_function***REMOVED***
