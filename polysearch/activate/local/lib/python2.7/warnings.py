***REMOVED***Python part of the warnings subsystem.***REMOVED***

# Note: function level imports should *not* be used
# in this module as it may cause import lock deadlock.
# See bug 683658.
import linecache
import sys
import types

__all__ = ["warn", "showwarning", "formatwarning", "filterwarnings",
           "resetwarnings", "catch_warnings"***REMOVED***


def warnpy3k(message, category=None, stacklevel=1***REMOVED***:
    ***REMOVED***Issue a deprecation warning for Python 3.x related changes.

    Warnings are omitted unless Python is started with the -3 option.
    ***REMOVED***
    if sys.py3kwarning:
        if category is None:
            category = DeprecationWarning
        warn(message, category, stacklevel+1***REMOVED***

def _show_warning(message, category, filename, lineno, file=None, line=None***REMOVED***:
    ***REMOVED***Hook to write a warning to a file; replace if you like.***REMOVED***
    if file is None:
        file = sys.stderr
    try:
        file.write(formatwarning(message, category, filename, lineno, line***REMOVED******REMOVED***
    except IOError:
        pass # the file (probably stderr***REMOVED*** is invalid - this warning gets lost.
# Keep a working version around in case the deprecation of the old API is
# triggered.
showwarning = _show_warning

def formatwarning(message, category, filename, lineno, line=None***REMOVED***:
    ***REMOVED***Function to format a warning the standard way.***REMOVED***
    s =  "%s:%s: %s: %s\n" % (filename, lineno, category.__name__, message***REMOVED***
    line = linecache.getline(filename, lineno***REMOVED*** if line is None else line
    if line:
        line = line.strip(***REMOVED***
        s += "  %s\n" % line
    return s

def filterwarnings(action, message="", category=Warning, module="", lineno=0,
                   append=0***REMOVED***:
    ***REMOVED***Insert an entry into the list of warnings filters (at the front***REMOVED***.

    'action' -- one of "error", "ignore", "always", "default", "module",
                or "once"
    'message' -- a regex that the warning message must match
    'category' -- a class that the warning must be a subclass of
    'module' -- a regex that the module name must match
    'lineno' -- an integer line number, 0 matches all warnings
    'append' -- if true, append to the list of filters
    ***REMOVED***
    import re
    assert action in ("error", "ignore", "always", "default", "module",
                      "once"***REMOVED***, "invalid action: %r" % (action,***REMOVED***
    assert isinstance(message, basestring***REMOVED***, "message must be a string"
    assert isinstance(category, (type, types.ClassType***REMOVED******REMOVED***, \
           "category must be a class"
    assert issubclass(category, Warning***REMOVED***, "category must be a Warning subclass"
    assert isinstance(module, basestring***REMOVED***, "module must be a string"
    assert isinstance(lineno, int***REMOVED*** and lineno >= 0, \
           "lineno must be an int >= 0"
    item = (action, re.compile(message, re.I***REMOVED***, category,
            re.compile(module***REMOVED***, lineno***REMOVED***
    if append:
        filters.append(item***REMOVED***
    else:
        filters.insert(0, item***REMOVED***

def simplefilter(action, category=Warning, lineno=0, append=0***REMOVED***:
    ***REMOVED***Insert a simple entry into the list of warnings filters (at the front***REMOVED***.

    A simple filter matches all modules and messages.
    'action' -- one of "error", "ignore", "always", "default", "module",
                or "once"
    'category' -- a class that the warning must be a subclass of
    'lineno' -- an integer line number, 0 matches all warnings
    'append' -- if true, append to the list of filters
    ***REMOVED***
    assert action in ("error", "ignore", "always", "default", "module",
                      "once"***REMOVED***, "invalid action: %r" % (action,***REMOVED***
    assert isinstance(lineno, int***REMOVED*** and lineno >= 0, \
           "lineno must be an int >= 0"
    item = (action, None, category, None, lineno***REMOVED***
    if append:
        filters.append(item***REMOVED***
    else:
        filters.insert(0, item***REMOVED***

def resetwarnings(***REMOVED***:
    ***REMOVED***Clear the list of warning filters, so that no filters are active.***REMOVED***
    filters[:***REMOVED*** = [***REMOVED***

class _OptionError(Exception***REMOVED***:
    ***REMOVED***Exception used by option processing helpers.***REMOVED***
    pass

# Helper to process -W options passed via sys.warnoptions
def _processoptions(args***REMOVED***:
    for arg in args:
        try:
            _setoption(arg***REMOVED***
        except _OptionError, msg:
            print >>sys.stderr, "Invalid -W option ignored:", msg

# Helper for _processoptions(***REMOVED***
def _setoption(arg***REMOVED***:
    import re
    parts = arg.split(':'***REMOVED***
    if len(parts***REMOVED*** > 5:
        raise _OptionError("too many fields (max 5***REMOVED***: %r" % (arg,***REMOVED******REMOVED***
    while len(parts***REMOVED*** < 5:
        parts.append(''***REMOVED***
    action, message, category, module, lineno = [s.strip(***REMOVED***
                                                 for s in parts***REMOVED***
    action = _getaction(action***REMOVED***
    message = re.escape(message***REMOVED***
    category = _getcategory(category***REMOVED***
    module = re.escape(module***REMOVED***
    if module:
        module = module + '$'
    if lineno:
        try:
            lineno = int(lineno***REMOVED***
            if lineno < 0:
                raise ValueError
        except (ValueError, OverflowError***REMOVED***:
            raise _OptionError("invalid lineno %r" % (lineno,***REMOVED******REMOVED***
    else:
        lineno = 0
    filterwarnings(action, message, category, module, lineno***REMOVED***

# Helper for _setoption(***REMOVED***
def _getaction(action***REMOVED***:
    if not action:
        return "default"
    if action == "all": return "always" # Alias
    for a in ('default', 'always', 'ignore', 'module', 'once', 'error'***REMOVED***:
        if a.startswith(action***REMOVED***:
            return a
    raise _OptionError("invalid action: %r" % (action,***REMOVED******REMOVED***

# Helper for _setoption(***REMOVED***
def _getcategory(category***REMOVED***:
    import re
    if not category:
        return Warning
    if re.match("^[a-zA-Z0-9_***REMOVED***+$", category***REMOVED***:
        try:
            cat = eval(category***REMOVED***
        except NameError:
            raise _OptionError("unknown warning category: %r" % (category,***REMOVED******REMOVED***
    else:
        i = category.rfind("."***REMOVED***
        module = category[:i***REMOVED***
        klass = category[i+1:***REMOVED***
        try:
            m = __import__(module, None, None, [klass***REMOVED******REMOVED***
        except ImportError:
            raise _OptionError("invalid module name: %r" % (module,***REMOVED******REMOVED***
        try:
            cat = getattr(m, klass***REMOVED***
        except AttributeError:
            raise _OptionError("unknown warning category: %r" % (category,***REMOVED******REMOVED***
    if not issubclass(cat, Warning***REMOVED***:
        raise _OptionError("invalid warning category: %r" % (category,***REMOVED******REMOVED***
    return cat


# Code typically replaced by _warnings
def warn(message, category=None, stacklevel=1***REMOVED***:
    ***REMOVED***Issue a warning, or maybe ignore it or raise an exception.***REMOVED***
    # Check if message is already a Warning object
    if isinstance(message, Warning***REMOVED***:
        category = message.__class__
    # Check category argument
    if category is None:
        category = UserWarning
    assert issubclass(category, Warning***REMOVED***
    # Get context information
    try:
        caller = sys._getframe(stacklevel***REMOVED***
    except ValueError:
        globals = sys.__dict__
        lineno = 1
    else:
        globals = caller.f_globals
        lineno = caller.f_lineno
    if '__name__' in globals:
        module = globals['__name__'***REMOVED***
    else:
        module = "<string>"
    filename = globals.get('__file__'***REMOVED***
    if filename:
        fnl = filename.lower(***REMOVED***
        if fnl.endswith((".pyc", ".pyo"***REMOVED******REMOVED***:
            filename = filename[:-1***REMOVED***
    else:
        if module == "__main__":
            try:
                filename = sys.argv[0***REMOVED***
            except AttributeError:
                # embedded interpreters don't have sys.argv, see bug #839151
                filename = '__main__'
        if not filename:
            filename = module
    registry = globals.setdefault("__warningregistry__", {***REMOVED******REMOVED***
    warn_explicit(message, category, filename, lineno, module, registry,
                  globals***REMOVED***

def warn_explicit(message, category, filename, lineno,
                  module=None, registry=None, module_globals=None***REMOVED***:
    lineno = int(lineno***REMOVED***
    if module is None:
        module = filename or "<unknown>"
        if module[-3:***REMOVED***.lower(***REMOVED*** == ".py":
            module = module[:-3***REMOVED*** # XXX What about leading pathname?
    if registry is None:
        registry = {***REMOVED***
    if isinstance(message, Warning***REMOVED***:
        text = str(message***REMOVED***
        category = message.__class__
    else:
        text = message
        message = category(message***REMOVED***
    key = (text, category, lineno***REMOVED***
    # Quick test for common case
    if registry.get(key***REMOVED***:
        return
    # Search the filters
    for item in filters:
        action, msg, cat, mod, ln = item
        if ((msg is None or msg.match(text***REMOVED******REMOVED*** and
            issubclass(category, cat***REMOVED*** and
            (mod is None or mod.match(module***REMOVED******REMOVED*** and
            (ln == 0 or lineno == ln***REMOVED******REMOVED***:
            break
    else:
        action = defaultaction
    # Early exit actions
    if action == "ignore":
        registry[key***REMOVED*** = 1
        return

    # Prime the linecache for formatting, in case the
    # "file" is actually in a zipfile or something.
    linecache.getlines(filename, module_globals***REMOVED***

    if action == "error":
        raise message
    # Other actions
    if action == "once":
        registry[key***REMOVED*** = 1
        oncekey = (text, category***REMOVED***
        if onceregistry.get(oncekey***REMOVED***:
            return
        onceregistry[oncekey***REMOVED*** = 1
    elif action == "always":
        pass
    elif action == "module":
        registry[key***REMOVED*** = 1
        altkey = (text, category, 0***REMOVED***
        if registry.get(altkey***REMOVED***:
            return
        registry[altkey***REMOVED*** = 1
    elif action == "default":
        registry[key***REMOVED*** = 1
    else:
        # Unrecognized actions are errors
        raise RuntimeError(
              "Unrecognized action (%r***REMOVED*** in warnings.filters:\n %s" %
              (action, item***REMOVED******REMOVED***
    # Print message and context
    showwarning(message, category, filename, lineno***REMOVED***


class WarningMessage(object***REMOVED***:

    ***REMOVED***Holds the result of a single showwarning(***REMOVED*** call.***REMOVED***

    _WARNING_DETAILS = ("message", "category", "filename", "lineno", "file",
                        "line"***REMOVED***

    def __init__(self, message, category, filename, lineno, file=None,
                    line=None***REMOVED***:
        local_values = locals(***REMOVED***
        for attr in self._WARNING_DETAILS:
            setattr(self, attr, local_values[attr***REMOVED******REMOVED***
        self._category_name = category.__name__ if category else None

    def __str__(self***REMOVED***:
        return ("{message : %r, category : %r, filename : %r, lineno : %s, "
                    "line : %r***REMOVED***" % (self.message, self._category_name,
                                    self.filename, self.lineno, self.line***REMOVED******REMOVED***


class catch_warnings(object***REMOVED***:

    ***REMOVED***A context manager that copies and restores the warnings filter upon
    exiting the context.

    The 'record' argument specifies whether warnings should be captured by a
    custom implementation of warnings.showwarning(***REMOVED*** and be appended to a list
    returned by the context manager. Otherwise None is returned by the context
    manager. The objects appended to the list are arguments whose attributes
    mirror the arguments to showwarning(***REMOVED***.

    The 'module' argument is to specify an alternative module to the module
    named 'warnings' and imported under that name. This argument is only useful
    when testing the warnings module itself.

    ***REMOVED***

    def __init__(self, record=False, module=None***REMOVED***:
        ***REMOVED***Specify whether to record warnings and if an alternative module
        should be used other than sys.modules['warnings'***REMOVED***.

        For compatibility with Python 3.0, please consider all arguments to be
        keyword-only.

        ***REMOVED***
        self._record = record
        self._module = sys.modules['warnings'***REMOVED*** if module is None else module
        self._entered = False

    def __repr__(self***REMOVED***:
        args = [***REMOVED***
        if self._record:
            args.append("record=True"***REMOVED***
        if self._module is not sys.modules['warnings'***REMOVED***:
            args.append("module=%r" % self._module***REMOVED***
        name = type(self***REMOVED***.__name__
        return "%s(%s***REMOVED***" % (name, ", ".join(args***REMOVED******REMOVED***

    def __enter__(self***REMOVED***:
        if self._entered:
            raise RuntimeError("Cannot enter %r twice" % self***REMOVED***
        self._entered = True
        self._filters = self._module.filters
        self._module.filters = self._filters[:***REMOVED***
        self._showwarning = self._module.showwarning
        if self._record:
            log = [***REMOVED***
            def showwarning(*args, **kwargs***REMOVED***:
                log.append(WarningMessage(*args, **kwargs***REMOVED******REMOVED***
            self._module.showwarning = showwarning
            return log
        else:
            return None

    def __exit__(self, *exc_info***REMOVED***:
        if not self._entered:
            raise RuntimeError("Cannot exit %r without entering first" % self***REMOVED***
        self._module.filters = self._filters
        self._module.showwarning = self._showwarning


# filters contains a sequence of filter 5-tuples
# The components of the 5-tuple are:
# - an action: error, ignore, always, default, module, or once
# - a compiled regex that must match the warning message
# - a class representing the warning category
# - a compiled regex that must match the module that is being warned
# - a line number for the line being warning, or 0 to mean any line
# If either if the compiled regexs are None, match anything.
_warnings_defaults = False
try:
    from _warnings import (filters, default_action, once_registry,
                            warn, warn_explicit***REMOVED***
    defaultaction = default_action
    onceregistry = once_registry
    _warnings_defaults = True
except ImportError:
    filters = [***REMOVED***
    defaultaction = "default"
    onceregistry = {***REMOVED***


# Module initialization
_processoptions(sys.warnoptions***REMOVED***
if not _warnings_defaults:
    silence = [ImportWarning, PendingDeprecationWarning***REMOVED***
    # Don't silence DeprecationWarning if -3 or -Q was used.
    if not sys.py3kwarning and not sys.flags.division_warning:
        silence.append(DeprecationWarning***REMOVED***
    for cls in silence:
        simplefilter("ignore", category=cls***REMOVED***
    bytes_warning = sys.flags.bytes_warning
    if bytes_warning > 1:
        bytes_action = "error"
    elif bytes_warning:
        bytes_action = "default"
    else:
        bytes_action = "ignore"
    simplefilter(bytes_action, category=BytesWarning, append=1***REMOVED***
del _warnings_defaults
