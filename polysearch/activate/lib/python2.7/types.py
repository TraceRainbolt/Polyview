***REMOVED***Define names for all type symbols known in the standard interpreter.

Types that are part of optional modules (e.g. array***REMOVED*** are not listed.
***REMOVED***
import sys

# Iterators in Python aren't a matter of type but of protocol.  A large
# and changing number of builtin types implement *some* flavor of
# iterator.  Don't check the type!  Use hasattr to check for both
# "__iter__" and "next" attributes instead.

NoneType = type(None***REMOVED***
TypeType = type
ObjectType = object

IntType = int
LongType = long
FloatType = float
BooleanType = bool
try:
    ComplexType = complex
except NameError:
    pass

StringType = str

# StringTypes is already outdated.  Instead of writing "type(x***REMOVED*** in
# types.StringTypes", you should use "isinstance(x, basestring***REMOVED***".  But
# we keep around for compatibility with Python 2.2.
try:
    UnicodeType = unicode
    StringTypes = (StringType, UnicodeType***REMOVED***
except NameError:
    StringTypes = (StringType,***REMOVED***

BufferType = buffer

TupleType = tuple
ListType = list
DictType = DictionaryType = dict

def _f(***REMOVED***: pass
FunctionType = type(_f***REMOVED***
LambdaType = type(lambda: None***REMOVED***         # Same as FunctionType
CodeType = type(_f.func_code***REMOVED***

def _g(***REMOVED***:
    yield 1
GeneratorType = type(_g(***REMOVED******REMOVED***

class _C:
    def _m(self***REMOVED***: pass
ClassType = type(_C***REMOVED***
UnboundMethodType = type(_C._m***REMOVED***         # Same as MethodType
_x = _C(***REMOVED***
InstanceType = type(_x***REMOVED***
MethodType = type(_x._m***REMOVED***

BuiltinFunctionType = type(len***REMOVED***
BuiltinMethodType = type([***REMOVED***.append***REMOVED***     # Same as BuiltinFunctionType

ModuleType = type(sys***REMOVED***
FileType = file
XRangeType = xrange

try:
    raise TypeError
except TypeError:
    tb = sys.exc_info(***REMOVED***[2***REMOVED***
    TracebackType = type(tb***REMOVED***
    FrameType = type(tb.tb_frame***REMOVED***
    del tb

SliceType = slice
EllipsisType = type(Ellipsis***REMOVED***

DictProxyType = type(TypeType.__dict__***REMOVED***
NotImplementedType = type(NotImplemented***REMOVED***

# For Jython, the following two types are identical
GetSetDescriptorType = type(FunctionType.func_code***REMOVED***
MemberDescriptorType = type(FunctionType.func_globals***REMOVED***

del sys, _f, _g, _C, _x                           # Not for export
