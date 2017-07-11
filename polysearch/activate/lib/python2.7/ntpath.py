# Module 'ntpath' -- common operations on WinNT/Win95 pathnames
***REMOVED***Common pathname manipulations, WindowsNT/95 version.

Instead of importing this module directly, ***REMOVED*** and refer to this
module as os.path.
***REMOVED***

***REMOVED***
import sys
import stat
import genericpath
import warnings

from genericpath import *

__all__ = ["normcase","isabs","join","splitdrive","split","splitext",
           "basename","dirname","commonprefix","getsize","getmtime",
           "getatime","getctime", "islink","exists","lexists","isdir","isfile",
           "ismount","walk","expanduser","expandvars","normpath","abspath",
           "splitunc","curdir","pardir","sep","pathsep","defpath","altsep",
           "extsep","devnull","realpath","supports_unicode_filenames","relpath"***REMOVED***

# strings representing various path-related bits and pieces
curdir = '.'
pardir = '..'
extsep = '.'
sep = '\\'
pathsep = ';'
altsep = '/'
defpath = '.;C:\\bin'
if 'ce' in sys.builtin_module_names:
    defpath = '\\Windows'
elif 'os2' in sys.builtin_module_names:
    # OS/2 w/ VACPP
    altsep = '/'
devnull = 'nul'

# Normalize the case of a pathname and map slashes to backslashes.
# Other normalizations (such as optimizing '../' away***REMOVED*** are not done
# (this is done by normpath***REMOVED***.

def normcase(s***REMOVED***:
    ***REMOVED***Normalize case of pathname.

    Makes all characters lowercase and all slashes into backslashes.***REMOVED***
    return s.replace("/", "\\"***REMOVED***.lower(***REMOVED***


# Return whether a path is absolute.
# Trivial in Posix, harder on the Mac or MS-DOS.
# For DOS it is absolute if it starts with a slash or backslash (current
# volume***REMOVED***, or if a pathname after the volume letter and colon / UNC resource
# starts with a slash or backslash.

def isabs(s***REMOVED***:
    ***REMOVED***Test whether a path is absolute***REMOVED***
    s = splitdrive(s***REMOVED***[1***REMOVED***
    return s != '' and s[:1***REMOVED*** in '/\\'


# Join two (or more***REMOVED*** paths.
def join(path, *paths***REMOVED***:
    ***REMOVED***Join two or more pathname components, inserting "\\" as needed.***REMOVED***
    result_drive, result_path = splitdrive(path***REMOVED***
    for p in paths:
        p_drive, p_path = splitdrive(p***REMOVED***
        if p_path and p_path[0***REMOVED*** in '\\/':
            # Second path is absolute
            if p_drive or not result_drive:
                result_drive = p_drive
            result_path = p_path
            continue
        elif p_drive and p_drive != result_drive:
            if p_drive.lower(***REMOVED*** != result_drive.lower(***REMOVED***:
                # Different drives => ignore the first path entirely
                result_drive = p_drive
                result_path = p_path
                continue
            # Same drive in different case
            result_drive = p_drive
        # Second path is relative to the first
        if result_path and result_path[-1***REMOVED*** not in '\\/':
            result_path = result_path + '\\'
        result_path = result_path + p_path
    return result_drive + result_path


# Split a path in a drive specification (a drive letter followed by a
# colon***REMOVED*** and the path specification.
# It is always true that drivespec + pathspec == p
def splitdrive(p***REMOVED***:
    ***REMOVED***Split a pathname into drive and path specifiers. Returns a 2-tuple
"(drive,path***REMOVED***";  either part may be empty***REMOVED***
    if p[1:2***REMOVED*** == ':':
        return p[0:2***REMOVED***, p[2:***REMOVED***
    return '', p


# Parse UNC paths
def splitunc(p***REMOVED***:
    ***REMOVED***Split a pathname into UNC mount point and relative path specifiers.

    Return a 2-tuple (unc, rest***REMOVED***; either part may be empty.
    If unc is not empty, it has the form '//host/mount' (or similar
    using backslashes***REMOVED***.  unc+rest is always the input path.
    Paths containing drive letters never have an UNC part.
    ***REMOVED***
    if p[1:2***REMOVED*** == ':':
        return '', p # Drive letter present
    firstTwo = p[0:2***REMOVED***
    if firstTwo == '//' or firstTwo == '\\\\':
        # is a UNC path:
        # vvvvvvvvvvvvvvvvvvvv equivalent to drive letter
        # \\machine\mountpoint\directories...
        #           directory ^^^^^^^^^^^^^^^
        normp = p.replace('\\', '/'***REMOVED***
        index = normp.find('/', 2***REMOVED***
        if index <= 2:
            return '', p
        index2 = normp.find('/', index + 1***REMOVED***
        # a UNC path can't have two slashes in a row
        # (after the initial two***REMOVED***
        if index2 == index + 1:
            return '', p
        if index2 == -1:
            index2 = len(p***REMOVED***
        return p[:index2***REMOVED***, p[index2:***REMOVED***
    return '', p


# Split a path in head (everything up to the last '/'***REMOVED*** and tail (the
# rest***REMOVED***.  After the trailing '/' is stripped, the invariant
# join(head, tail***REMOVED*** == p holds.
# The resulting head won't end in '/' unless it is the root.

def split(p***REMOVED***:
    ***REMOVED***Split a pathname.

    Return tuple (head, tail***REMOVED*** where tail is everything after the final slash.
    Either part may be empty.***REMOVED***

    d, p = splitdrive(p***REMOVED***
    # set i to index beyond p's last slash
    i = len(p***REMOVED***
    while i and p[i-1***REMOVED*** not in '/\\':
        i = i - 1
    head, tail = p[:i***REMOVED***, p[i:***REMOVED***  # now tail has no slashes
    # remove trailing slashes from head, unless it's all slashes
    head2 = head
    while head2 and head2[-1***REMOVED*** in '/\\':
        head2 = head2[:-1***REMOVED***
    head = head2 or head
    return d + head, tail


# Split a path in root and extension.
# The extension is everything starting at the last dot in the last
# pathname component; the root is everything before that.
# It is always true that root + ext == p.

def splitext(p***REMOVED***:
    return genericpath._splitext(p, sep, altsep, extsep***REMOVED***
splitext.__doc__ = genericpath._splitext.__doc__


# Return the tail (basename***REMOVED*** part of a path.

def basename(p***REMOVED***:
    ***REMOVED***Returns the final component of a pathname***REMOVED***
    return split(p***REMOVED***[1***REMOVED***


# Return the head (dirname***REMOVED*** part of a path.

def dirname(p***REMOVED***:
    ***REMOVED***Returns the directory component of a pathname***REMOVED***
    return split(p***REMOVED***[0***REMOVED***

# Is a path a symbolic link?
# This will always return false on systems where posix.lstat doesn't exist.

def islink(path***REMOVED***:
    ***REMOVED***Test for symbolic link.
    On WindowsNT/95 and OS/2 always returns false
    ***REMOVED***
    return False

# alias exists to lexists
lexists = exists

# Is a path a mount point?  Either a root (with or without drive letter***REMOVED***
# or an UNC path with at most a / or \ after the mount point.

def ismount(path***REMOVED***:
    ***REMOVED***Test whether a path is a mount point (defined as root of drive***REMOVED******REMOVED***
    unc, rest = splitunc(path***REMOVED***
    if unc:
        return rest in ("", "/", "\\"***REMOVED***
    p = splitdrive(path***REMOVED***[1***REMOVED***
    return len(p***REMOVED*** == 1 and p[0***REMOVED*** in '/\\'


# Directory tree walk.
# For each directory under top (including top itself, but excluding
# '.' and '..'***REMOVED***, func(arg, dirname, filenames***REMOVED*** is called, where
# dirname is the name of the directory and filenames is the list
# of files (and subdirectories etc.***REMOVED*** in the directory.
# The func may modify the filenames list, to implement a filter,
# or to impose a different order of visiting.

def walk(top, func, arg***REMOVED***:
    ***REMOVED***Directory tree walk with callback function.

    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'***REMOVED***, call func(arg, dirname, fnames***REMOVED***.
    dirname is the name of the directory, and fnames a list of the names of
    the files and subdirectories in dirname (excluding '.' and '..'***REMOVED***.  func
    may modify the fnames list in-place (e.g. via del or slice assignment***REMOVED***,
    and walk will only recurse into the subdirectories whose names remain in
    fnames; this can be used to implement a filter, or to impose a specific
    order of visiting.  No semantics are defined for, or required of, arg,
    beyond that arg is always passed to func.  It can be used, e.g., to pass
    a filename pattern, or a mutable object designed to accumulate
    statistics.  Passing None for arg is common.***REMOVED***
    warnings.warnpy3k("In 3.x, os.path.walk is removed in favor of os.walk.",
                      stacklevel=2***REMOVED***
    try:
        names = os.listdir(top***REMOVED***
    except os.error:
        return
    func(arg, top, names***REMOVED***
    for name in names:
        name = join(top, name***REMOVED***
        if isdir(name***REMOVED***:
            walk(name, func, arg***REMOVED***


# Expand paths beginning with '~' or '~user'.
# '~' means $HOME; '~user' means that user's home directory.
# If the path doesn't begin with '~', or if the user or $HOME is unknown,
# the path is returned unchanged (leaving error reporting to whatever
# function is called with the expanded path as argument***REMOVED***.
# See also module 'glob' for expansion of *, ? and [...***REMOVED*** in pathnames.
# (A function should also be defined to do full *sh-style environment
# variable expansion.***REMOVED***

def expanduser(path***REMOVED***:
    ***REMOVED***Expand ~ and ~user constructs.

    If user or $HOME is unknown, do nothing.***REMOVED***
    if path[:1***REMOVED*** != '~':
        return path
    i, n = 1, len(path***REMOVED***
    while i < n and path[i***REMOVED*** not in '/\\':
        i = i + 1

    if 'HOME' in os.environ:
        userhome = os.environ['HOME'***REMOVED***
    elif 'USERPROFILE' in os.environ:
        userhome = os.environ['USERPROFILE'***REMOVED***
    elif not 'HOMEPATH' in os.environ:
        return path
    else:
        try:
            drive = os.environ['HOMEDRIVE'***REMOVED***
        except KeyError:
            drive = ''
        userhome = join(drive, os.environ['HOMEPATH'***REMOVED******REMOVED***

    if i != 1: #~user
        userhome = join(dirname(userhome***REMOVED***, path[1:i***REMOVED******REMOVED***

    return userhome + path[i:***REMOVED***


# Expand paths containing shell variable substitutions.
# The following rules apply:
#       - no expansion within single quotes
#       - '$$' is translated into '$'
#       - '%%' is translated into '%' if '%%' are not seen in %var1%%var2%
#       - ${varname***REMOVED*** is accepted.
#       - $varname is accepted.
#       - %varname% is accepted.
#       - varnames can be made out of letters, digits and the characters '_-'
#         (though is not verified in the ${varname***REMOVED*** and %varname% cases***REMOVED***
# XXX With COMMAND.COM you can use any characters in a variable name,
# XXX except '^|<>='.

def expandvars(path***REMOVED***:
    ***REMOVED***Expand shell variables of the forms $var, ${var***REMOVED*** and %var%.

    Unknown variables are left unchanged.***REMOVED***
    if '$' not in path and '%' not in path:
        return path
    import string
    varchars = string.ascii_letters + string.digits + '_-'
    if isinstance(path, unicode***REMOVED***:
        encoding = sys.getfilesystemencoding(***REMOVED***
        def getenv(var***REMOVED***:
            return os.environ[var.encode(encoding***REMOVED******REMOVED***.decode(encoding***REMOVED***
    else:
        def getenv(var***REMOVED***:
            return os.environ[var***REMOVED***
    res = ''
    index = 0
    pathlen = len(path***REMOVED***
    while index < pathlen:
        c = path[index***REMOVED***
        if c == '\'':   # no expansion within single quotes
            path = path[index + 1:***REMOVED***
            pathlen = len(path***REMOVED***
            try:
                index = path.index('\''***REMOVED***
                res = res + '\'' + path[:index + 1***REMOVED***
            except ValueError:
                res = res + path
                index = pathlen - 1
        elif c == '%':  # variable or '%'
            if path[index + 1:index + 2***REMOVED*** == '%':
                res = res + c
                index = index + 1
            else:
                path = path[index+1:***REMOVED***
                pathlen = len(path***REMOVED***
                try:
                    index = path.index('%'***REMOVED***
                except ValueError:
                    res = res + '%' + path
                    index = pathlen - 1
                else:
                    var = path[:index***REMOVED***
                    try:
                        res = res + getenv(var***REMOVED***
                    except KeyError:
                        res = res + '%' + var + '%'
        elif c == '$':  # variable or '$$'
            if path[index + 1:index + 2***REMOVED*** == '$':
                res = res + c
                index = index + 1
            elif path[index + 1:index + 2***REMOVED*** == '{':
                path = path[index+2:***REMOVED***
                pathlen = len(path***REMOVED***
                try:
                    index = path.index('***REMOVED***'***REMOVED***
                    var = path[:index***REMOVED***
                    try:
                        res = res + getenv(var***REMOVED***
                    except KeyError:
                        res = res + '${' + var + '***REMOVED***'
                except ValueError:
                    res = res + '${' + path
                    index = pathlen - 1
            else:
                var = ''
                index = index + 1
                c = path[index:index + 1***REMOVED***
                while c != '' and c in varchars:
                    var = var + c
                    index = index + 1
                    c = path[index:index + 1***REMOVED***
                try:
                    res = res + getenv(var***REMOVED***
                except KeyError:
                    res = res + '$' + var
                if c != '':
                    index = index - 1
        else:
            res = res + c
        index = index + 1
    return res


# Normalize a path, e.g. A//B, A/./B and A/foo/../B all become A\B.
# Previously, this function also truncated pathnames to 8+3 format,
# but as this module is called "ntpath", that's obviously wrong!

def normpath(path***REMOVED***:
    ***REMOVED***Normalize path, eliminating double slashes, etc.***REMOVED***
    # Preserve unicode (if path is unicode***REMOVED***
    backslash, dot = (u'\\', u'.'***REMOVED*** if isinstance(path, unicode***REMOVED*** else ('\\', '.'***REMOVED***
    if path.startswith(('\\\\.\\', '\\\\?\\'***REMOVED******REMOVED***:
        # in the case of paths with these prefixes:
        # \\.\ -> device names
        # \\?\ -> literal paths
        # do not do any normalization, but return the path unchanged
        return path
    path = path.replace("/", "\\"***REMOVED***
    prefix, path = splitdrive(path***REMOVED***
    # We need to be careful here. If the prefix is empty, and the path starts
    # with a backslash, it could either be an absolute path on the current
    # drive (\dir1\dir2\file***REMOVED*** or a UNC filename (\\server\mount\dir1\file***REMOVED***. It
    # is therefore imperative NOT to collapse multiple backslashes blindly in
    # that case.
    # The code below preserves multiple backslashes when there is no drive
    # letter. This means that the invalid filename \\\a\b is preserved
    # unchanged, where a\\\b is normalised to a\b. It's not clear that there
    # is any better behaviour for such edge cases.
    if prefix == '':
        # No drive letter - preserve initial backslashes
        while path[:1***REMOVED*** == "\\":
            prefix = prefix + backslash
            path = path[1:***REMOVED***
    else:
        # We have a drive letter - collapse initial backslashes
        if path.startswith("\\"***REMOVED***:
            prefix = prefix + backslash
            path = path.lstrip("\\"***REMOVED***
    comps = path.split("\\"***REMOVED***
    i = 0
    while i < len(comps***REMOVED***:
        if comps[i***REMOVED*** in ('.', ''***REMOVED***:
            del comps[i***REMOVED***
        elif comps[i***REMOVED*** == '..':
            if i > 0 and comps[i-1***REMOVED*** != '..':
                del comps[i-1:i+1***REMOVED***
                i -= 1
            elif i == 0 and prefix.endswith("\\"***REMOVED***:
                del comps[i***REMOVED***
            else:
                i += 1
        else:
            i += 1
    # If the path is now empty, substitute '.'
    if not prefix and not comps:
        comps.append(dot***REMOVED***
    return prefix + backslash.join(comps***REMOVED***


# Return an absolute path.
try:
    from nt import _getfullpathname

except ImportError: # not running on Windows - mock up something sensible
    def abspath(path***REMOVED***:
        ***REMOVED***Return the absolute version of a path.***REMOVED***
        if not isabs(path***REMOVED***:
            if isinstance(path, unicode***REMOVED***:
                cwd = os.getcwdu(***REMOVED***
            else:
                cwd = os.getcwd(***REMOVED***
            path = join(cwd, path***REMOVED***
        return normpath(path***REMOVED***

else:  # use native Windows method on Windows
    def abspath(path***REMOVED***:
        ***REMOVED***Return the absolute version of a path.***REMOVED***

        if path: # Empty path must return current working directory.
            try:
                path = _getfullpathname(path***REMOVED***
            except WindowsError:
                pass # Bad path - return unchanged.
        elif isinstance(path, unicode***REMOVED***:
            path = os.getcwdu(***REMOVED***
        else:
            path = os.getcwd(***REMOVED***
        return normpath(path***REMOVED***

# realpath is a no-op on systems without islink support
realpath = abspath
# Win9x family and earlier have no Unicode filename support.
supports_unicode_filenames = (hasattr(sys, "getwindowsversion"***REMOVED*** and
                              sys.getwindowsversion(***REMOVED***[3***REMOVED*** >= 2***REMOVED***

def _abspath_split(path***REMOVED***:
    abs = abspath(normpath(path***REMOVED******REMOVED***
    prefix, rest = splitunc(abs***REMOVED***
    is_unc = bool(prefix***REMOVED***
    if not is_unc:
        prefix, rest = splitdrive(abs***REMOVED***
    return is_unc, prefix, [x for x in rest.split(sep***REMOVED*** if x***REMOVED***

def relpath(path, start=curdir***REMOVED***:
    ***REMOVED***Return a relative version of a path***REMOVED***

    if not path:
        raise ValueError("no path specified"***REMOVED***

    start_is_unc, start_prefix, start_list = _abspath_split(start***REMOVED***
    path_is_unc, path_prefix, path_list = _abspath_split(path***REMOVED***

    if path_is_unc ^ start_is_unc:
        raise ValueError("Cannot mix UNC and non-UNC paths (%s and %s***REMOVED***"
                                                            % (path, start***REMOVED******REMOVED***
    if path_prefix.lower(***REMOVED*** != start_prefix.lower(***REMOVED***:
        if path_is_unc:
            raise ValueError("path is on UNC root %s, start on UNC root %s"
                                                % (path_prefix, start_prefix***REMOVED******REMOVED***
        else:
            raise ValueError("path is on drive %s, start on drive %s"
                                                % (path_prefix, start_prefix***REMOVED******REMOVED***
    # Work out how much of the filepath is shared by start and path.
    i = 0
    for e1, e2 in zip(start_list, path_list***REMOVED***:
        if e1.lower(***REMOVED*** != e2.lower(***REMOVED***:
            break
        i += 1

    rel_list = [pardir***REMOVED*** * (len(start_list***REMOVED***-i***REMOVED*** + path_list[i:***REMOVED***
    if not rel_list:
        return curdir
    return join(*rel_list***REMOVED***

try:
    # The genericpath.isdir implementation uses os.stat and checks the mode
    # attribute to tell whether or not the path is a directory.
    # This is overkill on Windows - just pass the path to GetFileAttributes
    # and check the attribute from there.
    from nt import _isdir as isdir
except ImportError:
    # Use genericpath.isdir as imported above.
    pass
