***REMOVED***Cache lines from files.

This is intended to read lines from modules imported -- hence if a filename
is not found, it will look down the module search path for a file by
that name.
***REMOVED***

import sys
***REMOVED***

__all__ = ["getline", "clearcache", "checkcache"***REMOVED***

def getline(filename, lineno, module_globals=None***REMOVED***:
    lines = getlines(filename, module_globals***REMOVED***
    if 1 <= lineno <= len(lines***REMOVED***:
        return lines[lineno-1***REMOVED***
    else:
        return ''


# The cache

cache = {***REMOVED*** # The cache


def clearcache(***REMOVED***:
    ***REMOVED***Clear the cache entirely.***REMOVED***

    global cache
    cache = {***REMOVED***


def getlines(filename, module_globals=None***REMOVED***:
    ***REMOVED***Get the lines for a file from the cache.
    Update the cache if it doesn't contain an entry for this file already.***REMOVED***

    if filename in cache:
        return cache[filename***REMOVED***[2***REMOVED***
    else:
        return updatecache(filename, module_globals***REMOVED***


def checkcache(filename=None***REMOVED***:
    ***REMOVED***Discard cache entries that are out of date.
    (This is not checked upon each call!***REMOVED******REMOVED***

    if filename is None:
        filenames = cache.keys(***REMOVED***
    else:
        if filename in cache:
            filenames = [filename***REMOVED***
        else:
            return

    for filename in filenames:
        size, mtime, lines, fullname = cache[filename***REMOVED***
        if mtime is None:
            continue   # no-op for files loaded via a __loader__
        try:
            stat = os.stat(fullname***REMOVED***
        except os.error:
            del cache[filename***REMOVED***
            continue
        if size != stat.st_size or mtime != stat.st_mtime:
            del cache[filename***REMOVED***


def updatecache(filename, module_globals=None***REMOVED***:
    ***REMOVED***Update a cache entry and return its list of lines.
    If something's wrong, print a message, discard the cache entry,
    and return an empty list.***REMOVED***

    if filename in cache:
        del cache[filename***REMOVED***
    if not filename or (filename.startswith('<'***REMOVED*** and filename.endswith('>'***REMOVED******REMOVED***:
        return [***REMOVED***

    fullname = filename
    try:
        stat = os.stat(fullname***REMOVED***
    except OSError:
        basename = filename

        # Try for a __loader__, if available
        if module_globals and '__loader__' in module_globals:
            name = module_globals.get('__name__'***REMOVED***
            loader = module_globals['__loader__'***REMOVED***
            get_source = getattr(loader, 'get_source', None***REMOVED***

            if name and get_source:
                try:
                    data = get_source(name***REMOVED***
                except (ImportError, IOError***REMOVED***:
                    pass
                else:
                    if data is None:
                        # No luck, the PEP302 loader cannot find the source
                        # for this module.
                        return [***REMOVED***
                    cache[filename***REMOVED*** = (
                        len(data***REMOVED***, None,
                        [line+'\n' for line in data.splitlines(***REMOVED******REMOVED***, fullname
                    ***REMOVED***
                    return cache[filename***REMOVED***[2***REMOVED***

        # Try looking through the module search path, which is only useful
        # when handling a relative filename.
        if os.path.isabs(filename***REMOVED***:
            return [***REMOVED***

        # Take care to handle packages
        if basename == '__init__.py':
            # filename referes to a package
            basename = filename

        for dirname in sys.path:
            # When using imputil, sys.path may contain things other than
            # strings; ignore them when it happens.
            try:
                fullname = os.path.join(dirname, basename***REMOVED***
            except (TypeError, AttributeError***REMOVED***:
                # Not sufficiently string-like to do anything useful with.
                continue
            try:
                stat = os.stat(fullname***REMOVED***
                break
            except os.error:
                pass
        else:
            return [***REMOVED***
    try:
        with open(fullname, 'rU'***REMOVED*** as fp:
            lines = fp.readlines(***REMOVED***
    except IOError:
        return [***REMOVED***
    if lines and not lines[-1***REMOVED***.endswith('\n'***REMOVED***:
        lines[-1***REMOVED*** += '\n'
    size, mtime = stat.st_size, stat.st_mtime
    cache[filename***REMOVED*** = size, mtime, lines, fullname
    return lines
