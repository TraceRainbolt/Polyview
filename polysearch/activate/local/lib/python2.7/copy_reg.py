***REMOVED***Helper to provide extensibility for pickle/cPickle.

This is only useful to add pickle support for extension types defined in
C, not for instances of user-defined classes.
***REMOVED***

from types import ClassType as _ClassType

__all__ = ["pickle", "constructor",
           "add_extension", "remove_extension", "clear_extension_cache"***REMOVED***

dispatch_table = {***REMOVED***

def pickle(ob_type, pickle_function, constructor_ob=None***REMOVED***:
    if type(ob_type***REMOVED*** is _ClassType:
        raise TypeError("copy_reg is not intended for use with classes"***REMOVED***

    if not hasattr(pickle_function, '__call__'***REMOVED***:
        raise TypeError("reduction functions must be callable"***REMOVED***
    dispatch_table[ob_type***REMOVED*** = pickle_function

    # The constructor_ob function is a vestige of safe for unpickling.
    # There is no reason for the caller to pass it anymore.
    if constructor_ob is not None:
        constructor(constructor_ob***REMOVED***

def constructor(object***REMOVED***:
    if not hasattr(object, '__call__'***REMOVED***:
        raise TypeError("constructors must be callable"***REMOVED***

# Example: provide pickling support for complex numbers.

try:
    complex
except NameError:
    pass
else:

    def pickle_complex(c***REMOVED***:
        return complex, (c.real, c.imag***REMOVED***

    pickle(complex, pickle_complex, complex***REMOVED***

# Support for pickling new-style objects

def _reconstructor(cls, base, state***REMOVED***:
    if base is object:
        obj = object.__new__(cls***REMOVED***
    else:
        obj = base.__new__(cls, state***REMOVED***
        if base.__init__ != object.__init__:
            base.__init__(obj, state***REMOVED***
    return obj

_HEAPTYPE = 1<<9

# Python code for object.__reduce_ex__ for protocols 0 and 1

def _reduce_ex(self, proto***REMOVED***:
    assert proto < 2
    for base in self.__class__.__mro__:
        if hasattr(base, '__flags__'***REMOVED*** and not base.__flags__ & _HEAPTYPE:
            break
    else:
        base = object # not really reachable
    if base is object:
        state = None
    else:
        if base is self.__class__:
            raise TypeError, "can't pickle %s objects" % base.__name__
        state = base(self***REMOVED***
    args = (self.__class__, base, state***REMOVED***
    try:
        getstate = self.__getstate__
    except AttributeError:
        if getattr(self, "__slots__", None***REMOVED***:
            raise TypeError("a class that defines __slots__ without "
                            "defining __getstate__ cannot be pickled"***REMOVED***
        try:
            dict = self.__dict__
        except AttributeError:
            dict = None
    else:
        dict = getstate(***REMOVED***
    if dict:
        return _reconstructor, args, dict
    else:
        return _reconstructor, args

# Helper for __reduce_ex__ protocol 2

def __newobj__(cls, *args***REMOVED***:
    return cls.__new__(cls, *args***REMOVED***

def _slotnames(cls***REMOVED***:
    ***REMOVED***Return a list of slot names for a given class.

    This needs to find slots defined by the class and its bases, so we
    can't simply return the __slots__ attribute.  We must walk down
    the Method Resolution Order and concatenate the __slots__ of each
    class found there.  (This assumes classes don't modify their
    __slots__ attribute to misrepresent their slots after the class is
    defined.***REMOVED***
    ***REMOVED***

    # Get the value from a cache in the class if possible
    names = cls.__dict__.get("__slotnames__"***REMOVED***
    if names is not None:
        return names

    # Not cached -- calculate the value
    names = [***REMOVED***
    if not hasattr(cls, "__slots__"***REMOVED***:
        # This class has no slots
        pass
    else:
        # Slots found -- gather slot names from all base classes
        for c in cls.__mro__:
            if "__slots__" in c.__dict__:
                slots = c.__dict__['__slots__'***REMOVED***
                # if class has a single slot, it can be given as a string
                if isinstance(slots, basestring***REMOVED***:
                    slots = (slots,***REMOVED***
                for name in slots:
                    # special descriptors
                    if name in ("__dict__", "__weakref__"***REMOVED***:
                        continue
                    # mangled names
                    elif name.startswith('__'***REMOVED*** and not name.endswith('__'***REMOVED***:
                        names.append('_%s%s' % (c.__name__, name***REMOVED******REMOVED***
                    else:
                        names.append(name***REMOVED***

    # Cache the outcome in the class if at all possible
    try:
        cls.__slotnames__ = names
    except:
        pass # But don't die if we can't

    return names

# A registry of extension codes.  This is an ad-hoc compression
# mechanism.  Whenever a global reference to <module>, <name> is about
# to be pickled, the (<module>, <name>***REMOVED*** tuple is looked up here to see
# if it is a registered extension code for it.  Extension codes are
# universal, so that the meaning of a pickle does not depend on
# context.  (There are also some codes reserved for local use that
# don't have this restriction.***REMOVED***  Codes are positive ints; 0 is
# reserved.

_extension_registry = {***REMOVED***                # key -> code
_inverted_registry = {***REMOVED***                 # code -> key
_extension_cache = {***REMOVED***                   # code -> object
# Don't ever rebind those names:  cPickle grabs a reference to them when
# it's initialized, and won't see a rebinding.

def add_extension(module, name, code***REMOVED***:
    ***REMOVED***Register an extension code.***REMOVED***
    code = int(code***REMOVED***
    if not 1 <= code <= 0x7fffffff:
        raise ValueError, "code out of range"
    key = (module, name***REMOVED***
    if (_extension_registry.get(key***REMOVED*** == code and
        _inverted_registry.get(code***REMOVED*** == key***REMOVED***:
        return # Redundant registrations are benign
    if key in _extension_registry:
        raise ValueError("key %s is already registered with code %s" %
                         (key, _extension_registry[key***REMOVED******REMOVED******REMOVED***
    if code in _inverted_registry:
        raise ValueError("code %s is already in use for key %s" %
                         (code, _inverted_registry[code***REMOVED******REMOVED******REMOVED***
    _extension_registry[key***REMOVED*** = code
    _inverted_registry[code***REMOVED*** = key

def remove_extension(module, name, code***REMOVED***:
    ***REMOVED***Unregister an extension code.  For testing only.***REMOVED***
    key = (module, name***REMOVED***
    if (_extension_registry.get(key***REMOVED*** != code or
        _inverted_registry.get(code***REMOVED*** != key***REMOVED***:
        raise ValueError("key %s is not registered with code %s" %
                         (key, code***REMOVED******REMOVED***
    del _extension_registry[key***REMOVED***
    del _inverted_registry[code***REMOVED***
    if code in _extension_cache:
        del _extension_cache[code***REMOVED***

def clear_extension_cache(***REMOVED***:
    _extension_cache.clear(***REMOVED***

# Standard extension code assignments

# Reserved ranges

# First  Last Count  Purpose
#     1   127   127  Reserved for Python standard library
#   128   191    64  Reserved for Zope
#   192   239    48  Reserved for 3rd parties
#   240   255    16  Reserved for private use (will never be assigned***REMOVED***
#   256   Inf   Inf  Reserved for future assignment

# Extension codes are assigned by the Python Software Foundation.
