
/* Integer object interface */

/*
PyIntObject represents a (long***REMOVED*** integer.  This is an immutable object;
an integer cannot change its value after creation.

There are functions to create new integer objects, to test an object
for integer-ness, and to get the integer value.  The latter functions
returns -1 and sets errno to EBADF if the object is not an PyIntObject.
None of the functions should be applied to nil objects.

The type PyIntObject is (unfortunately***REMOVED*** exposed here so we can declare
_Py_TrueStruct and _Py_ZeroStruct in boolobject.h; don't use this.
*/

#ifndef Py_INTOBJECT_H
#define Py_INTOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    PyObject_HEAD
    long ob_ival;
***REMOVED*** PyIntObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyInt_Type;

#define PyInt_Check(op***REMOVED*** \
		 PyType_FastSubclass((op***REMOVED***->ob_type, Py_TPFLAGS_INT_SUBCLASS***REMOVED***
#define PyInt_CheckExact(op***REMOVED*** ((op***REMOVED***->ob_type == &PyInt_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyInt_FromString(char*, char**, int***REMOVED***;
#ifdef Py_USING_UNICODE
PyAPI_FUNC(PyObject ****REMOVED*** PyInt_FromUnicode(Py_UNICODE*, Py_ssize_t, int***REMOVED***;
#endif
PyAPI_FUNC(PyObject ****REMOVED*** PyInt_FromLong(long***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyInt_FromSize_t(size_t***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyInt_FromSsize_t(Py_ssize_t***REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyInt_AsLong(PyObject ****REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyInt_AsSsize_t(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyInt_AsInt(PyObject ****REMOVED***;
PyAPI_FUNC(unsigned long***REMOVED*** PyInt_AsUnsignedLongMask(PyObject ****REMOVED***;
#ifdef HAVE_LONG_LONG
PyAPI_FUNC(unsigned PY_LONG_LONG***REMOVED*** PyInt_AsUnsignedLongLongMask(PyObject ****REMOVED***;
#endif

PyAPI_FUNC(long***REMOVED*** PyInt_GetMax(void***REMOVED***;

/* Macro, trading safety for speed */
#define PyInt_AS_LONG(op***REMOVED*** (((PyIntObject ****REMOVED***(op***REMOVED******REMOVED***->ob_ival***REMOVED***

/* These aren't really part of the Int object, but they're handy; the protos
 * are necessary for systems that need the magic of PyAPI_FUNC and that want
 * to have stropmodule as a dynamically loaded module instead of building it
 * into the main Python shared library/DLL.  Guido thinks I'm weird for
 * building it this way.  :-***REMOVED***  [cjh***REMOVED***
 */
PyAPI_FUNC(unsigned long***REMOVED*** PyOS_strtoul(char *, char **, int***REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyOS_strtol(char *, char **, int***REMOVED***;

/* free list api */
PyAPI_FUNC(int***REMOVED*** PyInt_ClearFreeList(void***REMOVED***;

/* Convert an integer to the given base.  Returns a string.
   If base is 2, 8 or 16, add the proper prefix '0b', '0o' or '0x'.
   If newstyle is zero, then use the pre-2.6 behavior of octal having
   a leading "0" */
PyAPI_FUNC(PyObject****REMOVED*** _PyInt_Format(PyIntObject* v, int base, int newstyle***REMOVED***;

/* Format the object based on the format_spec, as defined in PEP 3101
   (Advanced String Formatting***REMOVED***. */
PyAPI_FUNC(PyObject ****REMOVED*** _PyInt_FormatAdvanced(PyObject *obj,
					     char *format_spec,
					     Py_ssize_t format_spec_len***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_INTOBJECT_H */
