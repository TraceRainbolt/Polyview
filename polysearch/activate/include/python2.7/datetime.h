/*  datetime.h
 */

#ifndef DATETIME_H
#define DATETIME_H
#ifdef __cplusplus
extern "C" {
#endif

/* Fields are packed into successive bytes, each viewed as unsigned and
 * big-endian, unless otherwise noted:
 *
 * byte offset
 *  0           year     2 bytes, 1-9999
 *  2           month    1 byte, 1-12
 *  3           day      1 byte, 1-31
 *  4           hour     1 byte, 0-23
 *  5           minute   1 byte, 0-59
 *  6           second   1 byte, 0-59
 *  7           usecond  3 bytes, 0-999999
 * 10
 */

/* # of bytes for year, month, and day. */
#define _PyDateTime_DATE_DATASIZE 4

/* # of bytes for hour, minute, second, and usecond. */
#define _PyDateTime_TIME_DATASIZE 6

/* # of bytes for year, month, day, hour, minute, second, and usecond. */
#define _PyDateTime_DATETIME_DATASIZE 10


typedef struct
{
    PyObject_HEAD
    long hashcode;              /* -1 when unknown */
    int days;                   /* -MAX_DELTA_DAYS <= days <= MAX_DELTA_DAYS */
    int seconds;                /* 0 <= seconds < 24*3600 is invariant */
    int microseconds;           /* 0 <= microseconds < 1000000 is invariant */
***REMOVED*** PyDateTime_Delta;

typedef struct
{
    PyObject_HEAD               /* a pure abstract base class */
***REMOVED*** PyDateTime_TZInfo;


/* The datetime and time types have hashcodes, and an optional tzinfo member,
 * present if and only if hastzinfo is true.
 */
#define _PyTZINFO_HEAD          \
    PyObject_HEAD               \
    long hashcode;              \
    char hastzinfo;             /* boolean flag */

/* No _PyDateTime_BaseTZInfo is allocated; it's just to have something
 * convenient to cast to, when getting at the hastzinfo member of objects
 * starting with _PyTZINFO_HEAD.
 */
typedef struct
{
    _PyTZINFO_HEAD
***REMOVED*** _PyDateTime_BaseTZInfo;

/* All time objects are of PyDateTime_TimeType, but that can be allocated
 * in two ways, with or without a tzinfo member.  Without is the same as
 * tzinfo == None, but consumes less memory.  _PyDateTime_BaseTime is an
 * internal struct used to allocate the right amount of space for the
 * "without" case.
 */
#define _PyDateTime_TIMEHEAD    \
    _PyTZINFO_HEAD              \
    unsigned char data[_PyDateTime_TIME_DATASIZE***REMOVED***;

typedef struct
{
    _PyDateTime_TIMEHEAD
***REMOVED*** _PyDateTime_BaseTime;         /* hastzinfo false */

typedef struct
{
    _PyDateTime_TIMEHEAD
    PyObject *tzinfo;
***REMOVED*** PyDateTime_Time;              /* hastzinfo true */


/* All datetime objects are of PyDateTime_DateTimeType, but that can be
 * allocated in two ways too, just like for time objects above.  In addition,
 * the plain date type is a base class for datetime, so it must also have
 * a hastzinfo member (although it's unused there***REMOVED***.
 */
typedef struct
{
    _PyTZINFO_HEAD
    unsigned char data[_PyDateTime_DATE_DATASIZE***REMOVED***;
***REMOVED*** PyDateTime_Date;

#define _PyDateTime_DATETIMEHEAD        \
    _PyTZINFO_HEAD                      \
    unsigned char data[_PyDateTime_DATETIME_DATASIZE***REMOVED***;

typedef struct
{
    _PyDateTime_DATETIMEHEAD
***REMOVED*** _PyDateTime_BaseDateTime;     /* hastzinfo false */

typedef struct
{
    _PyDateTime_DATETIMEHEAD
    PyObject *tzinfo;
***REMOVED*** PyDateTime_DateTime;          /* hastzinfo true */


/* Apply for date and datetime instances. */
#define PyDateTime_GET_YEAR(o***REMOVED***     ((((PyDateTime_Date****REMOVED***o***REMOVED***->data[0***REMOVED*** << 8***REMOVED*** | \
                     ((PyDateTime_Date****REMOVED***o***REMOVED***->data[1***REMOVED******REMOVED***
#define PyDateTime_GET_MONTH(o***REMOVED***    (((PyDateTime_Date****REMOVED***o***REMOVED***->data[2***REMOVED******REMOVED***
#define PyDateTime_GET_DAY(o***REMOVED***      (((PyDateTime_Date****REMOVED***o***REMOVED***->data[3***REMOVED******REMOVED***

#define PyDateTime_DATE_GET_HOUR(o***REMOVED***        (((PyDateTime_DateTime****REMOVED***o***REMOVED***->data[4***REMOVED******REMOVED***
#define PyDateTime_DATE_GET_MINUTE(o***REMOVED***      (((PyDateTime_DateTime****REMOVED***o***REMOVED***->data[5***REMOVED******REMOVED***
#define PyDateTime_DATE_GET_SECOND(o***REMOVED***      (((PyDateTime_DateTime****REMOVED***o***REMOVED***->data[6***REMOVED******REMOVED***
#define PyDateTime_DATE_GET_MICROSECOND(o***REMOVED***              \
    ((((PyDateTime_DateTime****REMOVED***o***REMOVED***->data[7***REMOVED*** << 16***REMOVED*** |       \
     (((PyDateTime_DateTime****REMOVED***o***REMOVED***->data[8***REMOVED*** << 8***REMOVED***  |       \
      ((PyDateTime_DateTime****REMOVED***o***REMOVED***->data[9***REMOVED******REMOVED***

/* Apply for time instances. */
#define PyDateTime_TIME_GET_HOUR(o***REMOVED***        (((PyDateTime_Time****REMOVED***o***REMOVED***->data[0***REMOVED******REMOVED***
#define PyDateTime_TIME_GET_MINUTE(o***REMOVED***      (((PyDateTime_Time****REMOVED***o***REMOVED***->data[1***REMOVED******REMOVED***
#define PyDateTime_TIME_GET_SECOND(o***REMOVED***      (((PyDateTime_Time****REMOVED***o***REMOVED***->data[2***REMOVED******REMOVED***
#define PyDateTime_TIME_GET_MICROSECOND(o***REMOVED***              \
    ((((PyDateTime_Time****REMOVED***o***REMOVED***->data[3***REMOVED*** << 16***REMOVED*** |           \
     (((PyDateTime_Time****REMOVED***o***REMOVED***->data[4***REMOVED*** << 8***REMOVED***  |           \
      ((PyDateTime_Time****REMOVED***o***REMOVED***->data[5***REMOVED******REMOVED***


/* Define structure for C API. */
typedef struct {
    /* type objects */
    PyTypeObject *DateType;
    PyTypeObject *DateTimeType;
    PyTypeObject *TimeType;
    PyTypeObject *DeltaType;
    PyTypeObject *TZInfoType;

    /* constructors */
    PyObject *(*Date_FromDate***REMOVED***(int, int, int, PyTypeObject****REMOVED***;
    PyObject *(*DateTime_FromDateAndTime***REMOVED***(int, int, int, int, int, int, int,
        PyObject*, PyTypeObject****REMOVED***;
    PyObject *(*Time_FromTime***REMOVED***(int, int, int, int, PyObject*, PyTypeObject****REMOVED***;
    PyObject *(*Delta_FromDelta***REMOVED***(int, int, int, int, PyTypeObject****REMOVED***;

    /* constructors for the DB API */
    PyObject *(*DateTime_FromTimestamp***REMOVED***(PyObject*, PyObject*, PyObject****REMOVED***;
    PyObject *(*Date_FromTimestamp***REMOVED***(PyObject*, PyObject****REMOVED***;

***REMOVED*** PyDateTime_CAPI;

#define PyDateTime_CAPSULE_NAME "datetime.datetime_CAPI"


/* "magic" constant used to partially protect against developer mistakes. */
#define DATETIME_API_MAGIC 0x414548d5

#ifdef Py_BUILD_CORE

/* Macros for type checking when building the Python core. */
#define PyDate_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyDateTime_DateType***REMOVED***
#define PyDate_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDateTime_DateType***REMOVED***

#define PyDateTime_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyDateTime_DateTimeType***REMOVED***
#define PyDateTime_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDateTime_DateTimeType***REMOVED***

#define PyTime_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyDateTime_TimeType***REMOVED***
#define PyTime_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDateTime_TimeType***REMOVED***

#define PyDelta_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyDateTime_DeltaType***REMOVED***
#define PyDelta_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDateTime_DeltaType***REMOVED***

#define PyTZInfo_Check(op***REMOVED*** PyObject_TypeCheck(op, &PyDateTime_TZInfoType***REMOVED***
#define PyTZInfo_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == &PyDateTime_TZInfoType***REMOVED***

#else

/* Define global variable for the C API and a macro for setting it. */
static PyDateTime_CAPI *PyDateTimeAPI = NULL;

#define PyDateTime_IMPORT \
    PyDateTimeAPI = (PyDateTime_CAPI ****REMOVED***PyCapsule_Import(PyDateTime_CAPSULE_NAME, 0***REMOVED***

/* Macros for type checking when not building the Python core. */
#define PyDate_Check(op***REMOVED*** PyObject_TypeCheck(op, PyDateTimeAPI->DateType***REMOVED***
#define PyDate_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == PyDateTimeAPI->DateType***REMOVED***

#define PyDateTime_Check(op***REMOVED*** PyObject_TypeCheck(op, PyDateTimeAPI->DateTimeType***REMOVED***
#define PyDateTime_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == PyDateTimeAPI->DateTimeType***REMOVED***

#define PyTime_Check(op***REMOVED*** PyObject_TypeCheck(op, PyDateTimeAPI->TimeType***REMOVED***
#define PyTime_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == PyDateTimeAPI->TimeType***REMOVED***

#define PyDelta_Check(op***REMOVED*** PyObject_TypeCheck(op, PyDateTimeAPI->DeltaType***REMOVED***
#define PyDelta_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == PyDateTimeAPI->DeltaType***REMOVED***

#define PyTZInfo_Check(op***REMOVED*** PyObject_TypeCheck(op, PyDateTimeAPI->TZInfoType***REMOVED***
#define PyTZInfo_CheckExact(op***REMOVED*** (Py_TYPE(op***REMOVED*** == PyDateTimeAPI->TZInfoType***REMOVED***

/* Macros for accessing constructors in a simplified fashion. */
#define PyDate_FromDate(year, month, day***REMOVED*** \
    PyDateTimeAPI->Date_FromDate(year, month, day, PyDateTimeAPI->DateType***REMOVED***

#define PyDateTime_FromDateAndTime(year, month, day, hour, min, sec, usec***REMOVED*** \
    PyDateTimeAPI->DateTime_FromDateAndTime(year, month, day, hour, \
        min, sec, usec, Py_None, PyDateTimeAPI->DateTimeType***REMOVED***

#define PyTime_FromTime(hour, minute, second, usecond***REMOVED*** \
    PyDateTimeAPI->Time_FromTime(hour, minute, second, usecond, \
        Py_None, PyDateTimeAPI->TimeType***REMOVED***

#define PyDelta_FromDSU(days, seconds, useconds***REMOVED*** \
    PyDateTimeAPI->Delta_FromDelta(days, seconds, useconds, 1, \
        PyDateTimeAPI->DeltaType***REMOVED***

/* Macros supporting the DB API. */
#define PyDateTime_FromTimestamp(args***REMOVED*** \
    PyDateTimeAPI->DateTime_FromTimestamp( \
        (PyObject****REMOVED*** (PyDateTimeAPI->DateTimeType***REMOVED***, args, NULL***REMOVED***

#define PyDate_FromTimestamp(args***REMOVED*** \
    PyDateTimeAPI->Date_FromTimestamp( \
        (PyObject****REMOVED*** (PyDateTimeAPI->DateType***REMOVED***, args***REMOVED***

#endif  /* Py_BUILD_CORE */

#ifdef __cplusplus
***REMOVED***
#endif
#endif
