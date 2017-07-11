
/* Interfaces to parse and execute pieces of python code */

#ifndef Py_PYTHONRUN_H
#define Py_PYTHONRUN_H
#ifdef __cplusplus
extern "C" {
#endif

#define PyCF_MASK (CO_FUTURE_DIVISION | CO_FUTURE_ABSOLUTE_IMPORT | \
                   CO_FUTURE_WITH_STATEMENT | CO_FUTURE_PRINT_FUNCTION | \
                   CO_FUTURE_UNICODE_LITERALS***REMOVED***
#define PyCF_MASK_OBSOLETE (CO_NESTED***REMOVED***
#define PyCF_SOURCE_IS_UTF8  0x0100
#define PyCF_DONT_IMPLY_DEDENT 0x0200
#define PyCF_ONLY_AST 0x0400

typedef struct {
    int cf_flags;  /* bitmask of CO_xxx flags relevant to future */
***REMOVED*** PyCompilerFlags;

PyAPI_FUNC(void***REMOVED*** Py_SetProgramName(char ****REMOVED***;
PyAPI_FUNC(char ****REMOVED*** Py_GetProgramName(void***REMOVED***;

PyAPI_FUNC(void***REMOVED*** Py_SetPythonHome(char ****REMOVED***;
PyAPI_FUNC(char ****REMOVED*** Py_GetPythonHome(void***REMOVED***;

PyAPI_FUNC(void***REMOVED*** Py_Initialize(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** Py_InitializeEx(int***REMOVED***;
PyAPI_FUNC(void***REMOVED*** Py_Finalize(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** Py_IsInitialized(void***REMOVED***;
PyAPI_FUNC(PyThreadState ****REMOVED*** Py_NewInterpreter(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** Py_EndInterpreter(PyThreadState ****REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyRun_AnyFileFlags(FILE *, const char *, PyCompilerFlags ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyRun_AnyFileExFlags(FILE *, const char *, int, PyCompilerFlags ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyRun_SimpleStringFlags(const char *, PyCompilerFlags ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyRun_SimpleFileExFlags(FILE *, const char *, int, PyCompilerFlags ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyRun_InteractiveOneFlags(FILE *, const char *, PyCompilerFlags ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyRun_InteractiveLoopFlags(FILE *, const char *, PyCompilerFlags ****REMOVED***;

PyAPI_FUNC(struct _mod ****REMOVED*** PyParser_ASTFromString(const char *, const char *,
                                                 int, PyCompilerFlags *flags,
                                                 PyArena ****REMOVED***;
PyAPI_FUNC(struct _mod ****REMOVED*** PyParser_ASTFromFile(FILE *, const char *, int,
                                               char *, char *,
                                               PyCompilerFlags *, int *,
                                               PyArena ****REMOVED***;
#define PyParser_SimpleParseString(S, B***REMOVED*** \
    PyParser_SimpleParseStringFlags(S, B, 0***REMOVED***
#define PyParser_SimpleParseFile(FP, S, B***REMOVED*** \
    PyParser_SimpleParseFileFlags(FP, S, B, 0***REMOVED***
PyAPI_FUNC(struct _node ****REMOVED*** PyParser_SimpleParseStringFlags(const char *, int,
                                                          int***REMOVED***;
PyAPI_FUNC(struct _node ****REMOVED*** PyParser_SimpleParseFileFlags(FILE *, const char *,
                                                        int, int***REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyRun_StringFlags(const char *, int, PyObject *,
                                         PyObject *, PyCompilerFlags ****REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyRun_FileExFlags(FILE *, const char *, int,
                                         PyObject *, PyObject *, int,
                                         PyCompilerFlags ****REMOVED***;

#define Py_CompileString(str, p, s***REMOVED*** Py_CompileStringFlags(str, p, s, NULL***REMOVED***
PyAPI_FUNC(PyObject ****REMOVED*** Py_CompileStringFlags(const char *, const char *, int,
                                             PyCompilerFlags ****REMOVED***;
PyAPI_FUNC(struct symtable ****REMOVED*** Py_SymtableString(const char *, const char *, int***REMOVED***;

PyAPI_FUNC(void***REMOVED*** PyErr_Print(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_PrintEx(int***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyErr_Display(PyObject *, PyObject *, PyObject ****REMOVED***;

PyAPI_FUNC(int***REMOVED*** Py_AtExit(void (*func***REMOVED***(void***REMOVED******REMOVED***;

PyAPI_FUNC(void***REMOVED*** Py_Exit(int***REMOVED***;

PyAPI_FUNC(int***REMOVED*** Py_FdIsInteractive(FILE *, const char ****REMOVED***;

/* Bootstrap */
PyAPI_FUNC(int***REMOVED*** Py_Main(int argc, char **argv***REMOVED***;

/* Use macros for a bunch of old variants */
#define PyRun_String(str, s, g, l***REMOVED*** PyRun_StringFlags(str, s, g, l, NULL***REMOVED***
#define PyRun_AnyFile(fp, name***REMOVED*** PyRun_AnyFileExFlags(fp, name, 0, NULL***REMOVED***
#define PyRun_AnyFileEx(fp, name, closeit***REMOVED*** \
    PyRun_AnyFileExFlags(fp, name, closeit, NULL***REMOVED***
#define PyRun_AnyFileFlags(fp, name, flags***REMOVED*** \
    PyRun_AnyFileExFlags(fp, name, 0, flags***REMOVED***
#define PyRun_SimpleString(s***REMOVED*** PyRun_SimpleStringFlags(s, NULL***REMOVED***
#define PyRun_SimpleFile(f, p***REMOVED*** PyRun_SimpleFileExFlags(f, p, 0, NULL***REMOVED***
#define PyRun_SimpleFileEx(f, p, c***REMOVED*** PyRun_SimpleFileExFlags(f, p, c, NULL***REMOVED***
#define PyRun_InteractiveOne(f, p***REMOVED*** PyRun_InteractiveOneFlags(f, p, NULL***REMOVED***
#define PyRun_InteractiveLoop(f, p***REMOVED*** PyRun_InteractiveLoopFlags(f, p, NULL***REMOVED***
#define PyRun_File(fp, p, s, g, l***REMOVED*** \
    PyRun_FileExFlags(fp, p, s, g, l, 0, NULL***REMOVED***
#define PyRun_FileEx(fp, p, s, g, l, c***REMOVED*** \
    PyRun_FileExFlags(fp, p, s, g, l, c, NULL***REMOVED***
#define PyRun_FileFlags(fp, p, s, g, l, flags***REMOVED*** \
    PyRun_FileExFlags(fp, p, s, g, l, 0, flags***REMOVED***

/* In getpath.c */
PyAPI_FUNC(char ****REMOVED*** Py_GetProgramFullPath(void***REMOVED***;
PyAPI_FUNC(char ****REMOVED*** Py_GetPrefix(void***REMOVED***;
PyAPI_FUNC(char ****REMOVED*** Py_GetExecPrefix(void***REMOVED***;
PyAPI_FUNC(char ****REMOVED*** Py_GetPath(void***REMOVED***;

/* In their own files */
PyAPI_FUNC(const char ****REMOVED*** Py_GetVersion(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** Py_GetPlatform(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** Py_GetCopyright(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** Py_GetCompiler(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** Py_GetBuildInfo(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** _Py_svnversion(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** Py_SubversionRevision(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** Py_SubversionShortBranch(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** _Py_hgidentifier(void***REMOVED***;
PyAPI_FUNC(const char ****REMOVED*** _Py_hgversion(void***REMOVED***;

/* Internal -- various one-time initializations */
PyAPI_FUNC(PyObject ****REMOVED*** _PyBuiltin_Init(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PySys_Init(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyImport_Init(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyExc_Init(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyImportHooks_Init(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyFrame_Init(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyInt_Init(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyLong_Init(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyFloat_Init(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyByteArray_Init(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyRandom_Init(void***REMOVED***;

/* Various internal finalizers */
PyAPI_FUNC(void***REMOVED*** _PyExc_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyImport_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyMethod_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyFrame_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyCFunction_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyDict_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyTuple_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyList_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PySet_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyString_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyInt_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyFloat_Fini(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyOS_FiniInterrupts(void***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyByteArray_Fini(void***REMOVED***;

/* Stuff with no proper home (yet***REMOVED*** */
PyAPI_FUNC(char ****REMOVED*** PyOS_Readline(FILE *, FILE *, char ****REMOVED***;
PyAPI_DATA(int***REMOVED*** (*PyOS_InputHook***REMOVED***(void***REMOVED***;
PyAPI_DATA(char***REMOVED*** *(*PyOS_ReadlineFunctionPointer***REMOVED***(FILE *, FILE *, char ****REMOVED***;
PyAPI_DATA(PyThreadState****REMOVED*** _PyOS_ReadlineTState;

/* Stack size, in "pointers" (so we get extra safety margins
   on 64-bit platforms***REMOVED***.  On a 32-bit platform, this translates
   to a 8k margin. */
#define PYOS_STACK_MARGIN 2048

#if defined(WIN32***REMOVED*** && !defined(MS_WIN64***REMOVED*** && defined(_MSC_VER***REMOVED*** && _MSC_VER >= 1300
/* Enable stack checking under Microsoft C */
#define USE_STACKCHECK
#endif

#ifdef USE_STACKCHECK
/* Check that we aren't overflowing our stack */
PyAPI_FUNC(int***REMOVED*** PyOS_CheckStack(void***REMOVED***;
#endif

/* Signals */
typedef void (*PyOS_sighandler_t***REMOVED***(int***REMOVED***;
PyAPI_FUNC(PyOS_sighandler_t***REMOVED*** PyOS_getsig(int***REMOVED***;
PyAPI_FUNC(PyOS_sighandler_t***REMOVED*** PyOS_setsig(int, PyOS_sighandler_t***REMOVED***;

/* Random */
PyAPI_FUNC(int***REMOVED*** _PyOS_URandom (void *buffer, Py_ssize_t size***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_PYTHONRUN_H */
