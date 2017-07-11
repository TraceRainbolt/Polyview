***REMOVED***Common operations on Posix pathnames.

Instead of importing this module directly, ***REMOVED*** and refer to
this module as os.path.  The "os.path" name is an alias for this
module on Posix systems; on other systems (e.g. Mac, Windows***REMOVED***,
os.path provides the same operations in a manner specific to that
platform, and is an alias to another module (e.g. macpath, ntpath***REMOVED***.

Some of this can actually be useful on non-Posix systems too, e.g.
for manipulation of the pathname component of URLs.
***REMOVED***

***REMOVED***
import sys
import stat
import genericpath
import warnings
from genericpath import *

try:
    _unicode = unicode
except NameError:
    # If Python is built without Unicode support, the unicode type
    # will not exist. Fake one.
    class _unicode(object***REMOVED***:
        pass

__all__ = ["normcase","isabs","join","splitdrive","split","splitext",
           "basename","dirname","commonprefix","getsize","getmtime",
           "getatime","getctime","islink","exists","lexists","isdir","isfile",
           "ismount","walk","expanduser","expandvars","normpath","abspath",
           "samefile","sameopenfile","samestat",
           "curdir","pardir","sep","pathsep","defpath","altsep","extsep",
           "devnull","realpath","supports_unicode_filenames","relpath"***REMOVED***

# strings representing various path-related bits and pieces
curdir = '.'
pardir = '..'
extsep = '.'
sep = '/'
pathsep = ':'
defpath = ':/bin:/usr/bin'
altsep = None
devnull = '/dev/null'

# Normalize the case of a pathname.  Trivial in Posix, string.lower on Mac.
# On MS-DOS this may also turn slashes into backslashes; however, other
# normalizations (such as optimizing '../' away***REMOVED*** are not allowed
# (another function should be defined to do that***REMOVED***.

def normcase(s***REMOVED***:
    ***REMOVED***Normalize case of pathname.  Has no effect under Posix***REMOVED***
    return s


# Return whether a path is absolute.
# Trivial in Posix, harder on the Mac or MS-DOS.

def isabs(s***REMOVED***:
    ***REMOVED***Test whether a path is absolute***REMOVED***
    return s.startswith('/'***REMOVED***


# Join pathnames.
# Ignore the previous parts if a part is absolute.
# Insert a '/' unless the first part is empty or already ends in '/'.

def join(a, *p***REMOVED***:
    ***REMOVED***Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator.***REMOVED***
    path = a
    for b in p:
        if b.startswith('/'***REMOVED***:
            path = b
        elif path == '' or path.endswith('/'***REMOVED***:
            path +=  b
        else:
            path += '/' + b
    return path


# Split a path in head (everything up to the last '/'***REMOVED*** and tail (the
# rest***REMOVED***.  If the path ends in '/', tail will be empty.  If there is no
# '/' in the path, head  will be empty.
# Trailing '/'es are stripped from head unless it is the root.

def split(p***REMOVED***:
    ***REMOVED***Split a pathname.  Returns tuple "(head, tail***REMOVED***" where "tail" is
    everything after the final slash.  Either part may be empty.***REMOVED***
    i = p.rfind('/'***REMOVED*** + 1
    head, tail = p[:i***REMOVED***, p[i:***REMOVED***
    if head and head != '/'*len(head***REMOVED***:
        head = head.rstrip('/'***REMOVED***
    return head, tail


# Split a path in root and extension.
# The extension is everything starting at the last dot in the last
# pathname component; the root is everything before that.
# It is always true that root + ext == p.

def splitext(p***REMOVED***:
    return genericpath._splitext(p, sep, altsep, extsep***REMOVED***
splitext.__doc__ = genericpath._splitext.__doc__

# Split a pathname into a drive specification and the rest of the
# path.  Useful on DOS/Windows/NT; on Unix, the drive is always empty.

def splitdrive(p***REMOVED***:
    ***REMOVED***Split a pathname into drive and path. On Posix, drive is always
    empty.***REMOVED***
    return '', p


# Return the tail (basename***REMOVED*** part of a path, same as split(path***REMOVED***[1***REMOVED***.

def basename(p***REMOVED***:
    ***REMOVED***Returns the final component of a pathname***REMOVED***
    i = p.rfind('/'***REMOVED*** + 1
    return p[i:***REMOVED***


# Return the head (dirname***REMOVED*** part of a path, same as split(path***REMOVED***[0***REMOVED***.

def dirname(p***REMOVED***:
    ***REMOVED***Returns the directory component of a pathname***REMOVED***
    i = p.rfind('/'***REMOVED*** + 1
    head = p[:i***REMOVED***
    if head and head != '/'*len(head***REMOVED***:
        head = head.rstrip('/'***REMOVED***
    return head


# Is a path a symbolic link?
# This will always return false on systems where os.lstat doesn't exist.

def islink(path***REMOVED***:
    ***REMOVED***Test whether a path is a symbolic link***REMOVED***
    try:
        st = os.lstat(path***REMOVED***
    except (os.error, AttributeError***REMOVED***:
        return False
    return stat.S_ISLNK(st.st_mode***REMOVED***

# Being true for dangling symbolic links is also useful.

def lexists(path***REMOVED***:
    ***REMOVED***Test whether a path exists.  Returns True for broken symbolic links***REMOVED***
    try:
        os.lstat(path***REMOVED***
    except os.error:
        return False
    return True


# Are two filenames really pointing to the same file?

def samefile(f1, f2***REMOVED***:
    ***REMOVED***Test whether two pathnames reference the same actual file***REMOVED***
    s1 = os.stat(f1***REMOVED***
    s2 = os.stat(f2***REMOVED***
    return samestat(s1, s2***REMOVED***


# Are two open files really referencing the same file?
# (Not necessarily the same file descriptor!***REMOVED***

def sameopenfile(fp1, fp2***REMOVED***:
    ***REMOVED***Test whether two open file objects reference the same file***REMOVED***
    s1 = os.fstat(fp1***REMOVED***
    s2 = os.fstat(fp2***REMOVED***
    return samestat(s1, s2***REMOVED***


# Are two stat buffers (obtained from stat, fstat or lstat***REMOVED***
# describing the same file?

def samestat(s1, s2***REMOVED***:
    ***REMOVED***Test whether two stat buffers reference the same file***REMOVED***
    return s1.st_ino == s2.st_ino and \
           s1.st_dev == s2.st_dev


# Is a path a mount point?
# (Does this work for all UNIXes?  Is it even guaranteed to work by Posix?***REMOVED***

def ismount(path***REMOVED***:
    ***REMOVED***Test whether a path is a mount point***REMOVED***
    if islink(path***REMOVED***:
        # A symlink can never be a mount point
        return False
    try:
        s1 = os.lstat(path***REMOVED***
        s2 = os.lstat(join(path, '..'***REMOVED******REMOVED***
    except os.error:
        return False # It doesn't exist -- so not a mount point :-***REMOVED***
    dev1 = s1.st_dev
    dev2 = s2.st_dev
    if dev1 != dev2:
        return True     # path/.. on a different device as path
    ino1 = s1.st_ino
    ino2 = s2.st_ino
    if ino1 == ino2:
        return True     # path/.. is the same i-node as path
    return False


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
        try:
            st = os.lstat(name***REMOVED***
        except os.error:
            continue
        if stat.S_ISDIR(st.st_mode***REMOVED***:
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
    ***REMOVED***Expand ~ and ~user constructions.  If user or $HOME is unknown,
    do nothing.***REMOVED***
    if not path.startswith('~'***REMOVED***:
        return path
    i = path.find('/', 1***REMOVED***
    if i < 0:
        i = len(path***REMOVED***
    if i == 1:
        if 'HOME' not in os.environ:
            import pwd
            userhome = pwd.getpwuid(os.getuid(***REMOVED******REMOVED***.pw_dir
        else:
            userhome = os.environ['HOME'***REMOVED***
    else:
        import pwd
        try:
            pwent = pwd.getpwnam(path[1:i***REMOVED******REMOVED***
        except KeyError:
            return path
        userhome = pwent.pw_dir
    userhome = userhome.rstrip('/'***REMOVED***
    return (userhome + path[i:***REMOVED******REMOVED*** or '/'


# Expand paths containing shell variable substitutions.
# This expands the forms $variable and ${variable***REMOVED*** only.
# Non-existent variables are left unchanged.

_varprog = None
_uvarprog = None

def expandvars(path***REMOVED***:
    ***REMOVED***Expand shell variables of form $var and ${var***REMOVED***.  Unknown variables
    are left unchanged.***REMOVED***
    global _varprog, _uvarprog
    if '$' not in path:
        return path
    if isinstance(path, _unicode***REMOVED***:
        if not _varprog:
            import re
            _varprog = re.compile(r'\$(\w+|\{[^***REMOVED******REMOVED****\***REMOVED******REMOVED***'***REMOVED***
        varprog = _varprog
        encoding = sys.getfilesystemencoding(***REMOVED***
    else:
        if not _uvarprog:
            import re
            _uvarprog = re.compile(_unicode(r'\$(\w+|\{[^***REMOVED******REMOVED****\***REMOVED******REMOVED***'***REMOVED***, re.UNICODE***REMOVED***
        varprog = _uvarprog
        encoding = None
    i = 0
    while True:
        m = varprog.search(path, i***REMOVED***
        if not m:
            break
        i, j = m.span(0***REMOVED***
        name = m.group(1***REMOVED***
        if name.startswith('{'***REMOVED*** and name.endswith('***REMOVED***'***REMOVED***:
            name = name[1:-1***REMOVED***
        if encoding:
            name = name.encode(encoding***REMOVED***
        if name in os.environ:
            tail = path[j:***REMOVED***
            value = os.environ[name***REMOVED***
            if encoding:
                value = value.decode(encoding***REMOVED***
            path = path[:i***REMOVED*** + value
            i = len(path***REMOVED***
            path += tail
        else:
            i = j
    return path


# Normalize a path, e.g. A//B, A/./B and A/foo/../B all become A/B.
# It should be understood that this may change the meaning of the path
# if it contains symbolic links!

def normpath(path***REMOVED***:
    ***REMOVED***Normalize path, eliminating double slashes, etc.***REMOVED***
    # Preserve unicode (if path is unicode***REMOVED***
    slash, dot = (u'/', u'.'***REMOVED*** if isinstance(path, _unicode***REMOVED*** else ('/', '.'***REMOVED***
    if path == '':
        return dot
    initial_slashes = path.startswith('/'***REMOVED***
    # POSIX allows one or two initial slashes, but treats three or more
    # as single slash.
    if (initial_slashes and
        path.startswith('//'***REMOVED*** and not path.startswith('///'***REMOVED******REMOVED***:
        initial_slashes = 2
    comps = path.split('/'***REMOVED***
    new_comps = [***REMOVED***
    for comp in comps:
        if comp in ('', '.'***REMOVED***:
            continue
        if (comp != '..' or (not initial_slashes and not new_comps***REMOVED*** or
             (new_comps and new_comps[-1***REMOVED*** == '..'***REMOVED******REMOVED***:
            new_comps.append(comp***REMOVED***
        elif new_comps:
            new_comps.pop(***REMOVED***
    comps = new_comps
    path = slash.join(comps***REMOVED***
    if initial_slashes:
        path = slash*initial_slashes + path
    return path or dot


def abspath(path***REMOVED***:
    ***REMOVED***Return an absolute path.***REMOVED***
    if not isabs(path***REMOVED***:
        if isinstance(path, _unicode***REMOVED***:
            cwd = os.getcwdu(***REMOVED***
        else:
            cwd = os.getcwd(***REMOVED***
        path = join(cwd, path***REMOVED***
    return normpath(path***REMOVED***


# Return a canonical path (i.e. the absolute location of a file on the
# filesystem***REMOVED***.

def realpath(filename***REMOVED***:
    ***REMOVED***Return the canonical path of the specified filename, eliminating any
symbolic links encountered in the path.***REMOVED***
    path, ok = _joinrealpath('', filename, {***REMOVED******REMOVED***
    return abspath(path***REMOVED***

# Join two paths, normalizing ang eliminating any symbolic links
# encountered in the second path.
def _joinrealpath(path, rest, seen***REMOVED***:
    if isabs(rest***REMOVED***:
        rest = rest[1:***REMOVED***
        path = sep

    while rest:
        name, _, rest = rest.partition(sep***REMOVED***
        if not name or name == curdir:
            # current dir
            continue
        if name == pardir:
            # parent dir
            if path:
                path, name = split(path***REMOVED***
                if name == pardir:
                    path = join(path, pardir, pardir***REMOVED***
            else:
                path = pardir
            continue
        newpath = join(path, name***REMOVED***
        if not islink(newpath***REMOVED***:
            path = newpath
            continue
        # Resolve the symbolic link
        if newpath in seen:
            # Already seen this path
            path = seen[newpath***REMOVED***
            if path is not None:
                # use cached value
                continue
            # The symlink is not resolved, so we must have a symlink loop.
            # Return already resolved part + rest of the path unchanged.
            return join(newpath, rest***REMOVED***, False
        seen[newpath***REMOVED*** = None # not resolved symlink
        path, ok = _joinrealpath(path, os.readlink(newpath***REMOVED***, seen***REMOVED***
        if not ok:
            return join(path, rest***REMOVED***, False
        seen[newpath***REMOVED*** = path # resolved symlink

    return path, True


supports_unicode_filenames = (sys.platform == 'darwin'***REMOVED***

def relpath(path, start=curdir***REMOVED***:
    ***REMOVED***Return a relative version of a path***REMOVED***

    if not path:
        raise ValueError("no path specified"***REMOVED***

    start_list = [x for x in abspath(start***REMOVED***.split(sep***REMOVED*** if x***REMOVED***
    path_list = [x for x in abspath(path***REMOVED***.split(sep***REMOVED*** if x***REMOVED***

    # Work out how much of the filepath is shared by start and path.
    i = len(commonprefix([start_list, path_list***REMOVED******REMOVED******REMOVED***

    rel_list = [pardir***REMOVED*** * (len(start_list***REMOVED***-i***REMOVED*** + path_list[i:***REMOVED***
    if not rel_list:
        return curdir
    return join(*rel_list***REMOVED***
