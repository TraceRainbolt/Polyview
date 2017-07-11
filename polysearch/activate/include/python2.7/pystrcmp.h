#ifndef Py_STRCMP_H
#define Py_STRCMP_H

#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(int***REMOVED*** PyOS_mystrnicmp(const char *, const char *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyOS_mystricmp(const char *, const char ****REMOVED***;

#if defined(MS_WINDOWS***REMOVED*** || defined(PYOS_OS2***REMOVED***
#define PyOS_strnicmp strnicmp
#define PyOS_stricmp stricmp
#else
#define PyOS_strnicmp PyOS_mystrnicmp
#define PyOS_stricmp PyOS_mystricmp
#endif

#ifdef __cplusplus
***REMOVED***
#endif

#endif /* !Py_STRCMP_H */
