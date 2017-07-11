#ifndef Py_DICTOBJECT_H
#define Py_DICTOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


/* Dictionary object type -- mapping from hashable object to object */

/* The distribution includes a separate file, Objects/dictnotes.txt,
   describing explorations into dictionary design and optimization.
   It covers typical dictionary use patterns, the parameters for
   tuning dictionaries, and several ideas for possible optimizations.
*/

/*
There are three kinds of slots in the table:

1. Unused.  me_key == me_value == NULL
   Does not hold an active (key, value***REMOVED*** pair now and never did.  Unused can
   transition to Active upon key insertion.  This is the only case in which
   me_key is NULL, and is each slot's initial state.

2. Active.  me_key != NULL and me_key != dummy and me_value != NULL
   Holds an active (key, value***REMOVED*** pair.  Active can transition to Dummy upon
   key deletion.  This is the only case in which me_value != NULL.

3. Dummy.  me_key == dummy and me_value == NULL
   Previously held an active (key, value***REMOVED*** pair, but that was deleted and an
   active pair has not yet overwritten the slot.  Dummy can transition to
   Active upon key insertion.  Dummy slots cannot be made Unused again
   (cannot have me_key set to NULL***REMOVED***, else the probe sequence in case of
   collision would have no way to know they were once active.

Note: .popitem(***REMOVED*** abuses the me_hash field of an Unused or Dummy slot to
hold a search finger.  The me_hash field of Unused or Dummy slots has no
meaning otherwise.
*/

/* PyDict_MINSIZE is the minimum size of a dictionary.  This many slots are
 * allocated directly in the dict object (in the ma_smalltable member***REMOVED***.
 * It must be a power of 2, and at least 4.  8 allows dicts with no more
 * than 5 active entries to live in ma_smalltable (and so avoid an
 * additional malloc***REMOVED***; instrumentation suggested this suffices for the
 * majority of dicts (consisting mostly of usually-small instance dicts and
 * usually-small dicts created to pass keyword arguments***REMOVED***.
 */
#define PyDict_MINSIZE 8

typedef struct {
    /* Cached hash code of me_key.  Note that hash codes are C longs.
     * We have to use Py_ssize_t instead because dict_popitem(***REMOVED*** abuses
     * me_hash to hold a search finger.
     */
    Py_ssize_t me_hash;
    PyObject *me_key;
    PyObject *me_value;
***REMOVED*** PyDictEntry;

/*
To ensure the lookup algorithm terminates, there must be at least one Unused
slot (NULL key***REMOVED*** in the table.
The value ma_fill is the number of non-NULL keys (sum of Active and Dummy***REMOVED***;
ma_used is the number of non-NULL, non-dummy keys (== the number of non-NULL
values == the number of Active items***REMOVED***.
To avoid slowing down lookups on a near-full table, we resize the table when
it's two-thirds full.
*/
typedef struct _dictobject PyDictObject;
struct _dictobject {
    PyObject_HEAD
    Py_ssize_t ma_fill;  /* # Active + # Dummy */
    Py_ssize_t ma_used;  /* # Active */

    /* The table contains ma_mask + 1 slots, and that's a power of 2.
     * We store the mask instead of the size because the mask is more
     * frequently needed.
     */
    Py_ssize_t ma_mask;

    /* ma_table points to ma_smalltable for small tables, else to
     * additional malloc'ed memory.  ma_table is never NULL!  This rule
     * saves repeated runtime null-tests in the workhorse getitem and
     * setitem calls.
     */
    PyDictEntry *ma_table;
    PyDictEntry *(*ma_lookup***REMOVED***(PyDictObject *mp, PyObject *key, long hash***REMOVED***;
    PyDictEntry ma_smalltable[PyDict_MINSIZE***REMOVED***;
***REMOVED***;

PyAPI_DATA(PyTypeObject***REMOVED*** PyDict_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyDictIterKey_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyDictIterValue_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyDictIterItem_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyDictKeys_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyDictItems_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyDictValues_Type;

#define PyDict_Check(op***REMOVED*** \
                 PyType_FastSubclass(Py_TYPE(op***REMOVED***, Py_TPFLAGS_DICT_SUBCLASS***REMOVED***
#define PyDict_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDict_Type***REMOVED***
#define PyDictKeys_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDictKeys_Type***REMOVED***
#define PyDictItems_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDictItems_Type***REMOVED***
#define PyDictValues_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDictValues_Type***REMOVED***
/* This excludes Values, since they are not sets. */
# define PyDictViewSet_Check(op***REMOVED*** \
    (PyDictKeys_Check(op***REMOVED*** || PyDictItems_Check(op***REMOVED******REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyDict_New(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDict_GetItem(PyObject *mp, PyObject *key***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyDict_SetItem(PyObject *mp, PyObject *key, PyObject *item***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyDict_DelItem(PyObject *mp, PyObject *key***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyDict_Clear(PyObject *mp***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyDict_Next(
    PyObject *mp, Py_ssize_t *pos, PyObject **key, PyObject **value***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyDict_Next(
    PyObject *mp, Py_ssize_t *pos, PyObject **key, PyObject **value, long *hash***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDict_Keys(PyObject *mp***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDict_Values(PyObject *mp***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDict_Items(PyObject *mp***REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyDict_Size(PyObject *mp***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDict_Copy(PyObject *mp***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyDict_Contains(PyObject *mp, PyObject *key***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyDict_Contains(PyObject *mp, PyObject *key, long hash***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyDict_NewPresized(Py_ssize_t minused***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyDict_MaybeUntrack(PyObject *mp***REMOVED***;

/* PyDict_Update(mp, other***REMOVED*** is equivalent to PyDict_Merge(mp, other, 1***REMOVED***. */
PyAPI_FUNC(int***REMOVED*** PyDict_Update(PyObject *mp, PyObject *other***REMOVED***;

/* PyDict_Merge updates/merges from a mapping object (an object that
   supports PyMapping_Keys(***REMOVED*** and PyObject_GetItem(***REMOVED******REMOVED***.  If override is true,
   the last occurrence of a key wins, else the first.  The Python
   dict.update(other***REMOVED*** is equivalent to PyDict_Merge(dict, other, 1***REMOVED***.
*/
PyAPI_FUNC(int***REMOVED*** PyDict_Merge(PyObject *mp,
                                   PyObject *other,
                                   int override***REMOVED***;

/* PyDict_MergeFromSeq2 updates/merges from an iterable object producing
   iterable objects of length 2.  If override is true, the last occurrence
   of a key wins, else the first.  The Python dict constructor dict(seq2***REMOVED***
   is equivalent to dict={***REMOVED***; PyDict_MergeFromSeq(dict, seq2, 1***REMOVED***.
*/
PyAPI_FUNC(int***REMOVED*** PyDict_MergeFromSeq2(PyObject *d,
                                           PyObject *seq2,
                                           int override***REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyDict_GetItemString(PyObject *dp, const char *key***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyDict_SetItemString(PyObject *dp, const char *key, PyObject *item***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyDict_DelItemString(PyObject *dp, const char *key***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_DICTOBJECT_H */
