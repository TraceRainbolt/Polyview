***REMOVED***A more or less complete user-defined wrapper around dictionary objects.***REMOVED***

class UserDict:
    def __init__(self, dict=None, **kwargs***REMOVED***:
        self.data = {***REMOVED***
        if dict is not None:
            self.update(dict***REMOVED***
        if len(kwargs***REMOVED***:
            self.update(kwargs***REMOVED***
    def __repr__(self***REMOVED***: return repr(self.data***REMOVED***
    def __cmp__(self, dict***REMOVED***:
        if isinstance(dict, UserDict***REMOVED***:
            return cmp(self.data, dict.data***REMOVED***
        else:
            return cmp(self.data, dict***REMOVED***
    __hash__ = None # Avoid Py3k warning
    def __len__(self***REMOVED***: return len(self.data***REMOVED***
    def __getitem__(self, key***REMOVED***:
        if key in self.data:
            return self.data[key***REMOVED***
        if hasattr(self.__class__, "__missing__"***REMOVED***:
            return self.__class__.__missing__(self, key***REMOVED***
        raise KeyError(key***REMOVED***
    def __setitem__(self, key, item***REMOVED***: self.data[key***REMOVED*** = item
    def __delitem__(self, key***REMOVED***: del self.data[key***REMOVED***
    def clear(self***REMOVED***: self.data.clear(***REMOVED***
    def copy(self***REMOVED***:
        if self.__class__ is UserDict:
            return UserDict(self.data.copy(***REMOVED******REMOVED***
        import copy
        data = self.data
        try:
            self.data = {***REMOVED***
            c = copy.copy(self***REMOVED***
        finally:
            self.data = data
        c.update(self***REMOVED***
        return c
    def keys(self***REMOVED***: return self.data.keys(***REMOVED***
    def items(self***REMOVED***: return self.data.items(***REMOVED***
    def iteritems(self***REMOVED***: return self.data.iteritems(***REMOVED***
    def iterkeys(self***REMOVED***: return self.data.iterkeys(***REMOVED***
    def itervalues(self***REMOVED***: return self.data.itervalues(***REMOVED***
    def values(self***REMOVED***: return self.data.values(***REMOVED***
    def has_key(self, key***REMOVED***: return key in self.data
    def update(self, dict=None, **kwargs***REMOVED***:
        if dict is None:
            pass
        elif isinstance(dict, UserDict***REMOVED***:
            self.data.update(dict.data***REMOVED***
        elif isinstance(dict, type({***REMOVED******REMOVED******REMOVED*** or not hasattr(dict, 'items'***REMOVED***:
            self.data.update(dict***REMOVED***
        else:
            for k, v in dict.items(***REMOVED***:
                self[k***REMOVED*** = v
        if len(kwargs***REMOVED***:
            self.data.update(kwargs***REMOVED***
    def get(self, key, failobj=None***REMOVED***:
        if key not in self:
            return failobj
        return self[key***REMOVED***
    def setdefault(self, key, failobj=None***REMOVED***:
        if key not in self:
            self[key***REMOVED*** = failobj
        return self[key***REMOVED***
    def pop(self, key, *args***REMOVED***:
        return self.data.pop(key, *args***REMOVED***
    def popitem(self***REMOVED***:
        return self.data.popitem(***REMOVED***
    def __contains__(self, key***REMOVED***:
        return key in self.data
    @classmethod
    def fromkeys(cls, iterable, value=None***REMOVED***:
        d = cls(***REMOVED***
        for key in iterable:
            d[key***REMOVED*** = value
        return d

class IterableUserDict(UserDict***REMOVED***:
    def __iter__(self***REMOVED***:
        return iter(self.data***REMOVED***

import _abcoll
_abcoll.MutableMapping.register(IterableUserDict***REMOVED***


class DictMixin:
    # Mixin defining all dictionary methods for classes that already have
    # a minimum dictionary interface including getitem, setitem, delitem,
    # and keys. Without knowledge of the subclass constructor, the mixin
    # does not define __init__(***REMOVED*** or copy(***REMOVED***.  In addition to the four base
    # methods, progressively more efficiency comes with defining
    # __contains__(***REMOVED***, __iter__(***REMOVED***, and iteritems(***REMOVED***.

    # second level definitions support higher levels
    def __iter__(self***REMOVED***:
        for k in self.keys(***REMOVED***:
            yield k
    def has_key(self, key***REMOVED***:
        try:
            self[key***REMOVED***
        except KeyError:
            return False
        return True
    def __contains__(self, key***REMOVED***:
        return self.has_key(key***REMOVED***

    # third level takes advantage of second level definitions
    def iteritems(self***REMOVED***:
        for k in self:
            yield (k, self[k***REMOVED******REMOVED***
    def iterkeys(self***REMOVED***:
        return self.__iter__(***REMOVED***

    # fourth level uses definitions from lower levels
    def itervalues(self***REMOVED***:
        for _, v in self.iteritems(***REMOVED***:
            yield v
    def values(self***REMOVED***:
        return [v for _, v in self.iteritems(***REMOVED******REMOVED***
    def items(self***REMOVED***:
        return list(self.iteritems(***REMOVED******REMOVED***
    def clear(self***REMOVED***:
        for key in self.keys(***REMOVED***:
            del self[key***REMOVED***
    def setdefault(self, key, default=None***REMOVED***:
        try:
            return self[key***REMOVED***
        except KeyError:
            self[key***REMOVED*** = default
        return default
    def pop(self, key, *args***REMOVED***:
        if len(args***REMOVED*** > 1:
            raise TypeError, "pop expected at most 2 arguments, got "\
                              + repr(1 + len(args***REMOVED******REMOVED***
        try:
            value = self[key***REMOVED***
        except KeyError:
            if args:
                return args[0***REMOVED***
            raise
        del self[key***REMOVED***
        return value
    def popitem(self***REMOVED***:
        try:
            k, v = self.iteritems(***REMOVED***.next(***REMOVED***
        except StopIteration:
            raise KeyError, 'container is empty'
        del self[k***REMOVED***
        return (k, v***REMOVED***
    def update(self, other=None, **kwargs***REMOVED***:
        # Make progressively weaker assumptions about "other"
        if other is None:
            pass
        elif hasattr(other, 'iteritems'***REMOVED***:  # iteritems saves memory and lookups
            for k, v in other.iteritems(***REMOVED***:
                self[k***REMOVED*** = v
        elif hasattr(other, 'keys'***REMOVED***:
            for k in other.keys(***REMOVED***:
                self[k***REMOVED*** = other[k***REMOVED***
        else:
            for k, v in other:
                self[k***REMOVED*** = v
        if kwargs:
            self.update(kwargs***REMOVED***
    def get(self, key, default=None***REMOVED***:
        try:
            return self[key***REMOVED***
        except KeyError:
            return default
    def __repr__(self***REMOVED***:
        return repr(dict(self.iteritems(***REMOVED******REMOVED******REMOVED***
    def __cmp__(self, other***REMOVED***:
        if other is None:
            return 1
        if isinstance(other, DictMixin***REMOVED***:
            other = dict(other.iteritems(***REMOVED******REMOVED***
        return cmp(dict(self.iteritems(***REMOVED******REMOVED***, other***REMOVED***
    def __len__(self***REMOVED***:
        return len(self.keys(***REMOVED******REMOVED***
