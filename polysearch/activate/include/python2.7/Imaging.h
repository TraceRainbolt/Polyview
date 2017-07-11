/*
 * The Python Imaging Library
 * $Id$
 *
 * declarations for the imaging core library
 *
 * Copyright (c***REMOVED*** 1997-2005 by Secret Labs AB
 * Copyright (c***REMOVED*** 1995-2005 by Fredrik Lundh
 *
 * See the README file for information on usage and redistribution.
 */


#include "ImPlatform.h"


#if defined(__cplusplus***REMOVED***
extern "C" {
#endif


#ifndef M_PI
#define	M_PI	3.14159265359
#endif


/* -------------------------------------------------------------------- */

/*
 * Image data organization:
 *
 * mode	    bytes	byte order
 * -------------------------------
 * 1	    1		1
 * L	    1		L
 * P	    1		P
 * I        4           I (32-bit integer, native byte order***REMOVED***
 * F        4           F (32-bit IEEE float, native byte order***REMOVED***
 * RGB	    4		R, G, B, -
 * RGBA	    4		R, G, B, A
 * CMYK	    4		C, M, Y, K
 * YCbCr    4		Y, Cb, Cr, -
 * Lab      4       L, a, b, -
 *
 * experimental modes (incomplete***REMOVED***:
 * LA       4           L, -, -, A
 * PA       4           P, -, -, A
 * I;16     2           I (16-bit integer, native byte order***REMOVED***
 *
 * "P" is an 8-bit palette mode, which should be mapped through the
 * palette member to get an output image.  Check palette->mode to
 * find the corresponding "real" mode.
 *
 * For information on how to access Imaging objects from your own C
 * extensions, see http://www.effbot.org/zone/pil-extending.htm
 */

/* Handles */

typedef struct ImagingMemoryInstance* Imaging;

typedef struct ImagingAccessInstance* ImagingAccess;
typedef struct ImagingHistogramInstance* ImagingHistogram;
typedef struct ImagingOutlineInstance* ImagingOutline;
typedef struct ImagingPaletteInstance* ImagingPalette;

/* handle magics (used with PyCObject***REMOVED***. */
#define IMAGING_MAGIC "PIL Imaging"

/* pixel types */
#define IMAGING_TYPE_UINT8 0
#define IMAGING_TYPE_INT32 1
#define IMAGING_TYPE_FLOAT32 2
#define IMAGING_TYPE_SPECIAL 3 /* check mode for details */

#define IMAGING_MODE_LENGTH 6+1 /* Band names ("1", "L", "P", "RGB", "RGBA", "CMYK", "YCbCr", "BGR;xy"***REMOVED*** */

struct ImagingMemoryInstance {

    /* Format */
    char mode[IMAGING_MODE_LENGTH***REMOVED***;	/* Band names ("1", "L", "P", "RGB", "RGBA", "CMYK", "YCbCr", "BGR;xy"***REMOVED*** */
    int type;		/* Data type (IMAGING_TYPE_****REMOVED*** */
    int depth;		/* Depth (ignored in this version***REMOVED*** */
    int bands;		/* Number of bands (1, 2, 3, or 4***REMOVED*** */
    int xsize;		/* Image dimension. */
    int ysize;

    /* Colour palette (for "P" images only***REMOVED*** */
    ImagingPalette palette;

    /* Data pointers */
    UINT8 **image8;	/* Set for 8-bit images (pixelsize=1***REMOVED***. */
    INT32 **image32;	/* Set for 32-bit images (pixelsize=4***REMOVED***. */

    /* Internals */
    char **image;	/* Actual raster data. */
    char *block;	/* Set if data is allocated in a single block. */

    int pixelsize;	/* Size of a pixel, in bytes (1, 2 or 4***REMOVED*** */
    int linesize;	/* Size of a line, in bytes (xsize * pixelsize***REMOVED*** */

    /* Virtual methods */
    void (*destroy***REMOVED***(Imaging im***REMOVED***;
***REMOVED***;


#define IMAGING_PIXEL_1(im,x,y***REMOVED*** ((im***REMOVED***->image8[(y***REMOVED******REMOVED***[(x***REMOVED******REMOVED******REMOVED***
#define IMAGING_PIXEL_L(im,x,y***REMOVED*** ((im***REMOVED***->image8[(y***REMOVED******REMOVED***[(x***REMOVED******REMOVED******REMOVED***
#define IMAGING_PIXEL_LA(im,x,y***REMOVED*** ((im***REMOVED***->image[(y***REMOVED******REMOVED***[(x***REMOVED****4***REMOVED******REMOVED***
#define IMAGING_PIXEL_P(im,x,y***REMOVED*** ((im***REMOVED***->image8[(y***REMOVED******REMOVED***[(x***REMOVED******REMOVED******REMOVED***
#define IMAGING_PIXEL_PA(im,x,y***REMOVED*** ((im***REMOVED***->image[(y***REMOVED******REMOVED***[(x***REMOVED****4***REMOVED******REMOVED***
#define IMAGING_PIXEL_I(im,x,y***REMOVED*** ((im***REMOVED***->image32[(y***REMOVED******REMOVED***[(x***REMOVED******REMOVED******REMOVED***
#define IMAGING_PIXEL_F(im,x,y***REMOVED*** (((FLOAT32****REMOVED***(im***REMOVED***->image32[y***REMOVED******REMOVED***[x***REMOVED******REMOVED***
#define IMAGING_PIXEL_RGB(im,x,y***REMOVED*** ((im***REMOVED***->image[(y***REMOVED******REMOVED***[(x***REMOVED****4***REMOVED******REMOVED***
#define IMAGING_PIXEL_RGBA(im,x,y***REMOVED*** ((im***REMOVED***->image[(y***REMOVED******REMOVED***[(x***REMOVED****4***REMOVED******REMOVED***
#define IMAGING_PIXEL_CMYK(im,x,y***REMOVED*** ((im***REMOVED***->image[(y***REMOVED******REMOVED***[(x***REMOVED****4***REMOVED******REMOVED***
#define IMAGING_PIXEL_YCbCr(im,x,y***REMOVED*** ((im***REMOVED***->image[(y***REMOVED******REMOVED***[(x***REMOVED****4***REMOVED******REMOVED***

#define IMAGING_PIXEL_UINT8(im,x,y***REMOVED*** ((im***REMOVED***->image8[(y***REMOVED******REMOVED***[(x***REMOVED******REMOVED******REMOVED***
#define IMAGING_PIXEL_INT32(im,x,y***REMOVED*** ((im***REMOVED***->image32[(y***REMOVED******REMOVED***[(x***REMOVED******REMOVED******REMOVED***
#define IMAGING_PIXEL_FLOAT32(im,x,y***REMOVED*** (((FLOAT32****REMOVED***(im***REMOVED***->image32[y***REMOVED******REMOVED***[x***REMOVED******REMOVED***

struct ImagingAccessInstance {
  const char* mode;
  void* (*line***REMOVED***(Imaging im, int x, int y***REMOVED***;
  void (*get_pixel***REMOVED***(Imaging im, int x, int y, void* pixel***REMOVED***;
  void (*put_pixel***REMOVED***(Imaging im, int x, int y, const void* pixel***REMOVED***;
***REMOVED***;

struct ImagingHistogramInstance {

    /* Format */
    char mode[IMAGING_MODE_LENGTH***REMOVED***;	/* Band names (of corresponding source image***REMOVED*** */
    int bands;		/* Number of bands (1, 3, or 4***REMOVED*** */

    /* Data */
    long *histogram;	/* Histogram (bands*256 longs***REMOVED*** */

***REMOVED***;


struct ImagingPaletteInstance {

    /* Format */
    char mode[IMAGING_MODE_LENGTH***REMOVED***;	/* Band names */

    /* Data */
    UINT8 palette[1024***REMOVED***;/* Palette data (same format as image data***REMOVED*** */

    INT16* cache;	/* Palette cache (used for predefined palettes***REMOVED*** */
    int keep_cache;	/* This palette will be reused; keep cache */

***REMOVED***;


/* Objects */
/* ------- */

extern int ImagingNewCount;

extern Imaging ImagingNew(const char* mode, int xsize, int ysize***REMOVED***;
extern Imaging ImagingNew2(const char* mode, Imaging imOut, Imaging imIn***REMOVED***;
extern void    ImagingDelete(Imaging im***REMOVED***;

extern Imaging ImagingNewBlock(const char* mode, int xsize, int ysize***REMOVED***;
extern Imaging ImagingNewArray(const char* mode, int xsize, int ysize***REMOVED***;
extern Imaging ImagingNewMap(const char* filename, int readonly,
                             const char* mode, int xsize, int ysize***REMOVED***;

extern Imaging ImagingNewPrologue(const char *mode,
                                  unsigned xsize, unsigned ysize***REMOVED***;
extern Imaging ImagingNewPrologueSubtype(const char *mode,
                                  unsigned xsize, unsigned ysize,
                                  int structure_size***REMOVED***;
extern Imaging ImagingNewEpilogue(Imaging im***REMOVED***;

extern void ImagingCopyInfo(Imaging destination, Imaging source***REMOVED***;

extern void ImagingHistogramDelete(ImagingHistogram histogram***REMOVED***;

extern void ImagingAccessInit(void***REMOVED***;
extern ImagingAccess ImagingAccessNew(Imaging im***REMOVED***;
extern void _ImagingAccessDelete(Imaging im, ImagingAccess access***REMOVED***;
#define ImagingAccessDelete(im, access***REMOVED*** /* nop, for now */
/*#define ImagingAccessDelete(im, access***REMOVED*** \
  ((access***REMOVED***->dynamic ? _ImagingAccessDelete((im***REMOVED***, (access***REMOVED******REMOVED***, 0 : 0***REMOVED******REMOVED*** */

extern ImagingPalette ImagingPaletteNew(const char *mode***REMOVED***;
extern ImagingPalette ImagingPaletteNewBrowser(void***REMOVED***;
extern ImagingPalette ImagingPaletteDuplicate(ImagingPalette palette***REMOVED***;
extern void           ImagingPaletteDelete(ImagingPalette palette***REMOVED***;

extern int  ImagingPaletteCachePrepare(ImagingPalette palette***REMOVED***;
extern void ImagingPaletteCacheUpdate(ImagingPalette palette,
				      int r, int g, int b***REMOVED***;
extern void ImagingPaletteCacheDelete(ImagingPalette palette***REMOVED***;

#define	ImagingPaletteCache(p, r, g, b***REMOVED***\
    p->cache[(r>>2***REMOVED*** + (g>>2***REMOVED****64 + (b>>2***REMOVED****64*64***REMOVED***

extern Imaging ImagingQuantize(Imaging im, int colours, int mode, int kmeans***REMOVED***;

/* Threading */
/* --------- */

typedef void* ImagingSectionCookie;

extern void ImagingSectionEnter(ImagingSectionCookie* cookie***REMOVED***;
extern void ImagingSectionLeave(ImagingSectionCookie* cookie***REMOVED***;

/* Exceptions */
/* ---------- */

extern void* ImagingError_IOError(void***REMOVED***;
extern void* ImagingError_MemoryError(void***REMOVED***;
extern void* ImagingError_ModeError(void***REMOVED***; /* maps to ValueError by default */
extern void* ImagingError_Mismatch(void***REMOVED***; /* maps to ValueError by default */
extern void* ImagingError_ValueError(const char* message***REMOVED***;
extern void ImagingError_Clear(void***REMOVED***;

/* Transform callbacks */
/* ------------------- */

/* standard transforms */
#define IMAGING_TRANSFORM_AFFINE 0
#define IMAGING_TRANSFORM_PERSPECTIVE 2
#define IMAGING_TRANSFORM_QUAD 3


/* standard filters */
#define IMAGING_TRANSFORM_NEAREST 0
#define IMAGING_TRANSFORM_ANTIALIAS 1
#define IMAGING_TRANSFORM_BILINEAR 2
#define IMAGING_TRANSFORM_BICUBIC 3

typedef int (*ImagingTransformMap***REMOVED***(double* X, double* Y,
                                   int x, int y, void* data***REMOVED***;
typedef int (*ImagingTransformFilter***REMOVED***(void* out, Imaging im,
                                      double x, double y,
                                      void* data***REMOVED***;

/* Image Manipulation Methods */
/* -------------------------- */

extern Imaging ImagingAlphaComposite(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingBlend(Imaging imIn1, Imaging imIn2, float alpha***REMOVED***;
extern Imaging ImagingCopy(Imaging im***REMOVED***;
extern Imaging ImagingConvert(Imaging im, const char* mode, ImagingPalette palette, int dither***REMOVED***;
extern Imaging ImagingConvertInPlace(Imaging im, const char* mode***REMOVED***;
extern Imaging ImagingConvertMatrix(Imaging im, const char *mode, float m[***REMOVED******REMOVED***;
extern Imaging ImagingConvertTransparent(Imaging im, const char *mode, int r, int g, int b***REMOVED***;
extern Imaging ImagingCrop(Imaging im, int x0, int y0, int x1, int y1***REMOVED***;
extern Imaging ImagingExpand(Imaging im, int x, int y, int mode***REMOVED***;
extern Imaging ImagingFill(Imaging im, const void* ink***REMOVED***;
extern int ImagingFill2(
    Imaging into, const void* ink, Imaging mask,
    int x0, int y0, int x1, int y1***REMOVED***;
extern Imaging ImagingFillBand(Imaging im, int band, int color***REMOVED***;
extern Imaging ImagingFillLinearGradient(const char* mode***REMOVED***;
extern Imaging ImagingFillRadialGradient(const char* mode***REMOVED***;
extern Imaging ImagingFilter(
    Imaging im, int xsize, int ysize, const FLOAT32* kernel,
    FLOAT32 offset, FLOAT32 divisor***REMOVED***;
extern Imaging ImagingFlipLeftRight(Imaging imOut, Imaging imIn***REMOVED***;
extern Imaging ImagingFlipTopBottom(Imaging imOut, Imaging imIn***REMOVED***;
extern Imaging ImagingGaussianBlur(Imaging im, Imaging imOut, float radius***REMOVED***;
extern Imaging ImagingGetBand(Imaging im, int band***REMOVED***;
extern int ImagingGetBBox(Imaging im, int bbox[4***REMOVED******REMOVED***;
typedef struct { int x, y; INT32 count; INT32 pixel; ***REMOVED*** ImagingColorItem;
extern ImagingColorItem* ImagingGetColors(Imaging im, int maxcolors,
    int *colors***REMOVED***;
extern int ImagingGetExtrema(Imaging im, void *extrema***REMOVED***;
extern int ImagingGetProjection(Imaging im, UINT8* xproj, UINT8* yproj***REMOVED***;
extern ImagingHistogram ImagingGetHistogram(
    Imaging im, Imaging mask, void *extrema***REMOVED***;
extern Imaging ImagingModeFilter(Imaging im, int size***REMOVED***;
extern Imaging ImagingNegative(Imaging im***REMOVED***;
extern Imaging ImagingOffset(Imaging im, int xoffset, int yoffset***REMOVED***;
extern int ImagingPaste(
    Imaging into, Imaging im, Imaging mask,
    int x0, int y0, int x1, int y1***REMOVED***;
extern Imaging ImagingPoint(
    Imaging im, const char* tablemode, const void* table***REMOVED***;
extern Imaging ImagingPointTransform(
    Imaging imIn, double scale, double offset***REMOVED***;
extern Imaging ImagingPutBand(Imaging im, Imaging imIn, int band***REMOVED***;
extern Imaging ImagingRankFilter(Imaging im, int size, int rank***REMOVED***;
extern Imaging ImagingResize(Imaging imOut, Imaging imIn, int filter***REMOVED***;
extern Imaging ImagingRotate(
    Imaging imOut, Imaging imIn, double theta, int filter***REMOVED***;
extern Imaging ImagingRotate90(Imaging imOut, Imaging imIn***REMOVED***;
extern Imaging ImagingRotate180(Imaging imOut, Imaging imIn***REMOVED***;
extern Imaging ImagingRotate270(Imaging imOut, Imaging imIn***REMOVED***;
extern Imaging ImagingStretch(Imaging imOut, Imaging imIn, int filter***REMOVED***;
extern Imaging ImagingTransformPerspective(
    Imaging imOut, Imaging imIn, int x0, int y0, int x1, int y1,
    double a[8***REMOVED***, int filter, int fill***REMOVED***;
extern Imaging ImagingTransformAffine(
    Imaging imOut, Imaging imIn, int x0, int y0, int x1, int y1,
    double a[6***REMOVED***, int filter, int fill***REMOVED***;
extern Imaging ImagingTransformQuad(
    Imaging imOut, Imaging imIn, int x0, int y0, int x1, int y1,
    double a[8***REMOVED***, int filter, int fill***REMOVED***;
extern Imaging ImagingTransform(
    Imaging imOut, Imaging imIn, int x0, int y0, int x1, int y1,
    ImagingTransformMap transform, void* transform_data,
    ImagingTransformFilter filter, void* filter_data,
    int fill***REMOVED***;
extern Imaging ImagingUnsharpMask(
    Imaging im, Imaging imOut, float radius, int percent, int threshold***REMOVED***;

extern Imaging ImagingCopy2(Imaging imOut, Imaging imIn***REMOVED***;
extern Imaging ImagingConvert2(Imaging imOut, Imaging imIn***REMOVED***;

/* Channel operations */
/* any mode, except "F" */
extern Imaging ImagingChopLighter(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopDarker(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopDifference(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopMultiply(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopScreen(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopAdd(
    Imaging imIn1, Imaging imIn2, float scale, int offset***REMOVED***;
extern Imaging ImagingChopSubtract(
    Imaging imIn1, Imaging imIn2, float scale, int offset***REMOVED***;
extern Imaging ImagingChopAddModulo(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopSubtractModulo(Imaging imIn1, Imaging imIn2***REMOVED***;

/* "1" images only */
extern Imaging ImagingChopAnd(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopOr(Imaging imIn1, Imaging imIn2***REMOVED***;
extern Imaging ImagingChopXor(Imaging imIn1, Imaging imIn2***REMOVED***;

/* Image measurement */
extern void ImagingCrack(Imaging im, int x0, int y0***REMOVED***;

/* Graphics */
struct ImagingAffineMatrixInstance {
    float a[9***REMOVED***;
***REMOVED***;

typedef struct ImagingAffineMatrixInstance *ImagingAffineMatrix;

extern int ImagingDrawArc(Imaging im, int x0, int y0, int x1, int y1,
                          int start, int end, const void* ink, int op***REMOVED***;
extern int ImagingDrawBitmap(Imaging im, int x0, int y0, Imaging bitmap,
                             const void* ink, int op***REMOVED***;
extern int ImagingDrawChord(Imaging im, int x0, int y0, int x1, int y1,
                            int start, int end, const void* ink, int fill,
                            int op***REMOVED***;
extern int ImagingDrawEllipse(Imaging im, int x0, int y0, int x1, int y1,
                              const void* ink, int fill, int op***REMOVED***;
extern int ImagingDrawLine(Imaging im, int x0, int y0, int x1, int y1,
			   const void* ink, int op***REMOVED***;
extern int ImagingDrawWideLine(Imaging im, int x0, int y0, int x1, int y1,
                               const void* ink, int width, int op***REMOVED***;
extern int ImagingDrawPieslice(Imaging im, int x0, int y0, int x1, int y1,
                               int start, int end, const void* ink, int fill,
                               int op***REMOVED***;
extern int ImagingDrawPoint(Imaging im, int x, int y, const void* ink, int op***REMOVED***;
extern int ImagingDrawPolygon(Imaging im, int points, int *xy,
			      const void* ink, int fill, int op***REMOVED***;
extern int ImagingDrawRectangle(Imaging im, int x0, int y0, int x1, int y1,
				const void* ink, int fill, int op***REMOVED***;

/* Level 2 graphics (WORK IN PROGRESS***REMOVED*** */
extern ImagingOutline ImagingOutlineNew(void***REMOVED***;
extern void ImagingOutlineDelete(ImagingOutline outline***REMOVED***;

extern int ImagingDrawOutline(Imaging im, ImagingOutline outline,
                              const void* ink, int fill, int op***REMOVED***;

extern int ImagingOutlineMove(ImagingOutline outline, float x, float y***REMOVED***;
extern int ImagingOutlineLine(ImagingOutline outline, float x, float y***REMOVED***;
extern int ImagingOutlineCurve(ImagingOutline outline, float x1, float y1,
                                float x2, float y2, float x3, float y3***REMOVED***;
extern int ImagingOutlineTransform(ImagingOutline outline, double a[6***REMOVED******REMOVED***;

extern int ImagingOutlineClose(ImagingOutline outline***REMOVED***;

/* Special effects */
extern Imaging ImagingEffectSpread(Imaging imIn, int distance***REMOVED***;
extern Imaging ImagingEffectNoise(int xsize, int ysize, float sigma***REMOVED***;
extern Imaging ImagingEffectMandelbrot(int xsize, int ysize,
                                       double extent[4***REMOVED***, int quality***REMOVED***;

/* Obsolete */
extern int ImagingToString(Imaging im, int orientation, char *buffer***REMOVED***;
extern int ImagingFromString(Imaging im, int orientation, char *buffer***REMOVED***;


/* File I/O */
/* -------- */

/* Built-in drivers */
extern Imaging ImagingOpenPPM(const char* filename***REMOVED***;
extern int ImagingSavePPM(Imaging im, const char* filename***REMOVED***;

/* Utility functions */
extern UINT32 ImagingCRC32(UINT32 crc, UINT8* buffer, int bytes***REMOVED***;

/* Codecs */
typedef struct ImagingCodecStateInstance *ImagingCodecState;
typedef int (*ImagingCodec***REMOVED***(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;

extern int ImagingBitDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingEpsEncode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingFliDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingGifDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingGifEncode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingHexDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
#ifdef	HAVE_LIBJPEG
extern int ImagingJpegDecode(Imaging im, ImagingCodecState state,
			     UINT8* buffer, int bytes***REMOVED***;
extern int ImagingJpegDecodeCleanup(ImagingCodecState state***REMOVED***;

extern int ImagingJpegEncode(Imaging im, ImagingCodecState state,
			     UINT8* buffer, int bytes***REMOVED***;
#endif
extern int ImagingLzwDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
#ifdef	HAVE_LIBTIFF
extern int ImagingLibTiffDecode(Imaging im, ImagingCodecState state,
				UINT8* buffer, int bytes***REMOVED***;
extern int ImagingLibTiffEncode(Imaging im, ImagingCodecState state,
				UINT8* buffer, int bytes***REMOVED***;
#endif
#ifdef	HAVE_LIBMPEG
extern int ImagingMpegDecode(Imaging im, ImagingCodecState state,
			     UINT8* buffer, int bytes***REMOVED***;
#endif
extern int ImagingMspDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingPackbitsDecode(Imaging im, ImagingCodecState state,
				 UINT8* buffer, int bytes***REMOVED***;
extern int ImagingPcdDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingPcxDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingPcxEncode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingRawDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingRawEncode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingSunRleDecode(Imaging im, ImagingCodecState state,
			       UINT8* buffer, int bytes***REMOVED***;
extern int ImagingTgaRleDecode(Imaging im, ImagingCodecState state,
			       UINT8* buffer, int bytes***REMOVED***;
extern int ImagingXbmDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingXbmEncode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
#ifdef	HAVE_LIBZ
extern int ImagingZipDecode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
extern int ImagingZipEncode(Imaging im, ImagingCodecState state,
			    UINT8* buffer, int bytes***REMOVED***;
#endif

typedef void (*ImagingShuffler***REMOVED***(UINT8* out, const UINT8* in, int pixels***REMOVED***;

/* Public shufflers */
extern void ImagingPackRGB(UINT8* out, const UINT8* in, int pixels***REMOVED***;
extern void ImagingPackBGR(UINT8* out, const UINT8* in, int pixels***REMOVED***;
extern void ImagingUnpackRGB(UINT8* out, const UINT8* in, int pixels***REMOVED***;
extern void ImagingUnpackBGR(UINT8* out, const UINT8* in, int pixels***REMOVED***;
extern void ImagingUnpackYCC(UINT8* out, const UINT8* in, int pixels***REMOVED***;
extern void ImagingUnpackYCCA(UINT8* out, const UINT8* in, int pixels***REMOVED***;
extern void ImagingUnpackYCbCr(UINT8* out, const UINT8* in, int pixels***REMOVED***;

extern void ImagingConvertRGB2YCbCr(UINT8* out, const UINT8* in, int pixels***REMOVED***;
extern void ImagingConvertYCbCr2RGB(UINT8* out, const UINT8* in, int pixels***REMOVED***;

extern ImagingShuffler ImagingFindUnpacker(const char* mode,
                                           const char* rawmode, int* bits_out***REMOVED***;
extern ImagingShuffler ImagingFindPacker(const char* mode,
                                         const char* rawmode, int* bits_out***REMOVED***;

struct ImagingCodecStateInstance {
    int count;
    int state;
    int errcode;
    int x, y;
    int ystep;
    int xsize, ysize, xoff, yoff;
    ImagingShuffler shuffle;
    int bits, bytes;
    UINT8 *buffer;
    void *context;
***REMOVED***;

/* Errcodes */
#define	IMAGING_CODEC_END	 1
#define	IMAGING_CODEC_OVERRUN	-1
#define	IMAGING_CODEC_BROKEN	-2
#define	IMAGING_CODEC_UNKNOWN	-3
#define	IMAGING_CODEC_CONFIG	-8
#define	IMAGING_CODEC_MEMORY	-9

#if defined(__cplusplus***REMOVED***
***REMOVED***
#endif
