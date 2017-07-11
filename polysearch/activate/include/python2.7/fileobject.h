
/* File object interface */

#ifndef Py_FILEOBJECT_H
#define Py_FILEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    PyObject_HEAD
    FILE *f_fp;
    PyObject *f_name;
    PyObject *f_mode;
    int (*f_close***REMOVED***(FILE ****REMOVED***;
    int f_softspace;            /* Flag used by 'print' command */
    int f_binary;               /* Flag which indicates whether the file is
                               open in binary (1***REMOVED*** or text (0***REMOVED*** mode */
    char* f_buf;                /* Allocated readahead buffer */
    char* f_bufend;             /* Points after last occupied position */
    char* f_bufptr;             /* Current buffer position */
    char *f_setbuf;             /* Buffer for setbuf(3***REMOVED*** and setvbuf(3***REMOVED*** */
    int f_univ_newline;         /* Handle any newline convention */
    int f_newlinetypes;         /* Types of newlines seen */
    int f_skipnextlf;           /* Skip next \n */
    PyObject *f_encoding;
    PyObject *f_errors;
    PyObject *weakreflist; /* List of weak references */
    int unlocked_count;         /* Num. currently running sections of code
                               using f_fp with the GIL released. */
    int readable;
    int writable;
***REMOVED*** PyFileObject;

PyAPI_DATA(PyTypeObject***REMOVED*** PyFile_Type;

#define PyFile_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyFile_Type***REMOVED***
#define PyFile_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyFile_Type***REMOVED***

PyAPI_FUNC(PyObject ****REMOVED*** PyFile_FromString(char *, char ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyFile_SetBufSize(PyObject *, int***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyFile_SetEncoding(PyObject *, const char ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyFile_SetEncodingAndErrors(PyObject *, const char *, char *errors***REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFile_FromFile(FILE *, char *, char *,
                                             int (****REMOVED***(FILE ****REMOVED******REMOVED***;
PyAPI_FUNC(FILE ****REMOVED*** PyFile_AsFile(PyObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyFile_IncUseCount(PyFileObject ****REMOVED***;
PyAPI_FUNC(void***REMOVED*** PyFile_DecUseCount(PyFileObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFile_Name(PyObject ****REMOVED***;
PyAPI_FUNC(PyObject ****REMOVED*** PyFile_GetLine(PyObject *, int***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyFile_WriteObject(PyObject *, PyObject *, int***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyFile_SoftSpace(PyObject *, int***REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyFile_WriteString(const char *, PyObject ****REMOVED***;
PyAPI_FUNC(int***REMOVED*** PyObject_AsFileDescriptor(PyObject ****REMOVED***;

/* The default encoding used by the platform file system APIs
   If non-NULL, this is different than the default encoding for strings
*/
PyAPI_DATA(const char ****REMOVED*** Py_FileSystemDefaultEncoding;

/* Routines to replace fread(***REMOVED*** and fgets(***REMOVED*** which accept any of \r, \n
   or \r\n as line terminators.
*/
#define PY_STDIOTEXTMODE "b"
char *Py_UniversalNewlineFgets(char *, int, FILE*, PyObject ****REMOVED***;
size_t Py_UniversalNewlineFread(char *, size_t, FILE *, PyObject ****REMOVED***;

/* A routine to do sanity checking on the file mode string.  returns
   non-zero on if an exception occurred
*/
int _PyFile_SanitizeMode(char *mode***REMOVED***;

#if defined _MSC_VER && _MSC_VER >= 1400
/* A routine to check if a file descriptor is valid on Windows.  Returns 0
 * and sets errno to EBADF if it isn't.  This is to avoid Assertions
 * from various functions in the Windows CRT beginning with
 * Visual Studio 2005
 */
int _PyVerify_fd(int fd***REMOVED***;
#elif defined _MSC_VER && _MSC_VER >= 1200
/* fdopen doesn't set errno EBADF and crashes for large fd on debug build */
#define _PyVerify_fd(fd***REMOVED*** (_get_osfhandle(fd***REMOVED*** >= 0***REMOVED***
#else
#define _PyVerify_fd(A***REMOVED*** (1***REMOVED*** /* dummy */
#endif

/* A routine to check if a file descriptor can be select(***REMOVED***-ed. */
#ifdef HAVE_SELECT
 #define _PyIsSelectable_fd(FD***REMOVED*** (((FD***REMOVED*** >= 0***REMOVED*** && ((FD***REMOVED*** < FD_SETSIZE***REMOVED******REMOVED***
#else
 #define _PyIsSelectable_fd(FD***REMOVED*** (1***REMOVED***
#endif /* HAVE_SELECT */

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_FILEOBJECT_H */
