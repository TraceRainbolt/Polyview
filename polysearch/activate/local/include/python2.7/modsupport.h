
#ifndef Py_MODSUPPORT_H
#define Py_MODSUPPORT_H
#ifdef __cplusplus
extern "C" {
#endif

/* Module support interface */

#include <stdarg.h>

/* If PY_SSIZE_T_CLEAN is defined, each functions treats #-specifier
   to mean Py_ssize_t */
#ifdef PY_SSIZE_T_CLEAN
#define PyArg_Parse			_PyArg_Parse_SizeT
#define PyArg_ParseTuple		_PyArg_ParseTuple_SizeT
#define PyArg_ParseTupleAndKeywords	_PyArg_ParseTupleAndKeywords_SizeT
#define PyArg_VaParse			_PyArg_VaParse_SizeT
#define PyArg_VaParseTupleAndKeywords	_PyArg_VaParseTupleAndKeywords_SizeT
#define Py_BuildValue			_Py_BuildValue_SizeT
#define Py_VaBuildValue			_Py_VaBuildValue_SizeT
#else
PyAPI_FUNC(PyObject ****REMOVED*** _Py_VaBuildValue_SizeT(const char *, va_list***REMOVED***;
#endif

PyAPI_FUNC(int***REMOVED*** PyArg_Parse(PyObject *, const char *, ...***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyArg_ParseTuple(PyObject *, const char *, ...***REMOVED*** Py_FORMAT_PARSETUPLE(PyArg_ParseTuple, 2, 3***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyArg_ParseTupleAndKeywords(PyObject *, PyObject *,
                                                  const char *, char **, ...***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyArg_UnpackTuple(PyObject *, const char *, Py_ssize_t, Py_ssize_t, ...***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** Py_BuildValue(const char *, ...***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _Py_BuildValue_SizeT(const char *, ...***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyArg_NoKeywords(const char *funcname, PyObject *kw***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyArg_VaParse(PyObject *, const char *, va_list***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyArg_VaParseTupleAndKeywords(PyObject *, PyObject *,
                                                  const char *, char **, va_list***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** Py_VaBuildValue(const char *, va_list***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyModule_AddObject(PyObject *, const char *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyModule_AddIntConstant(PyObject *, const char *, long***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyModule_AddStringConstant(PyObject *, const char *, const char ****REMOVED***;
#define PyModule_AddIntMacro(m, c***REMOVED*** PyModule_AddIntConstant(m, #c, c***REMOVED***
#define PyModule_AddStringMacro(m, c***REMOVED*** PyModule_AddStringConstant(m, #c, c***REMOVED***

#define PYTHON_API_VERSION 1013
#define PYTHON_API_STRING "1013"
/* The API version is maintained (independently from the Python version***REMOVED***
   so we can detect mismatches between the interpreter and dynamically
   loaded modules.  These are diagnosed by an error message but
   the module is still loaded (because the mismatch can only be tested
   after loading the module***REMOVED***.  The error message is intended to
   explain the core dump a few seconds later.

   The symbol PYTHON_API_STRING defines the same value as a string
   literal.  *** PLEASE MAKE SURE THE DEFINITIONS MATCH. ***

   Please add a line or two to the top of this log for each API
   version change:

   22-Feb-2006  MvL	1013	PEP 353 - long indices for sequence lengths

   19-Aug-2002  GvR	1012	Changes to string object struct for
   				interning changes, saving 3 bytes.

   17-Jul-2001	GvR	1011	Descr-branch, just to be on the safe side

   25-Jan-2001  FLD     1010    Parameters added to PyCode_New(***REMOVED*** and
                                PyFrame_New(***REMOVED***; Python 2.1a2

   14-Mar-2000  GvR     1009    Unicode API added

   3-Jan-1999	GvR	1007	Decided to change back!  (Don't reuse 1008!***REMOVED***

   3-Dec-1998	GvR	1008	Python 1.5.2b1

   18-Jan-1997	GvR	1007	string interning and other speedups

   11-Oct-1996	GvR	renamed Py_Ellipses to Py_Ellipsis :-(

   30-Jul-1996	GvR	Slice and ellipses syntax added

   23-Jul-1996	GvR	For 1.4 -- better safe than sorry this time :-***REMOVED***

   7-Nov-1995	GvR	Keyword arguments (should've been done at 1.3 :-( ***REMOVED***

   10-Jan-1995	GvR	Renamed globals to new naming scheme

   9-Jan-1995	GvR	Initial version (incompatible with older API***REMOVED***
*/

#ifdef MS_WINDOWS
/* Special defines for Windows versions used to live here.  Things
   have changed, and the "Version" is now in a global string variable.
   Reason for this is that this for easier branding of a "custom DLL"
   without actually needing a recompile.  */
#endif /* MS_WINDOWS */

#if SIZEOF_SIZE_T != SIZEOF_INT
/* On a 64-bit system, rename the Py_InitModule4 so that 2.4
   modules cannot get loaded into a 2.5 interpreter */
#define Py_InitModule4 Py_InitModule4_64
#endif

#ifdef Py_TRACE_REFS
 /* When we are tracing reference counts, rename Py_InitModule4 so
    modules compiled with incompatible settings will generate a
    link-time error. */
 #if SIZEOF_SIZE_T != SIZEOF_INT
 #undef Py_InitModule4
 #define Py_InitModule4 Py_InitModule4TraceRefs_64
 #else
 #define Py_InitModule4 Py_InitModule4TraceRefs
 #endif
#endif

PyAPI_FUNC(PyObject ****REMOVED*** Py_InitModule4(const char *name, PyMethodDef *methods,
                                      const char *doc, PyObject *self,
                                      int apiver***REMOVED***;

#define Py_InitModule(name, methods***REMOVED*** \
	Py_InitModule4(name, methods, (char ****REMOVED***NULL, (PyObject ****REMOVED***NULL, \
		       PYTHON_API_VERSION***REMOVED***

#define Py_InitModule3(name, methods, doc***REMOVED*** \
	Py_InitModule4(name, methods, doc, (PyObject ****REMOVED***NULL, \
		       PYTHON_API_VERSION***REMOVED***

PyAPI_DATA(char ****REMOVED*** _Py_PackageContext;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_MODSUPPORT_H */
