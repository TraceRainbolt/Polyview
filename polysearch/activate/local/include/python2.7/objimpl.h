/* The PyObject_ memory family:  high-level object memory interfaces.
   See pymem.h for the low-level PyMem_ family.
*/

#ifndef Py_OBJIMPL_H
#define Py_OBJIMPL_H

#include "pymem.h"

#ifdef __cplusplus
extern "C" {
#endif

/* BEWARE:

   Each interface exports both functions and macros.  Extension modules should
   use the functions, to ensure binary compatibility across Python versions.
   Because the Python implementation is free to change internal details, and
   the macros may (or may not***REMOVED*** expose details for speed, if you do use the
   macros you must recompile your extensions with each Python release.

   Never mix calls to PyObject_ memory functions with calls to the platform
   malloc/realloc/ calloc/free, or with calls to PyMem_.
*/

/*
Functions and macros for modules that implement new object types.

 - PyObject_New(type, typeobj***REMOVED*** allocates memory for a new object of the given
   type, and initializes part of it.  'type' must be the C structure type used
   to represent the object, and 'typeobj' the address of the corresponding
   type object.  Reference count and type pointer are filled in; the rest of
   the bytes of the object are *undefined*!  The resulting expression type is
   'type *'.  The size of the object is determined by the tp_basicsize field
   of the type object.

 - PyObject_NewVar(type, typeobj, n***REMOVED*** is similar but allocates a variable-size
   object with room for n items.  In addition to the refcount and type pointer
   fields, this also fills in the ob_size field.

 - PyObject_Del(op***REMOVED*** releases the memory allocated for an object.  It does not
   run a destructor -- it only frees the memory.  PyObject_Free is identical.

 - PyObject_Init(op, typeobj***REMOVED*** and PyObject_InitVar(op, typeobj, n***REMOVED*** don't
   allocate memory.  Instead of a 'type' parameter, they take a pointer to a
   new object (allocated by an arbitrary allocator***REMOVED***, and initialize its object
   header fields.

Note that objects created with PyObject_{New, NewVar***REMOVED*** are allocated using the
specialized Python allocator (implemented in obmalloc.c***REMOVED***, if WITH_PYMALLOC is
enabled.  In addition, a special debugging allocator is used if PYMALLOC_DEBUG
is also #defined.

In case a specific form of memory management is needed (for example, if you
must use the platform malloc heap(s***REMOVED***, or shared memory, or C++ local storage or
operator new***REMOVED***, you must first allocate the object with your custom allocator,
then pass its pointer to PyObject_{Init, InitVar***REMOVED*** for filling in its Python-
specific fields:  reference count, type pointer, possibly others.  You should
be aware that Python no control over these objects because they don't
cooperate with the Python memory manager.  Such objects may not be eligible
for automatic garbage collection and you have to make sure that they are
released accordingly whenever their destructor gets called (cf. the specific
form of memory management you're using***REMOVED***.

Unless you have specific memory management requirements, use
PyObject_{New, NewVar, Del***REMOVED***.
*/

/*
 * Raw object memory interface
 * ===========================
 */

/* Functions to call the same malloc/realloc/free as used by Python's
   object allocator.  If WITH_PYMALLOC is enabled, these may differ from
   the platform malloc/realloc/free.  The Python object allocator is
   designed for fast, cache-conscious allocation of many "small" objects,
   and with low hidden memory overhead.

   PyObject_Malloc(0***REMOVED*** returns a unique non-NULL pointer if possible.

   PyObject_Realloc(NULL, n***REMOVED*** acts like PyObject_Malloc(n***REMOVED***.
   PyObject_Realloc(p != NULL, 0***REMOVED*** does not return  NULL, or free the memory
   at p.

   Returned pointers must be checked for NULL explicitly; no action is
   performed on failure other than to return NULL (no warning it printed, no
   exception is set, etc***REMOVED***.

   For allocating objects, use PyObject_{New, NewVar***REMOVED*** instead whenever
   possible.  The PyObject_{Malloc, Realloc, Free***REMOVED*** family is exposed
   so that you can exploit Python's small-block allocator for non-object
   uses.  If you must use these routines to allocate object memory, make sure
   the object gets initialized via PyObject_{Init, InitVar***REMOVED*** after obtaining
   the raw memory.
*/
PyAPI_FUNC(void ****REMOVED*** PyObject_Malloc(size_t***REMOVED***;
PyAPI_FUNC(void ****REMOVED*** PyObject_Realloc(void *, size_t***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyObject_Free(void ****REMOVED***;


/* Macros */
#ifdef WITH_PYMALLOC
#ifdef PYMALLOC_DEBUG   /* WITH_PYMALLOC && PYMALLOC_DEBUG */
PyAPI_FUNC(void ****REMOVED*** _PyObject_DebugMalloc(size_t nbytes***REMOVED***;
PyAPI_FUNC(void ****REMOVED*** _PyObject_DebugRealloc(void *p, size_t nbytes***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyObject_DebugFree(void *p***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyObject_DebugDumpAddress(const void *p***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyObject_DebugCheckAddress(const void *p***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyObject_DebugMallocStats(void***REMOVED***;
PyAPI_FUNC(void ****REMOVED*** _PyObject_DebugMallocApi(char api, size_t nbytes***REMOVED***;
PyAPI_FUNC(void ****REMOVED*** _PyObject_DebugReallocApi(char api, void *p, size_t nbytes***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyObject_DebugFreeApi(char api, void *p***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyObject_DebugCheckAddressApi(char api, const void *p***REMOVED***;
PyAPI_FUNC(void ****REMOVED*** _PyMem_DebugMalloc(size_t nbytes***REMOVED***;
PyAPI_FUNC(void ****REMOVED*** _PyMem_DebugRealloc(void *p, size_t nbytes***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyMem_DebugFree(void *p***REMOVED***;
#define PyObject_MALLOC         _PyObject_DebugMalloc
#define PyObject_Malloc         _PyObject_DebugMalloc
#define PyObject_REALLOC        _PyObject_DebugRealloc
#define PyObject_Realloc        _PyObject_DebugRealloc
#define PyObject_FREE           _PyObject_DebugFree
#define PyObject_Free           _PyObject_DebugFree

#else   /* WITH_PYMALLOC && ! PYMALLOC_DEBUG */
#define PyObject_MALLOC         PyObject_Malloc
#define PyObject_REALLOC        PyObject_Realloc
#define PyObject_FREE           PyObject_Free
#endif

#else   /* ! WITH_PYMALLOC */
#define PyObject_MALLOC         PyMem_MALLOC
#define PyObject_REALLOC        PyMem_REALLOC
#define PyObject_FREE           PyMem_FREE

#endif  /* WITH_PYMALLOC */

#define PyObject_Del            PyObject_Free
#define PyObject_DEL            PyObject_FREE

/* for source compatibility with 2.2 */
#define _PyObject_Del           PyObject_Free

/*
 * Generic object allocator interface
 * ==================================
 */

/* Functions */
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_Init(PyObject *, PyTypeObject ****REMOVED***;
PyAPI_FUNC(PyVarObject ****REMOVED*** PyObject_InitVar(PyVarObject *,
                                                 PyTypeObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyObject_New(PyTypeObject ****REMOVED***;
PyAPI_FUNC(PyVarObject ****REMOVED*** _PyObject_NewVar(PyTypeObject *, Py_ssize_t***REMOVED***;

#define PyObject_New(type, typeobj***REMOVED*** \
                ( (type ****REMOVED*** _PyObject_New(typeobj***REMOVED*** ***REMOVED***
#define PyObject_NewVar(type, typeobj, n***REMOVED*** \
                ( (type ****REMOVED*** _PyObject_NewVar((typeobj***REMOVED***, (n***REMOVED******REMOVED*** ***REMOVED***

/* Macros trading binary compatibility for speed. See also pymem.h.
   Note that these macros expect non-NULL object pointers.*/
#define PyObject_INIT(op, typeobj***REMOVED*** \
    ( Py_TYPE(op***REMOVED*** = (typeobj***REMOVED***, _Py_NewReference((PyObject ****REMOVED***(op***REMOVED******REMOVED***, (op***REMOVED*** ***REMOVED***
#define PyObject_INIT_VAR(op, typeobj, size***REMOVED*** \
    ( Py_SIZE(op***REMOVED*** = (size***REMOVED***, PyObject_INIT((op***REMOVED***, (typeobj***REMOVED******REMOVED*** ***REMOVED***

#define _PyObject_SIZE(typeobj***REMOVED*** ( (typeobj***REMOVED***->tp_basicsize ***REMOVED***

/* _PyObject_VAR_SIZE returns the number of bytes (as size_t***REMOVED*** allocated for a
   vrbl-size object with nitems items, exclusive of gc overhead (if any***REMOVED***.  The
   value is rounded up to the closest multiple of sizeof(void ****REMOVED***, in order to
   ensure that pointer fields at the end of the object are correctly aligned
   for the platform (this is of special importance for subclasses of, e.g.,
   str or long, so that pointers can be stored after the embedded data***REMOVED***.

   Note that there's no memory wastage in doing this, as malloc has to
   return (at worst***REMOVED*** pointer-aligned memory anyway.
*/
#if ((SIZEOF_VOID_P - 1***REMOVED*** & SIZEOF_VOID_P***REMOVED*** != 0
#   error "_PyObject_VAR_SIZE requires SIZEOF_VOID_P be a power of 2"
#endif

#define _PyObject_VAR_SIZE(typeobj, nitems***REMOVED***     \
    (size_t***REMOVED***                                    \
    ( ( (typeobj***REMOVED***->tp_basicsize +               \
        (nitems***REMOVED****(typeobj***REMOVED***->tp_itemsize +       \
        (SIZEOF_VOID_P - 1***REMOVED***                     \
      ***REMOVED*** & ~(SIZEOF_VOID_P - 1***REMOVED***                  \
    ***REMOVED***

#define PyObject_NEW(type, typeobj***REMOVED*** \
( (type ****REMOVED*** PyObject_Init( \
    (PyObject ****REMOVED*** PyObject_MALLOC( _PyObject_SIZE(typeobj***REMOVED*** ***REMOVED***, (typeobj***REMOVED******REMOVED*** ***REMOVED***

#define PyObject_NEW_VAR(type, typeobj, n***REMOVED*** \
( (type ****REMOVED*** PyObject_InitVar( \
      (PyVarObject ****REMOVED*** PyObject_MALLOC(_PyObject_VAR_SIZE((typeobj***REMOVED***,(n***REMOVED******REMOVED*** ***REMOVED***,\
      (typeobj***REMOVED***, (n***REMOVED******REMOVED*** ***REMOVED***

/* This example code implements an object constructor with a custom
   allocator, where PyObject_New is inlined, and shows the important
   distinction between two steps (at least***REMOVED***:
       1***REMOVED*** the actual allocation of the object storage;
       2***REMOVED*** the initialization of the Python specific fields
      in this storage with PyObject_{Init, InitVar***REMOVED***.

   PyObject *
   YourObject_New(...***REMOVED***
   {
       PyObject *op;

       op = (PyObject ****REMOVED*** Your_Allocator(_PyObject_SIZE(YourTypeStruct***REMOVED******REMOVED***;
       if (op == NULL***REMOVED***
       return PyErr_NoMemory(***REMOVED***;

       PyObject_Init(op, &YourTypeStruct***REMOVED***;

       op->ob_field = value;
       ...
       return op;
   ***REMOVED***

   Note that in C++, the use of the new operator usually implies that
   the 1st step is performed automatically for you, so in a C++ class
   constructor you would start directly with PyObject_Init/InitVar
*/

/*
 * Garbage Collection Support
 * ==========================
 */

/* C equivalent of gc.collect(***REMOVED***. */
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyGC_Collect(void***REMOVED***;

/* Test if a type has a GC head */
#define PyType_IS_GC(t***REMOVED*** PyType_HasFeature((t***REMOVED***, Py_TPFLAGS_HAVE_GC***REMOVED***

/* Test if an object has a GC head */
#define PyObject_IS_GC(o***REMOVED*** (PyType_IS_GC(Py_TYPE(o***REMOVED******REMOVED*** && \
    (Py_TYPE(o***REMOVED***->tp_is_gc == NULL || Py_TYPE(o***REMOVED***->tp_is_gc(o***REMOVED******REMOVED******REMOVED***

PyAPI_FUNC(PyVarObject ****REMOVED*** _PyObject_GC_Resize(PyVarObject *, Py_ssize_t***REMOVED***;
#define PyObject_GC_Resize(type, op, n***REMOVED*** \
                ( (type ****REMOVED*** _PyObject_GC_Resize((PyVarObject ****REMOVED***(op***REMOVED***, (n***REMOVED******REMOVED*** ***REMOVED***

/* for source compatibility with 2.2 */
#define _PyObject_GC_Del PyObject_GC_Del

/* GC information is stored BEFORE the object structure. */
typedef union _gc_head {
    struct {
        union _gc_head *gc_next;
        union _gc_head *gc_prev;
        Py_ssize_t gc_refs;
***REMOVED*** gc;
    long double dummy;  /* force worst-case alignment */
***REMOVED*** PyGC_Head;

extern PyGC_Head *_PyGC_generation0;

#define _Py_AS_GC(o***REMOVED*** ((PyGC_Head ****REMOVED***(o***REMOVED***-1***REMOVED***

#define _PyGC_REFS_UNTRACKED                    (-2***REMOVED***
#define _PyGC_REFS_REACHABLE                    (-3***REMOVED***
#define _PyGC_REFS_TENTATIVELY_UNREACHABLE      (-4***REMOVED***

/* Tell the GC to track this object.  NB: While the object is tracked the
 * collector it must be safe to call the ob_traverse method. */
#define _PyObject_GC_TRACK(o***REMOVED*** do { \
    PyGC_Head *g = _Py_AS_GC(o***REMOVED***; \
    if (g->gc.gc_refs != _PyGC_REFS_UNTRACKED***REMOVED*** \
        Py_FatalError("GC object already tracked"***REMOVED***; \
    g->gc.gc_refs = _PyGC_REFS_REACHABLE; \
    g->gc.gc_next = _PyGC_generation0; \
    g->gc.gc_prev = _PyGC_generation0->gc.gc_prev; \
    g->gc.gc_prev->gc.gc_next = g; \
    _PyGC_generation0->gc.gc_prev = g; \
***REMOVED*** while (0***REMOVED***;

/* Tell the GC to stop tracking this object.
 * gc_next doesn't need to be set to NULL, but doing so is a good
 * way to provoke memory errors if calling code is confused.
 */
#define _PyObject_GC_UNTRACK(o***REMOVED*** do { \
    PyGC_Head *g = _Py_AS_GC(o***REMOVED***; \
    assert(g->gc.gc_refs != _PyGC_REFS_UNTRACKED***REMOVED***; \
    g->gc.gc_refs = _PyGC_REFS_UNTRACKED; \
    g->gc.gc_prev->gc.gc_next = g->gc.gc_next; \
    g->gc.gc_next->gc.gc_prev = g->gc.gc_prev; \
    g->gc.gc_next = NULL; \
***REMOVED*** while (0***REMOVED***;

/* True if the object is currently tracked by the GC. */
#define _PyObject_GC_IS_TRACKED(o***REMOVED*** \
    ((_Py_AS_GC(o***REMOVED******REMOVED***->gc.gc_refs != _PyGC_REFS_UNTRACKED***REMOVED***

/* True if the object may be tracked by the GC in the future, or already is.
   This can be useful to implement some optimizations. */
#define _PyObject_GC_MAY_BE_TRACKED(obj***REMOVED*** \
    (PyObject_IS_GC(obj***REMOVED*** && \
        (!PyTuple_CheckExact(obj***REMOVED*** || _PyObject_GC_IS_TRACKED(obj***REMOVED******REMOVED******REMOVED***


PyAPI_FUNC(PyObject ****REMOVED*** _PyObject_GC_Malloc(size_t***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyObject_GC_New(PyTypeObject ****REMOVED***;
PyAPI_FUNC(PyVarObject ****REMOVED*** _PyObject_GC_NewVar(PyTypeObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyObject_GC_Track(void ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyObject_GC_UnTrack(void ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyObject_GC_Del(void ****REMOVED***;

#define PyObject_GC_New(type, typeobj***REMOVED*** \
                ( (type ****REMOVED*** _PyObject_GC_New(typeobj***REMOVED*** ***REMOVED***
#define PyObject_GC_NewVar(type, typeobj, n***REMOVED*** \
                ( (type ****REMOVED*** _PyObject_GC_NewVar((typeobj***REMOVED***, (n***REMOVED******REMOVED*** ***REMOVED***


/* Utility macro to help write tp_traverse functions.
 * To use this macro, the tp_traverse function must name its arguments
 * "visit" and "arg".  This is intended to keep tp_traverse functions
 * looking as much alike as possible.
 */
#define Py_VISIT(op***REMOVED***                                                    \
    do {                                                                \
        if (op***REMOVED*** {                                                       \
            int vret = visit((PyObject ****REMOVED***(op***REMOVED***, arg***REMOVED***;                    \
            if (vret***REMOVED***                                                   \
                return vret;                                            \
    ***REMOVED***                                                               \
***REMOVED*** while (0***REMOVED***

/* This is here for the sake of backwards compatibility.  Extensions that
 * use the old GC API will still compile but the objects will not be
 * tracked by the GC. */
#define PyGC_HEAD_SIZE 0
#define PyObject_GC_Init(op***REMOVED***
#define PyObject_GC_Fini(op***REMOVED***
#define PyObject_AS_GC(op***REMOVED*** (op***REMOVED***
#define PyObject_FROM_GC(op***REMOVED*** (op***REMOVED***


/* Test if a type supports weak references */
#define PyType_SUPPORTS_WEAKREFS(t***REMOVED*** \
    (PyType_HasFeature((t***REMOVED***, Py_TPFLAGS_HAVE_WEAKREFS***REMOVED*** \
     && ((t***REMOVED***->tp_weaklistoffset > 0***REMOVED******REMOVED***

#define PyObject_GET_WEAKREFS_LISTPTR(o***REMOVED*** \
    ((PyObject *****REMOVED*** (((char ****REMOVED*** (o***REMOVED******REMOVED*** + Py_TYPE(o***REMOVED***->tp_weaklistoffset***REMOVED******REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_OBJIMPL_H */
