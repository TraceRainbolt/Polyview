# Access WeakSet through the weakref module.
# This code is separated-out because it is needed
# by abc.py to load everything else at startup.

from _weakref import ref

__all__ = ['WeakSet'***REMOVED***


class _IterationGuard(object***REMOVED***:
    # This context manager registers itself in the current iterators of the
    # weak container, such as to delay all removals until the context manager
    # exits.
    # This technique should be relatively thread-safe (since sets are***REMOVED***.

    def __init__(self, weakcontainer***REMOVED***:
        # Don't create cycles
        self.weakcontainer = ref(weakcontainer***REMOVED***

    def __enter__(self***REMOVED***:
        w = self.weakcontainer(***REMOVED***
        if w is not None:
            w._iterating.add(self***REMOVED***
        return self

    def __exit__(self, e, t, b***REMOVED***:
        w = self.weakcontainer(***REMOVED***
        if w is not None:
            s = w._iterating
            s.remove(self***REMOVED***
            if not s:
                w._commit_removals(***REMOVED***


class WeakSet(object***REMOVED***:
    def __init__(self, data=None***REMOVED***:
        self.data = set(***REMOVED***
        def _remove(item, selfref=ref(self***REMOVED******REMOVED***:
            self = selfref(***REMOVED***
            if self is not None:
                if self._iterating:
                    self._pending_removals.append(item***REMOVED***
                else:
                    self.data.discard(item***REMOVED***
        self._remove = _remove
        # A list of keys to be removed
        self._pending_removals = [***REMOVED***
        self._iterating = set(***REMOVED***
        if data is not None:
            self.update(data***REMOVED***

    def _commit_removals(self***REMOVED***:
        l = self._pending_removals
        discard = self.data.discard
        while l:
            discard(l.pop(***REMOVED******REMOVED***

    def __iter__(self***REMOVED***:
        with _IterationGuard(self***REMOVED***:
            for itemref in self.data:
                item = itemref(***REMOVED***
                if item is not None:
                    # Caveat: the iterator will keep a strong reference to
                    # `item` until it is resumed or closed.
                    yield item

    def __len__(self***REMOVED***:
        return len(self.data***REMOVED*** - len(self._pending_removals***REMOVED***

    def __contains__(self, item***REMOVED***:
        try:
            wr = ref(item***REMOVED***
        except TypeError:
            return False
        return wr in self.data

    def __reduce__(self***REMOVED***:
        return (self.__class__, (list(self***REMOVED***,***REMOVED***,
                getattr(self, '__dict__', None***REMOVED******REMOVED***

    __hash__ = None

    def add(self, item***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        self.data.add(ref(item, self._remove***REMOVED******REMOVED***

    def clear(self***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        self.data.clear(***REMOVED***

    def copy(self***REMOVED***:
        return self.__class__(self***REMOVED***

    def pop(self***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        while True:
            try:
                itemref = self.data.pop(***REMOVED***
            except KeyError:
                raise KeyError('pop from empty WeakSet'***REMOVED***
            item = itemref(***REMOVED***
            if item is not None:
                return item

    def remove(self, item***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        self.data.remove(ref(item***REMOVED******REMOVED***

    def discard(self, item***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        self.data.discard(ref(item***REMOVED******REMOVED***

    def update(self, other***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        for element in other:
            self.add(element***REMOVED***

    def __ior__(self, other***REMOVED***:
        self.update(other***REMOVED***
        return self

    def difference(self, other***REMOVED***:
        newset = self.copy(***REMOVED***
        newset.difference_update(other***REMOVED***
        return newset
    __sub__ = difference

    def difference_update(self, other***REMOVED***:
        self.__isub__(other***REMOVED***
    def __isub__(self, other***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        if self is other:
            self.data.clear(***REMOVED***
        else:
            self.data.difference_update(ref(item***REMOVED*** for item in other***REMOVED***
        return self

    def intersection(self, other***REMOVED***:
        return self.__class__(item for item in other if item in self***REMOVED***
    __and__ = intersection

    def intersection_update(self, other***REMOVED***:
        self.__iand__(other***REMOVED***
    def __iand__(self, other***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        self.data.intersection_update(ref(item***REMOVED*** for item in other***REMOVED***
        return self

    def issubset(self, other***REMOVED***:
        return self.data.issubset(ref(item***REMOVED*** for item in other***REMOVED***
    __le__ = issubset

    def __lt__(self, other***REMOVED***:
        return self.data < set(ref(item***REMOVED*** for item in other***REMOVED***

    def issuperset(self, other***REMOVED***:
        return self.data.issuperset(ref(item***REMOVED*** for item in other***REMOVED***
    __ge__ = issuperset

    def __gt__(self, other***REMOVED***:
        return self.data > set(ref(item***REMOVED*** for item in other***REMOVED***

    def __eq__(self, other***REMOVED***:
        if not isinstance(other, self.__class__***REMOVED***:
            return NotImplemented
        return self.data == set(ref(item***REMOVED*** for item in other***REMOVED***

    def __ne__(self, other***REMOVED***:
        opposite = self.__eq__(other***REMOVED***
        if opposite is NotImplemented:
            return NotImplemented
        return not opposite

    def symmetric_difference(self, other***REMOVED***:
        newset = self.copy(***REMOVED***
        newset.symmetric_difference_update(other***REMOVED***
        return newset
    __xor__ = symmetric_difference

    def symmetric_difference_update(self, other***REMOVED***:
        self.__ixor__(other***REMOVED***
    def __ixor__(self, other***REMOVED***:
        if self._pending_removals:
            self._commit_removals(***REMOVED***
        if self is other:
            self.data.clear(***REMOVED***
        else:
            self.data.symmetric_difference_update(ref(item, self._remove***REMOVED*** for item in other***REMOVED***
        return self

    def union(self, other***REMOVED***:
        return self.__class__(e for s in (self, other***REMOVED*** for e in s***REMOVED***
    __or__ = union

    def isdisjoint(self, other***REMOVED***:
        return len(self.intersection(other***REMOVED******REMOVED*** == 0
