/* An arena-like memory interface for the compiler.
 */

#ifndef Py_PYARENA_H
#define Py_PYARENA_H

#ifdef __cplusplus
extern "C" {
#endif

  typedef struct _arena PyArena;

  /* PyArena_New(***REMOVED*** and PyArena_Free(***REMOVED*** create a new arena and free it,
     respectively.  Once an arena has been created, it can be used
     to allocate memory via PyArena_Malloc(***REMOVED***.  Pointers to PyObject can
     also be registered with the arena via PyArena_AddPyObject(***REMOVED***, and the
     arena will ensure that the PyObjects stay alive at least until
     PyArena_Free(***REMOVED*** is called.  When an arena is freed, all the memory it
     allocated is freed, the arena releases internal references to registered
     PyObject*, and none of its pointers are valid.
     XXX (tim***REMOVED*** What does "none of its pointers are valid" mean?  Does it
     XXX mean that pointers previously obtained via PyArena_Malloc(***REMOVED*** are
     XXX no longer valid?  (That's clearly true, but not sure that's what
     XXX the text is trying to say.***REMOVED***

     PyArena_New(***REMOVED*** returns an arena pointer.  On error, it
     returns a negative number and sets an exception.
     XXX (tim***REMOVED***:  Not true.  On error, PyArena_New(***REMOVED*** actually returns NULL,
     XXX and looks like it may or may not set an exception (e.g., if the
     XXX internal PyList_New(0***REMOVED*** returns NULL, PyArena_New(***REMOVED*** passes that on
     XXX and an exception is set; OTOH, if the internal
     XXX block_new(DEFAULT_BLOCK_SIZE***REMOVED*** returns NULL, that's passed on but
     XXX an exception is not set in that case***REMOVED***.
  */
  PyAPI_FUNC(PyArena ****REMOVED*** PyArena_New(void***REMOVED***;
  PyAPI_FUNC(void***REMOVED*** PyArena_Free(PyArena ****REMOVED***;

  /* Mostly like malloc(***REMOVED***, return the address of a block of memory spanning
   * `size` bytes, or return NULL (without setting an exception***REMOVED*** if enough
   * new memory can't be obtained.  Unlike malloc(0***REMOVED***, PyArena_Malloc(***REMOVED*** with
   * size=0 does not guarantee to return a unique pointer (the pointer
   * returned may equal one or more other pointers obtained from
   * PyArena_Malloc(***REMOVED******REMOVED***.
   * Note that pointers obtained via PyArena_Malloc(***REMOVED*** must never be passed to
   * the system free(***REMOVED*** or realloc(***REMOVED***, or to any of Python's similar memory-
   * management functions.  PyArena_Malloc(***REMOVED***-obtained pointers remain valid
   * until PyArena_Free(ar***REMOVED*** is called, at which point all pointers obtained
   * from the arena `ar` become invalid simultaneously.
   */
  PyAPI_FUNC(void ****REMOVED*** PyArena_Malloc(PyArena *, size_t size***REMOVED***;

  /* This routine isn't a proper arena allocation routine.  It takes
   * a PyObject* and records it so that it can be DECREFed when the
   * arena is freed.
   */
  PyAPI_FUNC(int***REMOVED*** PyArena_AddPyObject(PyArena *, PyObject ****REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif

#endif /* !Py_PYARENA_H */
