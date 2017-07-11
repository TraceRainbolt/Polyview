/*
 * The Python Imaging Library
 * $Id$
 *
 * Windows DIB specifics
 *
 * Copyright (c***REMOVED*** Secret Labs AB 1997-98.
 * Copyright (c***REMOVED*** Fredrik Lundh 1996.
 *
 * See the README file for information on usage and redistribution.
 */

#ifdef WIN32

#if (defined(_MSC_VER***REMOVED*** && _MSC_VER >= 1200***REMOVED*** || (defined __GNUC__***REMOVED***
/* already defined in basetsd.h */
#undef INT8
#undef UINT8
#undef INT16
#undef UINT16
#undef INT32
#undef INT64
#undef UINT32
#endif

#include <windows.h>

#if defined(__cplusplus***REMOVED***
extern "C" {
#endif

struct ImagingDIBInstance {
    /* Windows interface */
    HDC dc;
    HBITMAP bitmap;
    HGDIOBJ old_bitmap;
    BITMAPINFO *info;
    UINT8 *bits;
    HPALETTE palette;
    /* Used by cut and paste */
    char mode[4***REMOVED***;
    int xsize, ysize;
    int pixelsize;
    int linesize;
    ImagingShuffler pack;
    ImagingShuffler unpack;
***REMOVED***;

typedef struct ImagingDIBInstance* ImagingDIB;

extern char* ImagingGetModeDIB(int size_out[2***REMOVED******REMOVED***;

extern ImagingDIB ImagingNewDIB(const char *mode, int xsize, int ysize***REMOVED***;

extern void ImagingDeleteDIB(ImagingDIB im***REMOVED***;

extern void ImagingDrawDIB(ImagingDIB dib, int dc, int dst[4***REMOVED***, int src[4***REMOVED******REMOVED***;
extern void ImagingExposeDIB(ImagingDIB dib, int dc***REMOVED***;

extern int ImagingQueryPaletteDIB(ImagingDIB dib, int dc***REMOVED***;

extern void ImagingPasteDIB(ImagingDIB dib, Imaging im, int xy[4***REMOVED******REMOVED***;

#if defined(__cplusplus***REMOVED***
***REMOVED***
#endif

#endif
