/* ByteArray object interface */

#ifndef Py_BYTEARRAYOBJECT_H
#define Py_BYTEARRAYOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

#include <stdarg.h>

/* Type PyByteArrayObject represents a mutable array of bytes.
 * The Python API is that of a sequence;
 * the bytes are mapped to ints in [0, 256***REMOVED***.
 * Bytes are not characters; they may be used to encode characters.
 * The only way to go between bytes and str/unicode is via encoding
 * and decoding.
 * For the convenience of C programmers, the bytes type is considered
 * to contain a char pointer, not an unsigned char pointer.
 */

/* Object layout */
typedef struct {
    PyObject_VAR_HEAD
    /* XXX(nnorwitz***REMOVED***: should ob_exports be Py_ssize_t? */
    int ob_exports; /* how many buffer exports */
    Py_ssize_t ob_alloc; /* How many bytes allocated */
    char *ob_bytes;
***REMOVED*** PyByteArrayObject;

/* Type object */
PyAPI_DATA(PyTypeObject***REMOVED*** PyByteArray_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyByteArrayIter_Type;

/* Type check macros */
#define PyByteArray_Check(self***REMOVED*** PyObject_TypeCheck(self, &PyByteArray_Type***REMOVED***
#define PyByteArray_CheckExact(self***REMOVED*** (Py_TYPE(self***REMOVED*** == &PyByteArray_Type***REMOVED***

/* Direct API functions */
PyAPI_FUNC(PyObject ****REMOVED*** PyByteArray_FromObject(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyByteArray_Concat(PyObject *, PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyByteArray_FromStringAndSize(const char *, Py_ssize_t***REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyByteArray_Size(PyObject ****REMOVED***;
PyAPI_FUNC(char ****REMOVED*** PyByteArray_AsString(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyByteArray_Resize(PyObject *, Py_ssize_t***REMOVED***;

/* Macros, trading safety for speed */
#define PyByteArray_AS_STRING(self***REMOVED*** \
    (assert(PyByteArray_Check(self***REMOVED******REMOVED***, \
     Py_SIZE(self***REMOVED*** ? ((PyByteArrayObject ****REMOVED***(self***REMOVED******REMOVED***->ob_bytes : _PyByteArray_empty_string***REMOVED***
#define PyByteArray_GET_SIZE(self***REMOVED***  (assert(PyByteArray_Check(self***REMOVED******REMOVED***,Py_SIZE(self***REMOVED******REMOVED***

PyAPI_DATA(char***REMOVED*** _PyByteArray_empty_string[***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_BYTEARRAYOBJECT_H */
