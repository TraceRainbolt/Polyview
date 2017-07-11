
#ifndef Py_BITSET_H
#define Py_BITSET_H
#ifdef __cplusplus
extern "C" {
#endif

/* Bitset interface */

#define BYTE		char

typedef BYTE *bitset;

bitset newbitset(int nbits***REMOVED***;
void delbitset(bitset bs***REMOVED***;
#define testbit(ss, ibit***REMOVED*** (((ss***REMOVED***[BIT2BYTE(ibit***REMOVED******REMOVED*** & BIT2MASK(ibit***REMOVED******REMOVED*** != 0***REMOVED***
int addbit(bitset bs, int ibit***REMOVED***; /* Returns 0 if already set */
int samebitset(bitset bs1, bitset bs2, int nbits***REMOVED***;
void mergebitset(bitset bs1, bitset bs2, int nbits***REMOVED***;

#define BITSPERBYTE	(8*sizeof(BYTE***REMOVED******REMOVED***
#define NBYTES(nbits***REMOVED***	(((nbits***REMOVED*** + BITSPERBYTE - 1***REMOVED*** / BITSPERBYTE***REMOVED***

#define BIT2BYTE(ibit***REMOVED***	((ibit***REMOVED*** / BITSPERBYTE***REMOVED***
#define BIT2SHIFT(ibit***REMOVED***	((ibit***REMOVED*** % BITSPERBYTE***REMOVED***
#define BIT2MASK(ibit***REMOVED***	(1 << BIT2SHIFT(ibit***REMOVED******REMOVED***
#define BYTE2BIT(ibyte***REMOVED***	((ibyte***REMOVED*** * BITSPERBYTE***REMOVED***

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_BITSET_H */
