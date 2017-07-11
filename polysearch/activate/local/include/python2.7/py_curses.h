
#ifndef Py_CURSES_H
#define Py_CURSES_H

#ifdef __APPLE__
/*
** On Mac OS X 10.2 [n***REMOVED***curses.h and stdlib.h use different guards
** against multiple definition of wchar_t.
*/
#ifdef	_BSD_WCHAR_T_DEFINED_
#define _WCHAR_T
#endif

/* the following define is necessary for OS X 10.6; without it, the
   Apple-supplied ncurses.h sets NCURSES_OPAQUE to 1, and then Python
   can't get at the WINDOW flags field. */
#define NCURSES_OPAQUE 0
#endif /* __APPLE__ */

#ifdef __FreeBSD__
/*
** On FreeBSD, [n***REMOVED***curses.h and stdlib.h/wchar.h use different guards
** against multiple definition of wchar_t and wint_t.
*/
#ifdef	_XOPEN_SOURCE_EXTENDED
#ifndef __FreeBSD_version
#include <osreldate.h>
#endif
#if __FreeBSD_version >= 500000
#ifndef __wchar_t
#define __wchar_t
#endif
#ifndef __wint_t
#define __wint_t
#endif
#else
#ifndef _WCHAR_T
#define _WCHAR_T
#endif
#ifndef _WINT_T
#define _WINT_T
#endif
#endif
#endif
#endif

#ifdef HAVE_NCURSES_H
#include <ncurses.h>
#else
#include <curses.h>
#ifdef HAVE_TERM_H
/* for tigetstr, which is not declared in SysV curses */
#include <term.h>
#endif
#endif

#ifdef HAVE_NCURSES_H
/* configure was checking <curses.h>, but we will
   use <ncurses.h>, which has all these features. */
#ifndef WINDOW_HAS_FLAGS
#define WINDOW_HAS_FLAGS 1
#endif
#ifndef MVWDELCH_IS_EXPRESSION
#define MVWDELCH_IS_EXPRESSION 1
#endif
#endif

#ifdef __cplusplus
extern "C" {
#endif

#define PyCurses_API_pointers 4

/* Type declarations */

typedef struct {
	PyObject_HEAD
	WINDOW *win;
***REMOVED*** PyCursesWindowObject;

#define PyCursesWindow_Check(v***REMOVED***	 (Py_TYPE(v***REMOVED*** == &PyCursesWindow_Type***REMOVED***

#define PyCurses_CAPSULE_NAME "_curses._C_API"


#ifdef CURSES_MODULE
/* This section is used when compiling _cursesmodule.c */

#else
/* This section is used in modules that use the _cursesmodule API */

static void **PyCurses_API;

#define PyCursesWindow_Type (*(PyTypeObject ****REMOVED*** PyCurses_API[0***REMOVED******REMOVED***
#define PyCursesSetupTermCalled  {if (! ((int (****REMOVED***(void***REMOVED******REMOVED***PyCurses_API[1***REMOVED******REMOVED*** (***REMOVED*** ***REMOVED*** return NULL;***REMOVED***
#define PyCursesInitialised  ***REMOVED***if (! ((int (****REMOVED***(void***REMOVED******REMOVED***PyCurses_API[2***REMOVED******REMOVED*** (***REMOVED*** ***REMOVED*** return NULL;***REMOVED***
#define PyCursesInitialisedColor {if (! ((int (****REMOVED***(void***REMOVED******REMOVED***PyCurses_API[3***REMOVED******REMOVED*** (***REMOVED*** ***REMOVED*** return NULL;***REMOVED***

#define import_curses(***REMOVED*** \
    PyCurses_API = (void *****REMOVED***PyCapsule_Import(PyCurses_CAPSULE_NAME, 1***REMOVED***;

#endif

/* general error messages */
static char *catchall_ERR  = "curses function returned ERR";
static char *catchall_NULL = "curses function returned NULL";

/* Function Prototype Macros - They are ugly but very, very useful. ;-***REMOVED***

   X - function name
   TYPE - parameter Type
   ERGSTR - format string for construction of the return value
   PARSESTR - format string for argument parsing
   */

#define NoArgNoReturnFunction(X***REMOVED*** \
static PyObject *PyCurses_ ## X (PyObject *self***REMOVED*** \
{ \
  PyCursesInitialised \
  return PyCursesCheckERR(X(***REMOVED***, # X***REMOVED***; ***REMOVED***

#define NoArgOrFlagNoReturnFunction(X***REMOVED*** \
static PyObject *PyCurses_ ## X (PyObject *self, PyObject *args***REMOVED*** \
{ \
  int flag = 0; \
  PyCursesInitialised \
  switch(PyTuple_Size(args***REMOVED******REMOVED*** { \
  case 0: \
    return PyCursesCheckERR(X(***REMOVED***, # X***REMOVED***; \
  case 1: \
    if (!PyArg_ParseTuple(args, "i;True(1***REMOVED*** or False(0***REMOVED***", &flag***REMOVED******REMOVED*** return NULL; \
    if (flag***REMOVED*** return PyCursesCheckERR(X(***REMOVED***, # X***REMOVED***; \
    else return PyCursesCheckERR(no ## X (***REMOVED***, # X***REMOVED***; \
  default: \
    PyErr_SetString(PyExc_TypeError, # X " requires 0 or 1 arguments"***REMOVED***; \
    return NULL; ***REMOVED*** ***REMOVED***

#define NoArgReturnIntFunction(X***REMOVED*** \
static PyObject *PyCurses_ ## X (PyObject *self***REMOVED*** \
{ \
 PyCursesInitialised \
 return PyInt_FromLong((long***REMOVED*** X(***REMOVED******REMOVED***; ***REMOVED***


#define NoArgReturnStringFunction(X***REMOVED*** \
static PyObject *PyCurses_ ## X (PyObject *self***REMOVED*** \
{ \
  PyCursesInitialised \
  return PyString_FromString(X(***REMOVED******REMOVED***; ***REMOVED***

#define NoArgTrueFalseFunction(X***REMOVED*** \
static PyObject *PyCurses_ ## X (PyObject *self***REMOVED*** \
{ \
  PyCursesInitialised \
  if (X (***REMOVED*** == FALSE***REMOVED*** { \
    Py_INCREF(Py_False***REMOVED***; \
    return Py_False; \
  ***REMOVED*** \
  Py_INCREF(Py_True***REMOVED***; \
  return Py_True; ***REMOVED***

#define NoArgNoReturnVoidFunction(X***REMOVED*** \
static PyObject *PyCurses_ ## X (PyObject *self***REMOVED*** \
{ \
  PyCursesInitialised \
  X(***REMOVED***; \
  Py_INCREF(Py_None***REMOVED***; \
  return Py_None; ***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif

#endif /* !defined(Py_CURSES_H***REMOVED*** */


