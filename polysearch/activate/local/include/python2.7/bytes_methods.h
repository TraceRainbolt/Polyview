#ifndef Py_BYTES_CTYPE_H
#define Py_BYTES_CTYPE_H

/*
 * The internal implementation behind PyString (bytes***REMOVED*** and PyBytes (buffer***REMOVED***
 * methods of the given names, they operate on ASCII byte strings.
 */
extern PyObject* _Py_bytes_isspace(const char *cptr, Py_ssize_t len***REMOVED***;
extern PyObject* _Py_bytes_isalpha(const char *cptr, Py_ssize_t len***REMOVED***;
extern PyObject* _Py_bytes_isalnum(const char *cptr, Py_ssize_t len***REMOVED***;
extern PyObject* _Py_bytes_isdigit(const char *cptr, Py_ssize_t len***REMOVED***;
extern PyObject* _Py_bytes_islower(const char *cptr, Py_ssize_t len***REMOVED***;
extern PyObject* _Py_bytes_isupper(const char *cptr, Py_ssize_t len***REMOVED***;
extern PyObject* _Py_bytes_istitle(const char *cptr, Py_ssize_t len***REMOVED***;

/* These store their len sized answer in the given preallocated *result arg. */
extern void _Py_bytes_lower(char *result, const char *cptr, Py_ssize_t len***REMOVED***;
extern void _Py_bytes_upper(char *result, const char *cptr, Py_ssize_t len***REMOVED***;
extern void _Py_bytes_title(char *result, char *s, Py_ssize_t len***REMOVED***;
extern void _Py_bytes_capitalize(char *result, char *s, Py_ssize_t len***REMOVED***;
extern void _Py_bytes_swapcase(char *result, char *s, Py_ssize_t len***REMOVED***;

/* Shared __doc__ strings. */
extern const char _Py_isspace__doc__[***REMOVED***;
extern const char _Py_isalpha__doc__[***REMOVED***;
extern const char _Py_isalnum__doc__[***REMOVED***;
extern const char _Py_isdigit__doc__[***REMOVED***;
extern const char _Py_islower__doc__[***REMOVED***;
extern const char _Py_isupper__doc__[***REMOVED***;
extern const char _Py_istitle__doc__[***REMOVED***;
extern const char _Py_lower__doc__[***REMOVED***;
extern const char _Py_upper__doc__[***REMOVED***;
extern const char _Py_title__doc__[***REMOVED***;
extern const char _Py_capitalize__doc__[***REMOVED***;
extern const char _Py_swapcase__doc__[***REMOVED***;

/* These are left in for backward compatibility and will be removed
   in 2.8/3.2 */
#define ISLOWER(c***REMOVED***  Py_ISLOWER(c***REMOVED***
#define ISUPPER(c***REMOVED***  Py_ISUPPER(c***REMOVED***
#define ISALPHA(c***REMOVED***  Py_ISALPHA(c***REMOVED***
#define ISDIGIT(c***REMOVED***  Py_ISDIGIT(c***REMOVED***
#define ISXDIGIT(c***REMOVED*** Py_ISXDIGIT(c***REMOVED***
#define ISALNUM(c***REMOVED***  Py_ISALNUM(c***REMOVED***
#define ISSPACE(c***REMOVED***  Py_ISSPACE(c***REMOVED***

#undef islower
#define islower(c***REMOVED*** undefined_islower(c***REMOVED***
#undef isupper
#define isupper(c***REMOVED*** undefined_isupper(c***REMOVED***
#undef isalpha
#define isalpha(c***REMOVED*** undefined_isalpha(c***REMOVED***
#undef isdigit
#define isdigit(c***REMOVED*** undefined_isdigit(c***REMOVED***
#undef isxdigit
#define isxdigit(c***REMOVED*** undefined_isxdigit(c***REMOVED***
#undef isalnum
#define isalnum(c***REMOVED*** undefined_isalnum(c***REMOVED***
#undef isspace
#define isspace(c***REMOVED*** undefined_isspace(c***REMOVED***

/* These are left in for backward compatibility and will be removed
   in 2.8/3.2 */
#define TOLOWER(c***REMOVED*** Py_TOLOWER(c***REMOVED***
#define TOUPPER(c***REMOVED*** Py_TOUPPER(c***REMOVED***

#undef tolower
#define tolower(c***REMOVED*** undefined_tolower(c***REMOVED***
#undef toupper
#define toupper(c***REMOVED*** undefined_toupper(c***REMOVED***

/* this is needed because some docs are shared from the .o, not static */
#define PyDoc_STRVAR_shared(name,str***REMOVED*** const char name[***REMOVED*** = PyDoc_STR(str***REMOVED***

#endif /* !Py_BYTES_CTYPE_H */
