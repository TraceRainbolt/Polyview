/* Definitions for bytecode */

#ifndef Py_CODE_H
#define Py_CODE_H
#ifdef __cplusplus
extern "C" {
#endif

/* Bytecode object */
typedef struct {
    PyObject_HEAD
    int co_argcount;		/* #arguments, except *args */
    int co_nlocals;		/* #local variables */
    int co_stacksize;		/* #entries needed for evaluation stack */
    int co_flags;		/* CO_..., see below */
    PyObject *co_code;		/* instruction opcodes */
    PyObject *co_consts;	/* list (constants used***REMOVED*** */
    PyObject *co_names;		/* list of strings (names used***REMOVED*** */
    PyObject *co_varnames;	/* tuple of strings (local variable names***REMOVED*** */
    PyObject *co_freevars;	/* tuple of strings (free variable names***REMOVED*** */
    PyObject *co_cellvars;      /* tuple of strings (cell variable names***REMOVED*** */
    /* The rest doesn't count for hash/cmp */
    PyObject *co_filename;	/* string (where it was loaded from***REMOVED*** */
    PyObject *co_name;		/* string (name, for reference***REMOVED*** */
    int co_firstlineno;		/* first source line number */
    PyObject *co_lnotab;	/* string (encoding addr<->lineno mapping***REMOVED*** See
				   Objects/lnotab_notes.txt for details. */
    void *co_zombieframe;     /* for optimization only (see frameobject.c***REMOVED*** */
    PyObject *co_weakreflist;   /* to support weakrefs to code objects */
***REMOVED*** PyCodeObject;

/* Masks for co_flags above */
#define CO_OPTIMIZED	0x0001
#define CO_NEWLOCALS	0x0002
#define CO_VARARGS	0x0004
#define CO_VARKEYWORDS	0x0008
#define CO_NESTED       0x0010
#define CO_GENERATOR    0x0020
/* The CO_NOFREE flag is set if there are no free or cell variables.
   This information is redundant, but it allows a single flag test
   to determine whether there is any extra work to be done when the
   call frame it setup.
*/
#define CO_NOFREE       0x0040

#if 0
/* This is no longer used.  Stopped defining in 2.5, do not re-use. */
#define CO_GENERATOR_ALLOWED    0x1000
#endif
#define CO_FUTURE_DIVISION    	0x2000
#define CO_FUTURE_ABSOLUTE_IMPORT 0x4000 /* do absolute imports by default */
#define CO_FUTURE_WITH_STATEMENT  0x8000
#define CO_FUTURE_PRINT_FUNCTION  0x10000
#define CO_FUTURE_UNICODE_LITERALS 0x20000

/* This should be defined if a future statement modifies the syntax.
   For example, when a keyword is added.
*/
#if 1
#define PY_PARSER_REQUIRES_FUTURE_KEYWORD
#endif

#define CO_MAXBLOCKS 20 /* Max static block nesting within a function */

PyAPI_DATA(PyTypeObject***REMOVED*** PyCode_Type;

#define PyCode_Check(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyCode_Type***REMOVED***
#define PyCode_GetNumFree(op***REMOVED*** (PyTuple_GET_SIZE((op***REMOVED***->co_freevars***REMOVED******REMOVED***

/* Public interface */
PyAPI_FUNC(PyCodeObject ****REMOVED*** PyCode_New(
	int, int, int, int, PyObject *, PyObject *, PyObject *, PyObject *,
	PyObject *, PyObject *, PyObject *, PyObject *, int, PyObject ****REMOVED***; 
        /* same as struct above */

/* Creates a new empty code object with the specified source location. */
PyAPI_FUNC(PyCodeObject ****REMOVED***
PyCode_NewEmpty(const char *filename, const char *funcname, int firstlineno***REMOVED***;

/* Return the line number associated with the specified bytecode index
   in this code object.  If you just need the line number of a frame,
   use PyFrame_GetLineNumber(***REMOVED*** instead. */
PyAPI_FUNC(int***REMOVED*** PyCode_Addr2Line(PyCodeObject *, int***REMOVED***;

/* for internal use only */
#define _PyCode_GETCODEPTR(co, pp***REMOVED*** \
	((*Py_TYPE((co***REMOVED***->co_code***REMOVED***->tp_as_buffer->bf_getreadbuffer***REMOVED*** \
	 ((co***REMOVED***->co_code, 0, (void *****REMOVED***(pp***REMOVED******REMOVED******REMOVED***

typedef struct _addr_pair {
        int ap_lower;
        int ap_upper;
***REMOVED*** PyAddrPair;

/* Update *bounds to describe the first and one-past-the-last instructions in the
   same line as lasti.  Return the number of that line.
*/
PyAPI_FUNC(int***REMOVED*** _PyCode_CheckLineNumber(PyCodeObject* co,
                                        int lasti, PyAddrPair *bounds***REMOVED***;

PyAPI_FUNC(PyObject****REMOVED*** PyCode_Optimize(PyObject *code, PyObject* consts,
                                      PyObject *names, PyObject *lineno_obj***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_CODE_H */
