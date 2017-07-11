
/* Tuple object interface */

#ifndef Py_TUPLEOBJECT_H
#define Py_TUPLEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/*
Another generally useful object type is a tuple of object pointers.
For Python, this is an immutable type.  C code can change the tuple items
(but not their number***REMOVED***, and even use tuples are general-purpose arrays of
object references, but in general only brand new tuples should be mutated,
not ones that might already have been exposed to Python code.

*** WARNING *** PyTuple_SetItem does not increment the new item's reference
count, but does decrement the reference count of the item it replaces,
if not nil.  It does *decrement* the reference count if it is *not*
inserted in the tuple.  Similarly, PyTuple_GetItem does not increment the
returned item's reference count.
*/

typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1***REMOVED***;

    /* ob_item contains space for 'ob_size' elements.
     * Items must normally not be NULL, except during construction when
     * the tuple is not yet visible outside the function that builds it.
     */
***REMOVED*** PyTupleObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyTuple_Type;

#define PyTuple_Check(op***REMOVED*** \
                 PyType_FastSubclass(Py_TYPE(op***REMOVED***, Py_TPFLAGS_TUPLE_SUBCLASS***REMOVED***
#define PyTuple_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyTuple_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyTuple_New(Py_ssize_t size***REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyTuple_Size(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyTuple_GetItem(PyObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyTuple_SetItem(PyObject *, Py_ssize_t, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyTuple_GetSlice(PyObject *, Py_ssize_t, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyTuple_Resize(PyObject **, Py_ssize_t***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyTuple_Pack(Py_ssize_t, ...***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyTuple_MaybeUntrack(PyObject ****REMOVED***;

/* Macro, trading safety for speed */
#define PyTuple_GET_ITEM(op, i***REMOVED*** (((PyTupleObject ****REMOVED***(op***REMOVED******REMOVED***->ob_item[i***REMOVED******REMOVED***
#define PyTuple_GET_SIZE(op***REMOVED***    Py_SIZE(op***REMOVED***

/* Macro, *only* to be used to fill in brand new tuples */
#define PyTuple_SET_ITEM(op, i, v***REMOVED*** (((PyTupleObject ****REMOVED***(op***REMOVED******REMOVED***->ob_item[i***REMOVED*** = v***REMOVED***

PyAPI_FUNC(int***REMOVED*** PyTuple_ClearFreeList(void***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_TUPLEOBJECT_H */
