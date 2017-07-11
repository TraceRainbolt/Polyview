#if defined(__linux__***REMOVED***
# if defined(__x86_64__***REMOVED*** && defined(__LP64__***REMOVED***
#  include <x86_64-linux-gnu/python2.7/pyconfig.h>
# elif defined(__x86_64__***REMOVED*** && defined(__ILP32__***REMOVED***
#  include <x86_64-linux-gnux32/python2.7/pyconfig.h>
# elif defined(__i386__***REMOVED***
#  include <i386-linux-gnu/python2.7/pyconfig.h>
# elif defined(__aarch64__***REMOVED*** && defined(__AARCH64EL__***REMOVED***
#  include <aarch64-linux-gnu/python2.7/pyconfig.h>
# elif defined(__alpha__***REMOVED***
#  include <alpha-linux-gnu/python2.7/pyconfig.h>
# elif defined(__ARM_EABI__***REMOVED*** && defined(__ARM_PCS_VFP***REMOVED***
#  include <arm-linux-gnueabihf/python2.7/pyconfig.h>
# elif defined(__ARM_EABI__***REMOVED*** && !defined(__ARM_PCS_VFP***REMOVED***
#  include <arm-linux-gnueabi/python2.7/pyconfig.h>
# elif defined(__hppa__***REMOVED***
#  include <hppa-linux-gnu/python2.7/pyconfig.h>
# elif defined(__ia64__***REMOVED***
#  include <ia64-linux-gnu/python2.7/pyconfig.h>
# elif defined(__m68k__***REMOVED*** && !defined(__mcoldfire__***REMOVED***
#  include <m68k-linux-gnu/python2.7/pyconfig.h>
# elif defined(__mips_hard_float***REMOVED*** && defined(_MIPSEL***REMOVED***
#  if _MIPS_SIM == _ABIO32
#   include <mipsel-linux-gnu/python2.7/pyconfig.h>
#  elif _MIPS_SIM == _ABIN32
#   include <mips64el-linux-gnuabin32/python2.7/pyconfig.h>
#  elif _MIPS_SIM == _ABI64
#   include <mips64el-linux-gnuabi64/python2.7/pyconfig.h>
#  else
#   error unknown multiarch location for pyconfig.h
#  endif
# elif defined(__mips_hard_float***REMOVED***
#  if _MIPS_SIM == _ABIO32
#   include <mips-linux-gnu/python2.7/pyconfig.h>
#  elif _MIPS_SIM == _ABIN32
#   include <mips64-linux-gnuabin32/python2.7/pyconfig.h>
#  elif _MIPS_SIM == _ABI64
#   include <mips64-linux-gnuabi64/python2.7/pyconfig.h>
#  else
#   error unknown multiarch location for pyconfig.h
#  endif
# elif defined(__or1k__***REMOVED***
#  include <or1k-linux-gnu/python2.7/pyconfig.h>
# elif defined(__powerpc__***REMOVED*** && defined(__SPE__***REMOVED***
#  include <powerpc-linux-gnuspe/python2.7/pyconfig.h>
# elif defined(__powerpc64__***REMOVED***
#  if defined(__LITTLE_ENDIAN__***REMOVED***
#    include <powerpc64le-linux-gnu/python2.7/pyconfig.h>
#  else
#    include <powerpc64-linux-gnu/python2.7/pyconfig.h>
#  endif
# elif defined(__powerpc__***REMOVED***
#  include <powerpc-linux-gnu/python2.7/pyconfig.h>
# elif defined(__s390x__***REMOVED***
#  include <s390x-linux-gnu/python2.7/pyconfig.h>
# elif defined(__s390__***REMOVED***
#  include <s390-linux-gnu/python2.7/pyconfig.h>
# elif defined(__sh__***REMOVED*** && defined(__LITTLE_ENDIAN__***REMOVED***
#  include <sh4-linux-gnu/python2.7/pyconfig.h>
# elif defined(__sparc__***REMOVED*** && defined(__arch64__***REMOVED***
#  include <sparc64-linux-gnu/python2.7/pyconfig.h>
# elif defined(__sparc__***REMOVED***
#  include <sparc-linux-gnu/python2.7/pyconfig.h>
# else
#   error unknown multiarch location for pyconfig.h
# endif
#elif defined(__FreeBSD_kernel__***REMOVED***
# if defined(__LP64__***REMOVED***
#  include <x86_64-kfreebsd-gnu/python2.7/pyconfig.h>
# elif defined(__i386__***REMOVED***
#  include <i386-kfreebsd-gnu/python2.7/pyconfig.h>
# else
#   error unknown multiarch location for pyconfig.h
# endif
#elif defined(__gnu_hurd__***REMOVED***
# include <i386-gnu/python2.7/pyconfig.h>
#else
# error unknown multiarch location for pyconfig.h
#endif
