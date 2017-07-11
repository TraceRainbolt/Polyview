# Copyright 2007 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

***REMOVED***Abstract Base Classes (ABCs***REMOVED*** according to PEP 3119.***REMOVED***

import types

from _weakrefset import WeakSet

# Instance of old-style class
class _C: pass
_InstanceType = type(_C(***REMOVED******REMOVED***


def abstractmethod(funcobj***REMOVED***:
    ***REMOVED***A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.

    Usage:

        class C:
            __metaclass__ = ABCMeta
            @abstractmethod
            def my_abstract_method(self, ...***REMOVED***:
                ...
    ***REMOVED***
    funcobj.__isabstractmethod__ = True
    return funcobj


class abstractproperty(property***REMOVED***:
    ***REMOVED***A decorator indicating abstract properties.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract properties are overridden.
    The abstract properties can be called using any of the normal
    'super' call mechanisms.

    Usage:

        class C:
            __metaclass__ = ABCMeta
            @abstractproperty
            def my_abstract_property(self***REMOVED***:
                ...

    This defines a read-only property; you can also define a read-write
    abstract property using the 'long' form of property declaration:

        class C:
            __metaclass__ = ABCMeta
            def getx(self***REMOVED***: ...
            def setx(self, value***REMOVED***: ...
            x = abstractproperty(getx, setx***REMOVED***
    ***REMOVED***
    __isabstractmethod__ = True


class ABCMeta(type***REMOVED***:

    ***REMOVED***Metaclass for defining Abstract Base Classes (ABCs***REMOVED***.

    Use this metaclass to create an ABC.  An ABC can be subclassed
    directly, and then acts as a mix-in class.  You can also register
    unrelated concrete classes (even built-in classes***REMOVED*** and unrelated
    ABCs as 'virtual subclasses' -- these and their descendants will
    be considered subclasses of the registering ABC by the built-in
    issubclass(***REMOVED*** function, but the registering ABC won't show up in
    their MRO (Method Resolution Order***REMOVED*** nor will method
    implementations defined by the registering ABC be callable (not
    even via super(***REMOVED******REMOVED***.

    ***REMOVED***

    # A global counter that is incremented each time a class is
    # registered as a virtual subclass of anything.  It forces the
    # negative cache to be cleared before its next use.
    _abc_invalidation_counter = 0

    def __new__(mcls, name, bases, namespace***REMOVED***:
        cls = super(ABCMeta, mcls***REMOVED***.__new__(mcls, name, bases, namespace***REMOVED***
        # Compute set of abstract method names
        abstracts = set(name
                     for name, value in namespace.items(***REMOVED***
                     if getattr(value, "__isabstractmethod__", False***REMOVED******REMOVED***
        for base in bases:
            for name in getattr(base, "__abstractmethods__", set(***REMOVED******REMOVED***:
                value = getattr(cls, name, None***REMOVED***
                if getattr(value, "__isabstractmethod__", False***REMOVED***:
                    abstracts.add(name***REMOVED***
        cls.__abstractmethods__ = frozenset(abstracts***REMOVED***
        # Set up inheritance registry
        cls._abc_registry = WeakSet(***REMOVED***
        cls._abc_cache = WeakSet(***REMOVED***
        cls._abc_negative_cache = WeakSet(***REMOVED***
        cls._abc_negative_cache_version = ABCMeta._abc_invalidation_counter
        return cls

    def register(cls, subclass***REMOVED***:
        ***REMOVED***Register a virtual subclass of an ABC.***REMOVED***
        if not isinstance(subclass, (type, types.ClassType***REMOVED******REMOVED***:
            raise TypeError("Can only register classes"***REMOVED***
        if issubclass(subclass, cls***REMOVED***:
            return  # Already a subclass
        # Subtle: test for cycles *after* testing for "already a subclass";
        # this means we allow X.register(X***REMOVED*** and interpret it as a no-op.
        if issubclass(cls, subclass***REMOVED***:
            # This would create a cycle, which is bad for the algorithm below
            raise RuntimeError("Refusing to create an inheritance cycle"***REMOVED***
        cls._abc_registry.add(subclass***REMOVED***
        ABCMeta._abc_invalidation_counter += 1  # Invalidate negative cache

    def _dump_registry(cls, file=None***REMOVED***:
        ***REMOVED***Debug helper to print the ABC registry.***REMOVED***
        print >> file, "Class: %s.%s" % (cls.__module__, cls.__name__***REMOVED***
        print >> file, "Inv.counter: %s" % ABCMeta._abc_invalidation_counter
        for name in sorted(cls.__dict__.keys(***REMOVED******REMOVED***:
            if name.startswith("_abc_"***REMOVED***:
                value = getattr(cls, name***REMOVED***
                print >> file, "%s: %r" % (name, value***REMOVED***

    def __instancecheck__(cls, instance***REMOVED***:
        ***REMOVED***Override for isinstance(instance, cls***REMOVED***.***REMOVED***
        # Inline the cache checking when it's simple.
        subclass = getattr(instance, '__class__', None***REMOVED***
        if subclass is not None and subclass in cls._abc_cache:
            return True
        subtype = type(instance***REMOVED***
        # Old-style instances
        if subtype is _InstanceType:
            subtype = subclass
        if subtype is subclass or subclass is None:
            if (cls._abc_negative_cache_version ==
                ABCMeta._abc_invalidation_counter and
                subtype in cls._abc_negative_cache***REMOVED***:
                return False
            # Fall back to the subclass check.
            return cls.__subclasscheck__(subtype***REMOVED***
        return (cls.__subclasscheck__(subclass***REMOVED*** or
                cls.__subclasscheck__(subtype***REMOVED******REMOVED***

    def __subclasscheck__(cls, subclass***REMOVED***:
        ***REMOVED***Override for issubclass(subclass, cls***REMOVED***.***REMOVED***
        # Check cache
        if subclass in cls._abc_cache:
            return True
        # Check negative cache; may have to invalidate
        if cls._abc_negative_cache_version < ABCMeta._abc_invalidation_counter:
            # Invalidate the negative cache
            cls._abc_negative_cache = WeakSet(***REMOVED***
            cls._abc_negative_cache_version = ABCMeta._abc_invalidation_counter
        elif subclass in cls._abc_negative_cache:
            return False
        # Check the subclass hook
        ok = cls.__subclasshook__(subclass***REMOVED***
        if ok is not NotImplemented:
            assert isinstance(ok, bool***REMOVED***
            if ok:
                cls._abc_cache.add(subclass***REMOVED***
            else:
                cls._abc_negative_cache.add(subclass***REMOVED***
            return ok
        # Check if it's a direct subclass
        if cls in getattr(subclass, '__mro__', (***REMOVED******REMOVED***:
            cls._abc_cache.add(subclass***REMOVED***
            return True
        # Check if it's a subclass of a registered class (recursive***REMOVED***
        for rcls in cls._abc_registry:
            if issubclass(subclass, rcls***REMOVED***:
                cls._abc_cache.add(subclass***REMOVED***
                return True
        # Check if it's a subclass of a subclass (recursive***REMOVED***
        for scls in cls.__subclasses__(***REMOVED***:
            if issubclass(subclass, scls***REMOVED***:
                cls._abc_cache.add(subclass***REMOVED***
                return True
        # No dice; update negative cache
        cls._abc_negative_cache.add(subclass***REMOVED***
        return False
