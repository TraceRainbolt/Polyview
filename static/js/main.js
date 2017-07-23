$(document***REMOVED***.ready(function(***REMOVED*** {
    $('.course-title'***REMOVED***.click(function(***REMOVED*** {
    	$(this***REMOVED***.parent(***REMOVED***.closest('div'***REMOVED***.find('thead'***REMOVED***.toggle(***REMOVED***;
    	$(this***REMOVED***.parent(***REMOVED***.closest('div'***REMOVED***.find('tbody'***REMOVED***.toggle(***REMOVED***;
***REMOVED******REMOVED***;

    $('.remove-container'***REMOVED***.click(function(***REMOVED*** {
        $(this***REMOVED***.parents('tbody'***REMOVED***.find('.row-toggleable'***REMOVED***.toggle(***REMOVED***;
        if($(this***REMOVED***.children(***REMOVED***.eq(0***REMOVED***.text(***REMOVED*** === "−"***REMOVED***
            $(this***REMOVED***.children(***REMOVED***.eq(0***REMOVED***.text("+"***REMOVED***;
        else
            $(this***REMOVED***.children(***REMOVED***.eq(0***REMOVED***.text("−"***REMOVED***;
***REMOVED******REMOVED***;
***REMOVED******REMOVED***