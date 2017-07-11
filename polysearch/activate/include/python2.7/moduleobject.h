
/* Module object interface */

#ifndef Py_MODULEOBJECT_H
#define Py_MODULEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject***REMOVED*** PyModule_Type;

#define PyModule_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyModule_Type***REMOVED***
#define PyModule_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyModule_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyModule_New(const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyModule_GetDict(PyObject ****REMOVED***;
PyAPI_FUNC(char ****REMOVED*** PyModule_GetName(PyObject ****REMOVED***;
PyAPI_FUNC(char ****REMOVED*** PyModule_GetFilename(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyModule_Clear(PyObject ****REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_MODULEOBJECT_H */
