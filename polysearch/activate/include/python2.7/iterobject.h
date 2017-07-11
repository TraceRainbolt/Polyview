#ifndef Py_ITEROBJECT_H
#define Py_ITEROBJECT_H
/* Iterators (the basic kind, over a sequence***REMOVED*** */
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject***REMOVED*** PySeqIter_Type;

#define PySeqIter_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PySeqIter_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PySeqIter_New(PyObject ****REMOVED***;

PyAPI_DATA(PyTypeObject***REMOVED*** PyCallIter_Type;

#define PyCallIter_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyCallIter_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyCallIter_New(PyObject *, PyObject ****REMOVED***;
#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_ITEROBJECT_H */

