
/* Parser-tokenizer link interface */

#ifndef Py_PARSETOK_H
#define Py_PARSETOK_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    int error;
    const char *filename;
    int lineno;
    int offset;
    char *text;
    int token;
    int expected;
***REMOVED*** perrdetail;

#if 0
#define PyPARSE_YIELD_IS_KEYWORD	0x0001
#endif

#define PyPARSE_DONT_IMPLY_DEDENT	0x0002

#if 0
#define PyPARSE_WITH_IS_KEYWORD		0x0003
#endif

#define PyPARSE_PRINT_IS_FUNCTION       0x0004
#define PyPARSE_UNICODE_LITERALS        0x0008



PyAPI_FUNC(node ****REMOVED*** PyParser_ParseString(const char *, grammar *, int,
                                              perrdetail ****REMOVED***;
PyAPI_FUNC(node ****REMOVED*** PyParser_ParseFile (FILE *, const char *, grammar *, int,
                                             char *, char *, perrdetail ****REMOVED***;

PyAPI_FUNC(node ****REMOVED*** PyParser_ParseStringFlags(const char *, grammar *, int,
                                              perrdetail *, int***REMOVED***;
PyAPI_FUNC(node ****REMOVED*** PyParser_ParseFileFlags(FILE *, const char *, grammar *,
						 int, char *, char *,
						 perrdetail *, int***REMOVED***;
PyAPI_FUNC(node ****REMOVED*** PyParser_ParseFileFlagsEx(FILE *, const char *, grammar *,
						 int, char *, char *,
						 perrdetail *, int ****REMOVED***;

PyAPI_FUNC(node ****REMOVED*** PyParser_ParseStringFlagsFilename(const char *,
					      const char *,
					      grammar *, int,
                                              perrdetail *, int***REMOVED***;
PyAPI_FUNC(node ****REMOVED*** PyParser_ParseStringFlagsFilenameEx(const char *,
					      const char *,
					      grammar *, int,
                                              perrdetail *, int ****REMOVED***;

/* Note that he following function is defined in pythonrun.c not parsetok.c. */
PyAPI_FUNC(void***REMOVED*** PyParser_SetError(perrdetail ****REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_PARSETOK_H */
