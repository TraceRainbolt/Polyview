
/* Buffer object interface */

/* Note: the object's structure is private */

#ifndef Py_BUFFEROBJECT_H
#define Py_BUFFEROBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


PyAPI_DATA(PyTypeObject***REMOVED*** PyBuffer_Type;

#define PyBuffer_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyBuffer_Type***REMOVED***

#define Py_END_OF_BUFFER	(-1***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyBuffer_FromObject(PyObject *base,
                                           Py_ssize_t offset, Py_ssize_t size***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyBuffer_FromReadWriteObject(PyObject *base,
                                                    Py_ssize_t offset,
                                                    Py_ssize_t size***REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyBuffer_FromMemory(void *ptr, Py_ssize_t size***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyBuffer_FromReadWriteMemory(void *ptr, Py_ssize_t size***REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyBuffer_New(Py_ssize_t size***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_BUFFEROBJECT_H */
