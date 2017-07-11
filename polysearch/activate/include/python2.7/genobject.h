
/* Generator object interface */

#ifndef Py_GENOBJECT_H
#define Py_GENOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

struct _frame; /* Avoid including frameobject.h */

typedef struct {
	PyObject_HEAD
	/* The gi_ prefix is intended to remind of generator-iterator. */

	/* Note: gi_frame can be NULL if the generator is "finished" */
	struct _frame *gi_frame;

	/* True if generator is being executed. */
	int gi_running;
    
	/* The code object backing the generator */
	PyObject *gi_code;

	/* List of weak reference. */
	PyObject *gi_weakreflist;
***REMOVED*** PyGenObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyGen_Type;

#define PyGen_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyGen_Type***REMOVED***
#define PyGen_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyGen_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyGen_New(struct _frame ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyGen_NeedsFinalizing(PyGenObject ****REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_GENOBJECT_H */
