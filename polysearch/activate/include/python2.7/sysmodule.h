
/* System module interface */

#ifndef Py_SYSMODULE_H
#define Py_SYSMODULE_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(PyObject ****REMOVED*** PySys_GetObject(char ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PySys_SetObject(char *, PyObject ****REMOVED***;
PyAPI_FUNC(FILE ****REMOVED*** PySys_GetFile(char *, FILE ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PySys_SetArgv(int, char *****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PySys_SetArgvEx(int, char **, int***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PySys_SetPath(char ****REMOVED***;

PyAPI_FUNC(void***REMOVED*** PySys_WriteStdout(const char *format, ...***REMOVED***
			Py_GCC_ATTRIBUTE((format(printf, 1, 2***REMOVED******REMOVED******REMOVED***;
PyAPI_FUNC(void***REMOVED*** PySys_WriteStderr(const char *format, ...***REMOVED***
			Py_GCC_ATTRIBUTE((format(printf, 1, 2***REMOVED******REMOVED******REMOVED***;

PyAPI_FUNC(void***REMOVED*** PySys_ResetWarnOptions(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PySys_AddWarnOption(char ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PySys_HasWarnOptions(void***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_SYSMODULE_H */
