#ifndef Py_CEVAL_H
#define Py_CEVAL_H
#ifdef __cplusplus
extern "C" {
#endif


/* Interface to random parts in ceval.c */

PyAPI_FUNC(PyObject ****REMOVED*** PyEval_CallObjectWithKeywords(
    PyObject *, PyObject *, PyObject ****REMOVED***;

/* Inline this */
#define PyEval_CallObject(func,arg***REMOVED*** \
    PyEval_CallObjectWithKeywords(func, arg, (PyObject ****REMOVED***NULL***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyEval_CallFunction(PyObject *obj,
                                           const char *format, ...***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyEval_CallMethod(PyObject *obj,
                                         const char *methodname,
                                         const char *format, ...***REMOVED***;

PyAPI_FUNC(void***REMOVED*** PyEval_SetProfile(Py_tracefunc, PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_SetTrace(Py_tracefunc, PyObject ****REMOVED***;

struct _frame; /* Avoid including frameobject.h */

PyAPI_FUNC(PyObject ****REMOVED*** PyEval_GetBuiltins(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyEval_GetGlobals(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyEval_GetLocals(void***REMOVED***;
PyAPI_FUNC(struct _frame ****REMOVED*** PyEval_GetFrame(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyEval_GetRestricted(void***REMOVED***;

/* Look at the current frame's (if any***REMOVED*** code's co_flags, and turn on
   the corresponding compiler flags in cf->cf_flags.  Return 1 if any
   flag was set, else return 0. */
PyAPI_FUNC(int***REMOVED*** PyEval_MergeCompilerFlags(PyCompilerFlags *cf***REMOVED***;

PyAPI_FUNC(int***REMOVED*** Py_FlushLine(void***REMOVED***;

PyAPI_FUNC(int***REMOVED*** Py_AddPendingCall(int (*func***REMOVED***(void ****REMOVED***, void *arg***REMOVED***;
PyAPI_FUNC(int***REMOVED*** Py_MakePendingCalls(void***REMOVED***;

/* Protection against deeply nested recursive calls */
PyAPI_FUNC(void***REMOVED*** Py_SetRecursionLimit(int***REMOVED***;
PyAPI_FUNC(int***REMOVED*** Py_GetRecursionLimit(void***REMOVED***;

#define Py_EnterRecursiveCall(where***REMOVED***                                    \
            (_Py_MakeRecCheck(PyThreadState_GET(***REMOVED***->recursion_depth***REMOVED*** &&  \
             _Py_CheckRecursiveCall(where***REMOVED******REMOVED***
#define Py_LeaveRecursiveCall(***REMOVED***                         \
            (--PyThreadState_GET(***REMOVED***->recursion_depth***REMOVED***
PyAPI_FUNC(int***REMOVED*** _Py_CheckRecursiveCall(char *where***REMOVED***;
PyAPI_DATA(int***REMOVED*** _Py_CheckRecursionLimit;
#ifdef USE_STACKCHECK
#  define _Py_MakeRecCheck(x***REMOVED***  (++(x***REMOVED*** > --_Py_CheckRecursionLimit***REMOVED***
#else
#  define _Py_MakeRecCheck(x***REMOVED***  (++(x***REMOVED*** > _Py_CheckRecursionLimit***REMOVED***
#endif

PyAPI_FUNC(const char ****REMOVED*** PyEval_GetFuncName(PyObject ****REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** PyEval_GetFuncDesc(PyObject ****REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyEval_GetCallStats(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyEval_EvalFrame(struct _frame ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyEval_EvalFrameEx(struct _frame *f, int exc***REMOVED***;

/* this used to be handled on a per-thread basis - now just two globals */
PyAPI_DATA(volatile int***REMOVED*** _Py_Ticker;
PyAPI_DATA(int***REMOVED*** _Py_CheckInterval;

/* Interface for threads.

   A module that plans to do a blocking system call (or something else
   that lasts a long time and doesn't touch Python data***REMOVED*** can allow other
   threads to run as follows:

    ...preparations here...
    Py_BEGIN_ALLOW_THREADS
    ...blocking system call here...
    Py_END_ALLOW_THREADS
    ...interpret result here...

   The Py_BEGIN_ALLOW_THREADS/Py_END_ALLOW_THREADS pair expands to a
   {***REMOVED***-surrounded block.
   To leave the block in the middle (e.g., with return***REMOVED***, you must insert
   a line containing Py_BLOCK_THREADS before the return, e.g.

    if (...premature_exit...***REMOVED*** {
        Py_BLOCK_THREADS
        PyErr_SetFromErrno(PyExc_IOError***REMOVED***;
        return NULL;
***REMOVED***

   An alternative is:

    Py_BLOCK_THREADS
    if (...premature_exit...***REMOVED*** {
        PyErr_SetFromErrno(PyExc_IOError***REMOVED***;
        return NULL;
***REMOVED***
    Py_UNBLOCK_THREADS

   For convenience, that the value of 'errno' is restored across
   Py_END_ALLOW_THREADS and Py_BLOCK_THREADS.

   WARNING: NEVER NEST CALLS TO Py_BEGIN_ALLOW_THREADS AND
   Py_END_ALLOW_THREADS!!!

   The function PyEval_InitThreads(***REMOVED*** should be called only from
   initthread(***REMOVED*** in "threadmodule.c".

   Note that not yet all candidates have been converted to use this
   mechanism!
*/

PyAPI_FUNC(PyThreadState ****REMOVED*** PyEval_SaveThread(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_RestoreThread(PyThreadState ****REMOVED***;

#ifdef WITH_THREAD

PyAPI_FUNC(int***REMOVED***  PyEval_ThreadsInitialized(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_InitThreads(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_AcquireLock(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_ReleaseLock(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_AcquireThread(PyThreadState *tstate***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_ReleaseThread(PyThreadState *tstate***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyEval_ReInitThreads(void***REMOVED***;

#define Py_BEGIN_ALLOW_THREADS { \
                        PyThreadState *_save; \
                        _save = PyEval_SaveThread(***REMOVED***;
#define Py_BLOCK_THREADS        PyEval_RestoreThread(_save***REMOVED***;
#define Py_UNBLOCK_THREADS      _save = PyEval_SaveThread(***REMOVED***;
#define Py_END_ALLOW_THREADS    PyEval_RestoreThread(_save***REMOVED***; \
             ***REMOVED***

#else /* !WITH_THREAD */

#define Py_BEGIN_ALLOW_THREADS {
#define Py_BLOCK_THREADS
#define Py_UNBLOCK_THREADS
#define Py_END_ALLOW_THREADS ***REMOVED***

#endif /* !WITH_THREAD */

PyAPI_FUNC(int***REMOVED*** _PyEval_SliceIndex(PyObject *, Py_ssize_t ****REMOVED***;


#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_CEVAL_H */
