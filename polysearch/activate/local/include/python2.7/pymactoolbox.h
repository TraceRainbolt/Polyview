/*
** pymactoolbox.h - globals defined in mactoolboxglue.c
*/
#ifndef Py_PYMACTOOLBOX_H
#define Py_PYMACTOOLBOX_H
#ifdef __cplusplus
	extern "C" {
#endif

#include <Carbon/Carbon.h>

#ifndef __LP64__
#include <QuickTime/QuickTime.h>
#endif /* !__LP64__ */

/*
** Helper routines for error codes and such.
*/
char *PyMac_StrError(int***REMOVED***;			/* strerror with mac errors */
extern PyObject *PyMac_OSErrException;		/* Exception for OSErr */
PyObject *PyMac_GetOSErrException(void***REMOVED***;	/* Initialize & return it */
PyObject *PyErr_Mac(PyObject *, int***REMOVED***;		/* Exception with a mac error */
PyObject *PyMac_Error(OSErr***REMOVED***;			/* Uses PyMac_GetOSErrException */
#ifndef __LP64__ 
extern OSErr PyMac_GetFullPathname(FSSpec *, char *, int***REMOVED***; /* convert
							      fsspec->path */
#endif /* __LP64__ */

/*
** These conversion routines are defined in mactoolboxglue.c itself.
*/
int PyMac_GetOSType(PyObject *, OSType ****REMOVED***;	/* argument parser for OSType */
PyObject *PyMac_BuildOSType(OSType***REMOVED***;		/* Convert OSType to PyObject */

PyObject *PyMac_BuildNumVersion(NumVersion***REMOVED***;/* Convert NumVersion to PyObject */

int PyMac_GetStr255(PyObject *, Str255***REMOVED***;	/* argument parser for Str255 */
PyObject *PyMac_BuildStr255(Str255***REMOVED***;		/* Convert Str255 to PyObject */
PyObject *PyMac_BuildOptStr255(Str255***REMOVED***;		/* Convert Str255 to PyObject,
						   NULL to None */

int PyMac_GetRect(PyObject *, Rect ****REMOVED***;		/* argument parser for Rect */
PyObject *PyMac_BuildRect(Rect ****REMOVED***;		/* Convert Rect to PyObject */

int PyMac_GetPoint(PyObject *, Point ****REMOVED***;	/* argument parser for Point */
PyObject *PyMac_BuildPoint(Point***REMOVED***;		/* Convert Point to PyObject */

int PyMac_GetEventRecord(PyObject *, EventRecord ****REMOVED***; /* argument parser for
							EventRecord */
PyObject *PyMac_BuildEventRecord(EventRecord ****REMOVED***; /* Convert EventRecord to
						    PyObject */

int PyMac_GetFixed(PyObject *, Fixed ****REMOVED***;	/* argument parser for Fixed */
PyObject *PyMac_BuildFixed(Fixed***REMOVED***;		/* Convert Fixed to PyObject */
int PyMac_Getwide(PyObject *, wide ****REMOVED***;		/* argument parser for wide */
PyObject *PyMac_Buildwide(wide ****REMOVED***;		/* Convert wide to PyObject */

/*
** The rest of the routines are implemented by extension modules. If they are
** dynamically loaded mactoolboxglue will contain a stub implementation of the
** routine, which imports the module, whereupon the module's init routine will
** communicate the routine pointer back to the stub.
** If USE_TOOLBOX_OBJECT_GLUE is not defined there is no glue code, and the
** extension modules simply declare the routine. This is the case for static
** builds (and could be the case for MacPython CFM builds, because CFM extension
** modules can reference each other without problems***REMOVED***.
*/

#ifdef USE_TOOLBOX_OBJECT_GLUE
/*
** These macros are used in the module init code. If we use toolbox object glue
** it sets the function pointer to point to the real function.
*/
#define PyMac_INIT_TOOLBOX_OBJECT_NEW(object, rtn***REMOVED*** { \
	extern PyObject *(*PyMacGluePtr_##rtn***REMOVED***(object***REMOVED***; \
	PyMacGluePtr_##rtn = _##rtn; \
***REMOVED***
#define PyMac_INIT_TOOLBOX_OBJECT_CONVERT(object, rtn***REMOVED*** { \
	extern int (*PyMacGluePtr_##rtn***REMOVED***(PyObject *, object ****REMOVED***; \
	PyMacGluePtr_##rtn = _##rtn; \
***REMOVED***
#else
/*
** If we don't use toolbox object glue the init macros are empty. Moreover, we define
** _xxx_New to be the same as xxx_New, and the code in mactoolboxglue isn't included.
*/
#define PyMac_INIT_TOOLBOX_OBJECT_NEW(object, rtn***REMOVED***
#define PyMac_INIT_TOOLBOX_OBJECT_CONVERT(object, rtn***REMOVED***
#endif /* USE_TOOLBOX_OBJECT_GLUE */

/* macfs exports */
#ifndef __LP64__
int PyMac_GetFSSpec(PyObject *, FSSpec ****REMOVED***;	/* argument parser for FSSpec */
PyObject *PyMac_BuildFSSpec(FSSpec ****REMOVED***;		/* Convert FSSpec to PyObject */
#endif /* !__LP64__ */

int PyMac_GetFSRef(PyObject *, FSRef ****REMOVED***;	/* argument parser for FSRef */
PyObject *PyMac_BuildFSRef(FSRef ****REMOVED***;		/* Convert FSRef to PyObject */

/* AE exports */
extern PyObject *AEDesc_New(AppleEvent ****REMOVED***; /* XXXX Why passed by address?? */
extern PyObject *AEDesc_NewBorrowed(AppleEvent ****REMOVED***;
extern int AEDesc_Convert(PyObject *, AppleEvent ****REMOVED***;

/* Cm exports */
extern PyObject *CmpObj_New(Component***REMOVED***;
extern int CmpObj_Convert(PyObject *, Component ****REMOVED***;
extern PyObject *CmpInstObj_New(ComponentInstance***REMOVED***;
extern int CmpInstObj_Convert(PyObject *, ComponentInstance ****REMOVED***;

/* Ctl exports */
#ifndef __LP64__
extern PyObject *CtlObj_New(ControlHandle***REMOVED***;
extern int CtlObj_Convert(PyObject *, ControlHandle ****REMOVED***;
#endif /* !__LP64__ */

/* Dlg exports */
#ifndef __LP64__
extern PyObject *DlgObj_New(DialogPtr***REMOVED***;
extern int DlgObj_Convert(PyObject *, DialogPtr ****REMOVED***;
extern PyObject *DlgObj_WhichDialog(DialogPtr***REMOVED***;
#endif /* !__LP64__ */

/* Drag exports */
#ifndef __LP64__
extern PyObject *DragObj_New(DragReference***REMOVED***;
extern int DragObj_Convert(PyObject *, DragReference ****REMOVED***;
#endif /* !__LP64__ */

/* List exports */
#ifndef __LP64__
extern PyObject *ListObj_New(ListHandle***REMOVED***;
extern int ListObj_Convert(PyObject *, ListHandle ****REMOVED***;
#endif /* !__LP64__ */

/* Menu exports */
#ifndef __LP64__
extern PyObject *MenuObj_New(MenuHandle***REMOVED***;
extern int MenuObj_Convert(PyObject *, MenuHandle ****REMOVED***;
#endif /* !__LP64__ */

/* Qd exports */
#ifndef __LP64__
extern PyObject *GrafObj_New(GrafPtr***REMOVED***;
extern int GrafObj_Convert(PyObject *, GrafPtr ****REMOVED***;
extern PyObject *BMObj_New(BitMapPtr***REMOVED***;
extern int BMObj_Convert(PyObject *, BitMapPtr ****REMOVED***;
extern PyObject *QdRGB_New(RGBColor ****REMOVED***;
extern int QdRGB_Convert(PyObject *, RGBColor ****REMOVED***;
#endif /* !__LP64__ */

/* Qdoffs exports */
#ifndef __LP64__
extern PyObject *GWorldObj_New(GWorldPtr***REMOVED***;
extern int GWorldObj_Convert(PyObject *, GWorldPtr ****REMOVED***;
#endif /* !__LP64__ */

/* Qt exports */
#ifndef __LP64__
extern PyObject *TrackObj_New(Track***REMOVED***;
extern int TrackObj_Convert(PyObject *, Track ****REMOVED***;
extern PyObject *MovieObj_New(Movie***REMOVED***;
extern int MovieObj_Convert(PyObject *, Movie ****REMOVED***;
extern PyObject *MovieCtlObj_New(MovieController***REMOVED***;
extern int MovieCtlObj_Convert(PyObject *, MovieController ****REMOVED***;
extern PyObject *TimeBaseObj_New(TimeBase***REMOVED***;
extern int TimeBaseObj_Convert(PyObject *, TimeBase ****REMOVED***;
extern PyObject *UserDataObj_New(UserData***REMOVED***;
extern int UserDataObj_Convert(PyObject *, UserData ****REMOVED***;
extern PyObject *MediaObj_New(Media***REMOVED***;
extern int MediaObj_Convert(PyObject *, Media ****REMOVED***;
#endif /* !__LP64__ */

/* Res exports */
extern PyObject *ResObj_New(Handle***REMOVED***;
extern int ResObj_Convert(PyObject *, Handle ****REMOVED***;
extern PyObject *OptResObj_New(Handle***REMOVED***;
extern int OptResObj_Convert(PyObject *, Handle ****REMOVED***;

/* TE exports */
#ifndef __LP64__
extern PyObject *TEObj_New(TEHandle***REMOVED***;
extern int TEObj_Convert(PyObject *, TEHandle ****REMOVED***;
#endif /* !__LP64__ */

/* Win exports */
#ifndef __LP64__
extern PyObject *WinObj_New(WindowPtr***REMOVED***;
extern int WinObj_Convert(PyObject *, WindowPtr ****REMOVED***;
extern PyObject *WinObj_WhichWindow(WindowPtr***REMOVED***;
#endif /* !__LP64__ */

/* CF exports */
extern PyObject *CFObj_New(CFTypeRef***REMOVED***;
extern int CFObj_Convert(PyObject *, CFTypeRef ****REMOVED***;
extern PyObject *CFTypeRefObj_New(CFTypeRef***REMOVED***;
extern int CFTypeRefObj_Convert(PyObject *, CFTypeRef ****REMOVED***;
extern PyObject *CFStringRefObj_New(CFStringRef***REMOVED***;
extern int CFStringRefObj_Convert(PyObject *, CFStringRef ****REMOVED***;
extern PyObject *CFMutableStringRefObj_New(CFMutableStringRef***REMOVED***;
extern int CFMutableStringRefObj_Convert(PyObject *, CFMutableStringRef ****REMOVED***;
extern PyObject *CFArrayRefObj_New(CFArrayRef***REMOVED***;
extern int CFArrayRefObj_Convert(PyObject *, CFArrayRef ****REMOVED***;
extern PyObject *CFMutableArrayRefObj_New(CFMutableArrayRef***REMOVED***;
extern int CFMutableArrayRefObj_Convert(PyObject *, CFMutableArrayRef ****REMOVED***;
extern PyObject *CFDictionaryRefObj_New(CFDictionaryRef***REMOVED***;
extern int CFDictionaryRefObj_Convert(PyObject *, CFDictionaryRef ****REMOVED***;
extern PyObject *CFMutableDictionaryRefObj_New(CFMutableDictionaryRef***REMOVED***;
extern int CFMutableDictionaryRefObj_Convert(PyObject *, CFMutableDictionaryRef ****REMOVED***;
extern PyObject *CFURLRefObj_New(CFURLRef***REMOVED***;
extern int CFURLRefObj_Convert(PyObject *, CFURLRef ****REMOVED***;
extern int OptionalCFURLRefObj_Convert(PyObject *, CFURLRef ****REMOVED***;

#ifdef __cplusplus
	***REMOVED***
#endif
#endif
