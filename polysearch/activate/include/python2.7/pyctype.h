#ifndef PYCTYPE_H
#define PYCTYPE_H

#define PY_CTF_LOWER  0x01
#define PY_CTF_UPPER  0x02
#define PY_CTF_ALPHA  (PY_CTF_LOWER|PY_CTF_UPPER***REMOVED***
#define PY_CTF_DIGIT  0x04
#define PY_CTF_ALNUM  (PY_CTF_ALPHA|PY_CTF_DIGIT***REMOVED***
#define PY_CTF_SPACE  0x08
#define PY_CTF_XDIGIT 0x10

PyAPI_DATA(const unsigned int***REMOVED*** _Py_ctype_table[256***REMOVED***;

/* Unlike their C counterparts, the following macros are not meant to
 * handle an int with any of the values [EOF, 0-UCHAR_MAX***REMOVED***. The argument
 * must be a signed/unsigned char. */
#define Py_ISLOWER(c***REMOVED***  (_Py_ctype_table[Py_CHARMASK(c***REMOVED******REMOVED*** & PY_CTF_LOWER***REMOVED***
#define Py_ISUPPER(c***REMOVED***  (_Py_ctype_table[Py_CHARMASK(c***REMOVED******REMOVED*** & PY_CTF_UPPER***REMOVED***
#define Py_ISALPHA(c***REMOVED***  (_Py_ctype_table[Py_CHARMASK(c***REMOVED******REMOVED*** & PY_CTF_ALPHA***REMOVED***
#define Py_ISDIGIT(c***REMOVED***  (_Py_ctype_table[Py_CHARMASK(c***REMOVED******REMOVED*** & PY_CTF_DIGIT***REMOVED***
#define Py_ISXDIGIT(c***REMOVED*** (_Py_ctype_table[Py_CHARMASK(c***REMOVED******REMOVED*** & PY_CTF_XDIGIT***REMOVED***
#define Py_ISALNUM(c***REMOVED***  (_Py_ctype_table[Py_CHARMASK(c***REMOVED******REMOVED*** & PY_CTF_ALNUM***REMOVED***
#define Py_ISSPACE(c***REMOVED***  (_Py_ctype_table[Py_CHARMASK(c***REMOVED******REMOVED*** & PY_CTF_SPACE***REMOVED***

PyAPI_DATA(const unsigned char***REMOVED*** _Py_ctype_tolower[256***REMOVED***;
PyAPI_DATA(const unsigned char***REMOVED*** _Py_ctype_toupper[256***REMOVED***;

#define Py_TOLOWER(c***REMOVED*** (_Py_ctype_tolower[Py_CHARMASK(c***REMOVED******REMOVED******REMOVED***
#define Py_TOUPPER(c***REMOVED*** (_Py_ctype_toupper[Py_CHARMASK(c***REMOVED******REMOVED******REMOVED***

#endif /* !PYCTYPE_H */
