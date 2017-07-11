
/* Parse tree node interface */

#ifndef Py_NODE_H
#define Py_NODE_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct _node {
    short		n_type;
    char		*n_str;
    int			n_lineno;
    int			n_col_offset;
    int			n_nchildren;
    struct _node	*n_child;
***REMOVED*** node;

PyAPI_FUNC(node ****REMOVED*** PyNode_New(int type***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyNode_AddChild(node *n, int type,
                                      char *str, int lineno, int col_offset***REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyNode_Free(node *n***REMOVED***;
#ifndef Py_LIMITED_API
Py_ssize_t _PyNode_SizeOf(node *n***REMOVED***;
#endif

/* Node access functions */
#define NCH(n***REMOVED***		((n***REMOVED***->n_nchildren***REMOVED***
	
#define CHILD(n, i***REMOVED***	(&(n***REMOVED***->n_child[i***REMOVED******REMOVED***
#define RCHILD(n, i***REMOVED***	(CHILD(n, NCH(n***REMOVED*** + i***REMOVED******REMOVED***
#define TYPE(n***REMOVED***		((n***REMOVED***->n_type***REMOVED***
#define STR(n***REMOVED***		((n***REMOVED***->n_str***REMOVED***

/* Assert that the type of a node is what we expect */
#define REQ(n, type***REMOVED*** assert(TYPE(n***REMOVED*** == (type***REMOVED******REMOVED***

PyAPI_FUNC(void***REMOVED*** PyNode_ListTree(node ****REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_NODE_H */
