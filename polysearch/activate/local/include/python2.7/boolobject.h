/* Boolean object interface */

#ifndef Py_BOOLOBJECT_H
#define Py_BOOLOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


typedef PyIntObject PyBoolObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyBool_Type;

#define PyBool_Check(x***REMOVED*** (Py_TYPE(x***REMOVED*** == &PyBool_Type***REMOVED***

/* Py_False and Py_True are the only two bools in existence.
Don't forget to apply Py_INCREF(***REMOVED*** when returning either!!! */

/* Don't use these directly */
PyAPI_DATA(PyIntObject***REMOVED*** _Py_ZeroStruct, _Py_TrueStruct;

/* Use these macros */
#define Py_False ((PyObject ****REMOVED*** &_Py_ZeroStruct***REMOVED***
#define Py_True ((PyObject ****REMOVED*** &_Py_TrueStruct***REMOVED***

/* Macros for returning Py_True or Py_False, respectively */
#define Py_RETURN_TRUE return Py_INCREF(Py_True***REMOVED***, Py_True
#define Py_RETURN_FALSE return Py_INCREF(Py_False***REMOVED***, Py_False

/* Function to return a bool from a C long */
PyAPI_FUNC(PyObject ****REMOVED*** PyBool_FromLong(long***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_BOOLOBJECT_H */
