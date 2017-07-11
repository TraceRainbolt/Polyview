#ifndef Py_OBJECT_H
#define Py_OBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


/* Object and type object interface */

/*
Objects are structures allocated on the heap.  Special rules apply to
the use of objects to ensure they are properly garbage-collected.
Objects are never allocated statically or on the stack; they must be
accessed through special macros and functions only.  (Type objects are
exceptions to the first rule; the standard types are represented by
statically initialized type objects, although work on type/class unification
for Python 2.2 made it possible to have heap-allocated type objects too***REMOVED***.

An object has a 'reference count' that is increased or decreased when a
pointer to the object is copied or deleted; when the reference count
reaches zero there are no references to the object left and it can be
removed from the heap.

An object has a 'type' that determines what it represents and what kind
of data it contains.  An object's type is fixed when it is created.
Types themselves are represented as objects; an object contains a
pointer to the corresponding type object.  The type itself has a type
pointer pointing to the object representing the type 'type', which
contains a pointer to itself!***REMOVED***.

Objects do not float around in memory; once allocated an object keeps
the same size and address.  Objects that must hold variable-size data
can contain pointers to variable-size parts of the object.  Not all
objects of the same type have the same size; but the size cannot change
after allocation.  (These restrictions are made so a reference to an
object can be simply a pointer -- moving an object would require
updating all the pointers, and changing an object's size would require
moving it if there was another object right next to it.***REMOVED***

Objects are always accessed through pointers of the type 'PyObject *'.
The type 'PyObject' is a structure that only contains the reference count
and the type pointer.  The actual memory allocated for an object
contains other data that can only be accessed after casting the pointer
to a pointer to a longer structure type.  This longer type must start
with the reference count and type fields; the macro PyObject_HEAD should be
used for this (to accommodate for future changes***REMOVED***.  The implementation
of a particular object type can cast the object pointer to the proper
type and back.

A standard interface exists for objects that contain an array of items
whose size is determined when the object is allocated.
*/

/* Py_DEBUG implies Py_TRACE_REFS. */
#if defined(Py_DEBUG***REMOVED*** && !defined(Py_TRACE_REFS***REMOVED***
#define Py_TRACE_REFS
#endif

/* Py_TRACE_REFS implies Py_REF_DEBUG. */
#if defined(Py_TRACE_REFS***REMOVED*** && !defined(Py_REF_DEBUG***REMOVED***
#define Py_REF_DEBUG
#endif

#ifdef Py_TRACE_REFS
/* Define pointers to support a doubly-linked list of all live heap objects. */
#define _PyObject_HEAD_EXTRA            \
    struct _object *_ob_next;           \
    struct _object *_ob_prev;

#define _PyObject_EXTRA_INIT 0, 0,

#else
#define _PyObject_HEAD_EXTRA
#define _PyObject_EXTRA_INIT
#endif

/* PyObject_HEAD defines the initial segment of every PyObject. */
#define PyObject_HEAD                   \
    _PyObject_HEAD_EXTRA                \
    Py_ssize_t ob_refcnt;               \
    struct _typeobject *ob_type;

#define PyObject_HEAD_INIT(type***REMOVED***        \
    _PyObject_EXTRA_INIT                \
    1, type,

#define PyVarObject_HEAD_INIT(type, size***REMOVED***       \
    PyObject_HEAD_INIT(type***REMOVED*** size,

/* PyObject_VAR_HEAD defines the initial segment of all variable-size
 * container objects.  These end with a declaration of an array with 1
 * element, but enough space is malloc'ed so that the array actually
 * has room for ob_size elements.  Note that ob_size is an element count,
 * not necessarily a byte count.
 */
#define PyObject_VAR_HEAD               \
    PyObject_HEAD                       \
    Py_ssize_t ob_size; /* Number of items in variable part */
#define Py_INVALID_SIZE (Py_ssize_t***REMOVED***-1

/* Nothing is actually declared to be a PyObject, but every pointer to
 * a Python object can be cast to a PyObject*.  This is inheritance built
 * by hand.  Similarly every pointer to a variable-size Python object can,
 * in addition, be cast to PyVarObject*.
 */
typedef struct _object {
    PyObject_HEAD
***REMOVED*** PyObject;

typedef struct {
    PyObject_VAR_HEAD
***REMOVED*** PyVarObject;

#define Py_REFCNT(ob***REMOVED***           (((PyObject****REMOVED***(ob***REMOVED******REMOVED***->ob_refcnt***REMOVED***
#define Py_TYPE(ob***REMOVED***             (((PyObject****REMOVED***(ob***REMOVED******REMOVED***->ob_type***REMOVED***
#define Py_SIZE(ob***REMOVED***             (((PyVarObject****REMOVED***(ob***REMOVED******REMOVED***->ob_size***REMOVED***

/*
Type objects contain a string containing the type name (to help somewhat
in debugging***REMOVED***, the allocation parameters (see PyObject_New(***REMOVED*** and
PyObject_NewVar(***REMOVED******REMOVED***,
and methods for accessing objects of the type.  Methods are optional, a
nil pointer meaning that particular kind of access is not available for
this type.  The Py_DECREF(***REMOVED*** macro uses the tp_dealloc method without
checking for a nil pointer; it should always be implemented except if
the implementation can guarantee that the reference count will never
reach zero (e.g., for statically allocated type objects***REMOVED***.

NB: the methods for certain type groups are now contained in separate
method blocks.
*/

typedef PyObject * (*unaryfunc***REMOVED***(PyObject ****REMOVED***;
typedef PyObject * (*binaryfunc***REMOVED***(PyObject *, PyObject ****REMOVED***;
typedef PyObject * (*ternaryfunc***REMOVED***(PyObject *, PyObject *, PyObject ****REMOVED***;
typedef int (*inquiry***REMOVED***(PyObject ****REMOVED***;
typedef Py_ssize_t (*lenfunc***REMOVED***(PyObject ****REMOVED***;
typedef int (*coercion***REMOVED***(PyObject **, PyObject *****REMOVED***;
typedef PyObject *(*intargfunc***REMOVED***(PyObject *, int***REMOVED*** Py_DEPRECATED(2.5***REMOVED***;
typedef PyObject *(*intintargfunc***REMOVED***(PyObject *, int, int***REMOVED*** Py_DEPRECATED(2.5***REMOVED***;
typedef PyObject *(*ssizeargfunc***REMOVED***(PyObject *, Py_ssize_t***REMOVED***;
typedef PyObject *(*ssizessizeargfunc***REMOVED***(PyObject *, Py_ssize_t, Py_ssize_t***REMOVED***;
typedef int(*intobjargproc***REMOVED***(PyObject *, int, PyObject ****REMOVED***;
typedef int(*intintobjargproc***REMOVED***(PyObject *, int, int, PyObject ****REMOVED***;
typedef int(*ssizeobjargproc***REMOVED***(PyObject *, Py_ssize_t, PyObject ****REMOVED***;
typedef int(*ssizessizeobjargproc***REMOVED***(PyObject *, Py_ssize_t, Py_ssize_t, PyObject ****REMOVED***;
typedef int(*objobjargproc***REMOVED***(PyObject *, PyObject *, PyObject ****REMOVED***;



/* int-based buffer interface */
typedef int (*getreadbufferproc***REMOVED***(PyObject *, int, void *****REMOVED***;
typedef int (*getwritebufferproc***REMOVED***(PyObject *, int, void *****REMOVED***;
typedef int (*getsegcountproc***REMOVED***(PyObject *, int ****REMOVED***;
typedef int (*getcharbufferproc***REMOVED***(PyObject *, int, char *****REMOVED***;
/* ssize_t-based buffer interface */
typedef Py_ssize_t (*readbufferproc***REMOVED***(PyObject *, Py_ssize_t, void *****REMOVED***;
typedef Py_ssize_t (*writebufferproc***REMOVED***(PyObject *, Py_ssize_t, void *****REMOVED***;
typedef Py_ssize_t (*segcountproc***REMOVED***(PyObject *, Py_ssize_t ****REMOVED***;
typedef Py_ssize_t (*charbufferproc***REMOVED***(PyObject *, Py_ssize_t, char *****REMOVED***;


/* Py3k buffer interface */
typedef struct bufferinfo {
    void *buf;
    PyObject *obj;        /* owned reference */
    Py_ssize_t len;
    Py_ssize_t itemsize;  /* This is Py_ssize_t so it can be
                             pointed to by strides in simple case.*/
    int readonly;
    int ndim;
    char *format;
    Py_ssize_t *shape;
    Py_ssize_t *strides;
    Py_ssize_t *suboffsets;
    Py_ssize_t smalltable[2***REMOVED***;  /* static store for shape and strides of
                                  mono-dimensional buffers. */
    void *internal;
***REMOVED*** Py_buffer;

typedef int (*getbufferproc***REMOVED***(PyObject *, Py_buffer *, int***REMOVED***;
typedef void (*releasebufferproc***REMOVED***(PyObject *, Py_buffer ****REMOVED***;

    /* Flags for getting buffers */
#define PyBUF_SIMPLE 0
#define PyBUF_WRITABLE 0x0001
/*  we used to include an E, backwards compatible alias  */
#define PyBUF_WRITEABLE PyBUF_WRITABLE
#define PyBUF_FORMAT 0x0004
#define PyBUF_ND 0x0008
#define PyBUF_STRIDES (0x0010 | PyBUF_ND***REMOVED***
#define PyBUF_C_CONTIGUOUS (0x0020 | PyBUF_STRIDES***REMOVED***
#define PyBUF_F_CONTIGUOUS (0x0040 | PyBUF_STRIDES***REMOVED***
#define PyBUF_ANY_CONTIGUOUS (0x0080 | PyBUF_STRIDES***REMOVED***
#define PyBUF_INDIRECT (0x0100 | PyBUF_STRIDES***REMOVED***

#define PyBUF_CONTIG (PyBUF_ND | PyBUF_WRITABLE***REMOVED***
#define PyBUF_CONTIG_RO (PyBUF_ND***REMOVED***

#define PyBUF_STRIDED (PyBUF_STRIDES | PyBUF_WRITABLE***REMOVED***
#define PyBUF_STRIDED_RO (PyBUF_STRIDES***REMOVED***

#define PyBUF_RECORDS (PyBUF_STRIDES | PyBUF_WRITABLE | PyBUF_FORMAT***REMOVED***
#define PyBUF_RECORDS_RO (PyBUF_STRIDES | PyBUF_FORMAT***REMOVED***

#define PyBUF_FULL (PyBUF_INDIRECT | PyBUF_WRITABLE | PyBUF_FORMAT***REMOVED***
#define PyBUF_FULL_RO (PyBUF_INDIRECT | PyBUF_FORMAT***REMOVED***


#define PyBUF_READ  0x100
#define PyBUF_WRITE 0x200
#define PyBUF_SHADOW 0x400
/* end Py3k buffer interface */

typedef int (*objobjproc***REMOVED***(PyObject *, PyObject ****REMOVED***;
typedef int (*visitproc***REMOVED***(PyObject *, void ****REMOVED***;
typedef int (*traverseproc***REMOVED***(PyObject *, visitproc, void ****REMOVED***;

typedef struct {
    /* For numbers without flag bit Py_TPFLAGS_CHECKTYPES set, all
       arguments are guaranteed to be of the object's type (modulo
       coercion hacks -- i.e. if the type's coercion function
       returns other types, then these are allowed as well***REMOVED***.  Numbers that
       have the Py_TPFLAGS_CHECKTYPES flag bit set should check *both*
       arguments for proper type and implement the necessary conversions
       in the slot functions themselves. */

    binaryfunc nb_add;
    binaryfunc nb_subtract;
    binaryfunc nb_multiply;
    binaryfunc nb_divide;
    binaryfunc nb_remainder;
    binaryfunc nb_divmod;
    ternaryfunc nb_power;
    unaryfunc nb_negative;
    unaryfunc nb_positive;
    unaryfunc nb_absolute;
    inquiry nb_nonzero;
    unaryfunc nb_invert;
    binaryfunc nb_lshift;
    binaryfunc nb_rshift;
    binaryfunc nb_and;
    binaryfunc nb_xor;
    binaryfunc nb_or;
    coercion nb_coerce;
    unaryfunc nb_int;
    unaryfunc nb_long;
    unaryfunc nb_float;
    unaryfunc nb_oct;
    unaryfunc nb_hex;
    /* Added in release 2.0 */
    binaryfunc nb_inplace_add;
    binaryfunc nb_inplace_subtract;
    binaryfunc nb_inplace_multiply;
    binaryfunc nb_inplace_divide;
    binaryfunc nb_inplace_remainder;
    ternaryfunc nb_inplace_power;
    binaryfunc nb_inplace_lshift;
    binaryfunc nb_inplace_rshift;
    binaryfunc nb_inplace_and;
    binaryfunc nb_inplace_xor;
    binaryfunc nb_inplace_or;

    /* Added in release 2.2 */
    /* The following require the Py_TPFLAGS_HAVE_CLASS flag */
    binaryfunc nb_floor_divide;
    binaryfunc nb_true_divide;
    binaryfunc nb_inplace_floor_divide;
    binaryfunc nb_inplace_true_divide;

    /* Added in release 2.5 */
    unaryfunc nb_index;
***REMOVED*** PyNumberMethods;

typedef struct {
    lenfunc sq_length;
    binaryfunc sq_concat;
    ssizeargfunc sq_repeat;
    ssizeargfunc sq_item;
    ssizessizeargfunc sq_slice;
    ssizeobjargproc sq_ass_item;
    ssizessizeobjargproc sq_ass_slice;
    objobjproc sq_contains;
    /* Added in release 2.0 */
    binaryfunc sq_inplace_concat;
    ssizeargfunc sq_inplace_repeat;
***REMOVED*** PySequenceMethods;

typedef struct {
    lenfunc mp_length;
    binaryfunc mp_subscript;
    objobjargproc mp_ass_subscript;
***REMOVED*** PyMappingMethods;

typedef struct {
    readbufferproc bf_getreadbuffer;
    writebufferproc bf_getwritebuffer;
    segcountproc bf_getsegcount;
    charbufferproc bf_getcharbuffer;
    getbufferproc bf_getbuffer;
    releasebufferproc bf_releasebuffer;
***REMOVED*** PyBufferProcs;


typedef void (*freefunc***REMOVED***(void ****REMOVED***;
typedef void (*destructor***REMOVED***(PyObject ****REMOVED***;
typedef int (*printfunc***REMOVED***(PyObject *, FILE *, int***REMOVED***;
typedef PyObject *(*getattrfunc***REMOVED***(PyObject *, char ****REMOVED***;
typedef PyObject *(*getattrofunc***REMOVED***(PyObject *, PyObject ****REMOVED***;
typedef int (*setattrfunc***REMOVED***(PyObject *, char *, PyObject ****REMOVED***;
typedef int (*setattrofunc***REMOVED***(PyObject *, PyObject *, PyObject ****REMOVED***;
typedef int (*cmpfunc***REMOVED***(PyObject *, PyObject ****REMOVED***;
typedef PyObject *(*reprfunc***REMOVED***(PyObject ****REMOVED***;
typedef long (*hashfunc***REMOVED***(PyObject ****REMOVED***;
typedef PyObject *(*richcmpfunc***REMOVED*** (PyObject *, PyObject *, int***REMOVED***;
typedef PyObject *(*getiterfunc***REMOVED*** (PyObject ****REMOVED***;
typedef PyObject *(*iternextfunc***REMOVED*** (PyObject ****REMOVED***;
typedef PyObject *(*descrgetfunc***REMOVED*** (PyObject *, PyObject *, PyObject ****REMOVED***;
typedef int (*descrsetfunc***REMOVED*** (PyObject *, PyObject *, PyObject ****REMOVED***;
typedef int (*initproc***REMOVED***(PyObject *, PyObject *, PyObject ****REMOVED***;
typedef PyObject *(*newfunc***REMOVED***(struct _typeobject *, PyObject *, PyObject ****REMOVED***;
typedef PyObject *(*allocfunc***REMOVED***(struct _typeobject *, Py_ssize_t***REMOVED***;

typedef struct _typeobject {
    PyObject_VAR_HEAD
    const char *tp_name; /* For printing, in format "<module>.<name>" */
    Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */

    /* Methods to implement standard operations */

    destructor tp_dealloc;
    printfunc tp_print;
    getattrfunc tp_getattr;
    setattrfunc tp_setattr;
    cmpfunc tp_compare;
    reprfunc tp_repr;

    /* Method suites for standard classes */

    PyNumberMethods *tp_as_number;
    PySequenceMethods *tp_as_sequence;
    PyMappingMethods *tp_as_mapping;

    /* More standard operations (here for binary compatibility***REMOVED*** */

    hashfunc tp_hash;
    ternaryfunc tp_call;
    reprfunc tp_str;
    getattrofunc tp_getattro;
    setattrofunc tp_setattro;

    /* Functions to access object as input/output buffer */
    PyBufferProcs *tp_as_buffer;

    /* Flags to define presence of optional/expanded features */
    long tp_flags;

    const char *tp_doc; /* Documentation string */

    /* Assigned meaning in release 2.0 */
    /* call function for all accessible objects */
    traverseproc tp_traverse;

    /* delete references to contained objects */
    inquiry tp_clear;

    /* Assigned meaning in release 2.1 */
    /* rich comparisons */
    richcmpfunc tp_richcompare;

    /* weak reference enabler */
    Py_ssize_t tp_weaklistoffset;

    /* Added in release 2.2 */
    /* Iterators */
    getiterfunc tp_iter;
    iternextfunc tp_iternext;

    /* Attribute descriptor and subclassing stuff */
    struct PyMethodDef *tp_methods;
    struct PyMemberDef *tp_members;
    struct PyGetSetDef *tp_getset;
    struct _typeobject *tp_base;
    PyObject *tp_dict;
    descrgetfunc tp_descr_get;
    descrsetfunc tp_descr_set;
    Py_ssize_t tp_dictoffset;
    initproc tp_init;
    allocfunc tp_alloc;
    newfunc tp_new;
    freefunc tp_free; /* Low-level free-memory routine */
    inquiry tp_is_gc; /* For PyObject_IS_GC */
    PyObject *tp_bases;
    PyObject *tp_mro; /* method resolution order */
    PyObject *tp_cache;
    PyObject *tp_subclasses;
    PyObject *tp_weaklist;
    destructor tp_del;

    /* Type attribute cache version tag. Added in version 2.6 */
    unsigned int tp_version_tag;

#ifdef COUNT_ALLOCS
    /* these must be last and never explicitly initialized */
    Py_ssize_t tp_allocs;
    Py_ssize_t tp_frees;
    Py_ssize_t tp_maxalloc;
    struct _typeobject *tp_prev;
    struct _typeobject *tp_next;
#endif
***REMOVED*** PyTypeObject;


/* The *real* layout of a type object when allocated on the heap */
typedef struct _heaptypeobject {
    /* Note: there's a dependency on the order of these members
       in slotptr(***REMOVED*** in typeobject.c . */
    PyTypeObject ht_type;
    PyNumberMethods as_number;
    PyMappingMethods as_mapping;
    PySequenceMethods as_sequence; /* as_sequence comes after as_mapping,
                                      so that the mapping wins when both
                                      the mapping and the sequence define
                                      a given operator (e.g. __getitem__***REMOVED***.
                                      see add_operators(***REMOVED*** in typeobject.c . */
    PyBufferProcs as_buffer;
    PyObject *ht_name, *ht_slots;
    /* here are optional user slots, followed by the members. */
***REMOVED*** PyHeapTypeObject;

/* access macro to the members which are floating "behind" the object */
#define PyHeapType_GET_MEMBERS(etype***REMOVED*** \
    ((PyMemberDef ****REMOVED***(((char ****REMOVED***etype***REMOVED*** + Py_TYPE(etype***REMOVED***->tp_basicsize***REMOVED******REMOVED***


/* Generic type check */
PyAPI_FUNC(int***REMOVED*** PyType_IsSubtype(PyTypeObject *, PyTypeObject ****REMOVED***;
#define PyObject_TypeCheck(ob, tp***REMOVED*** \
    (Py_TYPE(ob***REMOVED*** == (tp***REMOVED*** || PyType_IsSubtype(Py_TYPE(ob***REMOVED***, (tp***REMOVED******REMOVED******REMOVED***

PyAPI_DATA(PyTypeObject***REMOVED*** PyType_Type; /* built-in 'type' */
PyAPI_DATA(PyTypeObject***REMOVED*** PyBaseObject_Type; /* built-in 'object' */
PyAPI_DATA(PyTypeObject***REMOVED*** PySuper_Type; /* built-in 'super' */

#define PyType_Check(op***REMOVED*** \
    PyType_FastSubclass(Py_TYPE(op***REMOVED***, Py_TPFLAGS_TYPE_SUBCLASS***REMOVED***
#define PyType_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyType_Type***REMOVED***

PyAPI_FUNC(int***REMOVED*** PyType_Ready(PyTypeObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyType_GenericAlloc(PyTypeObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyType_GenericNew(PyTypeObject *,
                                               PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyType_Lookup(PyTypeObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyObject_LookupSpecial(PyObject *, char *, PyObject *****REMOVED***;
PyAPI_FUNC(unsigned int***REMOVED*** PyType_ClearCache(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyType_Modified(PyTypeObject ****REMOVED***;

/* Generic operations on objects */
PyAPI_FUNC(int***REMOVED*** PyObject_Print(PyObject *, FILE *, int***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyObject_Dump(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_Repr(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyObject_Str(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_Str(PyObject ****REMOVED***;
#define PyObject_Bytes PyObject_Str
#ifdef Py_USING_UNICODE
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_Unicode(PyObject ****REMOVED***;
#endif
PyAPI_FUNC(int***REMOVED*** PyObject_Compare(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_RichCompare(PyObject *, PyObject *, int***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_RichCompareBool(PyObject *, PyObject *, int***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_GetAttrString(PyObject *, const char ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_SetAttrString(PyObject *, const char *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_HasAttrString(PyObject *, const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_GetAttr(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_SetAttr(PyObject *, PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_HasAttr(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject *****REMOVED*** _PyObject_GetDictPtr(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_SelfIter(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyObject_NextNotImplemented(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_GenericGetAttr(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_GenericSetAttr(PyObject *,
                                              PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyObject_Hash(PyObject ****REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyObject_HashNotImplemented(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_IsTrue(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_Not(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyCallable_Check(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyNumber_Coerce(PyObject **, PyObject *****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyNumber_CoerceEx(PyObject **, PyObject *****REMOVED***;

PyAPI_FUNC(void***REMOVED*** PyObject_ClearWeakRefs(PyObject ****REMOVED***;

/* A slot function whose address we need to compare */
extern int _PyObject_SlotCompare(PyObject *, PyObject ****REMOVED***;
/* Same as PyObject_Generic{Get,Set***REMOVED***Attr, but passing the attributes
   dict as the last parameter. */
PyAPI_FUNC(PyObject ****REMOVED***
_PyObject_GenericGetAttrWithDict(PyObject *, PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED***
_PyObject_GenericSetAttrWithDict(PyObject *, PyObject *,
                                 PyObject *, PyObject ****REMOVED***;


/* PyObject_Dir(obj***REMOVED*** acts like Python __builtin__.dir(obj***REMOVED***, returning a
   list of strings.  PyObject_Dir(NULL***REMOVED*** is like __builtin__.dir(***REMOVED***,
   returning the names of the current locals.  In this case, if there are
   no current locals, NULL is returned, and PyErr_Occurred(***REMOVED*** is false.
*/
PyAPI_FUNC(PyObject ****REMOVED*** PyObject_Dir(PyObject ****REMOVED***;


/* Helpers for printing recursive container types */
PyAPI_FUNC(int***REMOVED*** Py_ReprEnter(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** Py_ReprLeave(PyObject ****REMOVED***;

/* Helpers for hash functions */
PyAPI_FUNC(long***REMOVED*** _Py_HashDouble(double***REMOVED***;
PyAPI_FUNC(long***REMOVED*** _Py_HashPointer(void****REMOVED***;

typedef struct {
    long prefix;
    long suffix;
***REMOVED*** _Py_HashSecret_t;
PyAPI_DATA(_Py_HashSecret_t***REMOVED*** _Py_HashSecret;

#ifdef Py_DEBUG
PyAPI_DATA(int***REMOVED*** _Py_HashSecret_Initialized;
#endif

/* Helper for passing objects to printf and the like */
#define PyObject_REPR(obj***REMOVED*** PyString_AS_STRING(PyObject_Repr(obj***REMOVED******REMOVED***

/* Flag bits for printing: */
#define Py_PRINT_RAW    1       /* No string quotes etc. */

/*
`Type flags (tp_flags***REMOVED***

These flags are used to extend the type structure in a backwards-compatible
fashion. Extensions can use the flags to indicate (and test***REMOVED*** when a given
type structure contains a new feature. The Python core will use these when
introducing new functionality between major revisions (to avoid mid-version
changes in the PYTHON_API_VERSION***REMOVED***.

Arbitration of the flag bit positions will need to be coordinated among
all extension writers who publically release their extensions (this will
be fewer than you might expect!***REMOVED***..

Python 1.5.2 introduced the bf_getcharbuffer slot into PyBufferProcs.

Type definitions should use Py_TPFLAGS_DEFAULT for their tp_flags value.

Code can use PyType_HasFeature(type_ob, flag_value***REMOVED*** to test whether the
given type object has a specified feature.

NOTE: when building the core, Py_TPFLAGS_DEFAULT includes
Py_TPFLAGS_HAVE_VERSION_TAG; outside the core, it doesn't.  This is so
that extensions that modify tp_dict of their own types directly don't
break, since this was allowed in 2.5.  In 3.0 they will have to
manually remove this flag though!
*/

/* PyBufferProcs contains bf_getcharbuffer */
#define Py_TPFLAGS_HAVE_GETCHARBUFFER  (1L<<0***REMOVED***

/* PySequenceMethods contains sq_contains */
#define Py_TPFLAGS_HAVE_SEQUENCE_IN (1L<<1***REMOVED***

/* This is here for backwards compatibility.  Extensions that use the old GC
 * API will still compile but the objects will not be tracked by the GC. */
#define Py_TPFLAGS_GC 0 /* used to be (1L<<2***REMOVED*** */

/* PySequenceMethods and PyNumberMethods contain in-place operators */
#define Py_TPFLAGS_HAVE_INPLACEOPS (1L<<3***REMOVED***

/* PyNumberMethods do their own coercion */
#define Py_TPFLAGS_CHECKTYPES (1L<<4***REMOVED***

/* tp_richcompare is defined */
#define Py_TPFLAGS_HAVE_RICHCOMPARE (1L<<5***REMOVED***

/* Objects which are weakly referencable if their tp_weaklistoffset is >0 */
#define Py_TPFLAGS_HAVE_WEAKREFS (1L<<6***REMOVED***

/* tp_iter is defined */
#define Py_TPFLAGS_HAVE_ITER (1L<<7***REMOVED***

/* New members introduced by Python 2.2 exist */
#define Py_TPFLAGS_HAVE_CLASS (1L<<8***REMOVED***

/* Set if the type object is dynamically allocated */
#define Py_TPFLAGS_HEAPTYPE (1L<<9***REMOVED***

/* Set if the type allows subclassing */
#define Py_TPFLAGS_BASETYPE (1L<<10***REMOVED***

/* Set if the type is 'ready' -- fully initialized */
#define Py_TPFLAGS_READY (1L<<12***REMOVED***

/* Set while the type is being 'readied', to prevent recursive ready calls */
#define Py_TPFLAGS_READYING (1L<<13***REMOVED***

/* Objects support garbage collection (see objimp.h***REMOVED*** */
#define Py_TPFLAGS_HAVE_GC (1L<<14***REMOVED***

/* These two bits are preserved for Stackless Python, next after this is 17 */
#ifdef STACKLESS
#define Py_TPFLAGS_HAVE_STACKLESS_EXTENSION (3L<<15***REMOVED***
#else
#define Py_TPFLAGS_HAVE_STACKLESS_EXTENSION 0
#endif

/* Objects support nb_index in PyNumberMethods */
#define Py_TPFLAGS_HAVE_INDEX (1L<<17***REMOVED***

/* Objects support type attribute cache */
#define Py_TPFLAGS_HAVE_VERSION_TAG   (1L<<18***REMOVED***
#define Py_TPFLAGS_VALID_VERSION_TAG  (1L<<19***REMOVED***

/* Type is abstract and cannot be instantiated */
#define Py_TPFLAGS_IS_ABSTRACT (1L<<20***REMOVED***

/* Has the new buffer protocol */
#define Py_TPFLAGS_HAVE_NEWBUFFER (1L<<21***REMOVED***

/* These flags are used to determine if a type is a subclass. */
#define Py_TPFLAGS_INT_SUBCLASS         (1L<<23***REMOVED***
#define Py_TPFLAGS_LONG_SUBCLASS        (1L<<24***REMOVED***
#define Py_TPFLAGS_LIST_SUBCLASS        (1L<<25***REMOVED***
#define Py_TPFLAGS_TUPLE_SUBCLASS       (1L<<26***REMOVED***
#define Py_TPFLAGS_STRING_SUBCLASS      (1L<<27***REMOVED***
#define Py_TPFLAGS_UNICODE_SUBCLASS     (1L<<28***REMOVED***
#define Py_TPFLAGS_DICT_SUBCLASS        (1L<<29***REMOVED***
#define Py_TPFLAGS_BASE_EXC_SUBCLASS    (1L<<30***REMOVED***
#define Py_TPFLAGS_TYPE_SUBCLASS        (1L<<31***REMOVED***

#define Py_TPFLAGS_DEFAULT_EXTERNAL ( \
                 Py_TPFLAGS_HAVE_GETCHARBUFFER | \
                 Py_TPFLAGS_HAVE_SEQUENCE_IN | \
                 Py_TPFLAGS_HAVE_INPLACEOPS | \
                 Py_TPFLAGS_HAVE_RICHCOMPARE | \
                 Py_TPFLAGS_HAVE_WEAKREFS | \
                 Py_TPFLAGS_HAVE_ITER | \
                 Py_TPFLAGS_HAVE_CLASS | \
                 Py_TPFLAGS_HAVE_STACKLESS_EXTENSION | \
                 Py_TPFLAGS_HAVE_INDEX | \
                 0***REMOVED***
#define Py_TPFLAGS_DEFAULT_CORE (Py_TPFLAGS_DEFAULT_EXTERNAL | \
                 Py_TPFLAGS_HAVE_VERSION_TAG***REMOVED***

#ifdef Py_BUILD_CORE
#define Py_TPFLAGS_DEFAULT Py_TPFLAGS_DEFAULT_CORE
#else
#define Py_TPFLAGS_DEFAULT Py_TPFLAGS_DEFAULT_EXTERNAL
#endif

#define PyType_HasFeature(t,f***REMOVED***  (((t***REMOVED***->tp_flags & (f***REMOVED******REMOVED*** != 0***REMOVED***
#define PyType_FastSubclass(t,f***REMOVED***  PyType_HasFeature(t,f***REMOVED***


/*
The macros Py_INCREF(op***REMOVED*** and Py_DECREF(op***REMOVED*** are used to increment or decrement
reference counts.  Py_DECREF calls the object's deallocator function when
the refcount falls to 0; for
objects that don't contain references to other objects or heap memory
this can be the standard function free(***REMOVED***.  Both macros can be used
wherever a void expression is allowed.  The argument must not be a
NULL pointer.  If it may be NULL, use Py_XINCREF/Py_XDECREF instead.
The macro _Py_NewReference(op***REMOVED*** initialize reference counts to 1, and
in special builds (Py_REF_DEBUG, Py_TRACE_REFS***REMOVED*** performs additional
bookkeeping appropriate to the special build.

We assume that the reference count field can never overflow; this can
be proven when the size of the field is the same as the pointer size, so
we ignore the possibility.  Provided a C int is at least 32 bits (which
is implicitly assumed in many parts of this code***REMOVED***, that's enough for
about 2**31 references to an object.

XXX The following became out of date in Python 2.2, but I'm not sure
XXX what the full truth is now.  Certainly, heap-allocated type objects
XXX can and should be deallocated.
Type objects should never be deallocated; the type pointer in an object
is not considered to be a reference to the type object, to save
complications in the deallocation function.  (This is actually a
decision that's up to the implementer of each new type so if you want,
you can count such references to the type object.***REMOVED***

*** WARNING*** The Py_DECREF macro must have a side-effect-free argument
since it may evaluate its argument multiple times.  (The alternative
would be to mace it a proper function or assign it to a global temporary
variable first, both of which are slower; and in a multi-threaded
environment the global variable trick is not safe.***REMOVED***
*/

/* First define a pile of simple helper macros, one set per special
 * build symbol.  These either expand to the obvious things, or to
 * nothing at all when the special mode isn't in effect.  The main
 * macros can later be defined just once then, yet expand to different
 * things depending on which special build options are and aren't in effect.
 * Trust me <wink>:  while painful, this is 20x easier to understand than,
 * e.g, defining _Py_NewReference five different times in a maze of nested
 * #ifdefs (we used to do that -- it was impenetrable***REMOVED***.
 */
#ifdef Py_REF_DEBUG
PyAPI_DATA(Py_ssize_t***REMOVED*** _Py_RefTotal;
PyAPI_FUNC(void***REMOVED*** _Py_NegativeRefcount(const char *fname,
                                            int lineno, PyObject *op***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyDict_Dummy(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PySet_Dummy(void***REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** _Py_GetRefTotal(void***REMOVED***;
#define _Py_INC_REFTOTAL        _Py_RefTotal++
#define _Py_DEC_REFTOTAL        _Py_RefTotal--
#define _Py_REF_DEBUG_COMMA     ,
#define _Py_CHECK_REFCNT(OP***REMOVED***                                    \
{       if (((PyObject****REMOVED***OP***REMOVED***->ob_refcnt < 0***REMOVED***                             \
                _Py_NegativeRefcount(__FILE__, __LINE__,        \
                                     (PyObject ****REMOVED***(OP***REMOVED******REMOVED***;         \
***REMOVED***
#else
#define _Py_INC_REFTOTAL
#define _Py_DEC_REFTOTAL
#define _Py_REF_DEBUG_COMMA
#define _Py_CHECK_REFCNT(OP***REMOVED***    /* a semicolon */;
#endif /* Py_REF_DEBUG */

#ifdef COUNT_ALLOCS
PyAPI_FUNC(void***REMOVED*** inc_count(PyTypeObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** dec_count(PyTypeObject ****REMOVED***;
#define _Py_INC_TPALLOCS(OP***REMOVED***    inc_count(Py_TYPE(OP***REMOVED******REMOVED***
#define _Py_INC_TPFREES(OP***REMOVED***     dec_count(Py_TYPE(OP***REMOVED******REMOVED***
#define _Py_DEC_TPFREES(OP***REMOVED***     Py_TYPE(OP***REMOVED***->tp_frees--
#define _Py_COUNT_ALLOCS_COMMA  ,
#else
#define _Py_INC_TPALLOCS(OP***REMOVED***
#define _Py_INC_TPFREES(OP***REMOVED***
#define _Py_DEC_TPFREES(OP***REMOVED***
#define _Py_COUNT_ALLOCS_COMMA
#endif /* COUNT_ALLOCS */

#ifdef Py_TRACE_REFS
/* Py_TRACE_REFS is such major surgery that we call external routines. */
PyAPI_FUNC(void***REMOVED*** _Py_NewReference(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _Py_ForgetReference(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _Py_Dealloc(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _Py_PrintReferences(FILE ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _Py_PrintReferenceAddresses(FILE ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _Py_AddToAllObjects(PyObject *, int force***REMOVED***;

#else
/* Without Py_TRACE_REFS, there's little enough to do that we expand code
 * inline.
 */
#define _Py_NewReference(op***REMOVED*** (                          \
    _Py_INC_TPALLOCS(op***REMOVED*** _Py_COUNT_ALLOCS_COMMA         \
    _Py_INC_REFTOTAL  _Py_REF_DEBUG_COMMA               \
    Py_REFCNT(op***REMOVED*** = 1***REMOVED***

#define _Py_ForgetReference(op***REMOVED*** _Py_INC_TPFREES(op***REMOVED***

#define _Py_Dealloc(op***REMOVED*** (                               \
    _Py_INC_TPFREES(op***REMOVED*** _Py_COUNT_ALLOCS_COMMA          \
    (*Py_TYPE(op***REMOVED***->tp_dealloc***REMOVED***((PyObject ****REMOVED***(op***REMOVED******REMOVED******REMOVED***
#endif /* !Py_TRACE_REFS */

#define Py_INCREF(op***REMOVED*** (                         \
    _Py_INC_REFTOTAL  _Py_REF_DEBUG_COMMA       \
    ((PyObject****REMOVED***(op***REMOVED******REMOVED***->ob_refcnt++***REMOVED***

#define Py_DECREF(op***REMOVED***                                   \
    do {                                                \
        if (_Py_DEC_REFTOTAL  _Py_REF_DEBUG_COMMA       \
        --((PyObject****REMOVED***(op***REMOVED******REMOVED***->ob_refcnt != 0***REMOVED***            \
            _Py_CHECK_REFCNT(op***REMOVED***                        \
        else                                            \
        _Py_Dealloc((PyObject ****REMOVED***(op***REMOVED******REMOVED***;                  \
***REMOVED*** while (0***REMOVED***

/* Safely decref `op` and set `op` to NULL, especially useful in tp_clear
 * and tp_dealloc implementatons.
 *
 * Note that "the obvious" code can be deadly:
 *
 *     Py_XDECREF(op***REMOVED***;
 *     op = NULL;
 *
 * Typically, `op` is something like self->containee, and `self` is done
 * using its `containee` member.  In the code sequence above, suppose
 * `containee` is non-NULL with a refcount of 1.  Its refcount falls to
 * 0 on the first line, which can trigger an arbitrary amount of code,
 * possibly including finalizers (like __del__ methods or weakref callbacks***REMOVED***
 * coded in Python, which in turn can release the GIL and allow other threads
 * to run, etc.  Such code may even invoke methods of `self` again, or cause
 * cyclic gc to trigger, but-- oops! --self->containee still points to the
 * object being torn down, and it may be in an insane state while being torn
 * down.  This has in fact been a rich historic source of miserable (rare &
 * hard-to-diagnose***REMOVED*** segfaulting (and other***REMOVED*** bugs.
 *
 * The safe way is:
 *
 *      Py_CLEAR(op***REMOVED***;
 *
 * That arranges to set `op` to NULL _before_ decref'ing, so that any code
 * triggered as a side-effect of `op` getting torn down no longer believes
 * `op` points to a valid object.
 *
 * There are cases where it's safe to use the naive code, but they're brittle.
 * For example, if `op` points to a Python integer, you know that destroying
 * one of those can't cause problems -- but in part that relies on that
 * Python integers aren't currently weakly referencable.  Best practice is
 * to use Py_CLEAR(***REMOVED*** even if you can't think of a reason for why you need to.
 */
#define Py_CLEAR(op***REMOVED***                            \
    do {                                        \
        if (op***REMOVED*** {                               \
            PyObject *_py_tmp = (PyObject ****REMOVED***(op***REMOVED***;               \
            (op***REMOVED*** = NULL;                        \
            Py_DECREF(_py_tmp***REMOVED***;                 \
    ***REMOVED***                                       \
***REMOVED*** while (0***REMOVED***

/* Macros to use in case the object pointer may be NULL: */
#define Py_XINCREF(op***REMOVED*** do { if ((op***REMOVED*** == NULL***REMOVED*** ; else Py_INCREF(op***REMOVED***; ***REMOVED*** while (0***REMOVED***
#define Py_XDECREF(op***REMOVED*** do { if ((op***REMOVED*** == NULL***REMOVED*** ; else Py_DECREF(op***REMOVED***; ***REMOVED*** while (0***REMOVED***

/*
These are provided as conveniences to Python runtime embedders, so that
they can have object code that is not dependent on Python compilation flags.
*/
PyAPI_FUNC(void***REMOVED*** Py_IncRef(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** Py_DecRef(PyObject ****REMOVED***;

/*
_Py_NoneStruct is an object of undefined type which can be used in contexts
where NULL (nil***REMOVED*** is not suitable (since NULL often means 'error'***REMOVED***.

Don't forget to apply Py_INCREF(***REMOVED*** when returning this value!!!
*/
PyAPI_DATA(PyObject***REMOVED*** _Py_NoneStruct; /* Don't use this directly */
#define Py_None (&_Py_NoneStruct***REMOVED***

/* Macro for returning Py_None from a function */
#define Py_RETURN_NONE return Py_INCREF(Py_None***REMOVED***, Py_None

/*
Py_NotImplemented is a singleton used to signal that an operation is
not implemented for a given type combination.
*/
PyAPI_DATA(PyObject***REMOVED*** _Py_NotImplementedStruct; /* Don't use this directly */
#define Py_NotImplemented (&_Py_NotImplementedStruct***REMOVED***

/* Rich comparison opcodes */
#define Py_LT 0
#define Py_LE 1
#define Py_EQ 2
#define Py_NE 3
#define Py_GT 4
#define Py_GE 5

/* Maps Py_LT to Py_GT, ..., Py_GE to Py_LE.
 * Defined in object.c.
 */
PyAPI_DATA(int***REMOVED*** _Py_SwappedOp[***REMOVED***;

/*
Define staticforward and statichere for source compatibility with old
C extensions.

The staticforward define was needed to support certain broken C
compilers (notably SCO ODT 3.0, perhaps early AIX as well***REMOVED*** botched the
static keyword when it was used with a forward declaration of a static
initialized structure.  Standard C allows the forward declaration with
static, and we've decided to stop catering to broken C compilers.
(In fact, we expect that the compilers are all fixed eight years later.***REMOVED***
*/

#define staticforward static
#define statichere static


/*
More conventions
================

Argument Checking
-----------------

Functions that take objects as arguments normally don't check for nil
arguments, but they do check the type of the argument, and return an
error if the function doesn't apply to the type.

Failure Modes
-------------

Functions may fail for a variety of reasons, including running out of
memory.  This is communicated to the caller in two ways: an error string
is set (see errors.h***REMOVED***, and the function result differs: functions that
normally return a pointer return NULL for failure, functions returning
an integer return -1 (which could be a legal return value too!***REMOVED***, and
other functions return 0 for success and -1 for failure.
Callers should always check for errors before using the result.  If
an error was set, the caller must either explicitly clear it, or pass
the error on to its caller.

Reference Counts
----------------

It takes a while to get used to the proper usage of reference counts.

Functions that create an object set the reference count to 1; such new
objects must be stored somewhere or destroyed again with Py_DECREF(***REMOVED***.
Some functions that 'store' objects, such as PyTuple_SetItem(***REMOVED*** and
PyList_SetItem(***REMOVED***,
don't increment the reference count of the object, since the most
frequent use is to store a fresh object.  Functions that 'retrieve'
objects, such as PyTuple_GetItem(***REMOVED*** and PyDict_GetItemString(***REMOVED***, also
don't increment
the reference count, since most frequently the object is only looked at
quickly.  Thus, to retrieve an object and store it again, the caller
must call Py_INCREF(***REMOVED*** explicitly.

NOTE: functions that 'consume' a reference count, like
PyList_SetItem(***REMOVED***, consume the reference even if the object wasn't
successfully stored, to simplify error handling.

It seems attractive to make other functions that take an object as
argument consume a reference count; however, this may quickly get
confusing (even the current practice is already confusing***REMOVED***.  Consider
it carefully, it may save lots of calls to Py_INCREF(***REMOVED*** and Py_DECREF(***REMOVED*** at
times.
*/


/* Trashcan mechanism, thanks to Christian Tismer.

When deallocating a container object, it's possible to trigger an unbounded
chain of deallocations, as each Py_DECREF in turn drops the refcount on "the
next" object in the chain to 0.  This can easily lead to stack faults, and
especially in threads (which typically have less stack space to work with***REMOVED***.

A container object that participates in cyclic gc can avoid this by
bracketing the body of its tp_dealloc function with a pair of macros:

static void
mytype_dealloc(mytype *p***REMOVED***
{
    ... declarations go here ...

    PyObject_GC_UnTrack(p***REMOVED***;        // must untrack first
    Py_TRASHCAN_SAFE_BEGIN(p***REMOVED***
    ... The body of the deallocator goes here, including all calls ...
    ... to Py_DECREF on contained objects.                         ...
    Py_TRASHCAN_SAFE_END(p***REMOVED***
***REMOVED***

CAUTION:  Never return from the middle of the body!  If the body needs to
"get out early", put a label immediately before the Py_TRASHCAN_SAFE_END
call, and goto it.  Else the call-depth counter (see below***REMOVED*** will stay
above 0 forever, and the trashcan will never get emptied.

How it works:  The BEGIN macro increments a call-depth counter.  So long
as this counter is small, the body of the deallocator is run directly without
further ado.  But if the counter gets large, it instead adds p to a list of
objects to be deallocated later, skips the body of the deallocator, and
resumes execution after the END macro.  The tp_dealloc routine then returns
without deallocating anything (and so unbounded call-stack depth is avoided***REMOVED***.

When the call stack finishes unwinding again, code generated by the END macro
notices this, and calls another routine to deallocate all the objects that
may have been added to the list of deferred deallocations.  In effect, a
chain of N deallocations is broken into N / PyTrash_UNWIND_LEVEL pieces,
with the call stack never exceeding a depth of PyTrash_UNWIND_LEVEL.
*/

/* This is the old private API, invoked by the macros before 2.7.4.
   Kept for binary compatibility of extensions. */
PyAPI_FUNC(void***REMOVED*** _PyTrash_deposit_object(PyObject****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyTrash_destroy_chain(void***REMOVED***;
PyAPI_DATA(int***REMOVED*** _PyTrash_delete_nesting;
PyAPI_DATA(PyObject ****REMOVED*** _PyTrash_delete_later;

/* The new thread-safe private API, invoked by the macros below. */
PyAPI_FUNC(void***REMOVED*** _PyTrash_thread_deposit_object(PyObject****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyTrash_thread_destroy_chain(void***REMOVED***;

#define PyTrash_UNWIND_LEVEL 50

/* Note the workaround for when the thread state is NULL (issue #17703***REMOVED*** */
#define Py_TRASHCAN_SAFE_BEGIN(op***REMOVED*** \
    do { \
        PyThreadState *_tstate = PyThreadState_GET(***REMOVED***; \
        if (!_tstate || \
            _tstate->trash_delete_nesting < PyTrash_UNWIND_LEVEL***REMOVED*** { \
            if (_tstate***REMOVED*** \
                ++_tstate->trash_delete_nesting;
            /* The body of the deallocator is here. */
#define Py_TRASHCAN_SAFE_END(op***REMOVED*** \
            if (_tstate***REMOVED*** { \
                --_tstate->trash_delete_nesting; \
                if (_tstate->trash_delete_later \
                    && _tstate->trash_delete_nesting <= 0***REMOVED*** \
                    _PyTrash_thread_destroy_chain(***REMOVED***; \
        ***REMOVED*** \
    ***REMOVED*** \
        else \
            _PyTrash_thread_deposit_object((PyObject****REMOVED***op***REMOVED***; \
***REMOVED*** while (0***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_OBJECT_H */
