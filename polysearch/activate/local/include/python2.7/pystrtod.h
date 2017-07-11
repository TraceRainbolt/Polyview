#ifndef Py_STRTOD_H
#define Py_STRTOD_H

#ifdef __cplusplus
extern "C" {
#endif


PyAPI_FUNC(double***REMOVED*** PyOS_ascii_strtod(const char *str, char **ptr***REMOVED***;
PyAPI_FUNC(double***REMOVED*** PyOS_ascii_atof(const char *str***REMOVED***;

/* Deprecated in 2.7 and 3.1. Will disappear in 2.8 (if it exists***REMOVED*** and 3.2 */
PyAPI_FUNC(char ****REMOVED*** PyOS_ascii_formatd(char *buffer, size_t buf_len,
                                      const char *format, double d***REMOVED***;
PyAPI_FUNC(double***REMOVED*** PyOS_string_to_double(const char *str,
                                         char **endptr,
                                         PyObject *overflow_exception***REMOVED***;

/* The caller is responsible for calling PyMem_Free to free the buffer
   that's is returned. */
PyAPI_FUNC(char ****REMOVED*** PyOS_double_to_string(double val,
                                         char format_code,
                                         int precision,
                                         int flags,
                                         int *type***REMOVED***;

PyAPI_FUNC(double***REMOVED*** _Py_parse_inf_or_nan(const char *p, char **endptr***REMOVED***;


/* PyOS_double_to_string's "flags" parameter can be set to 0 or more of: */
#define Py_DTSF_SIGN      0x01 /* always add the sign */
#define Py_DTSF_ADD_DOT_0 0x02 /* if the result is an integer add ".0" */
#define Py_DTSF_ALT       0x04 /* "alternate" formatting. it's format_code
                                  specific */

/* PyOS_double_to_string's "type", if non-NULL, will be set to one of: */
#define Py_DTST_FINITE 0
#define Py_DTST_INFINITE 1
#define Py_DTST_NAN 2

#ifdef __cplusplus
***REMOVED***
#endif

#endif /* !Py_STRTOD_H */
