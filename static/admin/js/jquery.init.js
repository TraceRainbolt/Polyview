/*global django:true, jQuery:false*/
/* Puts the included jQuery into our own namespace using noConflict and passing
 * it 'true'. This ensures that the included jQuery doesn't pollute the global
 * namespace (i.e. this preserves pre-existing values for both window.$ and
 * window.jQuery***REMOVED***.
 */
var django = django || {***REMOVED***;
django.jQuery = jQuery.noConflict(true***REMOVED***;
