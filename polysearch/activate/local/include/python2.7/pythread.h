
#ifndef Py_PYTHREAD_H
#define Py_PYTHREAD_H

typedef void *PyThread_type_lock;
typedef void *PyThread_type_sema;

#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(void***REMOVED*** PyThread_init_thread(void***REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyThread_start_new_thread(void (****REMOVED***(void ****REMOVED***, void ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyThread_exit_thread(void***REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyThread_get_thread_ident(void***REMOVED***;

PyAPI_FUNC(PyThread_type_lock***REMOVED*** PyThread_allocate_lock(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyThread_free_lock(PyThread_type_lock***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyThread_acquire_lock(PyThread_type_lock, int***REMOVED***;
#define WAIT_LOCK	1
#define NOWAIT_LOCK	0
PyAPI_FUNC(void***REMOVED*** PyThread_release_lock(PyThread_type_lock***REMOVED***;

PyAPI_FUNC(size_t***REMOVED*** PyThread_get_stacksize(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyThread_set_stacksize(size_t***REMOVED***;

/* Thread Local Storage (TLS***REMOVED*** API */
PyAPI_FUNC(int***REMOVED*** PyThread_create_key(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyThread_delete_key(int***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyThread_set_key_value(int, void ****REMOVED***;
PyAPI_FUNC(void ****REMOVED*** PyThread_get_key_value(int***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyThread_delete_key_value(int key***REMOVED***;

/* Cleanup after a fork */
PyAPI_FUNC(void***REMOVED*** PyThread_ReInitTLS(void***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif

#endif /* !Py_PYTHREAD_H */
