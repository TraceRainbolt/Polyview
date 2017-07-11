
#ifndef Py_COMPILE_H
#define Py_COMPILE_H

#include "code.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Public interface */
struct _node; /* Declare the existence of this type */
PyAPI_FUNC(PyCodeObject ****REMOVED*** PyNode_Compile(struct _node *, const char ****REMOVED***;

/* Future feature support */

typedef struct {
    int ff_features;      /* flags set by future statements */
    int ff_lineno;        /* line number of last future statement */
***REMOVED*** PyFutureFeatures;

#define FUTURE_NESTED_SCOPES "nested_scopes"
#define FUTURE_GENERATORS "generators"
#define FUTURE_DIVISION "division"
#define FUTURE_ABSOLUTE_IMPORT "absolute_import"
#define FUTURE_WITH_STATEMENT "with_statement"
#define FUTURE_PRINT_FUNCTION "print_function"
#define FUTURE_UNICODE_LITERALS "unicode_literals"


struct _mod; /* Declare the existence of this type */
PyAPI_FUNC(PyCodeObject ****REMOVED*** PyAST_Compile(struct _mod *, const char *,
					PyCompilerFlags *, PyArena ****REMOVED***;
PyAPI_FUNC(PyFutureFeatures ****REMOVED*** PyFuture_FromAST(struct _mod *, const char ****REMOVED***;


#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_COMPILE_H */
