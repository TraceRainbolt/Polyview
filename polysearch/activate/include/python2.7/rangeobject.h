
/* Range object interface */

#ifndef Py_RANGEOBJECT_H
#define Py_RANGEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/* This is about the type 'xrange', not the built-in function range(***REMOVED***, which
   returns regular lists. */

/*
A range object represents an integer range.  This is an immutable object;
a range cannot change its value after creation.

Range objects behave like the corresponding tuple objects except that
they are represented by a start, stop, and step datamembers.
*/

PyAPI_DATA(PyTypeObject***REMOVED*** PyRange_Type;

#define PyRange_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyRange_Type***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_RANGEOBJECT_H */
