
/* Module definition and import interface */

#ifndef Py_IMPORT_H
#define Py_IMPORT_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(long***REMOVED*** PyImport_GetMagicNumber(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_ExecCodeModule(char *name, PyObject *co***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_ExecCodeModuleEx(
	char *name, PyObject *co, char *pathname***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_GetModuleDict(void***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_AddModule(const char *name***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_ImportModule(const char *name***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_ImportModuleNoBlock(const char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_ImportModuleLevel(char *name,
	PyObject *globals, PyObject *locals, PyObject *fromlist, int level***REMOVED***;

#define PyImport_ImportModuleEx(n, g, l, f***REMOVED*** \
	PyImport_ImportModuleLevel(n, g, l, f, -1***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyImport_GetImporter(PyObject *path***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_Import(PyObject *name***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyImport_ReloadModule(PyObject *m***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyImport_Cleanup(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyImport_ImportFrozenModule(char ****REMOVED***;

#ifdef WITH_THREAD
PyAPI_FUNC(void***REMOVED*** _PyImport_AcquireLock(void***REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyImport_ReleaseLock(void***REMOVED***;
#else
#define _PyImport_AcquireLock(***REMOVED***
#define _PyImport_ReleaseLock(***REMOVED*** 1
#endif

PyAPI_FUNC(struct filedescr ****REMOVED*** _PyImport_FindModule(
	const char *, PyObject *, char *, size_t, FILE **, PyObject *****REMOVED***;
PyAPI_FUNC(int***REMOVED*** _PyImport_IsScript(struct filedescr ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** _PyImport_ReInitLock(void***REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** _PyImport_FindExtension(char *, char ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** _PyImport_FixupExtension(char *, char ****REMOVED***;

struct _inittab {
    char *name;
    void (*initfunc***REMOVED***(void***REMOVED***;
***REMOVED***;

PyAPI_DATA(PyTypeObject***REMOVED*** PyNullImporter_Type;
PyAPI_DATA(struct _inittab ****REMOVED*** PyImport_Inittab;

PyAPI_FUNC(int***REMOVED*** PyImport_AppendInittab(const char *name, void (*initfunc***REMOVED***(void***REMOVED******REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyImport_ExtendInittab(struct _inittab *newtab***REMOVED***;

struct _frozen {
    char *name;
    unsigned char *code;
    int size;
***REMOVED***;

/* Embedding apps may change this pointer to point to their favorite
   collection of frozen modules: */

PyAPI_DATA(struct _frozen ****REMOVED*** PyImport_FrozenModules;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_IMPORT_H */
