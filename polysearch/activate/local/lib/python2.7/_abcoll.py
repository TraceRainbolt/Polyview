# Copyright 2007 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

***REMOVED***Abstract Base Classes (ABCs***REMOVED*** for collections, according to PEP 3119.

DON'T USE THIS MODULE DIRECTLY!  The classes here should be imported
via collections; they are defined here only to alleviate certain
bootstrapping issues.  Unit tests are in test_collections.
***REMOVED***

from abc import ABCMeta, abstractmethod
import sys

__all__ = ["Hashable", "Iterable", "Iterator",
           "Sized", "Container", "Callable",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",
           ***REMOVED***

### ONE-TRICK PONIES ###

def _hasattr(C, attr***REMOVED***:
    try:
        return any(attr in B.__dict__ for B in C.__mro__***REMOVED***
    except AttributeError:
        # Old-style class
        return hasattr(C, attr***REMOVED***


class Hashable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __hash__(self***REMOVED***:
        return 0

    @classmethod
    def __subclasshook__(cls, C***REMOVED***:
        if cls is Hashable:
            try:
                for B in C.__mro__:
                    if "__hash__" in B.__dict__:
                        if B.__dict__["__hash__"***REMOVED***:
                            return True
                        break
            except AttributeError:
                # Old-style class
                if getattr(C, "__hash__", None***REMOVED***:
                    return True
        return NotImplemented


class Iterable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self***REMOVED***:
        while False:
            yield None

    @classmethod
    def __subclasshook__(cls, C***REMOVED***:
        if cls is Iterable:
            if _hasattr(C, "__iter__"***REMOVED***:
                return True
        return NotImplemented

Iterable.register(str***REMOVED***


class Iterator(Iterable***REMOVED***:

    @abstractmethod
    def next(self***REMOVED***:
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self***REMOVED***:
        return self

    @classmethod
    def __subclasshook__(cls, C***REMOVED***:
        if cls is Iterator:
            if _hasattr(C, "next"***REMOVED*** and _hasattr(C, "__iter__"***REMOVED***:
                return True
        return NotImplemented


class Sized:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __len__(self***REMOVED***:
        return 0

    @classmethod
    def __subclasshook__(cls, C***REMOVED***:
        if cls is Sized:
            if _hasattr(C, "__len__"***REMOVED***:
                return True
        return NotImplemented


class Container:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __contains__(self, x***REMOVED***:
        return False

    @classmethod
    def __subclasshook__(cls, C***REMOVED***:
        if cls is Container:
            if _hasattr(C, "__contains__"***REMOVED***:
                return True
        return NotImplemented


class Callable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, *args, **kwds***REMOVED***:
        return False

    @classmethod
    def __subclasshook__(cls, C***REMOVED***:
        if cls is Callable:
            if _hasattr(C, "__call__"***REMOVED***:
                return True
        return NotImplemented


### SETS ###


class Set(Sized, Iterable, Container***REMOVED***:
    ***REMOVED***A set is a finite, iterable container.

    This class provides concrete generic implementations of all
    methods except for __contains__, __iter__ and __len__.

    To override the comparisons (presumably for speed, as the
    semantics are fixed***REMOVED***, all you have to do is redefine __le__ and
    then the other operations will automatically follow suit.
    ***REMOVED***

    def __le__(self, other***REMOVED***:
        if not isinstance(other, Set***REMOVED***:
            return NotImplemented
        if len(self***REMOVED*** > len(other***REMOVED***:
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    def __lt__(self, other***REMOVED***:
        if not isinstance(other, Set***REMOVED***:
            return NotImplemented
        return len(self***REMOVED*** < len(other***REMOVED*** and self.__le__(other***REMOVED***

    def __gt__(self, other***REMOVED***:
        if not isinstance(other, Set***REMOVED***:
            return NotImplemented
        return other.__lt__(self***REMOVED***

    def __ge__(self, other***REMOVED***:
        if not isinstance(other, Set***REMOVED***:
            return NotImplemented
        return other.__le__(self***REMOVED***

    def __eq__(self, other***REMOVED***:
        if not isinstance(other, Set***REMOVED***:
            return NotImplemented
        return len(self***REMOVED*** == len(other***REMOVED*** and self.__le__(other***REMOVED***

    def __ne__(self, other***REMOVED***:
        return not (self == other***REMOVED***

    @classmethod
    def _from_iterable(cls, it***REMOVED***:
        '''Construct an instance of the class from any iterable input.

        Must override this method if the class constructor signature
        does not accept an iterable for an input.
        '''
        return cls(it***REMOVED***

    def __and__(self, other***REMOVED***:
        if not isinstance(other, Iterable***REMOVED***:
            return NotImplemented
        return self._from_iterable(value for value in other if value in self***REMOVED***

    def isdisjoint(self, other***REMOVED***:
        'Return True if two sets have a null intersection.'
        for value in other:
            if value in self:
                return False
        return True

    def __or__(self, other***REMOVED***:
        if not isinstance(other, Iterable***REMOVED***:
            return NotImplemented
        chain = (e for s in (self, other***REMOVED*** for e in s***REMOVED***
        return self._from_iterable(chain***REMOVED***

    def __sub__(self, other***REMOVED***:
        if not isinstance(other, Set***REMOVED***:
            if not isinstance(other, Iterable***REMOVED***:
                return NotImplemented
            other = self._from_iterable(other***REMOVED***
        return self._from_iterable(value for value in self
                                   if value not in other***REMOVED***

    def __xor__(self, other***REMOVED***:
        if not isinstance(other, Set***REMOVED***:
            if not isinstance(other, Iterable***REMOVED***:
                return NotImplemented
            other = self._from_iterable(other***REMOVED***
        return (self - other***REMOVED*** | (other - self***REMOVED***

    # Sets are not hashable by default, but subclasses can change this
    __hash__ = None

    def _hash(self***REMOVED***:
        ***REMOVED***Compute the hash value of a set.

        Note that we don't define __hash__: not all sets are hashable.
        But if you define a hashable set type, its __hash__ should
        call this function.

        This must be compatible __eq__.

        All sets ought to compare equal if they contain the same
        elements, regardless of how they are implemented, and
        regardless of the order of the elements; so there's not much
        freedom for __eq__ or __hash__.  We match the algorithm used
        by the built-in frozenset type.
        ***REMOVED***
        MAX = sys.maxint
        MASK = 2 * MAX + 1
        n = len(self***REMOVED***
        h = 1927868237 * (n + 1***REMOVED***
        h &= MASK
        for x in self:
            hx = hash(x***REMOVED***
            h ^= (hx ^ (hx << 16***REMOVED*** ^ 89869747***REMOVED***  * 3644798167
            h &= MASK
        h = h * 69069 + 907133923
        h &= MASK
        if h > MAX:
            h -= MASK + 1
        if h == -1:
            h = 590923713
        return h

Set.register(frozenset***REMOVED***


class MutableSet(Set***REMOVED***:
    ***REMOVED***A mutable set is a finite, iterable container.

    This class provides concrete generic implementations of all
    methods except for __contains__, __iter__, __len__,
    add(***REMOVED***, and discard(***REMOVED***.

    To override the comparisons (presumably for speed, as the
    semantics are fixed***REMOVED***, all you have to do is redefine __le__ and
    then the other operations will automatically follow suit.
    ***REMOVED***

    @abstractmethod
    def add(self, value***REMOVED***:
        ***REMOVED***Add an element.***REMOVED***
        raise NotImplementedError

    @abstractmethod
    def discard(self, value***REMOVED***:
        ***REMOVED***Remove an element.  Do not raise an exception if absent.***REMOVED***
        raise NotImplementedError

    def remove(self, value***REMOVED***:
        ***REMOVED***Remove an element. If not a member, raise a KeyError.***REMOVED***
        if value not in self:
            raise KeyError(value***REMOVED***
        self.discard(value***REMOVED***

    def pop(self***REMOVED***:
        ***REMOVED***Return the popped value.  Raise KeyError if empty.***REMOVED***
        it = iter(self***REMOVED***
        try:
            value = next(it***REMOVED***
        except StopIteration:
            raise KeyError
        self.discard(value***REMOVED***
        return value

    def clear(self***REMOVED***:
        ***REMOVED***This is slow (creates N new iterators!***REMOVED*** but effective.***REMOVED***
        try:
            while True:
                self.pop(***REMOVED***
        except KeyError:
            pass

    def __ior__(self, it***REMOVED***:
        for value in it:
            self.add(value***REMOVED***
        return self

    def __iand__(self, it***REMOVED***:
        for value in (self - it***REMOVED***:
            self.discard(value***REMOVED***
        return self

    def __ixor__(self, it***REMOVED***:
        if it is self:
            self.clear(***REMOVED***
        else:
            if not isinstance(it, Set***REMOVED***:
                it = self._from_iterable(it***REMOVED***
            for value in it:
                if value in self:
                    self.discard(value***REMOVED***
                else:
                    self.add(value***REMOVED***
        return self

    def __isub__(self, it***REMOVED***:
        if it is self:
            self.clear(***REMOVED***
        else:
            for value in it:
                self.discard(value***REMOVED***
        return self

MutableSet.register(set***REMOVED***


### MAPPINGS ###


class Mapping(Sized, Iterable, Container***REMOVED***:

    ***REMOVED***A Mapping is a generic container for associating key/value
    pairs.

    This class provides concrete generic implementations of all
    methods except for __getitem__, __iter__, and __len__.

    ***REMOVED***

    @abstractmethod
    def __getitem__(self, key***REMOVED***:
        raise KeyError

    def get(self, key, default=None***REMOVED***:
        'D.get(k[,d***REMOVED******REMOVED*** -> D[k***REMOVED*** if k in D, else d.  d defaults to None.'
        try:
            return self[key***REMOVED***
        except KeyError:
            return default

    def __contains__(self, key***REMOVED***:
        try:
            self[key***REMOVED***
        except KeyError:
            return False
        else:
            return True

    def iterkeys(self***REMOVED***:
        'D.iterkeys(***REMOVED*** -> an iterator over the keys of D'
        return iter(self***REMOVED***

    def itervalues(self***REMOVED***:
        'D.itervalues(***REMOVED*** -> an iterator over the values of D'
        for key in self:
            yield self[key***REMOVED***

    def iteritems(self***REMOVED***:
        'D.iteritems(***REMOVED*** -> an iterator over the (key, value***REMOVED*** items of D'
        for key in self:
            yield (key, self[key***REMOVED******REMOVED***

    def keys(self***REMOVED***:
        "D.keys(***REMOVED*** -> list of D's keys"
        return list(self***REMOVED***

    def items(self***REMOVED***:
        "D.items(***REMOVED*** -> list of D's (key, value***REMOVED*** pairs, as 2-tuples"
        return [(key, self[key***REMOVED******REMOVED*** for key in self***REMOVED***

    def values(self***REMOVED***:
        "D.values(***REMOVED*** -> list of D's values"
        return [self[key***REMOVED*** for key in self***REMOVED***

    # Mappings are not hashable by default, but subclasses can change this
    __hash__ = None

    def __eq__(self, other***REMOVED***:
        if not isinstance(other, Mapping***REMOVED***:
            return NotImplemented
        return dict(self.items(***REMOVED******REMOVED*** == dict(other.items(***REMOVED******REMOVED***

    def __ne__(self, other***REMOVED***:
        return not (self == other***REMOVED***

class MappingView(Sized***REMOVED***:

    def __init__(self, mapping***REMOVED***:
        self._mapping = mapping

    def __len__(self***REMOVED***:
        return len(self._mapping***REMOVED***

    def __repr__(self***REMOVED***:
        return '{0.__class__.__name__***REMOVED***({0._mapping!r***REMOVED******REMOVED***'.format(self***REMOVED***


class KeysView(MappingView, Set***REMOVED***:

    @classmethod
    def _from_iterable(self, it***REMOVED***:
        return set(it***REMOVED***

    def __contains__(self, key***REMOVED***:
        return key in self._mapping

    def __iter__(self***REMOVED***:
        for key in self._mapping:
            yield key


class ItemsView(MappingView, Set***REMOVED***:

    @classmethod
    def _from_iterable(self, it***REMOVED***:
        return set(it***REMOVED***

    def __contains__(self, item***REMOVED***:
        key, value = item
        try:
            v = self._mapping[key***REMOVED***
        except KeyError:
            return False
        else:
            return v == value

    def __iter__(self***REMOVED***:
        for key in self._mapping:
            yield (key, self._mapping[key***REMOVED******REMOVED***


class ValuesView(MappingView***REMOVED***:

    def __contains__(self, value***REMOVED***:
        for key in self._mapping:
            if value == self._mapping[key***REMOVED***:
                return True
        return False

    def __iter__(self***REMOVED***:
        for key in self._mapping:
            yield self._mapping[key***REMOVED***


class MutableMapping(Mapping***REMOVED***:

    ***REMOVED***A MutableMapping is a generic container for associating
    key/value pairs.

    This class provides concrete generic implementations of all
    methods except for __getitem__, __setitem__, __delitem__,
    __iter__, and __len__.

    ***REMOVED***

    @abstractmethod
    def __setitem__(self, key, value***REMOVED***:
        raise KeyError

    @abstractmethod
    def __delitem__(self, key***REMOVED***:
        raise KeyError

    __marker = object(***REMOVED***

    def pop(self, key, default=__marker***REMOVED***:
        '''D.pop(k[,d***REMOVED******REMOVED*** -> v, remove specified key and return the corresponding value.
          If key is not found, d is returned if given, otherwise KeyError is raised.
        '''
        try:
            value = self[key***REMOVED***
        except KeyError:
            if default is self.__marker:
                raise
            return default
        else:
            del self[key***REMOVED***
            return value

    def popitem(self***REMOVED***:
        '''D.popitem(***REMOVED*** -> (k, v***REMOVED***, remove and return some (key, value***REMOVED*** pair
           as a 2-tuple; but raise KeyError if D is empty.
        '''
        try:
            key = next(iter(self***REMOVED******REMOVED***
        except StopIteration:
            raise KeyError
        value = self[key***REMOVED***
        del self[key***REMOVED***
        return key, value

    def clear(self***REMOVED***:
        'D.clear(***REMOVED*** -> None.  Remove all items from D.'
        try:
            while True:
                self.popitem(***REMOVED***
        except KeyError:
            pass

    def update(*args, **kwds***REMOVED***:
        ''' D.update([E, ***REMOVED*****F***REMOVED*** -> None.  Update D from mapping/iterable E and F.
            If E present and has a .keys(***REMOVED*** method, does:     for k in E: D[k***REMOVED*** = E[k***REMOVED***
            If E present and lacks .keys(***REMOVED*** method, does:     for (k, v***REMOVED*** in E: D[k***REMOVED*** = v
            In either case, this is followed by: for k, v in F.items(***REMOVED***: D[k***REMOVED*** = v
        '''
        if len(args***REMOVED*** > 2:
            raise TypeError("update(***REMOVED*** takes at most 2 positional "
                            "arguments ({***REMOVED*** given***REMOVED***".format(len(args***REMOVED******REMOVED******REMOVED***
        elif not args:
            raise TypeError("update(***REMOVED*** takes at least 1 argument (0 given***REMOVED***"***REMOVED***
        self = args[0***REMOVED***
        other = args[1***REMOVED*** if len(args***REMOVED*** >= 2 else (***REMOVED***

        if isinstance(other, Mapping***REMOVED***:
            for key in other:
                self[key***REMOVED*** = other[key***REMOVED***
        elif hasattr(other, "keys"***REMOVED***:
            for key in other.keys(***REMOVED***:
                self[key***REMOVED*** = other[key***REMOVED***
        else:
            for key, value in other:
                self[key***REMOVED*** = value
        for key, value in kwds.items(***REMOVED***:
            self[key***REMOVED*** = value

    def setdefault(self, key, default=None***REMOVED***:
        'D.setdefault(k[,d***REMOVED******REMOVED*** -> D.get(k,d***REMOVED***, also set D[k***REMOVED***=d if k not in D'
        try:
            return self[key***REMOVED***
        except KeyError:
            self[key***REMOVED*** = default
        return default

MutableMapping.register(dict***REMOVED***


### SEQUENCES ###


class Sequence(Sized, Iterable, Container***REMOVED***:
    ***REMOVED***All the operations on a read-only sequence.

    Concrete subclasses must override __new__ or __init__,
    __getitem__, and __len__.
    ***REMOVED***

    @abstractmethod
    def __getitem__(self, index***REMOVED***:
        raise IndexError

    def __iter__(self***REMOVED***:
        i = 0
        try:
            while True:
                v = self[i***REMOVED***
                yield v
                i += 1
        except IndexError:
            return

    def __contains__(self, value***REMOVED***:
        for v in self:
            if v == value:
                return True
        return False

    def __reversed__(self***REMOVED***:
        for i in reversed(range(len(self***REMOVED******REMOVED******REMOVED***:
            yield self[i***REMOVED***

    def index(self, value***REMOVED***:
        '''S.index(value***REMOVED*** -> integer -- return first index of value.
           Raises ValueError if the value is not present.
        '''
        for i, v in enumerate(self***REMOVED***:
            if v == value:
                return i
        raise ValueError

    def count(self, value***REMOVED***:
        'S.count(value***REMOVED*** -> integer -- return number of occurrences of value'
        return sum(1 for v in self if v == value***REMOVED***

Sequence.register(tuple***REMOVED***
Sequence.register(basestring***REMOVED***
Sequence.register(buffer***REMOVED***
Sequence.register(xrange***REMOVED***


class MutableSequence(Sequence***REMOVED***:

    ***REMOVED***All the operations on a read-only sequence.

    Concrete subclasses must provide __new__ or __init__,
    __getitem__, __setitem__, __delitem__, __len__, and insert(***REMOVED***.

    ***REMOVED***

    @abstractmethod
    def __setitem__(self, index, value***REMOVED***:
        raise IndexError

    @abstractmethod
    def __delitem__(self, index***REMOVED***:
        raise IndexError

    @abstractmethod
    def insert(self, index, value***REMOVED***:
        'S.insert(index, object***REMOVED*** -- insert object before index'
        raise IndexError

    def append(self, value***REMOVED***:
        'S.append(object***REMOVED*** -- append object to the end of the sequence'
        self.insert(len(self***REMOVED***, value***REMOVED***

    def reverse(self***REMOVED***:
        'S.reverse(***REMOVED*** -- reverse *IN PLACE*'
        n = len(self***REMOVED***
        for i in range(n//2***REMOVED***:
            self[i***REMOVED***, self[n-i-1***REMOVED*** = self[n-i-1***REMOVED***, self[i***REMOVED***

    def extend(self, values***REMOVED***:
        'S.extend(iterable***REMOVED*** -- extend sequence by appending elements from the iterable'
        for v in values:
            self.append(v***REMOVED***

    def pop(self, index=-1***REMOVED***:
        '''S.pop([index***REMOVED******REMOVED*** -> item -- remove and return item at index (default last***REMOVED***.
           Raise IndexError if list is empty or index is out of range.
        '''
        v = self[index***REMOVED***
        del self[index***REMOVED***
        return v

    def remove(self, value***REMOVED***:
        '''S.remove(value***REMOVED*** -- remove first occurrence of value.
           Raise ValueError if the value is not present.
        '''
        del self[self.index(value***REMOVED******REMOVED***

    def __iadd__(self, values***REMOVED***:
        self.extend(values***REMOVED***
        return self

MutableSequence.register(list***REMOVED***
