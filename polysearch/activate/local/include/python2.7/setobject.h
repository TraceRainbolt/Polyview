/* Set object interface */

#ifndef Py_SETOBJECT_H
#define Py_SETOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


/*
There are three kinds of slots in the table:

1. Unused:  key == NULL
2. Active:  key != NULL and key != dummy
3. Dummy:   key == dummy

Note: .pop(***REMOVED*** abuses the hash field of an Unused or Dummy slot to
hold a search finger.  The hash field of Unused or Dummy slots has
no meaning otherwise.
*/

#define PySet_MINSIZE 8

typedef struct {
    long hash;      /* cached hash code for the entry key */
    PyObject *key;
***REMOVED*** setentry;


/*
This data structure is shared by set and frozenset objects.
*/

typedef struct _setobject PySetObject;
struct _setobject {
    PyObject_HEAD

    Py_ssize_t fill;  /* # Active + # Dummy */
    Py_ssize_t used;  /* # Active */

    /* The table contains mask + 1 slots, and that's a power of 2.
     * We store the mask instead of the size because the mask is more
     * frequently needed.
     */
    Py_ssize_t mask;

    /* table points to smalltable for small tables, else to
     * additional malloc'ed memory.  table is never NULL!  This rule
     * saves repeated runtime null-tests.
     */
    setentry *table;
    setentry *(*lookup***REMOVED***(PySetObject *so, PyObject *key, long hash***REMOVED***;
    setentry smalltable[PySet_MINSIZE***REMOVED***;

    long hash;                  /* only used by frozenset objects */
    PyObject *weakreflist;      /* List of weak references */
***REMOVED***;

PyAPI_DATA(PyTypeObject***REMOVED*** PySet_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyFrozenSet_Type;

/* Invariants for frozensets:
 *     data is immutable.
 *     hash is the hash of the frozenset or -1 if not computed yet.
 * Invariants for sets:
 *     hash is -1
 */

#define PyFrozenSet_CheckExact(ob***REMOVED*** (Py_TYPE(ob***REMOVED*** == &PyFrozenSet_Type***REMOVED***
#define PyAnySet_CheckExact(ob***REMOVED*** \
    (Py_TYPE(ob***REMOVED*** == &PySet_Type || Py_TYPE(ob***REMOVED*** == &PyFrozenSet_Type***REMOVED***
#define PyAnySet_Check(ob***REMOVED*** \
    (Py_TYPE(ob***REMOVED*** == &PySet_Type || Py_TYPE(ob***REMOVED*** == &PyFrozenSet_Type || \
      PyType_IsSubtype(Py_TYPE(ob***REMOVED***, &PySet_Type***REMOVED*** || \
      PyType_IsSubtype(Py_TYPE(ob***REMOVED***, &PyFrozenSet_Type***REMOVED******REMOVED***
#define PySet_Check(ob***REMOVED*** \
    (Py_TYPE(ob***REMOVED*** == &PySet_Type || \
    PyType_IsSubtype(Py_TYPE(ob***REMOVED***, &PySet_Type***REMOVED******REMOVED***
#define   PyFrozenSet_Check(ob***REMOVED*** \
    (Py_TYPE(ob***REMOVED*** == &PyFrozenSet_Type || \
      PyType_IsSubtype(Py_TYPE(ob***REMOVED***, &PyFrozenSet_Type***REMOVED******REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PySet_New(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFrozenSet_New(PyObject ****REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PySet_Size(PyObject *anyset***REMOVED***;
#define PySet_GET_SIZE(so***REMOVED*** (((PySetObject ****REMOVED***(so***REMOVED******REMOVED***->used***REMOVED***
PyAPI_FUNC(int***REMOVED*** PySet_Clear(PyObject *set***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PySet_Contains(PyObject *anyset, PyObject *key***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PySet_Discard(PyObject *set, PyObject *key***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PySet_Add(PyObject *set, PyObject *key***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PySet_Next(PyObject *set, Py_ssize_t *pos, PyObject **key***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PySet_NextEntry(PyObject *set, Py_ssize_t *pos, PyObject **key, long *hash***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PySet_Pop(PyObject *set***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PySet_Update(PyObject *set, PyObject *iterable***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_SETOBJECT_H */
