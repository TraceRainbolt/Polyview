
/* List object interface */

/*
Another generally useful object type is an list of object pointers.
This is a mutable type: the list items can be changed, and items can be
added or removed.  Out-of-range indices or non-list objects are ignored.

*** WARNING *** PyList_SetItem does not increment the new item's reference
count, but does decrement the reference count of the item it replaces,
if not nil.  It does *decrement* the reference count if it is *not*
inserted in the list.  Similarly, PyList_GetItem does not increment the
returned item's reference count.
*/

#ifndef Py_LISTOBJECT_H
#define Py_LISTOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    PyObject_VAR_HEAD
    /* Vector of pointers to list elements.  list[0***REMOVED*** is ob_item[0***REMOVED***, etc. */
    PyObject **ob_item;

    /* ob_item contains space for 'allocated' elements.  The number
     * currently in use is ob_size.
     * Invariants:
     *     0 <= ob_size <= allocated
     *     len(list***REMOVED*** == ob_size
     *     ob_item == NULL implies ob_size == allocated == 0
     * list.sort(***REMOVED*** temporarily sets allocated to -1 to detect mutations.
     *
     * Items must normally not be NULL, except during construction when
     * the list is not yet visible outside the function that builds it.
     */
    Py_ssize_t allocated;
***REMOVED*** PyListObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyList_Type;

#define PyList_Check(op***REMOVED*** \
		PyType_FastSubclass(Py_TYPE(op***REMOVED***, Py_TPFLAGS_LIST_SUBCLASS***REMOVED***
#define PyList_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyList_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyList_New(Py_ssize_t size***REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyList_Size(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyList_GetItem(PyObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyList_SetItem(PyObject *, Py_ssize_t, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyList_Insert(PyObject *, Py_ssize_t, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyList_Append(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyList_GetSlice(PyObject *, Py_ssize_t, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyList_SetSlice(PyObject *, Py_ssize_t, Py_ssize_t, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyList_Sort(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyList_Reverse(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyList_AsTuple(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyList_Extend(PyListObject *, PyObject ****REMOVED***;

/* Macro, trading safety for speed */
#define PyList_GET_ITEM(op, i***REMOVED*** (((PyListObject ****REMOVED***(op***REMOVED******REMOVED***->ob_item[i***REMOVED******REMOVED***
#define PyList_SET_ITEM(op, i, v***REMOVED*** (((PyListObject ****REMOVED***(op***REMOVED******REMOVED***->ob_item[i***REMOVED*** = (v***REMOVED******REMOVED***
#define PyList_GET_SIZE(op***REMOVED***    Py_SIZE(op***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_LISTOBJECT_H */
