
#ifndef Py_PYDEBUG_H
#define Py_PYDEBUG_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(int***REMOVED*** Py_DebugFlag;
PyAPI_DATA(int***REMOVED*** Py_VerboseFlag;
PyAPI_DATA(int***REMOVED*** Py_InteractiveFlag;
PyAPI_DATA(int***REMOVED*** Py_InspectFlag;
PyAPI_DATA(int***REMOVED*** Py_OptimizeFlag;
PyAPI_DATA(int***REMOVED*** Py_NoSiteFlag;
PyAPI_DATA(int***REMOVED*** Py_BytesWarningFlag;
PyAPI_DATA(int***REMOVED*** Py_UseClassExceptionsFlag;
PyAPI_DATA(int***REMOVED*** Py_FrozenFlag;
PyAPI_DATA(int***REMOVED*** Py_TabcheckFlag;
PyAPI_DATA(int***REMOVED*** Py_UnicodeFlag;
PyAPI_DATA(int***REMOVED*** Py_IgnoreEnvironmentFlag;
PyAPI_DATA(int***REMOVED*** Py_DivisionWarningFlag;
PyAPI_DATA(int***REMOVED*** Py_DontWriteBytecodeFlag;
PyAPI_DATA(int***REMOVED*** Py_NoUserSiteDirectory;
/* _XXX Py_QnewFlag should go away in 3.0.  It's true iff -Qnew is passed,
  on the command line, and is used in 2.2 by ceval.c to make all "/" divisions
  true divisions (which they will be in 3.0***REMOVED***. */
PyAPI_DATA(int***REMOVED*** _Py_QnewFlag;
/* Warn about 3.x issues */
PyAPI_DATA(int***REMOVED*** Py_Py3kWarningFlag;
PyAPI_DATA(int***REMOVED*** Py_HashRandomizationFlag;

/* this is a wrapper around getenv(***REMOVED*** that pays attention to
   Py_IgnoreEnvironmentFlag.  It should be used for getting variables like
   PYTHONPATH and PYTHONHOME from the environment */
#define Py_GETENV(s***REMOVED*** (Py_IgnoreEnvironmentFlag ? NULL : getenv(s***REMOVED******REMOVED***

PyAPI_FUNC(void***REMOVED*** Py_FatalError(const char *message***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_PYDEBUG_H */
