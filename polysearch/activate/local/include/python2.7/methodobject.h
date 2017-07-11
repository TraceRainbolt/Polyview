
/* Method object interface */

#ifndef Py_METHODOBJECT_H
#define Py_METHODOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/* This is about the type 'builtin_function_or_method',
   not Python methods in user-defined classes.  See classobject.h
   for the latter. */

PyAPI_DATA(PyTypeObject***REMOVED*** PyCFunction_Type;

#define PyCFunction_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyCFunction_Type***REMOVED***

typedef PyObject *(*PyCFunction***REMOVED***(PyObject *, PyObject ****REMOVED***;
typedef PyObject *(*PyCFunctionWithKeywords***REMOVED***(PyObject *, PyObject *,
					     PyObject ****REMOVED***;
typedef PyObject *(*PyNoArgsFunction***REMOVED***(PyObject ****REMOVED***;

PyAPI_FUNC(PyCFunction***REMOVED*** PyCFunction_GetFunction(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyCFunction_GetSelf(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyCFunction_GetFlags(PyObject ****REMOVED***;

/* Macros for direct access to these values. Type checks are *not*
   done, so use with care. */
#define PyCFunction_GET_FUNCTION(func***REMOVED*** \
        (((PyCFunctionObject ****REMOVED***func***REMOVED*** -> m_ml -> ml_meth***REMOVED***
#define PyCFunction_GET_SELF(func***REMOVED*** \
	(((PyCFunctionObject ****REMOVED***func***REMOVED*** -> m_self***REMOVED***
#define PyCFunction_GET_FLAGS(func***REMOVED*** \
	(((PyCFunctionObject ****REMOVED***func***REMOVED*** -> m_ml -> ml_flags***REMOVED***
PyAPI_FUNC(PyObject ****REMOVED*** PyCFunction_Call(PyObject *, PyObject *, PyObject ****REMOVED***;

struct PyMethodDef {
    const char	*ml_name;	/* The name of the built-in function/method */
    PyCFunction  ml_meth;	/* The C function that implements it */
    int		 ml_flags;	/* Combination of METH_xxx flags, which mostly
				   describe the args expected by the C func */
    const char	*ml_doc;	/* The __doc__ attribute, or NULL */
***REMOVED***;
typedef struct PyMethodDef PyMethodDef;

PyAPI_FUNC(PyObject ****REMOVED*** Py_FindMethod(PyMethodDef[***REMOVED***, PyObject *, const char ****REMOVED***;

#define PyCFunction_New(ML, SELF***REMOVED*** PyCFunction_NewEx((ML***REMOVED***, (SELF***REMOVED***, NULL***REMOVED***
PyAPI_FUNC(PyObject ****REMOVED*** PyCFunction_NewEx(PyMethodDef *, PyObject *, 
					 PyObject ****REMOVED***;

/* Flag passed to newmethodobject */
#define METH_OLDARGS  0x0000
#define METH_VARARGS  0x0001
#define METH_KEYWORDS 0x0002
/* METH_NOARGS and METH_O must not be combined with the flags above. */
#define METH_NOARGS   0x0004
#define METH_O        0x0008

/* METH_CLASS and METH_STATIC are a little different; these control
   the construction of methods for a class.  These cannot be used for
   functions in modules. */
#define METH_CLASS    0x0010
#define METH_STATIC   0x0020

/* METH_COEXIST allows a method to be entered eventhough a slot has
   already filled the entry.  When defined, the flag allows a separate
   method, "__contains__" for example, to coexist with a defined 
   slot like sq_contains. */

#define METH_COEXIST   0x0040

typedef struct PyMethodChain {
    PyMethodDef *methods;		/* Methods of this type */
    struct PyMethodChain *link;	/* NULL or base type */
***REMOVED*** PyMethodChain;

PyAPI_FUNC(PyObject ****REMOVED*** Py_FindMethodInChain(PyMethodChain *, PyObject *,
                                            const char ****REMOVED***;

typedef struct {
    PyObject_HEAD
    PyMethodDef *m_ml; /* Description of the C function to call */
    PyObject    *m_self; /* Passed as 'self' arg to the C func, can be NULL */
    PyObject    *m_module; /* The __module__ attribute, can be anything */
***REMOVED*** PyCFunctionObject;

PyAPI_FUNC(int***REMOVED*** PyCFunction_ClearFreeList(void***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_METHODOBJECT_H */
