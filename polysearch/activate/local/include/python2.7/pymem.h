/* The PyMem_ family:  low-level memory allocation interfaces.
   See objimpl.h for the PyObject_ memory family.
*/

#ifndef Py_PYMEM_H
#define Py_PYMEM_H

#include "pyport.h"

#ifdef __cplusplus
extern "C" {
#endif

/* BEWARE:

   Each interface exports both functions and macros.  Extension modules should
   use the functions, to ensure binary compatibility across Python versions.
   Because the Python implementation is free to change internal details, and
   the macros may (or may not***REMOVED*** expose details for speed, if you do use the
   macros you must recompile your extensions with each Python release.

   Never mix calls to PyMem_ with calls to the platform malloc/realloc/
   calloc/free.  For example, on Windows different DLLs may end up using
   different heaps, and if you use PyMem_Malloc you'll get the memory from the
   heap used by the Python DLL; it could be a disaster if you free(***REMOVED***'ed that
   directly in your own extension.  Using PyMem_Free instead ensures Python
   can return the memory to the proper heap.  As another example, in
   PYMALLOC_DEBUG mode, Python wraps all calls to all PyMem_ and PyObject_
   memory functions in special debugging wrappers that add additional
   debugging info to dynamic memory blocks.  The system routines have no idea
   what to do with that stuff, and the Python wrappers have no idea what to do
   with raw blocks obtained directly by the system routines then.

   The GIL must be held when using these APIs.
*/

/*
 * Raw memory interface
 * ====================
 */

/* Functions

   Functions supplying platform-independent semantics for malloc/realloc/
   free.  These functions make sure that allocating 0 bytes returns a distinct
   non-NULL pointer (whenever possible -- if we're flat out of memory, NULL
   may be returned***REMOVED***, even if the platform malloc and realloc don't.
   Returned pointers must be checked for NULL explicitly.  No action is
   performed on failure (no exception is set, no warning is printed, etc***REMOVED***.
*/

PyAPI_FUNC(void ****REMOVED*** PyMem_Malloc(size_t***REMOVED***;
PyAPI_FUNC(void ****REMOVED*** PyMem_Realloc(void *, size_t***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyMem_Free(void ****REMOVED***;

/* Starting from Python 1.6, the wrappers Py_{Malloc,Realloc,Free***REMOVED*** are
   no longer supported. They used to call PyErr_NoMemory(***REMOVED*** on failure. */

/* Macros. */
#ifdef PYMALLOC_DEBUG
/* Redirect all memory operations to Python's debugging allocator. */
#define PyMem_MALLOC		_PyMem_DebugMalloc
#define PyMem_REALLOC		_PyMem_DebugRealloc
#define PyMem_FREE		_PyMem_DebugFree

#else	/* ! PYMALLOC_DEBUG */

/* PyMem_MALLOC(0***REMOVED*** means malloc(1***REMOVED***. Some systems would return NULL
   for malloc(0***REMOVED***, which would be treated as an error. Some platforms
   would return a pointer with no memory behind it, which would break
   pymalloc. To solve these problems, allocate an extra byte. */
/* Returns NULL to indicate error if a negative size or size larger than
   Py_ssize_t can represent is supplied.  Helps prevents security holes. */
#define PyMem_MALLOC(n***REMOVED***		((size_t***REMOVED***(n***REMOVED*** > (size_t***REMOVED***PY_SSIZE_T_MAX ? NULL \
				: malloc((n***REMOVED*** ? (n***REMOVED*** : 1***REMOVED******REMOVED***
#define PyMem_REALLOC(p, n***REMOVED***	((size_t***REMOVED***(n***REMOVED*** > (size_t***REMOVED***PY_SSIZE_T_MAX  ? NULL \
				: realloc((p***REMOVED***, (n***REMOVED*** ? (n***REMOVED*** : 1***REMOVED******REMOVED***
#define PyMem_FREE		free

#endif	/* PYMALLOC_DEBUG */

/*
 * Type-oriented memory interface
 * ==============================
 *
 * Allocate memory for n objects of the given type.  Returns a new pointer
 * or NULL if the request was too large or memory allocation failed.  Use
 * these macros rather than doing the multiplication yourself so that proper
 * overflow checking is always done.
 */

#define PyMem_New(type, n***REMOVED*** \
  ( ((size_t***REMOVED***(n***REMOVED*** > PY_SSIZE_T_MAX / sizeof(type***REMOVED******REMOVED*** ? NULL :	\
	( (type ****REMOVED*** PyMem_Malloc((n***REMOVED*** * sizeof(type***REMOVED******REMOVED*** ***REMOVED*** ***REMOVED***
#define PyMem_NEW(type, n***REMOVED*** \
  ( ((size_t***REMOVED***(n***REMOVED*** > PY_SSIZE_T_MAX / sizeof(type***REMOVED******REMOVED*** ? NULL :	\
	( (type ****REMOVED*** PyMem_MALLOC((n***REMOVED*** * sizeof(type***REMOVED******REMOVED*** ***REMOVED*** ***REMOVED***

/*
 * The value of (p***REMOVED*** is always clobbered by this macro regardless of success.
 * The caller MUST check if (p***REMOVED*** is NULL afterwards and deal with the memory
 * error if so.  This means the original value of (p***REMOVED*** MUST be saved for the
 * caller's memory error handler to not lose track of it.
 */
#define PyMem_Resize(p, type, n***REMOVED*** \
  ( (p***REMOVED*** = ((size_t***REMOVED***(n***REMOVED*** > PY_SSIZE_T_MAX / sizeof(type***REMOVED******REMOVED*** ? NULL :	\
	(type ****REMOVED*** PyMem_Realloc((p***REMOVED***, (n***REMOVED*** * sizeof(type***REMOVED******REMOVED*** ***REMOVED***
#define PyMem_RESIZE(p, type, n***REMOVED*** \
  ( (p***REMOVED*** = ((size_t***REMOVED***(n***REMOVED*** > PY_SSIZE_T_MAX / sizeof(type***REMOVED******REMOVED*** ? NULL :	\
	(type ****REMOVED*** PyMem_REALLOC((p***REMOVED***, (n***REMOVED*** * sizeof(type***REMOVED******REMOVED*** ***REMOVED***

/* PyMem{Del,DEL***REMOVED*** are left over from ancient days, and shouldn't be used
 * anymore.  They're just confusing aliases for PyMem_{Free,FREE***REMOVED*** now.
 */
#define PyMem_Del		PyMem_Free
#define PyMem_DEL		PyMem_FREE

#ifdef __cplusplus
***REMOVED***
#endif

#endif /* !Py_PYMEM_H */
