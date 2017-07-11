/* Complex number structure */

#ifndef Py_COMPLEXOBJECT_H
#define Py_COMPLEXOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    double real;
    double imag;
***REMOVED*** Py_complex;

/* Operations on complex numbers from complexmodule.c */

#define c_sum _Py_c_sum
#define c_diff _Py_c_diff
#define c_neg _Py_c_neg
#define c_prod _Py_c_prod
#define c_quot _Py_c_quot
#define c_pow _Py_c_pow
#define c_abs _Py_c_abs

PyAPI_FUNC(Py_complex***REMOVED*** c_sum(Py_complex, Py_complex***REMOVED***;
PyAPI_FUNC(Py_complex***REMOVED*** c_diff(Py_complex, Py_complex***REMOVED***;
PyAPI_FUNC(Py_complex***REMOVED*** c_neg(Py_complex***REMOVED***;
PyAPI_FUNC(Py_complex***REMOVED*** c_prod(Py_complex, Py_complex***REMOVED***;
PyAPI_FUNC(Py_complex***REMOVED*** c_quot(Py_complex, Py_complex***REMOVED***;
PyAPI_FUNC(Py_complex***REMOVED*** c_pow(Py_complex, Py_complex***REMOVED***;
PyAPI_FUNC(double***REMOVED*** c_abs(Py_complex***REMOVED***;


/* Complex object interface */

/*
PyComplexObject represents a complex number with double-precision
real and imaginary parts.
*/

typedef struct {
    PyObject_HEAD
    Py_complex cval;
***REMOVED*** PyComplexObject;     

PyAPI_DATA(PyTypeObject***REMOVED*** PyComplex_Type;

#define PyComplex_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyComplex_Type***REMOVED***
#define PyComplex_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyComplex_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyComplex_FromCComplex(Py_complex***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyComplex_FromDoubles(double real, double imag***REMOVED***;

PyAPI_FUNC(double***REMOVED*** PyComplex_RealAsDouble(PyObject *op***REMOVED***;
PyAPI_FUNC(double***REMOVED*** PyComplex_ImagAsDouble(PyObject *op***REMOVED***;
PyAPI_FUNC(Py_complex***REMOVED*** PyComplex_AsCComplex(PyObject *op***REMOVED***;

/* Format the object based on the format_spec, as defined in PEP 3101
   (Advanced String Formatting***REMOVED***. */
PyAPI_FUNC(PyObject ****REMOVED*** _PyComplex_FormatAdvanced(PyObject *obj,
                                                 char *format_spec,
                                                 Py_ssize_t format_spec_len***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_COMPLEXOBJECT_H */
