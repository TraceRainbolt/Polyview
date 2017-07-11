
/* Capsule objects let you wrap a C "void *" pointer in a Python
   object.  They're a way of passing data through the Python interpreter
   without creating your own custom type.

   Capsules are used for communication between extension modules.
   They provide a way for an extension module to export a C interface
   to other extension modules, so that extension modules can use the
   Python import mechanism to link to one another.

   For more information, please see "c-api/capsule.html" in the
   documentation.
*/

#ifndef Py_CAPSULE_H
#define Py_CAPSULE_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject***REMOVED*** PyCapsule_Type;

typedef void (*PyCapsule_Destructor***REMOVED***(PyObject ****REMOVED***;

#define PyCapsule_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyCapsule_Type***REMOVED***


PyAPI_FUNC(PyObject ****REMOVED*** PyCapsule_New(
    void *pointer,
    const char *name,
    PyCapsule_Destructor destructor***REMOVED***;

PyAPI_FUNC(void ****REMOVED*** PyCapsule_GetPointer(PyObject *capsule, const char *name***REMOVED***;

PyAPI_FUNC(PyCapsule_Destructor***REMOVED*** PyCapsule_GetDestructor(PyObject *capsule***REMOVED***;

PyAPI_FUNC(const char ****REMOVED*** PyCapsule_GetName(PyObject *capsule***REMOVED***;

PyAPI_FUNC(void ****REMOVED*** PyCapsule_GetContext(PyObject *capsule***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyCapsule_IsValid(PyObject *capsule, const char *name***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyCapsule_SetPointer(PyObject *capsule, void *pointer***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyCapsule_SetDestructor(PyObject *capsule, PyCapsule_Destructor destructor***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyCapsule_SetName(PyObject *capsule, const char *name***REMOVED***;

PyAPI_FUNC(int***REMOVED*** PyCapsule_SetContext(PyObject *capsule, void *context***REMOVED***;

PyAPI_FUNC(void ****REMOVED*** PyCapsule_Import(const char *name, int no_block***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_CAPSULE_H */
