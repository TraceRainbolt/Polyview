
/* Class object interface */

/* Revealing some structures (not for general use***REMOVED*** */

#ifndef Py_CLASSOBJECT_H
#define Py_CLASSOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    PyObject_HEAD
    PyObject	*cl_bases;	/* A tuple of class objects */
    PyObject	*cl_dict;	/* A dictionary */
    PyObject	*cl_name;	/* A string */
    /* The following three are functions or NULL */
    PyObject	*cl_getattr;
    PyObject	*cl_setattr;
    PyObject	*cl_delattr;
    PyObject    *cl_weakreflist; /* List of weak references */
***REMOVED*** PyClassObject;

typedef struct {
    PyObject_HEAD
    PyClassObject *in_class;	/* The class object */
    PyObject	  *in_dict;	/* A dictionary */
    PyObject	  *in_weakreflist; /* List of weak references */
***REMOVED*** PyInstanceObject;

typedef struct {
    PyObject_HEAD
    PyObject *im_func;   /* The callable object implementing the method */
    PyObject *im_self;   /* The instance it is bound to, or NULL */
    PyObject *im_class;  /* The class that asked for the method */
    PyObject *im_weakreflist; /* List of weak references */
***REMOVED*** PyMethodObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyClass_Type, PyInstance_Type, PyMethod_Type;

#define PyClass_Check(op***REMOVED*** ((op***REMOVED***->ob_type == &PyClass_Type***REMOVED***
#define PyInstance_Check(op***REMOVED*** ((op***REMOVED***->ob_type == &PyInstance_Type***REMOVED***
#define PyMethod_Check(op***REMOVED*** ((op***REMOVED***->ob_type == &PyMethod_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyClass_New(PyObject *, PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyInstance_New(PyObject *, PyObject *,
                                            PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyInstance_NewRaw(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyMethod_New(PyObject *, PyObject *, PyObject ****REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyMethod_Function(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyMethod_Self(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyMethod_Class(PyObject ****REMOVED***;

/* Look up attribute with name (a string***REMOVED*** on instance object pinst, using
 * only the instance and base class dicts.  If a descriptor is found in
 * a class dict, the descriptor is returned without calling it.
 * Returns NULL if nothing found, else a borrowed reference to the
 * value associated with name in the dict in which name was found.
 * The point of this routine is that it never calls arbitrary Python
 * code, so is always "safe":  all it does is dict lookups.  The function
 * can't fail, never sets an exception, and NULL is not an error (it just
 * means "not found"***REMOVED***.
 */
PyAPI_FUNC(PyObject ****REMOVED*** _PyInstance_Lookup(PyObject *pinst, PyObject *name***REMOVED***;

/* Macros for direct access to these values. Type checks are *not*
   done, so use with care. */
#define PyMethod_GET_FUNCTION(meth***REMOVED*** \
        (((PyMethodObject ****REMOVED***meth***REMOVED*** -> im_func***REMOVED***
#define PyMethod_GET_SELF(meth***REMOVED*** \
	(((PyMethodObject ****REMOVED***meth***REMOVED*** -> im_self***REMOVED***
#define PyMethod_GET_CLASS(meth***REMOVED*** \
	(((PyMethodObject ****REMOVED***meth***REMOVED*** -> im_class***REMOVED***

PyAPI_FUNC(int***REMOVED*** PyClass_IsSubclass(PyObject *, PyObject ****REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyMethod_ClearFreeList(void***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_CLASSOBJECT_H */
