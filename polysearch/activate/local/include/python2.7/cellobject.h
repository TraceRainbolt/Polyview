/* Cell object interface */

#ifndef Py_CELLOBJECT_H
#define Py_CELLOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
	PyObject_HEAD
	PyObject *ob_ref;	/* Content of the cell or NULL when empty */
***REMOVED*** PyCellObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyCell_Type;

#define PyCell_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyCell_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyCell_New(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyCell_Get(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyCell_Set(PyObject *, PyObject ****REMOVED***;

#define PyCell_GET(op***REMOVED*** (((PyCellObject ****REMOVED***(op***REMOVED******REMOVED***->ob_ref***REMOVED***
#define PyCell_SET(op, v***REMOVED*** (((PyCellObject ****REMOVED***(op***REMOVED******REMOVED***->ob_ref = v***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_TUPLEOBJECT_H */
