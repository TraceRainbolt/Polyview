#ifndef Py_WARNINGS_H
#define Py_WARNINGS_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(void***REMOVED*** _PyWarnings_Init(void***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyErr_WarnEx(PyObject *, const char *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyErr_WarnExplicit(PyObject *, const char *, const char *, int,
                                    const char *, PyObject ****REMOVED***;

#define PyErr_WarnPy3k(msg, stacklevel***REMOVED*** \
  (Py_Py3kWarningFlag ? PyErr_WarnEx(PyExc_DeprecationWarning, msg, stacklevel***REMOVED*** : 0***REMOVED***

/* DEPRECATED: Use PyErr_WarnEx(***REMOVED*** instead. */
#define PyErr_Warn(category, msg***REMOVED*** PyErr_WarnEx(category, msg, 1***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_WARNINGS_H */

