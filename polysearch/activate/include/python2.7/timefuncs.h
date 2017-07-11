/*  timefuncs.h
 */

/* Utility function related to timemodule.c. */

#ifndef TIMEFUNCS_H
#define TIMEFUNCS_H
#ifdef __cplusplus
extern "C" {
#endif


/* Cast double x to time_t, but raise ValueError if x is too large
 * to fit in a time_t.  ValueError is set on return iff the return
 * value is (time_t***REMOVED***-1 and PyErr_Occurred(***REMOVED***.
 */
PyAPI_FUNC(time_t***REMOVED*** _PyTime_DoubleToTimet(double x***REMOVED***;

/* Get the current time since the epoch in seconds */
PyAPI_FUNC(double***REMOVED*** _PyTime_FloatTime(void***REMOVED***;


#ifdef __cplusplus
***REMOVED***
#endif
#endif  /* TIMEFUNCS_H */
