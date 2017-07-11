
/* String (str/bytes***REMOVED*** object interface */

#ifndef Py_STRINGOBJECT_H
#define Py_STRINGOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

#include <stdarg.h>

/*
Type PyStringObject represents a character string.  An extra zero byte is
reserved at the end to ensure it is zero-terminated, but a size is
present so strings with null bytes in them can be represented.  This
is an immutable object type.

There are functions to create new string objects, to test
an object for string-ness, and to get the
string value.  The latter function returns a null pointer
if the object is not of the proper type.
There is a variant that takes an explicit size as well as a
variant that assumes a zero-terminated string.  Note that none of the
functions should be applied to nil objects.
*/

/* Caching the hash (ob_shash***REMOVED*** saves recalculation of a string's hash value.
   Interning strings (ob_sstate***REMOVED*** tries to ensure that only one string
   object with a given value exists, so equality tests can be one pointer
   comparison.  This is generally restricted to strings that "look like"
   Python identifiers, although the intern(***REMOVED*** builtin can be used to force
   interning of any string.
   Together, these sped the interpreter by up to 20%. */

typedef struct {
    PyObject_VAR_HEAD
    long ob_shash;
    int ob_sstate;
    char ob_sval[1***REMOVED***;

    /* Invariants:
     *     ob_sval contains space for 'ob_size+1' elements.
     *     ob_sval[ob_size***REMOVED*** == 0.
     *     ob_shash is the hash of the string or -1 if not computed yet.
     *     ob_sstate != 0 iff the string object is in stringobject.c's
     *       'interned' dictionary; in this case the two references
     *       from 'interned' to this object are *not counted* in ob_refcnt.
     */
***REMOVED*** PyStringObject;

#define SSTATE_NOT_INTERNED 0
#define SSTATE_INTERNED_MORTAL 1
#define SSTATE_INTERNED_IMMORTAL 2

PyAPI_DATA(PyTypeObject***REMOVED*** PyBaseString_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyString_Type;

#define PyString_Check(op***REMOVED*** \
                 PyType_FastSubclass(Py_TYPE(op***REMOVED***, Py_TPFLAGS_STRING_SUBCLASS***REMOVED***
#define PyString_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyString_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyString_FromStringAndSize(const char *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyString_FromString(const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyString_FromFormatV(const char*, va_list***REMOVED***
				Py_GCC_ATTRIBUTE((format(printf, 1, 0***REMOVED******REMOVED******REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyString_FromFormat(const char*, ...***REMOVED***
				Py_GCC_ATTRIBUTE((format(printf, 1, 2***REMOVED******REMOVED******REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyString_Size(PyObject ****REMOVED***;
PyAPI_FUNC(char ****REMOVED*** PyString_AsString(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyString_Repr(PyObject *, int***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyString_Concat(PyObject **, PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyString_ConcatAndDel(PyObject **, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyString_Resize(PyObject **, Py_ssize_t***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyString_Eq(PyObject *, PyObject****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyString_Format(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyString_FormatLong(PyObject*, int, int,
						  int, char**, int****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyString_DecodeEscape(const char *, Py_ssize_t, 
						   const char *, Py_ssize_t,
						   const char ****REMOVED***;

PyAPI_FUNC(void***REMOVED*** PyString_InternInPlace(PyObject *****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyString_InternImmortal(PyObject *****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyString_InternFromString(const char ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _Py_ReleaseInternedStrings(void***REMOVED***;

/* Use only if you know it's a string */
#define PyString_CHECK_INTERNED(op***REMOVED*** (((PyStringObject ****REMOVED***(op***REMOVED******REMOVED***->ob_sstate***REMOVED***

/* Macro, trading safety for speed */
#define PyString_AS_STRING(op***REMOVED*** (((PyStringObject ****REMOVED***(op***REMOVED******REMOVED***->ob_sval***REMOVED***
#define PyString_GET_SIZE(op***REMOVED***  Py_SIZE(op***REMOVED***

/* _PyString_Join(sep, x***REMOVED*** is like sep.join(x***REMOVED***.  sep must be PyStringObject*,
   x must be an iterable object. */
PyAPI_FUNC(PyObject ****REMOVED*** _PyString_Join(PyObject *sep, PyObject *x***REMOVED***;

/* --- Generic Codecs ----------------------------------------------------- */

/* Create an object by decoding the encoded string s of the
   given size. */

PyAPI_FUNC(PyObject****REMOVED*** PyString_Decode(
    const char *s,              /* encoded string */
    Py_ssize_t size,            /* size of buffer */
    const char *encoding,       /* encoding */
    const char *errors          /* error handling */
    ***REMOVED***;

/* Encodes a char buffer of the given size and returns a 
   Python object. */

PyAPI_FUNC(PyObject****REMOVED*** PyString_Encode(
    const char *s,              /* string char buffer */
    Py_ssize_t size,            /* number of chars to encode */
    const char *encoding,       /* encoding */
    const char *errors          /* error handling */
    ***REMOVED***;

/* Encodes a string object and returns the result as Python 
   object. */

PyAPI_FUNC(PyObject****REMOVED*** PyString_AsEncodedObject(
    PyObject *str,	 	/* string object */
    const char *encoding,	/* encoding */
    const char *errors		/* error handling */
    ***REMOVED***;

/* Encodes a string object and returns the result as Python string
   object.   
   
   If the codec returns an Unicode object, the object is converted
   back to a string using the default encoding.

   DEPRECATED - use PyString_AsEncodedObject(***REMOVED*** instead. */

PyAPI_FUNC(PyObject****REMOVED*** PyString_AsEncodedString(
    PyObject *str,	 	/* string object */
    const char *encoding,	/* encoding */
    const char *errors		/* error handling */
    ***REMOVED***;

/* Decodes a string object and returns the result as Python 
   object. */

PyAPI_FUNC(PyObject****REMOVED*** PyString_AsDecodedObject(
    PyObject *str,	 	/* string object */
    const char *encoding,	/* encoding */
    const char *errors		/* error handling */
    ***REMOVED***;

/* Decodes a string object and returns the result as Python string
   object.  
   
   If the codec returns an Unicode object, the object is converted
   back to a string using the default encoding.

   DEPRECATED - use PyString_AsDecodedObject(***REMOVED*** instead. */

PyAPI_FUNC(PyObject****REMOVED*** PyString_AsDecodedString(
    PyObject *str,	 	/* string object */
    const char *encoding,	/* encoding */
    const char *errors		/* error handling */
    ***REMOVED***;

/* Provides access to the internal data buffer and size of a string
   object or the default encoded version of an Unicode object. Passing
   NULL as *len parameter will force the string buffer to be
   0-terminated (passing a string with embedded NULL characters will
   cause an exception***REMOVED***.  */

PyAPI_FUNC(int***REMOVED*** PyString_AsStringAndSize(
    register PyObject *obj,	/* string or Unicode object */
    register char **s,		/* pointer to buffer variable */
    register Py_ssize_t *len	/* pointer to length variable or NULL
				   (only possible for 0-terminated
				   strings***REMOVED*** */
    ***REMOVED***;


/* Using the current locale, insert the thousands grouping
   into the string pointed to by buffer.  For the argument descriptions,
   see Objects/stringlib/localeutil.h */
PyAPI_FUNC(Py_ssize_t***REMOVED*** _PyString_InsertThousandsGroupingLocale(char *buffer,
                                  Py_ssize_t n_buffer,
                                  char *digits,
                                  Py_ssize_t n_digits,
                                  Py_ssize_t min_width***REMOVED***;

/* Using explicit passed-in values, insert the thousands grouping
   into the string pointed to by buffer.  For the argument descriptions,
   see Objects/stringlib/localeutil.h */
PyAPI_FUNC(Py_ssize_t***REMOVED*** _PyString_InsertThousandsGrouping(char *buffer,
                                  Py_ssize_t n_buffer,
                                  char *digits,
                                  Py_ssize_t n_digits,
                                  Py_ssize_t min_width,
                                  const char *grouping,
                                  const char *thousands_sep***REMOVED***;

/* Format the object based on the format_spec, as defined in PEP 3101
   (Advanced String Formatting***REMOVED***. */
PyAPI_FUNC(PyObject ****REMOVED*** _PyBytes_FormatAdvanced(PyObject *obj,
					       char *format_spec,
					       Py_ssize_t format_spec_len***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_STRINGOBJECT_H */
