
/* Thread and interpreter state structures and their interfaces */


#ifndef Py_PYSTATE_H
#define Py_PYSTATE_H
#ifdef __cplusplus
extern "C" {
#endif

/* State shared between threads */

struct _ts; /* Forward */
struct _is; /* Forward */

typedef struct _is {

    struct _is *next;
    struct _ts *tstate_head;

    PyObject *modules;
    PyObject *sysdict;
    PyObject *builtins;
    PyObject *modules_reloading;

    PyObject *codec_search_path;
    PyObject *codec_search_cache;
    PyObject *codec_error_registry;

#ifdef HAVE_DLOPEN
    int dlopenflags;
#endif
#ifdef WITH_TSC
    int tscdump;
#endif

***REMOVED*** PyInterpreterState;


/* State unique per thread */

struct _frame; /* Avoid including frameobject.h */

/* Py_tracefunc return -1 when raising an exception, or 0 for success. */
typedef int (*Py_tracefunc***REMOVED***(PyObject *, struct _frame *, int, PyObject ****REMOVED***;

/* The following values are used for 'what' for tracefunc functions: */
#define PyTrace_CALL 0
#define PyTrace_EXCEPTION 1
#define PyTrace_LINE 2
#define PyTrace_RETURN 3
#define PyTrace_C_CALL 4
#define PyTrace_C_EXCEPTION 5
#define PyTrace_C_RETURN 6

typedef struct _ts {
    /* See Python/ceval.c for comments explaining most fields */

    struct _ts *next;
    PyInterpreterState *interp;

    struct _frame *frame;
    int recursion_depth;
    /* 'tracing' keeps track of the execution depth when tracing/profiling.
       This is to prevent the actual trace/profile code from being recorded in
       the trace/profile. */
    int tracing;
    int use_tracing;

    Py_tracefunc c_profilefunc;
    Py_tracefunc c_tracefunc;
    PyObject *c_profileobj;
    PyObject *c_traceobj;

    PyObject *curexc_type;
    PyObject *curexc_value;
    PyObject *curexc_traceback;

    PyObject *exc_type;
    PyObject *exc_value;
    PyObject *exc_traceback;

    PyObject *dict;  /* Stores per-thread state */

    /* tick_counter is incremented whenever the check_interval ticker
     * reaches zero. The purpose is to give a useful measure of the number
     * of interpreted bytecode instructions in a given thread.  This
     * extremely lightweight statistic collector may be of interest to
     * profilers (like psyco.jit(***REMOVED******REMOVED***, although nothing in the core uses it.
     */
    int tick_counter;

    int gilstate_counter;

    PyObject *async_exc; /* Asynchronous exception to raise */
    long thread_id; /* Thread id where this tstate was created */

    int trash_delete_nesting;
    PyObject *trash_delete_later;

    /* XXX signal handlers should also be here */

***REMOVED*** PyThreadState;


PyAPI_FUNC(PyInterpreterState ****REMOVED*** PyInterpreterState_New(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyInterpreterState_Clear(PyInterpreterState ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyInterpreterState_Delete(PyInterpreterState ****REMOVED***;

PyAPI_FUNC(PyThreadState ****REMOVED*** PyThreadState_New(PyInterpreterState ****REMOVED***;
PyAPI_FUNC(PyThreadState ****REMOVED*** _PyThreadState_Prealloc(PyInterpreterState ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyThreadState_Init(PyThreadState ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyThreadState_Clear(PyThreadState ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyThreadState_Delete(PyThreadState ****REMOVED***;
#ifdef WITH_THREAD
PyAPI_FUNC(void***REMOVED*** PyThreadState_DeleteCurrent(void***REMOVED***;
#endif

PyAPI_FUNC(PyThreadState ****REMOVED*** PyThreadState_Get(void***REMOVED***;
PyAPI_FUNC(PyThreadState ****REMOVED*** PyThreadState_Swap(PyThreadState ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyThreadState_GetDict(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyThreadState_SetAsyncExc(long, PyObject ****REMOVED***;


/* Variable and macro for in-line access to current thread state */

PyAPI_DATA(PyThreadState ****REMOVED*** _PyThreadState_Current;

#ifdef Py_DEBUG
#define PyThreadState_GET(***REMOVED*** PyThreadState_Get(***REMOVED***
#else
#define PyThreadState_GET(***REMOVED*** (_PyThreadState_Current***REMOVED***
#endif

typedef
    enum {PyGILState_LOCKED, PyGILState_UNLOCKED***REMOVED***
        PyGILState_STATE;

/* Ensure that the current thread is ready to call the Python
   C API, regardless of the current state of Python, or of its
   thread lock.  This may be called as many times as desired
   by a thread so long as each call is matched with a call to
   PyGILState_Release(***REMOVED***.  In general, other thread-state APIs may
   be used between _Ensure(***REMOVED*** and _Release(***REMOVED*** calls, so long as the
   thread-state is restored to its previous state before the Release(***REMOVED***.
   For example, normal use of the Py_BEGIN_ALLOW_THREADS/
   Py_END_ALLOW_THREADS macros are acceptable.

   The return value is an opaque "handle" to the thread state when
   PyGILState_Ensure(***REMOVED*** was called, and must be passed to
   PyGILState_Release(***REMOVED*** to ensure Python is left in the same state. Even
   though recursive calls are allowed, these handles can *not* be shared -
   each unique call to PyGILState_Ensure must save the handle for its
   call to PyGILState_Release.

   When the function returns, the current thread will hold the GIL.

   Failure is a fatal error.
*/
PyAPI_FUNC(PyGILState_STATE***REMOVED*** PyGILState_Ensure(void***REMOVED***;

/* Release any resources previously acquired.  After this call, Python's
   state will be the same as it was prior to the corresponding
   PyGILState_Ensure(***REMOVED*** call (but generally this state will be unknown to
   the caller, hence the use of the GILState API.***REMOVED***

   Every call to PyGILState_Ensure must be matched by a call to
   PyGILState_Release on the same thread.
*/
PyAPI_FUNC(void***REMOVED*** PyGILState_Release(PyGILState_STATE***REMOVED***;

/* Helper/diagnostic function - get the current thread state for
   this thread.  May return NULL if no GILState API has been used
   on the current thread.  Note that the main thread always has such a
   thread-state, even if no auto-thread-state call has been made
   on the main thread.
*/
PyAPI_FUNC(PyThreadState ****REMOVED*** PyGILState_GetThisThreadState(void***REMOVED***;

/* The implementation of sys._current_frames(***REMOVED***  Returns a dict mapping
   thread id to that thread's current frame.
*/
PyAPI_FUNC(PyObject ****REMOVED*** _PyThread_CurrentFrames(void***REMOVED***;

/* Routines for advanced debuggers, requested by David Beazley.
   Don't use unless you know what you are doing! */
PyAPI_FUNC(PyInterpreterState ****REMOVED*** PyInterpreterState_Head(void***REMOVED***;
PyAPI_FUNC(PyInterpreterState ****REMOVED*** PyInterpreterState_Next(PyInterpreterState ****REMOVED***;
PyAPI_FUNC(PyThreadState ****REMOVED*** PyInterpreterState_ThreadHead(PyInterpreterState ****REMOVED***;
PyAPI_FUNC(PyThreadState ****REMOVED*** PyThreadState_Next(PyThreadState ****REMOVED***;

typedef struct _frame *(*PyThreadFrameGetter***REMOVED***(PyThreadState *self_***REMOVED***;

/* hook for PyEval_GetFrame(***REMOVED***, requested for Psyco */
PyAPI_DATA(PyThreadFrameGetter***REMOVED*** _PyThreadState_GetFrame;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_PYSTATE_H */
