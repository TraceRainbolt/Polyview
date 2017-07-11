
/* Function object interface */

#ifndef Py_FUNCOBJECT_H
#define Py_FUNCOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/* Function objects and code objects should not be confused with each other:
 *
 * Function objects are created by the execution of the 'def' statement.
 * They reference a code object in their func_code attribute, which is a
 * purely syntactic object, i.e. nothing more than a compiled version of some
 * source code lines.  There is one code object per source code "fragment",
 * but each code object can be referenced by zero or many function objects
 * depending only on how many times the 'def' statement in the source was
 * executed so far.
 */

typedef struct {
    PyObject_HEAD
    PyObject *func_code;	/* A code object */
    PyObject *func_globals;	/* A dictionary (other mappings won't do***REMOVED*** */
    PyObject *func_defaults;	/* NULL or a tuple */
    PyObject *func_closure;	/* NULL or a tuple of cell objects */
    PyObject *func_doc;		/* The __doc__ attribute, can be anything */
    PyObject *func_name;	/* The __name__ attribute, a string object */
    PyObject *func_dict;	/* The __dict__ attribute, a dict or NULL */
    PyObject *func_weakreflist;	/* List of weak references */
    PyObject *func_module;	/* The __module__ attribute, can be anything */

    /* Invariant:
     *     func_closure contains the bindings for func_code->co_freevars, so
     *     PyTuple_Size(func_closure***REMOVED*** == PyCode_GetNumFree(func_code***REMOVED***
     *     (func_closure may be NULL if PyCode_GetNumFree(func_code***REMOVED*** == 0***REMOVED***.
     */
***REMOVED*** PyFunctionObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyFunction_Type;

#define PyFunction_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyFunction_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyFunction_New(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFunction_GetCode(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFunction_GetGlobals(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFunction_GetModule(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFunction_GetDefaults(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyFunction_SetDefaults(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFunction_GetClosure(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyFunction_SetClosure(PyObject *, PyObject ****REMOVED***;

/* Macros for direct access to these values. Type checks are *not*
   done, so use with care. */
#define PyFunction_GET_CODE(func***REMOVED*** \
        (((PyFunctionObject ****REMOVED***func***REMOVED*** -> func_code***REMOVED***
#define PyFunction_GET_GLOBALS(func***REMOVED*** \
	(((PyFunctionObject ****REMOVED***func***REMOVED*** -> func_globals***REMOVED***
#define PyFunction_GET_MODULE(func***REMOVED*** \
	(((PyFunctionObject ****REMOVED***func***REMOVED*** -> func_module***REMOVED***
#define PyFunction_GET_DEFAULTS(func***REMOVED*** \
	(((PyFunctionObject ****REMOVED***func***REMOVED*** -> func_defaults***REMOVED***
#define PyFunction_GET_CLOSURE(func***REMOVED*** \
	(((PyFunctionObject ****REMOVED***func***REMOVED*** -> func_closure***REMOVED***

/* The classmethod and staticmethod types lives here, too */
PyAPI_DATA(PyTypeObject***REMOVED*** PyClassMethod_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyStaticMethod_Type;

PyAPI_FUNC(PyObject ****REMOVED*** PyClassMethod_New(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyStaticMethod_New(PyObject ****REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_FUNCOBJECT_H */
