
#ifndef Py_PYGETOPT_H
#define Py_PYGETOPT_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(int***REMOVED*** _PyOS_opterr;
PyAPI_DATA(int***REMOVED*** _PyOS_optind;
PyAPI_DATA(char ****REMOVED*** _PyOS_optarg;

PyAPI_FUNC(void***REMOVED*** _PyOS_ResetGetOpt(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyOS_GetOpt(int argc, char **argv, char *optstring***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_PYGETOPT_H */
