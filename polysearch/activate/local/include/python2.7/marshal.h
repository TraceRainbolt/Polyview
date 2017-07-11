
/* Interface for marshal.c */

#ifndef Py_MARSHAL_H
#define Py_MARSHAL_H
#ifdef __cplusplus
extern "C" {
#endif

#define Py_MARSHAL_VERSION 2

PyAPI_FUNC(void***REMOVED*** PyMarshal_WriteLongToFile(long, FILE *, int***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyMarshal_WriteObjectToFile(PyObject *, FILE *, int***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyMarshal_WriteObjectToString(PyObject *, int***REMOVED***;

PyAPI_FUNC(long***REMOVED*** PyMarshal_ReadLongFromFile(FILE ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyMarshal_ReadShortFromFile(FILE ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyMarshal_ReadObjectFromFile(FILE ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyMarshal_ReadLastObjectFromFile(FILE ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyMarshal_ReadObjectFromString(char *, Py_ssize_t***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_MARSHAL_H */
