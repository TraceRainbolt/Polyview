#ifndef Py_LONGOBJECT_H
#define Py_LONGOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


/* Long (arbitrary precision***REMOVED*** integer object interface */

typedef struct _longobject PyLongObject; /* Revealed in longintrepr.h */

PyAPI_DATA(PyTypeObject***REMOVED*** PyLong_Type;

#define PyLong_Check(op***REMOVED*** \
		PyType_FastSubclass(Py_TYPE(op***REMOVED***, Py_TPFLAGS_LONG_SUBCLASS***REMOVED***
#define PyLong_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyLong_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromLong(long***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromUnsignedLong(unsigned long***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromDouble(double***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromSize_t(size_t***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromSsize_t(Py_ssize_t***REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyLong_AsLong(PyObject ****REMOVED***;
PyAPI_FUNC(long***REMOVED*** PyLong_AsLongAndOverflow(PyObject *, int ****REMOVED***;
PyAPI_FUNC(unsigned long***REMOVED*** PyLong_AsUnsignedLong(PyObject ****REMOVED***;
PyAPI_FUNC(unsigned long***REMOVED*** PyLong_AsUnsignedLongMask(PyObject ****REMOVED***;
PyAPI_FUNC(Py_ssize_t***REMOVED*** PyLong_AsSsize_t(PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyLong_AsInt(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_GetInfo(void***REMOVED***;

/* For use by intobject.c only */
#define _PyLong_AsSsize_t PyLong_AsSsize_t
#define _PyLong_FromSize_t PyLong_FromSize_t
#define _PyLong_FromSsize_t PyLong_FromSsize_t
PyAPI_DATA(int***REMOVED*** _PyLong_DigitValue[256***REMOVED***;

/* _PyLong_Frexp returns a double x and an exponent e such that the
   true value is approximately equal to x * 2**e.  e is >= 0.  x is
   0.0 if and only if the input is 0 (in which case, e and x are both
   zeroes***REMOVED***; otherwise, 0.5 <= abs(x***REMOVED*** < 1.0.  On overflow, which is
   possible if the number of bits doesn't fit into a Py_ssize_t, sets
   OverflowError and returns -1.0 for x, 0 for e. */
PyAPI_FUNC(double***REMOVED*** _PyLong_Frexp(PyLongObject *a, Py_ssize_t *e***REMOVED***;

PyAPI_FUNC(double***REMOVED*** PyLong_AsDouble(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromVoidPtr(void ****REMOVED***;
PyAPI_FUNC(void ****REMOVED*** PyLong_AsVoidPtr(PyObject ****REMOVED***;

#ifdef HAVE_LONG_LONG
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromLongLong(PY_LONG_LONG***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromUnsignedLongLong(unsigned PY_LONG_LONG***REMOVED***;
PyAPI_FUNC(PY_LONG_LONG***REMOVED*** PyLong_AsLongLong(PyObject ****REMOVED***;
PyAPI_FUNC(unsigned PY_LONG_LONG***REMOVED*** PyLong_AsUnsignedLongLong(PyObject ****REMOVED***;
PyAPI_FUNC(unsigned PY_LONG_LONG***REMOVED*** PyLong_AsUnsignedLongLongMask(PyObject ****REMOVED***;
PyAPI_FUNC(PY_LONG_LONG***REMOVED*** PyLong_AsLongLongAndOverflow(PyObject *, int ****REMOVED***;
#endif /* HAVE_LONG_LONG */

PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromString(char *, char **, int***REMOVED***;
#ifdef Py_USING_UNICODE
PyAPI_FUNC(PyObject ****REMOVED*** PyLong_FromUnicode(Py_UNICODE*, Py_ssize_t, int***REMOVED***;
#endif

/* _PyLong_Sign.  Return 0 if v is 0, -1 if v < 0, +1 if v > 0.
   v must not be NULL, and must be a normalized long.
   There are no error cases.
*/
PyAPI_FUNC(int***REMOVED*** _PyLong_Sign(PyObject *v***REMOVED***;


/* _PyLong_NumBits.  Return the number of bits needed to represent the
   absolute value of a long.  For example, this returns 1 for 1 and -1, 2
   for 2 and -2, and 2 for 3 and -3.  It returns 0 for 0.
   v must not be NULL, and must be a normalized long.
   (size_t***REMOVED***-1 is returned and OverflowError set if the true result doesn't
   fit in a size_t.
*/
PyAPI_FUNC(size_t***REMOVED*** _PyLong_NumBits(PyObject *v***REMOVED***;

/* _PyLong_FromByteArray:  View the n unsigned bytes as a binary integer in
   base 256, and return a Python long with the same numeric value.
   If n is 0, the integer is 0.  Else:
   If little_endian is 1/true, bytes[n-1***REMOVED*** is the MSB and bytes[0***REMOVED*** the LSB;
   else (little_endian is 0/false***REMOVED*** bytes[0***REMOVED*** is the MSB and bytes[n-1***REMOVED*** the
   LSB.
   If is_signed is 0/false, view the bytes as a non-negative integer.
   If is_signed is 1/true, view the bytes as a 2's-complement integer,
   non-negative if bit 0x80 of the MSB is clear, negative if set.
   Error returns:
   + Return NULL with the appropriate exception set if there's not
     enough memory to create the Python long.
*/
PyAPI_FUNC(PyObject ****REMOVED*** _PyLong_FromByteArray(
	const unsigned char* bytes, size_t n,
	int little_endian, int is_signed***REMOVED***;

/* _PyLong_AsByteArray: Convert the least-significant 8*n bits of long
   v to a base-256 integer, stored in array bytes.  Normally return 0,
   return -1 on error.
   If little_endian is 1/true, store the MSB at bytes[n-1***REMOVED*** and the LSB at
   bytes[0***REMOVED***; else (little_endian is 0/false***REMOVED*** store the MSB at bytes[0***REMOVED*** and
   the LSB at bytes[n-1***REMOVED***.
   If is_signed is 0/false, it's an error if v < 0; else (v >= 0***REMOVED*** n bytes
   are filled and there's nothing special about bit 0x80 of the MSB.
   If is_signed is 1/true, bytes is filled with the 2's-complement
   representation of v's value.  Bit 0x80 of the MSB is the sign bit.
   Error returns (-1***REMOVED***:
   + is_signed is 0 and v < 0.  TypeError is set in this case, and bytes
     isn't altered.
   + n isn't big enough to hold the full mathematical value of v.  For
     example, if is_signed is 0 and there are more digits in the v than
     fit in n; or if is_signed is 1, v < 0, and n is just 1 bit shy of
     being large enough to hold a sign bit.  OverflowError is set in this
     case, but bytes holds the least-signficant n bytes of the true value.
*/
PyAPI_FUNC(int***REMOVED*** _PyLong_AsByteArray(PyLongObject* v,
	unsigned char* bytes, size_t n,
	int little_endian, int is_signed***REMOVED***;

/* _PyLong_Format: Convert the long to a string object with given base,
   appending a base prefix of 0[box***REMOVED*** if base is 2, 8 or 16.
   Add a trailing "L" if addL is non-zero.
   If newstyle is zero, then use the pre-2.6 behavior of octal having
   a leading "0", instead of the prefix "0o" */
PyAPI_FUNC(PyObject ****REMOVED*** _PyLong_Format(PyObject *aa, int base, int addL, int newstyle***REMOVED***;

/* Format the object based on the format_spec, as defined in PEP 3101
   (Advanced String Formatting***REMOVED***. */
PyAPI_FUNC(PyObject ****REMOVED*** _PyLong_FormatAdvanced(PyObject *obj,
					      char *format_spec,
					      Py_ssize_t format_spec_len***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_LONGOBJECT_H */
