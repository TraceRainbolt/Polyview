***REMOVED***Constants/functions for interpreting results of os.stat(***REMOVED*** and os.lstat(***REMOVED***.

Suggested usage: from stat import *
***REMOVED***

# Indices for stat struct members in the tuple returned by os.stat(***REMOVED***

ST_MODE  = 0
ST_INO   = 1
ST_DEV   = 2
ST_NLINK = 3
ST_UID   = 4
ST_GID   = 5
ST_SIZE  = 6
ST_ATIME = 7
ST_MTIME = 8
ST_CTIME = 9

# Extract bits from the mode

def S_IMODE(mode***REMOVED***:
    return mode & 07777

def S_IFMT(mode***REMOVED***:
    return mode & 0170000

# Constants used as S_IFMT(***REMOVED*** for various file types
# (not all are implemented on all systems***REMOVED***

S_IFDIR  = 0040000
S_IFCHR  = 0020000
S_IFBLK  = 0060000
S_IFREG  = 0100000
S_IFIFO  = 0010000
S_IFLNK  = 0120000
S_IFSOCK = 0140000

# Functions to test for each file type

def S_ISDIR(mode***REMOVED***:
    return S_IFMT(mode***REMOVED*** == S_IFDIR

def S_ISCHR(mode***REMOVED***:
    return S_IFMT(mode***REMOVED*** == S_IFCHR

def S_ISBLK(mode***REMOVED***:
    return S_IFMT(mode***REMOVED*** == S_IFBLK

def S_ISREG(mode***REMOVED***:
    return S_IFMT(mode***REMOVED*** == S_IFREG

def S_ISFIFO(mode***REMOVED***:
    return S_IFMT(mode***REMOVED*** == S_IFIFO

def S_ISLNK(mode***REMOVED***:
    return S_IFMT(mode***REMOVED*** == S_IFLNK

def S_ISSOCK(mode***REMOVED***:
    return S_IFMT(mode***REMOVED*** == S_IFSOCK

# Names for permission bits

S_ISUID = 04000
S_ISGID = 02000
S_ENFMT = S_ISGID
S_ISVTX = 01000
S_IREAD = 00400
S_IWRITE = 00200
S_IEXEC = 00100
S_IRWXU = 00700
S_IRUSR = 00400
S_IWUSR = 00200
S_IXUSR = 00100
S_IRWXG = 00070
S_IRGRP = 00040
S_IWGRP = 00020
S_IXGRP = 00010
S_IRWXO = 00007
S_IROTH = 00004
S_IWOTH = 00002
S_IXOTH = 00001

# Names for file flags

UF_NODUMP    = 0x00000001
UF_IMMUTABLE = 0x00000002
UF_APPEND    = 0x00000004
UF_OPAQUE    = 0x00000008
UF_NOUNLINK  = 0x00000010
UF_COMPRESSED = 0x00000020  # OS X: file is hfs-compressed
UF_HIDDEN    = 0x00008000   # OS X: file should not be displayed
SF_ARCHIVED  = 0x00010000
SF_IMMUTABLE = 0x00020000
SF_APPEND    = 0x00040000
SF_NOUNLINK  = 0x00100000
SF_SNAPSHOT  = 0x00200000
