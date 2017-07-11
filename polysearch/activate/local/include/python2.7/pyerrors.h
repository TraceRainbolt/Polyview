#ifndef Py_ERRORS_H
#define Py_ERRORS_H
#ifdef __cplusplus
extern "C" {
#endif

/* Error objects */

typedef struct {
    PyObject_HEAD
    PyObject *dict;
    PyObject *args;
    PyObject *message;
***REMOVED*** PyBaseExceptionObject;

typedef struct {
    PyObject_HEAD
    PyObject *dict;
    PyObject *args;
    PyObject *message;
    PyObject *msg;
    PyObject *filename;
    PyObject *lineno;
    PyObject *offset;
    PyObject *text;
    PyObject *print_file_and_line;
***REMOVED*** PySyntaxErrorObject;

#ifdef Py_USING_UNICODE
typedef struct {
    PyObject_HEAD
    PyObject *dict;
    PyObject *args;
    PyObject *message;
    PyObject *encoding;
    PyObject *object;
    Py_ssize_t start;
    Py_ssize_t end;
    PyObject *reason;
***REMOVED*** PyUnicodeErrorObject;
#endif

typedef struct {
    PyObject_HEAD
    PyObject *dict;
    PyObject *args;
    PyObject *message;
    PyObject *code;
***REMOVED*** PySystemExitObject;

typedef struct {
    PyObject_HEAD
    PyObject *dict;
    PyObject *args;
    PyObject *message;
    PyObject *myerrno;
    PyObject *strerror;
    PyObject *filename;
***REMOVED*** PyEnvironmentErrorObject;

#ifdef MS_WINDOWS
typedef struct {
    PyObject_HEAD
    PyObject *dict;
    PyObject *args;
    PyObject *message;
    PyObject *myerrno;
    PyObject *strerror;
    PyObject *filename;
    PyObject *winerror;
***REMOVED*** PyWindowsErrorObject;
#endif

/* Error handling definitions */

PyAPI_FUNC(void***REMOVED*** PyErr_SetNone(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_SetObject(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_SetString(PyObject *, const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_Occurred(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_Clear(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_Fetch(PyObject **, PyObject **, PyObject *****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_Restore(PyObject *, PyObject *, PyObject ****REMOVED***;

#ifdef Py_DEBUG
#define _PyErr_OCCURRED(***REMOVED*** PyErr_Occurred(***REMOVED***
#else
#define _PyErr_OCCURRED(***REMOVED*** (_PyThreadState_Current->curexc_type***REMOVED***
#endif

/* Error testing and normalization */
PyAPI_FUNC(int***REMOVED*** PyErr_GivenExceptionMatches(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyErr_ExceptionMatches(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_NormalizeException(PyObject**, PyObject**, PyObject*****REMOVED***;

/* */

#define PyExceptionClass_Check(x***REMOVED***                                       \
    (PyClass_Check((x***REMOVED******REMOVED*** || (PyType_Check((x***REMOVED******REMOVED*** &&                        \
      PyType_FastSubclass((PyTypeObject****REMOVED***(x***REMOVED***, Py_TPFLAGS_BASE_EXC_SUBCLASS***REMOVED******REMOVED******REMOVED***

#define PyExceptionInstance_Check(x***REMOVED***                    \
    (PyInstance_Check((x***REMOVED******REMOVED*** ||                           \
     PyType_FastSubclass((x***REMOVED***->ob_type, Py_TPFLAGS_BASE_EXC_SUBCLASS***REMOVED******REMOVED***

#define PyExceptionClass_Name(x***REMOVED***                                   \
    (PyClass_Check((x***REMOVED******REMOVED***                                            \
     ? PyString_AS_STRING(((PyClassObject****REMOVED***(x***REMOVED******REMOVED***->cl_name***REMOVED***          \
     : (char ****REMOVED***(((PyTypeObject****REMOVED***(x***REMOVED******REMOVED***->tp_name***REMOVED******REMOVED***

#define PyExceptionInstance_Class(x***REMOVED***                                    \
    ((PyInstance_Check((x***REMOVED******REMOVED***                                             \
      ? (PyObject****REMOVED***((PyInstanceObject****REMOVED***(x***REMOVED******REMOVED***->in_class                   \
      : (PyObject****REMOVED***((x***REMOVED***->ob_type***REMOVED******REMOVED******REMOVED***


/* Predefined exceptions */

PyAPI_DATA(PyObject ****REMOVED*** PyExc_BaseException;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_Exception;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_StopIteration;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_GeneratorExit;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_StandardError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_ArithmeticError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_LookupError;

PyAPI_DATA(PyObject ****REMOVED*** PyExc_AssertionError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_AttributeError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_EOFError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_FloatingPointError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_EnvironmentError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_IOError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_OSError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_ImportError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_IndexError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_KeyError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_KeyboardInterrupt;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_MemoryError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_NameError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_OverflowError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_RuntimeError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_NotImplementedError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_SyntaxError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_IndentationError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_TabError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_ReferenceError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_SystemError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_SystemExit;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_TypeError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_UnboundLocalError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_UnicodeError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_UnicodeEncodeError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_UnicodeDecodeError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_UnicodeTranslateError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_ValueError;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_ZeroDivisionError;
#ifdef MS_WINDOWS
PyAPI_DATA(PyObject ****REMOVED*** PyExc_WindowsError;
#endif
#ifdef __VMS
PyAPI_DATA(PyObject ****REMOVED*** PyExc_VMSError;
#endif

PyAPI_DATA(PyObject ****REMOVED*** PyExc_BufferError;

PyAPI_DATA(PyObject ****REMOVED*** PyExc_MemoryErrorInst;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_RecursionErrorInst;

/* Predefined warning categories */
PyAPI_DATA(PyObject ****REMOVED*** PyExc_Warning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_UserWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_DeprecationWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_PendingDeprecationWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_SyntaxWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_RuntimeWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_FutureWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_ImportWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_UnicodeWarning;
PyAPI_DATA(PyObject ****REMOVED*** PyExc_BytesWarning;


/* Convenience functions */

PyAPI_FUNC(int***REMOVED*** PyErr_BadArgument(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_NoMemory(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromErrno(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromErrnoWithFilenameObject(
    PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromErrnoWithFilename(
    PyObject *, const char ****REMOVED***;
#ifdef MS_WINDOWS
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromErrnoWithUnicodeFilename(
    PyObject *, const Py_UNICODE ****REMOVED***;
#endif /* MS_WINDOWS */

PyAPI_FUNC(PyObject ****REMOVED*** PyErr_Format(PyObject *, const char *, ...***REMOVED***
                        Py_GCC_ATTRIBUTE((format(printf, 2, 3***REMOVED******REMOVED******REMOVED***;

#ifdef MS_WINDOWS
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromWindowsErrWithFilenameObject(
    int, const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromWindowsErrWithFilename(
    int, const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromWindowsErrWithUnicodeFilename(
    int, const Py_UNICODE ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetFromWindowsErr(int***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetExcFromWindowsErrWithFilenameObject(
    PyObject *,int, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetExcFromWindowsErrWithFilename(
    PyObject *,int, const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetExcFromWindowsErrWithUnicodeFilename(
    PyObject *,int, const Py_UNICODE ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_SetExcFromWindowsErr(PyObject *, int***REMOVED***;
#endif /* MS_WINDOWS */

/* Export the old function so that the existing API remains available: */
PyAPI_FUNC(void***REMOVED*** PyErr_BadInternalCall(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyErr_BadInternalCall(char *filename, int lineno***REMOVED***;
/* Mask the old API with a call to the new API for code compiled under
   Python 2.0: */
#define PyErr_BadInternalCall(***REMOVED*** _PyErr_BadInternalCall(__FILE__, __LINE__***REMOVED***

/* Function to create a new exception */
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_NewException(
    char *name, PyObject *base, PyObject *dict***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_NewExceptionWithDoc(
    char *name, char *doc, PyObject *base, PyObject *dict***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_WriteUnraisable(PyObject ****REMOVED***;

/* In sigcheck.c or signalmodule.c */
PyAPI_FUNC(int***REMOVED*** PyErr_CheckSignals(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_SetInterrupt(void***REMOVED***;

/* In signalmodule.c */
int PySignal_SetWakeupFd(int fd***REMOVED***;

/* Support for adding program text to SyntaxErrors */
PyAPI_FUNC(void***REMOVED*** PyErr_SyntaxLocation(const char *, int***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyErr_ProgramText(const char *, int***REMOVED***;

#ifdef Py_USING_UNICODE
/* The following functions are used to create and modify unicode
   exceptions from C */

/* create a UnicodeDecodeError object */
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeDecodeError_Create(
    const char *, const char *, Py_ssize_t, Py_ssize_t, Py_ssize_t, const char ****REMOVED***;

/* create a UnicodeEncodeError object */
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeEncodeError_Create(
    const char *, const Py_UNICODE *, Py_ssize_t, Py_ssize_t, Py_ssize_t, const char ****REMOVED***;

/* create a UnicodeTranslateError object */
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeTranslateError_Create(
    const Py_UNICODE *, Py_ssize_t, Py_ssize_t, Py_ssize_t, const char ****REMOVED***;

/* get the encoding attribute */
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeEncodeError_GetEncoding(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeDecodeError_GetEncoding(PyObject ****REMOVED***;

/* get the object attribute */
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeEncodeError_GetObject(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeDecodeError_GetObject(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeTranslateError_GetObject(PyObject ****REMOVED***;

/* get the value of the start attribute (the int * may not be NULL***REMOVED***
   return 0 on success, -1 on failure */
PyAPI_FUNC(int***REMOVED*** PyUnicodeEncodeError_GetStart(PyObject *, Py_ssize_t ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeDecodeError_GetStart(PyObject *, Py_ssize_t ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeTranslateError_GetStart(PyObject *, Py_ssize_t ****REMOVED***;

/* assign a new value to the start attribute
   return 0 on success, -1 on failure */
PyAPI_FUNC(int***REMOVED*** PyUnicodeEncodeError_SetStart(PyObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeDecodeError_SetStart(PyObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeTranslateError_SetStart(PyObject *, Py_ssize_t***REMOVED***;

/* get the value of the end attribute (the int *may not be NULL***REMOVED***
 return 0 on success, -1 on failure */
PyAPI_FUNC(int***REMOVED*** PyUnicodeEncodeError_GetEnd(PyObject *, Py_ssize_t ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeDecodeError_GetEnd(PyObject *, Py_ssize_t ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeTranslateError_GetEnd(PyObject *, Py_ssize_t ****REMOVED***;

/* assign a new value to the end attribute
   return 0 on success, -1 on failure */
PyAPI_FUNC(int***REMOVED*** PyUnicodeEncodeError_SetEnd(PyObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeDecodeError_SetEnd(PyObject *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeTranslateError_SetEnd(PyObject *, Py_ssize_t***REMOVED***;

/* get the value of the reason attribute */
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeEncodeError_GetReason(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeDecodeError_GetReason(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyUnicodeTranslateError_GetReason(PyObject ****REMOVED***;

/* assign a new value to the reason attribute
   return 0 on success, -1 on failure */
PyAPI_FUNC(int***REMOVED*** PyUnicodeEncodeError_SetReason(
    PyObject *, const char ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeDecodeError_SetReason(
    PyObject *, const char ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyUnicodeTranslateError_SetReason(
    PyObject *, const char ****REMOVED***;
#endif


/* These APIs aren't really part of the error implementation, but
   often needed to format error messages; the native C lib APIs are
   not available on all platforms, which is why we provide emulations
   for those platforms in Python/mysnprintf.c,
   WARNING:  The return value of snprintf varies across platforms; do
   not rely on any particular behavior; eventually the C99 defn may
   be reliable.
*/
#if defined(MS_WIN32***REMOVED*** && !defined(HAVE_SNPRINTF***REMOVED***
# define HAVE_SNPRINTF
# define snprintf _snprintf
# define vsnprintf _vsnprintf
#endif

#include <stdarg.h>
PyAPI_FUNC(int***REMOVED*** PyOS_snprintf(char *str, size_t size, const char  *format, ...***REMOVED***
                        Py_GCC_ATTRIBUTE((format(printf, 3, 4***REMOVED******REMOVED******REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyOS_vsnprintf(char *str, size_t size, const char  *format, va_list va***REMOVED***
                        Py_GCC_ATTRIBUTE((format(printf, 3, 0***REMOVED******REMOVED******REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_ERRORS_H */
