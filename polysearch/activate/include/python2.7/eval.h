
/* Interface to execute compiled code */

#ifndef Py_EVAL_H
#define Py_EVAL_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(PyObject ****REMOVED*** PyEval_EvalCode(PyCodeObject *, PyObject *, PyObject ****REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyEval_EvalCodeEx(PyCodeObject *co,
					PyObject *globals,
					PyObject *locals,
					PyObject **args, int argc,
					PyObject **kwds, int kwdc,
					PyObject **defs, int defc,
					PyObject *closure***REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** _PyEval_CallTracing(PyObject *func, PyObject *args***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_EVAL_H */
