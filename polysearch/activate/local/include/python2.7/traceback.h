
#ifndef Py_TRACEBACK_H
#define Py_TRACEBACK_H
#ifdef __cplusplus
extern "C" {
#endif

struct _frame;

/* Traceback interface */

typedef struct _traceback {
	PyObject_HEAD
	struct _traceback *tb_next;
	struct _frame *tb_frame;
	int tb_lasti;
	int tb_lineno;
***REMOVED*** PyTracebackObject;

PyAPI_FUNC(int***REMOVED*** PyTraceBack_Here(struct _frame ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyTraceBack_Print(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** _Py_DisplaySourceLine(PyObject *, const char *, int, int***REMOVED***;

/* Reveal traceback type so we can typecheck traceback objects */
PyAPI_DATA(PyTypeObject***REMOVED*** PyTraceBack_Type;
#define PyTraceBack_Check(v***REMOVED*** (Py_TYPE(v***REMOVED*** == &PyTraceBack_Type***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_TRACEBACK_H */
