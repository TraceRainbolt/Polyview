
/* Tuple object interface */

#ifndef Py_STRUCTSEQ_H
#define Py_STRUCTSEQ_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct PyStructSequence_Field {
	char *name;
	char *doc;
***REMOVED*** PyStructSequence_Field;

typedef struct PyStructSequence_Desc {
	char *name;
	char *doc;
	struct PyStructSequence_Field *fields;
	int n_in_sequence;
***REMOVED*** PyStructSequence_Desc;

extern char* PyStructSequence_UnnamedField;

PyAPI_FUNC(void***REMOVED*** PyStructSequence_InitType(PyTypeObject *type,
					   PyStructSequence_Desc *desc***REMOVED***;

PyAPI_FUNC(PyObject ****REMOVED*** PyStructSequence_New(PyTypeObject* type***REMOVED***;

typedef struct {
	PyObject_VAR_HEAD
	PyObject *ob_item[1***REMOVED***;
***REMOVED*** PyStructSequence;

/* Macro, *only* to be used to fill in brand new objects */
#define PyStructSequence_SET_ITEM(op, i, v***REMOVED*** \
	(((PyStructSequence ****REMOVED***(op***REMOVED******REMOVED***->ob_item[i***REMOVED*** = v***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_STRUCTSEQ_H */
