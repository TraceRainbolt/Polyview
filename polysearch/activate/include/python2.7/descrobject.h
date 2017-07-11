/* Descriptors */
#ifndef Py_DESCROBJECT_H
#define Py_DESCROBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef PyObject *(*getter***REMOVED***(PyObject *, void ****REMOVED***;
typedef int (*setter***REMOVED***(PyObject *, PyObject *, void ****REMOVED***;

typedef struct PyGetSetDef {
    char *name;
    getter get;
    setter set;
    char *doc;
    void *closure;
***REMOVED*** PyGetSetDef;

typedef PyObject *(*wrapperfunc***REMOVED***(PyObject *self, PyObject *args,
                                 void *wrapped***REMOVED***;

typedef PyObject *(*wrapperfunc_kwds***REMOVED***(PyObject *self, PyObject *args,
                                      void *wrapped, PyObject *kwds***REMOVED***;

struct wrapperbase {
    char *name;
    int offset;
    void *function;
    wrapperfunc wrapper;
    char *doc;
    int flags;
    PyObject *name_strobj;
***REMOVED***;

/* Flags for above struct */
#define PyWrapperFlag_KEYWORDS 1 /* wrapper function takes keyword args */

/* Various kinds of descriptor objects */

#define PyDescr_COMMON \
    PyObject_HEAD \
    PyTypeObject *d_type; \
    PyObject *d_name

typedef struct {
    PyDescr_COMMON;
***REMOVED*** PyDescrObject;

typedef struct {
    PyDescr_COMMON;
    PyMethodDef *d_method;
***REMOVED*** PyMethodDescrObject;

typedef struct {
    PyDescr_COMMON;
    struct PyMemberDef *d_member;
***REMOVED*** PyMemberDescrObject;

typedef struct {
    PyDescr_COMMON;
    PyGetSetDef *d_getset;
***REMOVED*** PyGetSetDescrObject;

typedef struct {
    PyDescr_COMMON;
    struct wrapperbase *d_base;
    void *d_wrapped; /* This can be any function pointer */
***REMOVED*** PyWrapperDescrObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyWrapperDescr_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyDictProxy_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyGetSetDescr_Type;
PyAPI_DATA(PyTypeObject***REMOVED*** PyMemberDescr_Type;

PyAPI_FUNC(PyObject ****REMOVED*** PyDescr_NewMethod(PyTypeObject *, PyMethodDef ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDescr_NewClassMethod(PyTypeObject *, PyMethodDef ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDescr_NewMember(PyTypeObject *,
                                               struct PyMemberDef ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDescr_NewGetSet(PyTypeObject *,
                                               struct PyGetSetDef ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyDescr_NewWrapper(PyTypeObject *,
                                                struct wrapperbase *, void ****REMOVED***;
#define PyDescr_IsData(d***REMOVED*** (Py_TYPE(d***REMOVED***->tp_descr_set != NULL***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyDictProxy_New(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyWrapper_New(PyObject *, PyObject ****REMOVED***;


PyAPI_DATA(PyTypeObject***REMOVED*** PyProperty_Type;
#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_DESCROBJECT_H */

