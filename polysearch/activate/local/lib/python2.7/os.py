r***REMOVED***OS routines for Mac, NT, or Posix depending on what system we're on.

This exports:
  - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
  - os.path is one of the modules posixpath, or ntpath
  - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
  - os.curdir is a string representing the current directory ('.' or ':'***REMOVED***
  - os.pardir is a string representing the parent directory ('..' or '::'***REMOVED***
  - os.sep is the (or a most common***REMOVED*** pathname separator ('/' or ':' or '\\'***REMOVED***
  - os.extsep is the extension separator ('.' or '/'***REMOVED***
  - os.altsep is the alternate pathname separator (None or '/'***REMOVED***
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n'***REMOVED***
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.***REMOVED***

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir***REMOVED***, and leave all pathname manipulation to os.path
(e.g., split and join***REMOVED***.
***REMOVED***

#'

import sys, errno

_names = sys.builtin_module_names

# Note:  more names are added to __all__ later.
__all__ = ["altsep", "curdir", "pardir", "sep", "extsep", "pathsep", "linesep",
           "defpath", "name", "path", "devnull",
           "SEEK_SET", "SEEK_CUR", "SEEK_END"***REMOVED***

def _get_exports_list(module***REMOVED***:
    try:
        return list(module.__all__***REMOVED***
    except AttributeError:
        return [n for n in dir(module***REMOVED*** if n[0***REMOVED*** != '_'***REMOVED***

if 'posix' in _names:
    name = 'posix'
    linesep = '\n'
    from posix import *
    try:
        from posix import _exit
    except ImportError:
        pass
    import posixpath as path

    import posix
    __all__.extend(_get_exports_list(posix***REMOVED******REMOVED***
    del posix

elif 'nt' in _names:
    name = 'nt'
    linesep = '\r\n'
    from nt import *
    try:
        from nt import _exit
    except ImportError:
        pass
    import ntpath as path

    import nt
    __all__.extend(_get_exports_list(nt***REMOVED******REMOVED***
    del nt

elif 'os2' in _names:
    name = 'os2'
    linesep = '\r\n'
    from os2 import *
    try:
        from os2 import _exit
    except ImportError:
        pass
    if sys.version.find('EMX GCC'***REMOVED*** == -1:
        import ntpath as path
    else:
        ***REMOVED***2emxpath as path
        from _emx_link import link

    ***REMOVED***2
    __all__.extend(_get_exports_list(os2***REMOVED******REMOVED***
    del os2

elif 'ce' in _names:
    name = 'ce'
    linesep = '\r\n'
    from ce import *
    try:
        from ce import _exit
    except ImportError:
        pass
    # We can use the standard Windows path.
    import ntpath as path

    import ce
    __all__.extend(_get_exports_list(ce***REMOVED******REMOVED***
    del ce

elif 'riscos' in _names:
    name = 'riscos'
    linesep = '\n'
    from riscos import *
    try:
        from riscos import _exit
    except ImportError:
        pass
    import riscospath as path

    import riscos
    __all__.extend(_get_exports_list(riscos***REMOVED******REMOVED***
    del riscos

else:
    raise ImportError, 'no os specific module found'

sys.modules['os.path'***REMOVED*** = path
from os.path import (curdir, pardir, sep, pathsep, defpath, extsep, altsep,
    devnull***REMOVED***

del _names

# Python uses fixed values for the SEEK_ constants; they are mapped
# to native constants if necessary in posixmodule.c
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

#'

# Super directory utilities.
# (Inspired by Eric Raymond; the doc strings are mostly his***REMOVED***

def makedirs(name, mode=0777***REMOVED***:
    ***REMOVED***makedirs(path [, mode=0777***REMOVED******REMOVED***

    Super-mkdir; create a leaf directory and all intermediate ones.
    Works like mkdir, except that any intermediate path segment (not
    just the rightmost***REMOVED*** will be created if it does not exist.  This is
    recursive.

    ***REMOVED***
    head, tail = path.split(name***REMOVED***
    if not tail:
        head, tail = path.split(head***REMOVED***
    if head and tail and not path.exists(head***REMOVED***:
        try:
            makedirs(head, mode***REMOVED***
        except OSError, e:
            # be happy if someone already created the path
            if e.errno != errno.EEXIST:
                raise
        if tail == curdir:           # xxx/newdir/. exists if xxx/newdir exists
            return
    mkdir(name, mode***REMOVED***

def removedirs(name***REMOVED***:
    ***REMOVED***removedirs(path***REMOVED***

    Super-rmdir; remove a leaf directory and all empty intermediate
    ones.  Works like rmdir except that, if the leaf directory is
    successfully removed, directories corresponding to rightmost path
    segments will be pruned away until either the whole path is
    consumed or an error occurs.  Errors during this latter phase are
    ignored -- they generally mean that a directory was not empty.

    ***REMOVED***
    rmdir(name***REMOVED***
    head, tail = path.split(name***REMOVED***
    if not tail:
        head, tail = path.split(head***REMOVED***
    while head and tail:
        try:
            rmdir(head***REMOVED***
        except error:
            break
        head, tail = path.split(head***REMOVED***

def renames(old, new***REMOVED***:
    ***REMOVED***renames(old, new***REMOVED***

    Super-rename; create directories as necessary and delete any left
    empty.  Works like rename, except creation of any intermediate
    directories needed to make the new pathname good is attempted
    first.  After the rename, directories corresponding to rightmost
    path segments of the old name will be pruned way until either the
    whole path is consumed or a nonempty directory is found.

    Note: this function can fail with the new directory structure made
    if you lack permissions needed to unlink the leaf directory or
    file.

    ***REMOVED***
    head, tail = path.split(new***REMOVED***
    if head and tail and not path.exists(head***REMOVED***:
        makedirs(head***REMOVED***
    rename(old, new***REMOVED***
    head, tail = path.split(old***REMOVED***
    if head and tail:
        try:
            removedirs(head***REMOVED***
        except error:
            pass

__all__.extend(["makedirs", "removedirs", "renames"***REMOVED******REMOVED***

def walk(top, topdown=True, onerror=None, followlinks=False***REMOVED***:
    ***REMOVED***Directory tree generator.

    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'***REMOVED***, yields a 3-tuple

        dirpath, dirnames, filenames

    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (excluding '.' and '..'***REMOVED***.
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top***REMOVED*** to a file or directory in
    dirpath, do os.path.join(dirpath, name***REMOVED***.

    If optional arg 'topdown' is true or not specified, the triple for a
    directory is generated before the triples for any of its subdirectories
    (directories are generated top down***REMOVED***.  If topdown is false, the triple
    for a directory is generated after the triples for all of its
    subdirectories (directories are generated bottom up***REMOVED***.

    When topdown is true, the caller can modify the dirnames list in-place
    (e.g., via del or slice assignment***REMOVED***, and walk will only recurse into the
    subdirectories whose names remain in dirnames; this can be used to prune
    the search, or to impose a specific order of visiting.  Modifying
    dirnames when topdown is false is ineffective, since the directories in
    dirnames have already been generated by the time dirnames itself is
    generated.

    By default errors from the os.listdir(***REMOVED*** call are ignored.  If
    optional arg 'onerror' is specified, it should be a function; it
    will be called with one argument, an os.error instance.  It can
    report the error to continue with the walk, or raise the exception
    to abort the walk.  Note that the filename is available as the
    filename attribute of the exception object.

    By default, os.walk does not follow symbolic links to subdirectories on
    systems that support them.  In order to get this functionality, set the
    optional argument 'followlinks' to true.

    Caution:  if you pass a relative pathname for top, don't change the
    current working directory between resumptions of walk.  walk never
    changes the current directory, and assumes that the client doesn't
    either.

    Example:

    ***REMOVED***
    from os.path import join, getsize
    for root, dirs, files in os.walk('python/Lib/email'***REMOVED***:
        print root, "consumes",
        print sum([getsize(join(root, name***REMOVED******REMOVED*** for name in files***REMOVED******REMOVED***,
        print "bytes in", len(files***REMOVED***, "non-directory files"
        if 'CVS' in dirs:
            dirs.remove('CVS'***REMOVED***  # don't visit CVS directories
    ***REMOVED***

    islink, join, isdir = path.islink, path.join, path.isdir

    # We may not have read permission for top, in which case we can't
    # get a list of the files the directory contains.  os.path.walk
    # always suppressed the exception then, rather than blow up for a
    # minor reason when (say***REMOVED*** a thousand readable directories are still
    # left to visit.  That logic is copied here.
    try:
        # Note that listdir and error are globals in this module due
        # to earlier import-*.
        names = listdir(top***REMOVED***
    except error, err:
        if onerror is not None:
            onerror(err***REMOVED***
        return

    dirs, nondirs = [***REMOVED***, [***REMOVED***
    for name in names:
        if isdir(join(top, name***REMOVED******REMOVED***:
            dirs.append(name***REMOVED***
        else:
            nondirs.append(name***REMOVED***

    if topdown:
        yield top, dirs, nondirs
    for name in dirs:
        new_path = join(top, name***REMOVED***
        if followlinks or not islink(new_path***REMOVED***:
            for x in walk(new_path, topdown, onerror, followlinks***REMOVED***:
                yield x
    if not topdown:
        yield top, dirs, nondirs

__all__.append("walk"***REMOVED***

# Make sure os.environ exists, at least
try:
    environ
except NameError:
    environ = {***REMOVED***

def execl(file, *args***REMOVED***:
    ***REMOVED***execl(file, *args***REMOVED***

    Execute the executable file with argument list args, replacing the
    current process. ***REMOVED***
    execv(file, args***REMOVED***

def execle(file, *args***REMOVED***:
    ***REMOVED***execle(file, *args, env***REMOVED***

    Execute the executable file with argument list args and
    environment env, replacing the current process. ***REMOVED***
    env = args[-1***REMOVED***
    execve(file, args[:-1***REMOVED***, env***REMOVED***

def execlp(file, *args***REMOVED***:
    ***REMOVED***execlp(file, *args***REMOVED***

    Execute the executable file (which is searched for along $PATH***REMOVED***
    with argument list args, replacing the current process. ***REMOVED***
    execvp(file, args***REMOVED***

def execlpe(file, *args***REMOVED***:
    ***REMOVED***execlpe(file, *args, env***REMOVED***

    Execute the executable file (which is searched for along $PATH***REMOVED***
    with argument list args and environment env, replacing the current
    process. ***REMOVED***
    env = args[-1***REMOVED***
    execvpe(file, args[:-1***REMOVED***, env***REMOVED***

def execvp(file, args***REMOVED***:
    ***REMOVED***execvp(file, args***REMOVED***

    Execute the executable file (which is searched for along $PATH***REMOVED***
    with argument list args, replacing the current process.
    args may be a list or tuple of strings. ***REMOVED***
    _execvpe(file, args***REMOVED***

def execvpe(file, args, env***REMOVED***:
    ***REMOVED***execvpe(file, args, env***REMOVED***

    Execute the executable file (which is searched for along $PATH***REMOVED***
    with argument list args and environment env , replacing the
    current process.
    args may be a list or tuple of strings. ***REMOVED***
    _execvpe(file, args, env***REMOVED***

__all__.extend(["execl","execle","execlp","execlpe","execvp","execvpe"***REMOVED******REMOVED***

def _execvpe(file, args, env=None***REMOVED***:
    if env is not None:
        func = execve
        argrest = (args, env***REMOVED***
    else:
        func = execv
        argrest = (args,***REMOVED***
        env = environ

    head, tail = path.split(file***REMOVED***
    if head:
        func(file, *argrest***REMOVED***
        return
    if 'PATH' in env:
        envpath = env['PATH'***REMOVED***
    else:
        envpath = defpath
    PATH = envpath.split(pathsep***REMOVED***
    saved_exc = None
    saved_tb = None
    for dir in PATH:
        fullname = path.join(dir, file***REMOVED***
        try:
            func(fullname, *argrest***REMOVED***
        except error, e:
            tb = sys.exc_info(***REMOVED***[2***REMOVED***
            if (e.errno != errno.ENOENT and e.errno != errno.ENOTDIR
                and saved_exc is None***REMOVED***:
                saved_exc = e
                saved_tb = tb
    if saved_exc:
        raise error, saved_exc, saved_tb
    raise error, e, tb

# Change environ to automatically call putenv(***REMOVED*** if it exists
try:
    # This will fail if there's no putenv
    putenv
except NameError:
    pass
else:
    import UserDict

    # Fake unsetenv(***REMOVED*** for Windows
    # not sure about os2 here but
    # I'm guessing they are the same.

    if name in ('os2', 'nt'***REMOVED***:
        def unsetenv(key***REMOVED***:
            putenv(key, ""***REMOVED***

    if name == "riscos":
        # On RISC OS, all env access goes through getenv and putenv
        from riscosenviron import _Environ
    elif name in ('os2', 'nt'***REMOVED***:  # Where Env Var Names Must Be UPPERCASE
        # But we store them as upper case
        class _Environ(UserDict.IterableUserDict***REMOVED***:
            def __init__(self, environ***REMOVED***:
                UserDict.UserDict.__init__(self***REMOVED***
                data = self.data
                for k, v in environ.items(***REMOVED***:
                    data[k.upper(***REMOVED******REMOVED*** = v
            def __setitem__(self, key, item***REMOVED***:
                putenv(key, item***REMOVED***
                self.data[key.upper(***REMOVED******REMOVED*** = item
            def __getitem__(self, key***REMOVED***:
                return self.data[key.upper(***REMOVED******REMOVED***
            try:
                unsetenv
            except NameError:
                def __delitem__(self, key***REMOVED***:
                    del self.data[key.upper(***REMOVED******REMOVED***
            else:
                def __delitem__(self, key***REMOVED***:
                    unsetenv(key***REMOVED***
                    del self.data[key.upper(***REMOVED******REMOVED***
                def clear(self***REMOVED***:
                    for key in self.data.keys(***REMOVED***:
                        unsetenv(key***REMOVED***
                        del self.data[key***REMOVED***
                def pop(self, key, *args***REMOVED***:
                    unsetenv(key***REMOVED***
                    return self.data.pop(key.upper(***REMOVED***, *args***REMOVED***
            def has_key(self, key***REMOVED***:
                return key.upper(***REMOVED*** in self.data
            def __contains__(self, key***REMOVED***:
                return key.upper(***REMOVED*** in self.data
            def get(self, key, failobj=None***REMOVED***:
                return self.data.get(key.upper(***REMOVED***, failobj***REMOVED***
            def update(self, dict=None, **kwargs***REMOVED***:
                if dict:
                    try:
                        keys = dict.keys(***REMOVED***
                    except AttributeError:
                        # List of (key, value***REMOVED***
                        for k, v in dict:
                            self[k***REMOVED*** = v
                    else:
                        # got keys
                        # cannot use items(***REMOVED***, since mappings
                        # may not have them.
                        for k in keys:
                            self[k***REMOVED*** = dict[k***REMOVED***
                if kwargs:
                    self.update(kwargs***REMOVED***
            def copy(self***REMOVED***:
                return dict(self***REMOVED***

    else:  # Where Env Var Names Can Be Mixed Case
        class _Environ(UserDict.IterableUserDict***REMOVED***:
            def __init__(self, environ***REMOVED***:
                UserDict.UserDict.__init__(self***REMOVED***
                self.data = environ
            def __setitem__(self, key, item***REMOVED***:
                putenv(key, item***REMOVED***
                self.data[key***REMOVED*** = item
            def update(self,  dict=None, **kwargs***REMOVED***:
                if dict:
                    try:
                        keys = dict.keys(***REMOVED***
                    except AttributeError:
                        # List of (key, value***REMOVED***
                        for k, v in dict:
                            self[k***REMOVED*** = v
                    else:
                        # got keys
                        # cannot use items(***REMOVED***, since mappings
                        # may not have them.
                        for k in keys:
                            self[k***REMOVED*** = dict[k***REMOVED***
                if kwargs:
                    self.update(kwargs***REMOVED***
            try:
                unsetenv
            except NameError:
                pass
            else:
                def __delitem__(self, key***REMOVED***:
                    unsetenv(key***REMOVED***
                    del self.data[key***REMOVED***
                def clear(self***REMOVED***:
                    for key in self.data.keys(***REMOVED***:
                        unsetenv(key***REMOVED***
                        del self.data[key***REMOVED***
                def pop(self, key, *args***REMOVED***:
                    unsetenv(key***REMOVED***
                    return self.data.pop(key, *args***REMOVED***
            def copy(self***REMOVED***:
                return dict(self***REMOVED***


    environ = _Environ(environ***REMOVED***

def getenv(key, default=None***REMOVED***:
    ***REMOVED***Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.***REMOVED***
    return environ.get(key, default***REMOVED***
__all__.append("getenv"***REMOVED***

def _exists(name***REMOVED***:
    return name in globals(***REMOVED***

# Supply spawn*(***REMOVED*** (probably only for Unix***REMOVED***
if _exists("fork"***REMOVED*** and not _exists("spawnv"***REMOVED*** and _exists("execv"***REMOVED***:

    P_WAIT = 0
    P_NOWAIT = P_NOWAITO = 1

    # XXX Should we support P_DETACH?  I suppose it could fork(***REMOVED*****2
    # and close the std I/O streams.  Also, P_OVERLAY is the same
    # as execv*(***REMOVED***?

    def _spawnvef(mode, file, args, env, func***REMOVED***:
        # Internal helper; func is the exec*(***REMOVED*** function to use
        pid = fork(***REMOVED***
        if not pid:
            # Child
            try:
                if env is None:
                    func(file, args***REMOVED***
                else:
                    func(file, args, env***REMOVED***
            except:
                _exit(127***REMOVED***
        else:
            # Parent
            if mode == P_NOWAIT:
                return pid # Caller is responsible for waiting!
            while 1:
                wpid, sts = waitpid(pid, 0***REMOVED***
                if WIFSTOPPED(sts***REMOVED***:
                    continue
                elif WIFSIGNALED(sts***REMOVED***:
                    return -WTERMSIG(sts***REMOVED***
                elif WIFEXITED(sts***REMOVED***:
                    return WEXITSTATUS(sts***REMOVED***
                else:
                    raise error, "Not stopped, signaled or exited???"

    def spawnv(mode, file, args***REMOVED***:
        ***REMOVED***spawnv(mode, file, args***REMOVED*** -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        return _spawnvef(mode, file, args, None, execv***REMOVED***

    def spawnve(mode, file, args, env***REMOVED***:
        ***REMOVED***spawnve(mode, file, args, env***REMOVED*** -> integer

Execute file with arguments from args in a subprocess with the
specified environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        return _spawnvef(mode, file, args, env, execve***REMOVED***

    # Note: spawnvp[e***REMOVED*** is't currently supported on Windows

    def spawnvp(mode, file, args***REMOVED***:
        ***REMOVED***spawnvp(mode, file, args***REMOVED*** -> integer

Execute file (which is looked for along $PATH***REMOVED*** with arguments from
args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        return _spawnvef(mode, file, args, None, execvp***REMOVED***

    def spawnvpe(mode, file, args, env***REMOVED***:
        ***REMOVED***spawnvpe(mode, file, args, env***REMOVED*** -> integer

Execute file (which is looked for along $PATH***REMOVED*** with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        return _spawnvef(mode, file, args, env, execvpe***REMOVED***

if _exists("spawnv"***REMOVED***:
    # These aren't supplied by the basic Windows code
    # but can be easily implemented in Python

    def spawnl(mode, file, *args***REMOVED***:
        ***REMOVED***spawnl(mode, file, *args***REMOVED*** -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        return spawnv(mode, file, args***REMOVED***

    def spawnle(mode, file, *args***REMOVED***:
        ***REMOVED***spawnle(mode, file, *args, env***REMOVED*** -> integer

Execute file with arguments from args in a subprocess with the
supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        env = args[-1***REMOVED***
        return spawnve(mode, file, args[:-1***REMOVED***, env***REMOVED***


    __all__.extend(["spawnv", "spawnve", "spawnl", "spawnle",***REMOVED******REMOVED***


if _exists("spawnvp"***REMOVED***:
    # At the moment, Windows doesn't implement spawnvp[e***REMOVED***,
    # so it won't have spawnlp[e***REMOVED*** either.
    def spawnlp(mode, file, *args***REMOVED***:
        ***REMOVED***spawnlp(mode, file, *args***REMOVED*** -> integer

Execute file (which is looked for along $PATH***REMOVED*** with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        return spawnvp(mode, file, args***REMOVED***

    def spawnlpe(mode, file, *args***REMOVED***:
        ***REMOVED***spawnlpe(mode, file, *args, env***REMOVED*** -> integer

Execute file (which is looked for along $PATH***REMOVED*** with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. ***REMOVED***
        env = args[-1***REMOVED***
        return spawnvpe(mode, file, args[:-1***REMOVED***, env***REMOVED***


    __all__.extend(["spawnvp", "spawnvpe", "spawnlp", "spawnlpe",***REMOVED******REMOVED***


# Supply popen2 etc. (for Unix***REMOVED***
if _exists("fork"***REMOVED***:
    if not _exists("popen2"***REMOVED***:
        def popen2(cmd, mode="t", bufsize=-1***REMOVED***:
            ***REMOVED***Execute the shell command 'cmd' in a sub-process.  On UNIX, 'cmd'
            may be a sequence, in which case arguments will be passed directly to
            the program without shell intervention (as with os.spawnv(***REMOVED******REMOVED***.  If 'cmd'
            is a string it will be passed to the shell (as with os.system(***REMOVED******REMOVED***. If
            'bufsize' is specified, it sets the buffer size for the I/O pipes.  The
            file objects (child_stdin, child_stdout***REMOVED*** are returned.***REMOVED***
            import warnings
            msg = "os.popen2 is deprecated.  Use the subprocess module."
            warnings.warn(msg, DeprecationWarning, stacklevel=2***REMOVED***

            import subprocess
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell=isinstance(cmd, basestring***REMOVED***,
                                 bufsize=bufsize, stdin=PIPE, stdout=PIPE,
                                 close_fds=True***REMOVED***
            return p.stdin, p.stdout
        __all__.append("popen2"***REMOVED***

    if not _exists("popen3"***REMOVED***:
        def popen3(cmd, mode="t", bufsize=-1***REMOVED***:
            ***REMOVED***Execute the shell command 'cmd' in a sub-process.  On UNIX, 'cmd'
            may be a sequence, in which case arguments will be passed directly to
            the program without shell intervention (as with os.spawnv(***REMOVED******REMOVED***.  If 'cmd'
            is a string it will be passed to the shell (as with os.system(***REMOVED******REMOVED***. If
            'bufsize' is specified, it sets the buffer size for the I/O pipes.  The
            file objects (child_stdin, child_stdout, child_stderr***REMOVED*** are returned.***REMOVED***
            import warnings
            msg = "os.popen3 is deprecated.  Use the subprocess module."
            warnings.warn(msg, DeprecationWarning, stacklevel=2***REMOVED***

            import subprocess
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell=isinstance(cmd, basestring***REMOVED***,
                                 bufsize=bufsize, stdin=PIPE, stdout=PIPE,
                                 stderr=PIPE, close_fds=True***REMOVED***
            return p.stdin, p.stdout, p.stderr
        __all__.append("popen3"***REMOVED***

    if not _exists("popen4"***REMOVED***:
        def popen4(cmd, mode="t", bufsize=-1***REMOVED***:
            ***REMOVED***Execute the shell command 'cmd' in a sub-process.  On UNIX, 'cmd'
            may be a sequence, in which case arguments will be passed directly to
            the program without shell intervention (as with os.spawnv(***REMOVED******REMOVED***.  If 'cmd'
            is a string it will be passed to the shell (as with os.system(***REMOVED******REMOVED***. If
            'bufsize' is specified, it sets the buffer size for the I/O pipes.  The
            file objects (child_stdin, child_stdout_stderr***REMOVED*** are returned.***REMOVED***
            import warnings
            msg = "os.popen4 is deprecated.  Use the subprocess module."
            warnings.warn(msg, DeprecationWarning, stacklevel=2***REMOVED***

            import subprocess
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell=isinstance(cmd, basestring***REMOVED***,
                                 bufsize=bufsize, stdin=PIPE, stdout=PIPE,
                                 stderr=subprocess.STDOUT, close_fds=True***REMOVED***
            return p.stdin, p.stdout
        __all__.append("popen4"***REMOVED***

import copy_reg as _copy_reg

def _make_stat_result(tup, dict***REMOVED***:
    return stat_result(tup, dict***REMOVED***

def _pickle_stat_result(sr***REMOVED***:
    (type, args***REMOVED*** = sr.__reduce__(***REMOVED***
    return (_make_stat_result, args***REMOVED***

try:
    _copy_reg.pickle(stat_result, _pickle_stat_result, _make_stat_result***REMOVED***
except NameError: # stat_result may not exist
    pass

def _make_statvfs_result(tup, dict***REMOVED***:
    return statvfs_result(tup, dict***REMOVED***

def _pickle_statvfs_result(sr***REMOVED***:
    (type, args***REMOVED*** = sr.__reduce__(***REMOVED***
    return (_make_statvfs_result, args***REMOVED***

try:
    _copy_reg.pickle(statvfs_result, _pickle_statvfs_result,
                     _make_statvfs_result***REMOVED***
except NameError: # statvfs_result may not exist
    pass
