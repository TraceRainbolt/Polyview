***REMOVED***
Path operations common to more than one OS
Do not use directly.  The OS specific modules import the appropriate
functions from this module themselves.
***REMOVED***
***REMOVED***
import stat

__all__ = ['commonprefix', 'exists', 'getatime', 'getctime', 'getmtime',
           'getsize', 'isdir', 'isfile'***REMOVED***


# Does a path exist?
# This is false for dangling symbolic links on systems that support them.
def exists(path***REMOVED***:
    ***REMOVED***Test whether a path exists.  Returns False for broken symbolic links***REMOVED***
    try:
        os.stat(path***REMOVED***
    except os.error:
        return False
    return True


# This follows symbolic links, so both islink(***REMOVED*** and isdir(***REMOVED*** can be true
# for the same path on systems that support symlinks
def isfile(path***REMOVED***:
    ***REMOVED***Test whether a path is a regular file***REMOVED***
    try:
        st = os.stat(path***REMOVED***
    except os.error:
        return False
    return stat.S_ISREG(st.st_mode***REMOVED***


# Is a path a directory?
# This follows symbolic links, so both islink(***REMOVED*** and isdir(***REMOVED***
# can be true for the same path on systems that support symlinks
def isdir(s***REMOVED***:
    ***REMOVED***Return true if the pathname refers to an existing directory.***REMOVED***
    try:
        st = os.stat(s***REMOVED***
    except os.error:
        return False
    return stat.S_ISDIR(st.st_mode***REMOVED***


def getsize(filename***REMOVED***:
    ***REMOVED***Return the size of a file, reported by os.stat(***REMOVED***.***REMOVED***
    return os.stat(filename***REMOVED***.st_size


def getmtime(filename***REMOVED***:
    ***REMOVED***Return the last modification time of a file, reported by os.stat(***REMOVED***.***REMOVED***
    return os.stat(filename***REMOVED***.st_mtime


def getatime(filename***REMOVED***:
    ***REMOVED***Return the last access time of a file, reported by os.stat(***REMOVED***.***REMOVED***
    return os.stat(filename***REMOVED***.st_atime


def getctime(filename***REMOVED***:
    ***REMOVED***Return the metadata change time of a file, reported by os.stat(***REMOVED***.***REMOVED***
    return os.stat(filename***REMOVED***.st_ctime


# Return the longest prefix of all list elements.
def commonprefix(m***REMOVED***:
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    s1 = min(m***REMOVED***
    s2 = max(m***REMOVED***
    for i, c in enumerate(s1***REMOVED***:
        if c != s2[i***REMOVED***:
            return s1[:i***REMOVED***
    return s1

# Split a path in root and extension.
# The extension is everything starting at the last dot in the last
# pathname component; the root is everything before that.
# It is always true that root + ext == p.

# Generic implementation of splitext, to be parametrized with
# the separators
def _splitext(p, sep, altsep, extsep***REMOVED***:
    ***REMOVED***Split the extension from a pathname.

    Extension is everything from the last dot to the end, ignoring
    leading dots.  Returns "(root, ext***REMOVED***"; ext may be empty.***REMOVED***

    sepIndex = p.rfind(sep***REMOVED***
    if altsep:
        altsepIndex = p.rfind(altsep***REMOVED***
        sepIndex = max(sepIndex, altsepIndex***REMOVED***

    dotIndex = p.rfind(extsep***REMOVED***
    if dotIndex > sepIndex:
        # skip all leading dots
        filenameIndex = sepIndex + 1
        while filenameIndex < dotIndex:
            if p[filenameIndex***REMOVED*** != extsep:
                return p[:dotIndex***REMOVED***, p[dotIndex:***REMOVED***
            filenameIndex += 1

    return p, ''
