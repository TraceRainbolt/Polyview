
/* Float object interface */

/*
PyFloatObject represents a (double precision***REMOVED*** floating point number.
*/

#ifndef Py_FLOATOBJECT_H
#define Py_FLOATOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    PyObject_HEAD
    double ob_fval;
***REMOVED*** PyFloatObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyFloat_Type;

#define PyFloat_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyFloat_Type***REMOVED***
#define PyFloat_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyFloat_Type***REMOVED***

/* The str(***REMOVED*** precision PyFloat_STR_PRECISION is chosen so that in most cases,
   the rounding noise created by various operations is suppressed, while
   giving plenty of precision for practical use. */

#define PyFloat_STR_PRECISION 12

#ifdef Py_NAN
#define Py_RETURN_NAN return PyFloat_FromDouble(Py_NAN***REMOVED***
#endif

#define Py_RETURN_INF(sign***REMOVED*** do					\
	if (copysign(1., sign***REMOVED*** == 1.***REMOVED*** {				\
		return PyFloat_FromDouble(Py_HUGE_VAL***REMOVED***;	\
	***REMOVED*** else {						\
		return PyFloat_FromDouble(-Py_HUGE_VAL***REMOVED***;	\
	***REMOVED*** while(0***REMOVED***

PyAPI_FUNC(double***REMOVED*** PyFloat_GetMax(void***REMOVED***;
PyAPI_FUNC(double***REMOVED*** PyFloat_GetMin(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFloat_GetInfo(void***REMOVED***;

/* Return Python float from string PyObject.  Second argument ignored on
   input, and, if non-NULL, NULL is stored into *junk (this tried to serve a
   purpose once but can't be made to work as intended***REMOVED***. */
PyAPI_FUNC(PyObject ****REMOVED*** PyFloat_FromString(PyObject*, char** junk***REMOVED***;

/* Return Python float from C double. */
PyAPI_FUNC(PyObject ****REMOVED*** PyFloat_FromDouble(double***REMOVED***;

/* Extract C double from Python float.  The macro version trades safety for
   speed. */
PyAPI_FUNC(double***REMOVED*** PyFloat_AsDouble(PyObject ****REMOVED***;
#define PyFloat_AS_DOUBLE(op***REMOVED*** (((PyFloatObject ****REMOVED***(op***REMOVED******REMOVED***->ob_fval***REMOVED***

/* Write repr(v***REMOVED*** into the char buffer argument, followed by null byte.  The
   buffer must be "big enough"; >= 100 is very safe.
   PyFloat_AsReprString(buf, x***REMOVED*** strives to print enough digits so that
   PyFloat_FromString(buf***REMOVED*** then reproduces x exactly. */
PyAPI_FUNC(void***REMOVED*** PyFloat_AsReprString(char*, PyFloatObject *v***REMOVED***;

/* Write str(v***REMOVED*** into the char buffer argument, followed by null byte.  The
   buffer must be "big enough"; >= 100 is very safe.  Note that it's
   unusual to be able to get back the float you started with from
   PyFloat_AsString's result -- use PyFloat_AsReprString(***REMOVED*** if you want to
   preserve precision across conversions. */
PyAPI_FUNC(void***REMOVED*** PyFloat_AsString(char*, PyFloatObject *v***REMOVED***;

/* _PyFloat_{Pack,Unpack***REMOVED***{4,8***REMOVED***
 *
 * The struct and pickle (at least***REMOVED*** modules need an efficient platform-
 * independent way to store floating-point values as byte strings.
 * The Pack routines produce a string from a C double, and the Unpack
 * routines produce a C double from such a string.  The suffix (4 or 8***REMOVED***
 * specifies the number of bytes in the string.
 *
 * On platforms that appear to use (see _PyFloat_Init(***REMOVED******REMOVED*** IEEE-754 formats
 * these functions work by copying bits.  On other platforms, the formats the
 * 4- byte format is identical to the IEEE-754 single precision format, and
 * the 8-byte format to the IEEE-754 double precision format, although the
 * packing of INFs and NaNs (if such things exist on the platform***REMOVED*** isn't
 * handled correctly, and attempting to unpack a string containing an IEEE
 * INF or NaN will raise an exception.
 *
 * On non-IEEE platforms with more precision, or larger dynamic range, than
 * 754 supports, not all values can be packed; on non-IEEE platforms with less
 * precision, or smaller dynamic range, not all values can be unpacked.  What
 * happens in such cases is partly accidental (alas***REMOVED***.
 */

/* The pack routines write 4 or 8 bytes, starting at p.  le is a bool
 * argument, true if you want the string in little-endian format (exponent
 * last, at p+3 or p+7***REMOVED***, false if you want big-endian format (exponent
 * first, at p***REMOVED***.
 * Return value:  0 if all is OK, -1 if error (and an exception is
 * set, most likely OverflowError***REMOVED***.
 * There are two problems on non-IEEE platforms:
 * 1***REMOVED***:  What this does is undefined if x is a NaN or infinity.
 * 2***REMOVED***:  -0.0 and +0.0 produce the same string.
 */
PyAPI_FUNC(int***REMOVED*** _PyFloat_Pack4(double x, unsigned char *p, int le***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyFloat_Pack8(double x, unsigned char *p, int le***REMOVED***;

/* Used to get the important decimal digits of a double */
PyAPI_FUNC(int***REMOVED*** _PyFloat_Digits(char *buf, double v, int *signum***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyFloat_DigitsInit(void***REMOVED***;

/* The unpack routines read 4 or 8 bytes, starting at p.  le is a bool
 * argument, true if the string is in little-endian format (exponent
 * last, at p+3 or p+7***REMOVED***, false if big-endian (exponent first, at p***REMOVED***.
 * Return value:  The unpacked double.  On error, this is -1.0 and
 * PyErr_Occurred(***REMOVED*** is true (and an exception is set, most likely
 * OverflowError***REMOVED***.  Note that on a non-IEEE platform this will refuse
 * to unpack a string that represents a NaN or infinity.
 */
PyAPI_FUNC(double***REMOVED*** _PyFloat_Unpack4(const unsigned char *p, int le***REMOVED***;
PyAPI_FUNC(double***REMOVED*** _PyFloat_Unpack8(const unsigned char *p, int le***REMOVED***;

/* free list api */
PyAPI_FUNC(int***REMOVED*** PyFloat_ClearFreeList(void***REMOVED***;

/* Format the object based on the format_spec, as defined in PEP 3101
   (Advanced String Formatting***REMOVED***. */
PyAPI_FUNC(PyObject ****REMOVED*** _PyFloat_FormatAdvanced(PyObject *obj,
					       char *format_spec,
					       Py_ssize_t format_spec_len***REMOVED***;

/* Round a C double x to the closest multiple of 10**-ndigits.  Returns a
   Python float on success, or NULL (with an appropriate exception set***REMOVED*** on
   failure.  Used in builtin_round in bltinmodule.c. */
PyAPI_FUNC(PyObject ****REMOVED*** _Py_double_round(double x, int ndigits***REMOVED***;



#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_FLOATOBJECT_H */
