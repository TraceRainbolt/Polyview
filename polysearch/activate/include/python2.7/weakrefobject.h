/* Weak references objects for Python. */

#ifndef Py_WEAKREFOBJECT_H
#define Py_WEAKREFOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


typedef struct _PyWeakReference PyWeakReference;

/* PyWeakReference is the base struct for the Python ReferenceType, ProxyType,
 * and CallableProxyType.
 */
struct _PyWeakReference {
    PyObject_HEAD

    /* The object to which this is a weak reference, or Py_None if none.
     * Note that this is a stealth reference:  wr_object's refcount is
     * not incremented to reflect this pointer.
     */
    PyObject *wr_object;

    /* A callable to invoke when wr_object dies, or NULL if none. */
    PyObject *wr_callback;

    /* A cache for wr_object's hash code.  As usual for hashes, this is -1
     * if the hash code isn't known yet.
     */
    long hash;

    /* If wr_object is weakly referenced, wr_object has a doubly-linked NULL-
     * terminated list of weak references to it.  These are the list pointers.
     * If wr_object goes away, wr_object is set to Py_None, and these pointers
     * have no meaning then.
     */
    PyWeakReference *wr_prev;
    PyWeakReference *wr_next;
***REMOVED***;

PyAPI_DATA(PyTypeObject***REMOVED*** _PyWeakref_RefType;
PyAPI_DATA(PyTypeObject***REMOVED*** _PyWeakref_ProxyType;
PyAPI_DATA(PyTypeObject***REMOVED*** _PyWeakref_CallableProxyType;

#define PyWeakref_CheckRef(op***REMOVED*** PyObject_TypeCheck(op, &_PyWeakref_RefType***REMOVED***
#define PyWeakref_CheckRefExact(op***REMOVED*** \
        (Py_TYPE(op***REMOVED*** == &_PyWeakref_RefType***REMOVED***
#define PyWeakref_CheckProxy(op***REMOVED*** \
        ((Py_TYPE(op***REMOVED*** == &_PyWeakref_ProxyType***REMOVED*** || \
         (Py_TYPE(op***REMOVED*** == &_PyWeakref_CallableProxyType***REMOVED******REMOVED***

#define PyWeakref_Check(op***REMOVED*** \
        (PyWeakref_CheckRef(op***REMOVED*** || PyWeakref_CheckProxy(op***REMOVED******REMOVED***


PyAPI_FUNC(PyObject ****REMOVED*** PyWeakref_NewRef(PyObject *ob,
                                              PyObject *callback***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyWeakref_NewProxy(PyObject *ob,
                                                PyObject *callback***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyWeakref_GetObject(PyObject *ref***REMOVED***;

PyAPI_FUNC(Py_ssize_t***REMOVED*** _PyWeakref_GetWeakrefCount(PyWeakReference *head***REMOVED***;

PyAPI_FUNC(void***REMOVED*** _PyWeakref_ClearRef(PyWeakReference *self***REMOVED***;

/* Explanation for the Py_REFCNT(***REMOVED*** check: when a weakref's target is part
   of a long chain of deallocations which triggers the trashcan mechanism,
   clearing the weakrefs can be delayed long after the target's refcount
   has dropped to zero.  In the meantime, code accessing the weakref will
   be able to "see" the target object even though it is supposed to be
   unreachable.  See issue #16602. */

#define PyWeakref_GET_OBJECT(ref***REMOVED***                           \
    (Py_REFCNT(((PyWeakReference ****REMOVED***(ref***REMOVED******REMOVED***->wr_object***REMOVED*** > 0   \
     ? ((PyWeakReference ****REMOVED***(ref***REMOVED******REMOVED***->wr_object                \
     : Py_None***REMOVED***


#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_WEAKREFOBJECT_H */
