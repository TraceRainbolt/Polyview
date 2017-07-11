#ifndef Py_OSDEFS_H
#define Py_OSDEFS_H
#ifdef __cplusplus
extern "C" {
#endif


/* Operating system dependencies */

/* Mod by chrish: QNX has WATCOM, but isn't DOS */
#if !defined(__QNX__***REMOVED***
#if defined(MS_WINDOWS***REMOVED*** || defined(__BORLANDC__***REMOVED*** || defined(__WATCOMC__***REMOVED*** || defined(__DJGPP__***REMOVED*** || defined(PYOS_OS2***REMOVED***
#if defined(PYOS_OS2***REMOVED*** && defined(PYCC_GCC***REMOVED***
#define MAXPATHLEN 260
#define SEP '/'
#define ALTSEP '\\'
#else
#define SEP '\\'
#define ALTSEP '/'
#define MAXPATHLEN 256
#endif
#define DELIM ';'
#endif
#endif

#ifdef RISCOS
#define SEP '.'
#define MAXPATHLEN 256
#define DELIM ','
#endif


/* Filename separator */
#ifndef SEP
#define SEP '/'
#endif

/* Max pathname length */
#ifdef __hpux
#include <sys/param.h>
#include <limits.h>
#ifndef PATH_MAX
#define PATH_MAX MAXPATHLEN
#endif
#endif

#ifndef MAXPATHLEN
#if defined(PATH_MAX***REMOVED*** && PATH_MAX > 1024
#define MAXPATHLEN PATH_MAX
#else
#define MAXPATHLEN 1024
#endif
#endif

/* Search path entry delimiter */
#ifndef DELIM
#define DELIM ':'
#endif

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_OSDEFS_H */
