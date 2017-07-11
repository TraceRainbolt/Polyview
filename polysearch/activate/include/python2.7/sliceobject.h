#ifndef Py_SLICEOBJECT_H
#define Py_SLICEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/* The unique ellipsis object "..." */

PyAPI_DATA(PyObject***REMOVED*** _Py_EllipsisObject; /* Don't use this directly */

#define Py_Ellipsis (&_Py_EllipsisObject***REMOVED***

/* Slice object interface */

/*

A slice object containing start, stop, and step data members (the
names are from range***REMOVED***.  After much talk with Guido, it was decided to
let these be any arbitrary python type.  Py_None stands for omitted values.
*/

typedef struct {
    PyObject_HEAD
    PyObject *start, *stop, *step;	/* not NULL */
***REMOVED*** PySliceObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PySlice_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyEllipsis_Type;

#define PySlice_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PySlice_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PySlice_New(PyObject* start, PyObject* stop,
                                  PyObject* step***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PySlice_FromIndices(Py_ssize_t start, Py_ssize_t stop***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PySlice_GetIndices(PySliceObject *r, Py_ssize_t length,
                                  Py_ssize_t *start, Py_ssize_t *stop, Py_ssize_t *step***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PySlice_GetIndicesEx(PySliceObject *r, Py_ssize_t length,
				    Py_ssize_t *start, Py_ssize_t *stop, 
				    Py_ssize_t *step, Py_ssize_t *slicelength***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_SLICEOBJECT_H */
