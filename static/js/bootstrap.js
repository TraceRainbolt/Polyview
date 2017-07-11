/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com***REMOVED***
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under the MIT license
 */

if (typeof jQuery === 'undefined'***REMOVED*** {
  throw new Error('Bootstrap\'s JavaScript requires jQuery'***REMOVED***
***REMOVED***

+function ($***REMOVED*** {
  'use strict';
  var version = $.fn.jquery.split(' '***REMOVED***[0***REMOVED***.split('.'***REMOVED***
  if ((version[0***REMOVED*** < 2 && version[1***REMOVED*** < 9***REMOVED*** || (version[0***REMOVED*** == 1 && version[1***REMOVED*** == 9 && version[2***REMOVED*** < 1***REMOVED*** || (version[0***REMOVED*** > 3***REMOVED******REMOVED*** {
    throw new Error('Bootstrap\'s JavaScript requires jQuery version 1.9.1 or higher, but lower than version 4'***REMOVED***
  ***REMOVED***
***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: transition.js v3.3.7
 * http://getbootstrap.com/javascript/#transitions
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // CSS TRANSITION SUPPORT (Shoutout: http://www.modernizr.com/***REMOVED***
  // ============================================================

  function transitionEnd(***REMOVED*** {
    var el = document.createElement('bootstrap'***REMOVED***

    var transEndEventNames = {
      WebkitTransition : 'webkitTransitionEnd',
      MozTransition    : 'transitionend',
      OTransition      : 'oTransitionEnd otransitionend',
      transition       : 'transitionend'
***REMOVED***

    for (var name in transEndEventNames***REMOVED*** {
      if (el.style[name***REMOVED*** !== undefined***REMOVED*** {
        return { end: transEndEventNames[name***REMOVED*** ***REMOVED***
  ***REMOVED***
***REMOVED***

    return false // explicit for ie8 (  ._.***REMOVED***
  ***REMOVED***

  // http://blog.alexmaccaw.com/css-transitions
  $.fn.emulateTransitionEnd = function (duration***REMOVED*** {
    var called = false
    var $el = this
    $(this***REMOVED***.one('bsTransitionEnd', function (***REMOVED*** { called = true ***REMOVED******REMOVED***
    var callback = function (***REMOVED*** { if (!called***REMOVED*** $($el***REMOVED***.trigger($.support.transition.end***REMOVED*** ***REMOVED***
    setTimeout(callback, duration***REMOVED***
    return this
  ***REMOVED***

  $(function (***REMOVED*** {
    $.support.transition = transitionEnd(***REMOVED***

    if (!$.support.transition***REMOVED*** return

    $.event.special.bsTransitionEnd = {
      bindType: $.support.transition.end,
      delegateType: $.support.transition.end,
      handle: function (e***REMOVED*** {
        if ($(e.target***REMOVED***.is(this***REMOVED******REMOVED*** return e.handleObj.handler.apply(this, arguments***REMOVED***
  ***REMOVED***
***REMOVED***
  ***REMOVED******REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: alert.js v3.3.7
 * http://getbootstrap.com/javascript/#alerts
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // ALERT CLASS DEFINITION
  // ======================

  var dismiss = '[data-dismiss="alert"***REMOVED***'
  var Alert   = function (el***REMOVED*** {
    $(el***REMOVED***.on('click', dismiss, this.close***REMOVED***
  ***REMOVED***

  Alert.VERSION = '3.3.7'

  Alert.TRANSITION_DURATION = 150

  Alert.prototype.close = function (e***REMOVED*** {
    var $this    = $(this***REMOVED***
    var selector = $this.attr('data-target'***REMOVED***

    if (!selector***REMOVED*** {
      selector = $this.attr('href'***REMOVED***
      selector = selector && selector.replace(/.*(?=#[^\s***REMOVED****$***REMOVED***/, ''***REMOVED*** // strip for ie7
***REMOVED***

    var $parent = $(selector === '#' ? [***REMOVED*** : selector***REMOVED***

    if (e***REMOVED*** e.preventDefault(***REMOVED***

    if (!$parent.length***REMOVED*** {
      $parent = $this.closest('.alert'***REMOVED***
***REMOVED***

    $parent.trigger(e = $.Event('close.bs.alert'***REMOVED******REMOVED***

    if (e.isDefaultPrevented(***REMOVED******REMOVED*** return

    $parent.removeClass('in'***REMOVED***

    function removeElement(***REMOVED*** {
      // detach from parent, fire event then clean up data
      $parent.detach(***REMOVED***.trigger('closed.bs.alert'***REMOVED***.remove(***REMOVED***
***REMOVED***

    $.support.transition && $parent.hasClass('fade'***REMOVED*** ?
      $parent
        .one('bsTransitionEnd', removeElement***REMOVED***
        .emulateTransitionEnd(Alert.TRANSITION_DURATION***REMOVED*** :
      removeElement(***REMOVED***
  ***REMOVED***


  // ALERT PLUGIN DEFINITION
  // =======================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this = $(this***REMOVED***
      var data  = $this.data('bs.alert'***REMOVED***

      if (!data***REMOVED*** $this.data('bs.alert', (data = new Alert(this***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***.call($this***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.alert

  $.fn.alert             = Plugin
  $.fn.alert.Constructor = Alert


  // ALERT NO CONFLICT
  // =================

  $.fn.alert.noConflict = function (***REMOVED*** {
    $.fn.alert = old
    return this
  ***REMOVED***


  // ALERT DATA-API
  // ==============

  $(document***REMOVED***.on('click.bs.alert.data-api', dismiss, Alert.prototype.close***REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: button.js v3.3.7
 * http://getbootstrap.com/javascript/#buttons
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // BUTTON PUBLIC CLASS DEFINITION
  // ==============================

  var Button = function (element, options***REMOVED*** {
    this.$element  = $(element***REMOVED***
    this.options   = $.extend({***REMOVED***, Button.DEFAULTS, options***REMOVED***
    this.isLoading = false
  ***REMOVED***

  Button.VERSION  = '3.3.7'

  Button.DEFAULTS = {
    loadingText: 'loading...'
  ***REMOVED***

  Button.prototype.setState = function (state***REMOVED*** {
    var d    = 'disabled'
    var $el  = this.$element
    var val  = $el.is('input'***REMOVED*** ? 'val' : 'html'
    var data = $el.data(***REMOVED***

    state += 'Text'

    if (data.resetText == null***REMOVED*** $el.data('resetText', $el[val***REMOVED***(***REMOVED******REMOVED***

    // push to event loop to allow forms to submit
    setTimeout($.proxy(function (***REMOVED*** {
      $el[val***REMOVED***(data[state***REMOVED*** == null ? this.options[state***REMOVED*** : data[state***REMOVED******REMOVED***

      if (state == 'loadingText'***REMOVED*** {
        this.isLoading = true
        $el.addClass(d***REMOVED***.attr(d, d***REMOVED***.prop(d, true***REMOVED***
  ***REMOVED*** else if (this.isLoading***REMOVED*** {
        this.isLoading = false
        $el.removeClass(d***REMOVED***.removeAttr(d***REMOVED***.prop(d, false***REMOVED***
  ***REMOVED***
***REMOVED***, this***REMOVED***, 0***REMOVED***
  ***REMOVED***

  Button.prototype.toggle = function (***REMOVED*** {
    var changed = true
    var $parent = this.$element.closest('[data-toggle="buttons"***REMOVED***'***REMOVED***

    if ($parent.length***REMOVED*** {
      var $input = this.$element.find('input'***REMOVED***
      if ($input.prop('type'***REMOVED*** == 'radio'***REMOVED*** {
        if ($input.prop('checked'***REMOVED******REMOVED*** changed = false
        $parent.find('.active'***REMOVED***.removeClass('active'***REMOVED***
        this.$element.addClass('active'***REMOVED***
  ***REMOVED*** else if ($input.prop('type'***REMOVED*** == 'checkbox'***REMOVED*** {
        if (($input.prop('checked'***REMOVED******REMOVED*** !== this.$element.hasClass('active'***REMOVED******REMOVED*** changed = false
        this.$element.toggleClass('active'***REMOVED***
  ***REMOVED***
      $input.prop('checked', this.$element.hasClass('active'***REMOVED******REMOVED***
      if (changed***REMOVED*** $input.trigger('change'***REMOVED***
***REMOVED*** else {
      this.$element.attr('aria-pressed', !this.$element.hasClass('active'***REMOVED******REMOVED***
      this.$element.toggleClass('active'***REMOVED***
***REMOVED***
  ***REMOVED***


  // BUTTON PLUGIN DEFINITION
  // ========================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.button'***REMOVED***
      var options = typeof option == 'object' && option

      if (!data***REMOVED*** $this.data('bs.button', (data = new Button(this, options***REMOVED******REMOVED******REMOVED***

      if (option == 'toggle'***REMOVED*** data.toggle(***REMOVED***
      else if (option***REMOVED*** data.setState(option***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.button

  $.fn.button             = Plugin
  $.fn.button.Constructor = Button


  // BUTTON NO CONFLICT
  // ==================

  $.fn.button.noConflict = function (***REMOVED*** {
    $.fn.button = old
    return this
  ***REMOVED***


  // BUTTON DATA-API
  // ===============

  $(document***REMOVED***
    .on('click.bs.button.data-api', '[data-toggle^="button"***REMOVED***', function (e***REMOVED*** {
      var $btn = $(e.target***REMOVED***.closest('.btn'***REMOVED***
      Plugin.call($btn, 'toggle'***REMOVED***
      if (!($(e.target***REMOVED***.is('input[type="radio"***REMOVED***, input[type="checkbox"***REMOVED***'***REMOVED******REMOVED******REMOVED*** {
        // Prevent double click on radios, and the double selections (so cancellation***REMOVED*** on checkboxes
        e.preventDefault(***REMOVED***
        // The target component still receive the focus
        if ($btn.is('input,button'***REMOVED******REMOVED*** $btn.trigger('focus'***REMOVED***
        else $btn.find('input:visible,button:visible'***REMOVED***.first(***REMOVED***.trigger('focus'***REMOVED***
  ***REMOVED***
***REMOVED******REMOVED***
    .on('focus.bs.button.data-api blur.bs.button.data-api', '[data-toggle^="button"***REMOVED***', function (e***REMOVED*** {
      $(e.target***REMOVED***.closest('.btn'***REMOVED***.toggleClass('focus', /^focus(in***REMOVED***?$/.test(e.type***REMOVED******REMOVED***
***REMOVED******REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: carousel.js v3.3.7
 * http://getbootstrap.com/javascript/#carousel
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // CAROUSEL CLASS DEFINITION
  // =========================

  var Carousel = function (element, options***REMOVED*** {
    this.$element    = $(element***REMOVED***
    this.$indicators = this.$element.find('.carousel-indicators'***REMOVED***
    this.options     = options
    this.paused      = null
    this.sliding     = null
    this.interval    = null
    this.$active     = null
    this.$items      = null

    this.options.keyboard && this.$element.on('keydown.bs.carousel', $.proxy(this.keydown, this***REMOVED******REMOVED***

    this.options.pause == 'hover' && !('ontouchstart' in document.documentElement***REMOVED*** && this.$element
      .on('mouseenter.bs.carousel', $.proxy(this.pause, this***REMOVED******REMOVED***
      .on('mouseleave.bs.carousel', $.proxy(this.cycle, this***REMOVED******REMOVED***
  ***REMOVED***

  Carousel.VERSION  = '3.3.7'

  Carousel.TRANSITION_DURATION = 600

  Carousel.DEFAULTS = {
    interval: 5000,
    pause: 'hover',
    wrap: true,
    keyboard: true
  ***REMOVED***

  Carousel.prototype.keydown = function (e***REMOVED*** {
    if (/input|textarea/i.test(e.target.tagName***REMOVED******REMOVED*** return
    switch (e.which***REMOVED*** {
      case 37: this.prev(***REMOVED***; break
      case 39: this.next(***REMOVED***; break
      default: return
***REMOVED***

    e.preventDefault(***REMOVED***
  ***REMOVED***

  Carousel.prototype.cycle = function (e***REMOVED*** {
    e || (this.paused = false***REMOVED***

    this.interval && clearInterval(this.interval***REMOVED***

    this.options.interval
      && !this.paused
      && (this.interval = setInterval($.proxy(this.next, this***REMOVED***, this.options.interval***REMOVED******REMOVED***

    return this
  ***REMOVED***

  Carousel.prototype.getItemIndex = function (item***REMOVED*** {
    this.$items = item.parent(***REMOVED***.children('.item'***REMOVED***
    return this.$items.index(item || this.$active***REMOVED***
  ***REMOVED***

  Carousel.prototype.getItemForDirection = function (direction, active***REMOVED*** {
    var activeIndex = this.getItemIndex(active***REMOVED***
    var willWrap = (direction == 'prev' && activeIndex === 0***REMOVED***
                || (direction == 'next' && activeIndex == (this.$items.length - 1***REMOVED******REMOVED***
    if (willWrap && !this.options.wrap***REMOVED*** return active
    var delta = direction == 'prev' ? -1 : 1
    var itemIndex = (activeIndex + delta***REMOVED*** % this.$items.length
    return this.$items.eq(itemIndex***REMOVED***
  ***REMOVED***

  Carousel.prototype.to = function (pos***REMOVED*** {
    var that        = this
    var activeIndex = this.getItemIndex(this.$active = this.$element.find('.item.active'***REMOVED******REMOVED***

    if (pos > (this.$items.length - 1***REMOVED*** || pos < 0***REMOVED*** return

    if (this.sliding***REMOVED***       return this.$element.one('slid.bs.carousel', function (***REMOVED*** { that.to(pos***REMOVED*** ***REMOVED******REMOVED*** // yes, "slid"
    if (activeIndex == pos***REMOVED*** return this.pause(***REMOVED***.cycle(***REMOVED***

    return this.slide(pos > activeIndex ? 'next' : 'prev', this.$items.eq(pos***REMOVED******REMOVED***
  ***REMOVED***

  Carousel.prototype.pause = function (e***REMOVED*** {
    e || (this.paused = true***REMOVED***

    if (this.$element.find('.next, .prev'***REMOVED***.length && $.support.transition***REMOVED*** {
      this.$element.trigger($.support.transition.end***REMOVED***
      this.cycle(true***REMOVED***
***REMOVED***

    this.interval = clearInterval(this.interval***REMOVED***

    return this
  ***REMOVED***

  Carousel.prototype.next = function (***REMOVED*** {
    if (this.sliding***REMOVED*** return
    return this.slide('next'***REMOVED***
  ***REMOVED***

  Carousel.prototype.prev = function (***REMOVED*** {
    if (this.sliding***REMOVED*** return
    return this.slide('prev'***REMOVED***
  ***REMOVED***

  Carousel.prototype.slide = function (type, next***REMOVED*** {
    var $active   = this.$element.find('.item.active'***REMOVED***
    var $next     = next || this.getItemForDirection(type, $active***REMOVED***
    var isCycling = this.interval
    var direction = type == 'next' ? 'left' : 'right'
    var that      = this

    if ($next.hasClass('active'***REMOVED******REMOVED*** return (this.sliding = false***REMOVED***

    var relatedTarget = $next[0***REMOVED***
    var slideEvent = $.Event('slide.bs.carousel', {
      relatedTarget: relatedTarget,
      direction: direction
***REMOVED******REMOVED***
    this.$element.trigger(slideEvent***REMOVED***
    if (slideEvent.isDefaultPrevented(***REMOVED******REMOVED*** return

    this.sliding = true

    isCycling && this.pause(***REMOVED***

    if (this.$indicators.length***REMOVED*** {
      this.$indicators.find('.active'***REMOVED***.removeClass('active'***REMOVED***
      var $nextIndicator = $(this.$indicators.children(***REMOVED***[this.getItemIndex($next***REMOVED******REMOVED******REMOVED***
      $nextIndicator && $nextIndicator.addClass('active'***REMOVED***
***REMOVED***

    var slidEvent = $.Event('slid.bs.carousel', { relatedTarget: relatedTarget, direction: direction ***REMOVED******REMOVED*** // yes, "slid"
    if ($.support.transition && this.$element.hasClass('slide'***REMOVED******REMOVED*** {
      $next.addClass(type***REMOVED***
      $next[0***REMOVED***.offsetWidth // force reflow
      $active.addClass(direction***REMOVED***
      $next.addClass(direction***REMOVED***
      $active
        .one('bsTransitionEnd', function (***REMOVED*** {
          $next.removeClass([type, direction***REMOVED***.join(' '***REMOVED******REMOVED***.addClass('active'***REMOVED***
          $active.removeClass(['active', direction***REMOVED***.join(' '***REMOVED******REMOVED***
          that.sliding = false
          setTimeout(function (***REMOVED*** {
            that.$element.trigger(slidEvent***REMOVED***
      ***REMOVED***, 0***REMOVED***
    ***REMOVED******REMOVED***
        .emulateTransitionEnd(Carousel.TRANSITION_DURATION***REMOVED***
***REMOVED*** else {
      $active.removeClass('active'***REMOVED***
      $next.addClass('active'***REMOVED***
      this.sliding = false
      this.$element.trigger(slidEvent***REMOVED***
***REMOVED***

    isCycling && this.cycle(***REMOVED***

    return this
  ***REMOVED***


  // CAROUSEL PLUGIN DEFINITION
  // ==========================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.carousel'***REMOVED***
      var options = $.extend({***REMOVED***, Carousel.DEFAULTS, $this.data(***REMOVED***, typeof option == 'object' && option***REMOVED***
      var action  = typeof option == 'string' ? option : options.slide

      if (!data***REMOVED*** $this.data('bs.carousel', (data = new Carousel(this, options***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'number'***REMOVED*** data.to(option***REMOVED***
      else if (action***REMOVED*** data[action***REMOVED***(***REMOVED***
      else if (options.interval***REMOVED*** data.pause(***REMOVED***.cycle(***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.carousel

  $.fn.carousel             = Plugin
  $.fn.carousel.Constructor = Carousel


  // CAROUSEL NO CONFLICT
  // ====================

  $.fn.carousel.noConflict = function (***REMOVED*** {
    $.fn.carousel = old
    return this
  ***REMOVED***


  // CAROUSEL DATA-API
  // =================

  var clickHandler = function (e***REMOVED*** {
    var href
    var $this   = $(this***REMOVED***
    var $target = $($this.attr('data-target'***REMOVED*** || (href = $this.attr('href'***REMOVED******REMOVED*** && href.replace(/.*(?=#[^\s***REMOVED***+$***REMOVED***/, ''***REMOVED******REMOVED*** // strip for ie7
    if (!$target.hasClass('carousel'***REMOVED******REMOVED*** return
    var options = $.extend({***REMOVED***, $target.data(***REMOVED***, $this.data(***REMOVED******REMOVED***
    var slideIndex = $this.attr('data-slide-to'***REMOVED***
    if (slideIndex***REMOVED*** options.interval = false

    Plugin.call($target, options***REMOVED***

    if (slideIndex***REMOVED*** {
      $target.data('bs.carousel'***REMOVED***.to(slideIndex***REMOVED***
***REMOVED***

    e.preventDefault(***REMOVED***
  ***REMOVED***

  $(document***REMOVED***
    .on('click.bs.carousel.data-api', '[data-slide***REMOVED***', clickHandler***REMOVED***
    .on('click.bs.carousel.data-api', '[data-slide-to***REMOVED***', clickHandler***REMOVED***

  $(window***REMOVED***.on('load', function (***REMOVED*** {
    $('[data-ride="carousel"***REMOVED***'***REMOVED***.each(function (***REMOVED*** {
      var $carousel = $(this***REMOVED***
      Plugin.call($carousel, $carousel.data(***REMOVED******REMOVED***
***REMOVED******REMOVED***
  ***REMOVED******REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: collapse.js v3.3.7
 * http://getbootstrap.com/javascript/#collapse
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */

/* jshint latedef: false */

+function ($***REMOVED*** {
  'use strict';

  // COLLAPSE PUBLIC CLASS DEFINITION
  // ================================

  var Collapse = function (element, options***REMOVED*** {
    this.$element      = $(element***REMOVED***
    this.options       = $.extend({***REMOVED***, Collapse.DEFAULTS, options***REMOVED***
    this.$trigger      = $('[data-toggle="collapse"***REMOVED***[href="#' + element.id + '"***REMOVED***,' +
                           '[data-toggle="collapse"***REMOVED***[data-target="#' + element.id + '"***REMOVED***'***REMOVED***
    this.transitioning = null

    if (this.options.parent***REMOVED*** {
      this.$parent = this.getParent(***REMOVED***
***REMOVED*** else {
      this.addAriaAndCollapsedClass(this.$element, this.$trigger***REMOVED***
***REMOVED***

    if (this.options.toggle***REMOVED*** this.toggle(***REMOVED***
  ***REMOVED***

  Collapse.VERSION  = '3.3.7'

  Collapse.TRANSITION_DURATION = 350

  Collapse.DEFAULTS = {
    toggle: true
  ***REMOVED***

  Collapse.prototype.dimension = function (***REMOVED*** {
    var hasWidth = this.$element.hasClass('width'***REMOVED***
    return hasWidth ? 'width' : 'height'
  ***REMOVED***

  Collapse.prototype.show = function (***REMOVED*** {
    if (this.transitioning || this.$element.hasClass('in'***REMOVED******REMOVED*** return

    var activesData
    var actives = this.$parent && this.$parent.children('.panel'***REMOVED***.children('.in, .collapsing'***REMOVED***

    if (actives && actives.length***REMOVED*** {
      activesData = actives.data('bs.collapse'***REMOVED***
      if (activesData && activesData.transitioning***REMOVED*** return
***REMOVED***

    var startEvent = $.Event('show.bs.collapse'***REMOVED***
    this.$element.trigger(startEvent***REMOVED***
    if (startEvent.isDefaultPrevented(***REMOVED******REMOVED*** return

    if (actives && actives.length***REMOVED*** {
      Plugin.call(actives, 'hide'***REMOVED***
      activesData || actives.data('bs.collapse', null***REMOVED***
***REMOVED***

    var dimension = this.dimension(***REMOVED***

    this.$element
      .removeClass('collapse'***REMOVED***
      .addClass('collapsing'***REMOVED***[dimension***REMOVED***(0***REMOVED***
      .attr('aria-expanded', true***REMOVED***

    this.$trigger
      .removeClass('collapsed'***REMOVED***
      .attr('aria-expanded', true***REMOVED***

    this.transitioning = 1

    var complete = function (***REMOVED*** {
      this.$element
        .removeClass('collapsing'***REMOVED***
        .addClass('collapse in'***REMOVED***[dimension***REMOVED***(''***REMOVED***
      this.transitioning = 0
      this.$element
        .trigger('shown.bs.collapse'***REMOVED***
***REMOVED***

    if (!$.support.transition***REMOVED*** return complete.call(this***REMOVED***

    var scrollSize = $.camelCase(['scroll', dimension***REMOVED***.join('-'***REMOVED******REMOVED***

    this.$element
      .one('bsTransitionEnd', $.proxy(complete, this***REMOVED******REMOVED***
      .emulateTransitionEnd(Collapse.TRANSITION_DURATION***REMOVED***[dimension***REMOVED***(this.$element[0***REMOVED***[scrollSize***REMOVED******REMOVED***
  ***REMOVED***

  Collapse.prototype.hide = function (***REMOVED*** {
    if (this.transitioning || !this.$element.hasClass('in'***REMOVED******REMOVED*** return

    var startEvent = $.Event('hide.bs.collapse'***REMOVED***
    this.$element.trigger(startEvent***REMOVED***
    if (startEvent.isDefaultPrevented(***REMOVED******REMOVED*** return

    var dimension = this.dimension(***REMOVED***

    this.$element[dimension***REMOVED***(this.$element[dimension***REMOVED***(***REMOVED******REMOVED***[0***REMOVED***.offsetHeight

    this.$element
      .addClass('collapsing'***REMOVED***
      .removeClass('collapse in'***REMOVED***
      .attr('aria-expanded', false***REMOVED***

    this.$trigger
      .addClass('collapsed'***REMOVED***
      .attr('aria-expanded', false***REMOVED***

    this.transitioning = 1

    var complete = function (***REMOVED*** {
      this.transitioning = 0
      this.$element
        .removeClass('collapsing'***REMOVED***
        .addClass('collapse'***REMOVED***
        .trigger('hidden.bs.collapse'***REMOVED***
***REMOVED***

    if (!$.support.transition***REMOVED*** return complete.call(this***REMOVED***

    this.$element
      [dimension***REMOVED***(0***REMOVED***
      .one('bsTransitionEnd', $.proxy(complete, this***REMOVED******REMOVED***
      .emulateTransitionEnd(Collapse.TRANSITION_DURATION***REMOVED***
  ***REMOVED***

  Collapse.prototype.toggle = function (***REMOVED*** {
    this[this.$element.hasClass('in'***REMOVED*** ? 'hide' : 'show'***REMOVED***(***REMOVED***
  ***REMOVED***

  Collapse.prototype.getParent = function (***REMOVED*** {
    return $(this.options.parent***REMOVED***
      .find('[data-toggle="collapse"***REMOVED***[data-parent="' + this.options.parent + '"***REMOVED***'***REMOVED***
      .each($.proxy(function (i, element***REMOVED*** {
        var $element = $(element***REMOVED***
        this.addAriaAndCollapsedClass(getTargetFromTrigger($element***REMOVED***, $element***REMOVED***
  ***REMOVED***, this***REMOVED******REMOVED***
      .end(***REMOVED***
  ***REMOVED***

  Collapse.prototype.addAriaAndCollapsedClass = function ($element, $trigger***REMOVED*** {
    var isOpen = $element.hasClass('in'***REMOVED***

    $element.attr('aria-expanded', isOpen***REMOVED***
    $trigger
      .toggleClass('collapsed', !isOpen***REMOVED***
      .attr('aria-expanded', isOpen***REMOVED***
  ***REMOVED***

  function getTargetFromTrigger($trigger***REMOVED*** {
    var href
    var target = $trigger.attr('data-target'***REMOVED***
      || (href = $trigger.attr('href'***REMOVED******REMOVED*** && href.replace(/.*(?=#[^\s***REMOVED***+$***REMOVED***/, ''***REMOVED*** // strip for ie7

    return $(target***REMOVED***
  ***REMOVED***


  // COLLAPSE PLUGIN DEFINITION
  // ==========================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.collapse'***REMOVED***
      var options = $.extend({***REMOVED***, Collapse.DEFAULTS, $this.data(***REMOVED***, typeof option == 'object' && option***REMOVED***

      if (!data && options.toggle && /show|hide/.test(option***REMOVED******REMOVED*** options.toggle = false
      if (!data***REMOVED*** $this.data('bs.collapse', (data = new Collapse(this, options***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***(***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.collapse

  $.fn.collapse             = Plugin
  $.fn.collapse.Constructor = Collapse


  // COLLAPSE NO CONFLICT
  // ====================

  $.fn.collapse.noConflict = function (***REMOVED*** {
    $.fn.collapse = old
    return this
  ***REMOVED***


  // COLLAPSE DATA-API
  // =================

  $(document***REMOVED***.on('click.bs.collapse.data-api', '[data-toggle="collapse"***REMOVED***', function (e***REMOVED*** {
    var $this   = $(this***REMOVED***

    if (!$this.attr('data-target'***REMOVED******REMOVED*** e.preventDefault(***REMOVED***

    var $target = getTargetFromTrigger($this***REMOVED***
    var data    = $target.data('bs.collapse'***REMOVED***
    var option  = data ? 'toggle' : $this.data(***REMOVED***

    Plugin.call($target, option***REMOVED***
  ***REMOVED******REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: dropdown.js v3.3.7
 * http://getbootstrap.com/javascript/#dropdowns
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // DROPDOWN CLASS DEFINITION
  // =========================

  var backdrop = '.dropdown-backdrop'
  var toggle   = '[data-toggle="dropdown"***REMOVED***'
  var Dropdown = function (element***REMOVED*** {
    $(element***REMOVED***.on('click.bs.dropdown', this.toggle***REMOVED***
  ***REMOVED***

  Dropdown.VERSION = '3.3.7'

  function getParent($this***REMOVED*** {
    var selector = $this.attr('data-target'***REMOVED***

    if (!selector***REMOVED*** {
      selector = $this.attr('href'***REMOVED***
      selector = selector && /#[A-Za-z***REMOVED***/.test(selector***REMOVED*** && selector.replace(/.*(?=#[^\s***REMOVED****$***REMOVED***/, ''***REMOVED*** // strip for ie7
***REMOVED***

    var $parent = selector && $(selector***REMOVED***

    return $parent && $parent.length ? $parent : $this.parent(***REMOVED***
  ***REMOVED***

  function clearMenus(e***REMOVED*** {
    if (e && e.which === 3***REMOVED*** return
    $(backdrop***REMOVED***.remove(***REMOVED***
    $(toggle***REMOVED***.each(function (***REMOVED*** {
      var $this         = $(this***REMOVED***
      var $parent       = getParent($this***REMOVED***
      var relatedTarget = { relatedTarget: this ***REMOVED***

      if (!$parent.hasClass('open'***REMOVED******REMOVED*** return

      if (e && e.type == 'click' && /input|textarea/i.test(e.target.tagName***REMOVED*** && $.contains($parent[0***REMOVED***, e.target***REMOVED******REMOVED*** return

      $parent.trigger(e = $.Event('hide.bs.dropdown', relatedTarget***REMOVED******REMOVED***

      if (e.isDefaultPrevented(***REMOVED******REMOVED*** return

      $this.attr('aria-expanded', 'false'***REMOVED***
      $parent.removeClass('open'***REMOVED***.trigger($.Event('hidden.bs.dropdown', relatedTarget***REMOVED******REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  Dropdown.prototype.toggle = function (e***REMOVED*** {
    var $this = $(this***REMOVED***

    if ($this.is('.disabled, :disabled'***REMOVED******REMOVED*** return

    var $parent  = getParent($this***REMOVED***
    var isActive = $parent.hasClass('open'***REMOVED***

    clearMenus(***REMOVED***

    if (!isActive***REMOVED*** {
      if ('ontouchstart' in document.documentElement && !$parent.closest('.navbar-nav'***REMOVED***.length***REMOVED*** {
        // if mobile we use a backdrop because click events don't delegate
        $(document.createElement('div'***REMOVED******REMOVED***
          .addClass('dropdown-backdrop'***REMOVED***
          .insertAfter($(this***REMOVED******REMOVED***
          .on('click', clearMenus***REMOVED***
  ***REMOVED***

      var relatedTarget = { relatedTarget: this ***REMOVED***
      $parent.trigger(e = $.Event('show.bs.dropdown', relatedTarget***REMOVED******REMOVED***

      if (e.isDefaultPrevented(***REMOVED******REMOVED*** return

      $this
        .trigger('focus'***REMOVED***
        .attr('aria-expanded', 'true'***REMOVED***

      $parent
        .toggleClass('open'***REMOVED***
        .trigger($.Event('shown.bs.dropdown', relatedTarget***REMOVED******REMOVED***
***REMOVED***

    return false
  ***REMOVED***

  Dropdown.prototype.keydown = function (e***REMOVED*** {
    if (!/(38|40|27|32***REMOVED***/.test(e.which***REMOVED*** || /input|textarea/i.test(e.target.tagName***REMOVED******REMOVED*** return

    var $this = $(this***REMOVED***

    e.preventDefault(***REMOVED***
    e.stopPropagation(***REMOVED***

    if ($this.is('.disabled, :disabled'***REMOVED******REMOVED*** return

    var $parent  = getParent($this***REMOVED***
    var isActive = $parent.hasClass('open'***REMOVED***

    if (!isActive && e.which != 27 || isActive && e.which == 27***REMOVED*** {
      if (e.which == 27***REMOVED*** $parent.find(toggle***REMOVED***.trigger('focus'***REMOVED***
      return $this.trigger('click'***REMOVED***
***REMOVED***

    var desc = ' li:not(.disabled***REMOVED***:visible a'
    var $items = $parent.find('.dropdown-menu' + desc***REMOVED***

    if (!$items.length***REMOVED*** return

    var index = $items.index(e.target***REMOVED***

    if (e.which == 38 && index > 0***REMOVED***                 index--         // up
    if (e.which == 40 && index < $items.length - 1***REMOVED*** index++         // down
    if (!~index***REMOVED***                                    index = 0

    $items.eq(index***REMOVED***.trigger('focus'***REMOVED***
  ***REMOVED***


  // DROPDOWN PLUGIN DEFINITION
  // ==========================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this = $(this***REMOVED***
      var data  = $this.data('bs.dropdown'***REMOVED***

      if (!data***REMOVED*** $this.data('bs.dropdown', (data = new Dropdown(this***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***.call($this***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.dropdown

  $.fn.dropdown             = Plugin
  $.fn.dropdown.Constructor = Dropdown


  // DROPDOWN NO CONFLICT
  // ====================

  $.fn.dropdown.noConflict = function (***REMOVED*** {
    $.fn.dropdown = old
    return this
  ***REMOVED***


  // APPLY TO STANDARD DROPDOWN ELEMENTS
  // ===================================

  $(document***REMOVED***
    .on('click.bs.dropdown.data-api', clearMenus***REMOVED***
    .on('click.bs.dropdown.data-api', '.dropdown form', function (e***REMOVED*** { e.stopPropagation(***REMOVED*** ***REMOVED******REMOVED***
    .on('click.bs.dropdown.data-api', toggle, Dropdown.prototype.toggle***REMOVED***
    .on('keydown.bs.dropdown.data-api', toggle, Dropdown.prototype.keydown***REMOVED***
    .on('keydown.bs.dropdown.data-api', '.dropdown-menu', Dropdown.prototype.keydown***REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: modal.js v3.3.7
 * http://getbootstrap.com/javascript/#modals
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // MODAL CLASS DEFINITION
  // ======================

  var Modal = function (element, options***REMOVED*** {
    this.options             = options
    this.$body               = $(document.body***REMOVED***
    this.$element            = $(element***REMOVED***
    this.$dialog             = this.$element.find('.modal-dialog'***REMOVED***
    this.$backdrop           = null
    this.isShown             = null
    this.originalBodyPad     = null
    this.scrollbarWidth      = 0
    this.ignoreBackdropClick = false

    if (this.options.remote***REMOVED*** {
      this.$element
        .find('.modal-content'***REMOVED***
        .load(this.options.remote, $.proxy(function (***REMOVED*** {
          this.$element.trigger('loaded.bs.modal'***REMOVED***
    ***REMOVED***, this***REMOVED******REMOVED***
***REMOVED***
  ***REMOVED***

  Modal.VERSION  = '3.3.7'

  Modal.TRANSITION_DURATION = 300
  Modal.BACKDROP_TRANSITION_DURATION = 150

  Modal.DEFAULTS = {
    backdrop: true,
    keyboard: true,
    show: true
  ***REMOVED***

  Modal.prototype.toggle = function (_relatedTarget***REMOVED*** {
    return this.isShown ? this.hide(***REMOVED*** : this.show(_relatedTarget***REMOVED***
  ***REMOVED***

  Modal.prototype.show = function (_relatedTarget***REMOVED*** {
    var that = this
    var e    = $.Event('show.bs.modal', { relatedTarget: _relatedTarget ***REMOVED******REMOVED***

    this.$element.trigger(e***REMOVED***

    if (this.isShown || e.isDefaultPrevented(***REMOVED******REMOVED*** return

    this.isShown = true

    this.checkScrollbar(***REMOVED***
    this.setScrollbar(***REMOVED***
    this.$body.addClass('modal-open'***REMOVED***

    this.escape(***REMOVED***
    this.resize(***REMOVED***

    this.$element.on('click.dismiss.bs.modal', '[data-dismiss="modal"***REMOVED***', $.proxy(this.hide, this***REMOVED******REMOVED***

    this.$dialog.on('mousedown.dismiss.bs.modal', function (***REMOVED*** {
      that.$element.one('mouseup.dismiss.bs.modal', function (e***REMOVED*** {
        if ($(e.target***REMOVED***.is(that.$element***REMOVED******REMOVED*** that.ignoreBackdropClick = true
  ***REMOVED******REMOVED***
***REMOVED******REMOVED***

    this.backdrop(function (***REMOVED*** {
      var transition = $.support.transition && that.$element.hasClass('fade'***REMOVED***

      if (!that.$element.parent(***REMOVED***.length***REMOVED*** {
        that.$element.appendTo(that.$body***REMOVED*** // don't move modals dom position
  ***REMOVED***

      that.$element
        .show(***REMOVED***
        .scrollTop(0***REMOVED***

      that.adjustDialog(***REMOVED***

      if (transition***REMOVED*** {
        that.$element[0***REMOVED***.offsetWidth // force reflow
  ***REMOVED***

      that.$element.addClass('in'***REMOVED***

      that.enforceFocus(***REMOVED***

      var e = $.Event('shown.bs.modal', { relatedTarget: _relatedTarget ***REMOVED******REMOVED***

      transition ?
        that.$dialog // wait for modal to slide in
          .one('bsTransitionEnd', function (***REMOVED*** {
            that.$element.trigger('focus'***REMOVED***.trigger(e***REMOVED***
      ***REMOVED******REMOVED***
          .emulateTransitionEnd(Modal.TRANSITION_DURATION***REMOVED*** :
        that.$element.trigger('focus'***REMOVED***.trigger(e***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  Modal.prototype.hide = function (e***REMOVED*** {
    if (e***REMOVED*** e.preventDefault(***REMOVED***

    e = $.Event('hide.bs.modal'***REMOVED***

    this.$element.trigger(e***REMOVED***

    if (!this.isShown || e.isDefaultPrevented(***REMOVED******REMOVED*** return

    this.isShown = false

    this.escape(***REMOVED***
    this.resize(***REMOVED***

    $(document***REMOVED***.off('focusin.bs.modal'***REMOVED***

    this.$element
      .removeClass('in'***REMOVED***
      .off('click.dismiss.bs.modal'***REMOVED***
      .off('mouseup.dismiss.bs.modal'***REMOVED***

    this.$dialog.off('mousedown.dismiss.bs.modal'***REMOVED***

    $.support.transition && this.$element.hasClass('fade'***REMOVED*** ?
      this.$element
        .one('bsTransitionEnd', $.proxy(this.hideModal, this***REMOVED******REMOVED***
        .emulateTransitionEnd(Modal.TRANSITION_DURATION***REMOVED*** :
      this.hideModal(***REMOVED***
  ***REMOVED***

  Modal.prototype.enforceFocus = function (***REMOVED*** {
    $(document***REMOVED***
      .off('focusin.bs.modal'***REMOVED*** // guard against infinite focus loop
      .on('focusin.bs.modal', $.proxy(function (e***REMOVED*** {
        if (document !== e.target &&
            this.$element[0***REMOVED*** !== e.target &&
            !this.$element.has(e.target***REMOVED***.length***REMOVED*** {
          this.$element.trigger('focus'***REMOVED***
    ***REMOVED***
  ***REMOVED***, this***REMOVED******REMOVED***
  ***REMOVED***

  Modal.prototype.escape = function (***REMOVED*** {
    if (this.isShown && this.options.keyboard***REMOVED*** {
      this.$element.on('keydown.dismiss.bs.modal', $.proxy(function (e***REMOVED*** {
        e.which == 27 && this.hide(***REMOVED***
  ***REMOVED***, this***REMOVED******REMOVED***
***REMOVED*** else if (!this.isShown***REMOVED*** {
      this.$element.off('keydown.dismiss.bs.modal'***REMOVED***
***REMOVED***
  ***REMOVED***

  Modal.prototype.resize = function (***REMOVED*** {
    if (this.isShown***REMOVED*** {
      $(window***REMOVED***.on('resize.bs.modal', $.proxy(this.handleUpdate, this***REMOVED******REMOVED***
***REMOVED*** else {
      $(window***REMOVED***.off('resize.bs.modal'***REMOVED***
***REMOVED***
  ***REMOVED***

  Modal.prototype.hideModal = function (***REMOVED*** {
    var that = this
    this.$element.hide(***REMOVED***
    this.backdrop(function (***REMOVED*** {
      that.$body.removeClass('modal-open'***REMOVED***
      that.resetAdjustments(***REMOVED***
      that.resetScrollbar(***REMOVED***
      that.$element.trigger('hidden.bs.modal'***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  Modal.prototype.removeBackdrop = function (***REMOVED*** {
    this.$backdrop && this.$backdrop.remove(***REMOVED***
    this.$backdrop = null
  ***REMOVED***

  Modal.prototype.backdrop = function (callback***REMOVED*** {
    var that = this
    var animate = this.$element.hasClass('fade'***REMOVED*** ? 'fade' : ''

    if (this.isShown && this.options.backdrop***REMOVED*** {
      var doAnimate = $.support.transition && animate

      this.$backdrop = $(document.createElement('div'***REMOVED******REMOVED***
        .addClass('modal-backdrop ' + animate***REMOVED***
        .appendTo(this.$body***REMOVED***

      this.$element.on('click.dismiss.bs.modal', $.proxy(function (e***REMOVED*** {
        if (this.ignoreBackdropClick***REMOVED*** {
          this.ignoreBackdropClick = false
          return
    ***REMOVED***
        if (e.target !== e.currentTarget***REMOVED*** return
        this.options.backdrop == 'static'
          ? this.$element[0***REMOVED***.focus(***REMOVED***
          : this.hide(***REMOVED***
  ***REMOVED***, this***REMOVED******REMOVED***

      if (doAnimate***REMOVED*** this.$backdrop[0***REMOVED***.offsetWidth // force reflow

      this.$backdrop.addClass('in'***REMOVED***

      if (!callback***REMOVED*** return

      doAnimate ?
        this.$backdrop
          .one('bsTransitionEnd', callback***REMOVED***
          .emulateTransitionEnd(Modal.BACKDROP_TRANSITION_DURATION***REMOVED*** :
        callback(***REMOVED***

***REMOVED*** else if (!this.isShown && this.$backdrop***REMOVED*** {
      this.$backdrop.removeClass('in'***REMOVED***

      var callbackRemove = function (***REMOVED*** {
        that.removeBackdrop(***REMOVED***
        callback && callback(***REMOVED***
  ***REMOVED***
      $.support.transition && this.$element.hasClass('fade'***REMOVED*** ?
        this.$backdrop
          .one('bsTransitionEnd', callbackRemove***REMOVED***
          .emulateTransitionEnd(Modal.BACKDROP_TRANSITION_DURATION***REMOVED*** :
        callbackRemove(***REMOVED***

***REMOVED*** else if (callback***REMOVED*** {
      callback(***REMOVED***
***REMOVED***
  ***REMOVED***

  // these following methods are used to handle overflowing modals

  Modal.prototype.handleUpdate = function (***REMOVED*** {
    this.adjustDialog(***REMOVED***
  ***REMOVED***

  Modal.prototype.adjustDialog = function (***REMOVED*** {
    var modalIsOverflowing = this.$element[0***REMOVED***.scrollHeight > document.documentElement.clientHeight

    this.$element.css({
      paddingLeft:  !this.bodyIsOverflowing && modalIsOverflowing ? this.scrollbarWidth : '',
      paddingRight: this.bodyIsOverflowing && !modalIsOverflowing ? this.scrollbarWidth : ''
***REMOVED******REMOVED***
  ***REMOVED***

  Modal.prototype.resetAdjustments = function (***REMOVED*** {
    this.$element.css({
      paddingLeft: '',
      paddingRight: ''
***REMOVED******REMOVED***
  ***REMOVED***

  Modal.prototype.checkScrollbar = function (***REMOVED*** {
    var fullWindowWidth = window.innerWidth
    if (!fullWindowWidth***REMOVED*** { // workaround for missing window.innerWidth in IE8
      var documentElementRect = document.documentElement.getBoundingClientRect(***REMOVED***
      fullWindowWidth = documentElementRect.right - Math.abs(documentElementRect.left***REMOVED***
***REMOVED***
    this.bodyIsOverflowing = document.body.clientWidth < fullWindowWidth
    this.scrollbarWidth = this.measureScrollbar(***REMOVED***
  ***REMOVED***

  Modal.prototype.setScrollbar = function (***REMOVED*** {
    var bodyPad = parseInt((this.$body.css('padding-right'***REMOVED*** || 0***REMOVED***, 10***REMOVED***
    this.originalBodyPad = document.body.style.paddingRight || ''
    if (this.bodyIsOverflowing***REMOVED*** this.$body.css('padding-right', bodyPad + this.scrollbarWidth***REMOVED***
  ***REMOVED***

  Modal.prototype.resetScrollbar = function (***REMOVED*** {
    this.$body.css('padding-right', this.originalBodyPad***REMOVED***
  ***REMOVED***

  Modal.prototype.measureScrollbar = function (***REMOVED*** { // thx walsh
    var scrollDiv = document.createElement('div'***REMOVED***
    scrollDiv.className = 'modal-scrollbar-measure'
    this.$body.append(scrollDiv***REMOVED***
    var scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth
    this.$body[0***REMOVED***.removeChild(scrollDiv***REMOVED***
    return scrollbarWidth
  ***REMOVED***


  // MODAL PLUGIN DEFINITION
  // =======================

  function Plugin(option, _relatedTarget***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.modal'***REMOVED***
      var options = $.extend({***REMOVED***, Modal.DEFAULTS, $this.data(***REMOVED***, typeof option == 'object' && option***REMOVED***

      if (!data***REMOVED*** $this.data('bs.modal', (data = new Modal(this, options***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***(_relatedTarget***REMOVED***
      else if (options.show***REMOVED*** data.show(_relatedTarget***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.modal

  $.fn.modal             = Plugin
  $.fn.modal.Constructor = Modal


  // MODAL NO CONFLICT
  // =================

  $.fn.modal.noConflict = function (***REMOVED*** {
    $.fn.modal = old
    return this
  ***REMOVED***


  // MODAL DATA-API
  // ==============

  $(document***REMOVED***.on('click.bs.modal.data-api', '[data-toggle="modal"***REMOVED***', function (e***REMOVED*** {
    var $this   = $(this***REMOVED***
    var href    = $this.attr('href'***REMOVED***
    var $target = $($this.attr('data-target'***REMOVED*** || (href && href.replace(/.*(?=#[^\s***REMOVED***+$***REMOVED***/, ''***REMOVED******REMOVED******REMOVED*** // strip for ie7
    var option  = $target.data('bs.modal'***REMOVED*** ? 'toggle' : $.extend({ remote: !/#/.test(href***REMOVED*** && href ***REMOVED***, $target.data(***REMOVED***, $this.data(***REMOVED******REMOVED***

    if ($this.is('a'***REMOVED******REMOVED*** e.preventDefault(***REMOVED***

    $target.one('show.bs.modal', function (showEvent***REMOVED*** {
      if (showEvent.isDefaultPrevented(***REMOVED******REMOVED*** return // only register focus restorer if modal will actually get shown
      $target.one('hidden.bs.modal', function (***REMOVED*** {
        $this.is(':visible'***REMOVED*** && $this.trigger('focus'***REMOVED***
  ***REMOVED******REMOVED***
***REMOVED******REMOVED***
    Plugin.call($target, option, this***REMOVED***
  ***REMOVED******REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: tooltip.js v3.3.7
 * http://getbootstrap.com/javascript/#tooltip
 * Inspired by the original jQuery.tipsy by Jason Frame
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // TOOLTIP PUBLIC CLASS DEFINITION
  // ===============================

  var Tooltip = function (element, options***REMOVED*** {
    this.type       = null
    this.options    = null
    this.enabled    = null
    this.timeout    = null
    this.hoverState = null
    this.$element   = null
    this.inState    = null

    this.init('tooltip', element, options***REMOVED***
  ***REMOVED***

  Tooltip.VERSION  = '3.3.7'

  Tooltip.TRANSITION_DURATION = 150

  Tooltip.DEFAULTS = {
    animation: true,
    placement: 'top',
    selector: false,
    template: '<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',
    trigger: 'hover focus',
    title: '',
    delay: 0,
    html: false,
    container: false,
    viewport: {
      selector: 'body',
      padding: 0
***REMOVED***
  ***REMOVED***

  Tooltip.prototype.init = function (type, element, options***REMOVED*** {
    this.enabled   = true
    this.type      = type
    this.$element  = $(element***REMOVED***
    this.options   = this.getOptions(options***REMOVED***
    this.$viewport = this.options.viewport && $($.isFunction(this.options.viewport***REMOVED*** ? this.options.viewport.call(this, this.$element***REMOVED*** : (this.options.viewport.selector || this.options.viewport***REMOVED******REMOVED***
    this.inState   = { click: false, hover: false, focus: false ***REMOVED***

    if (this.$element[0***REMOVED*** instanceof document.constructor && !this.options.selector***REMOVED*** {
      throw new Error('`selector` option must be specified when initializing ' + this.type + ' on the window.document object!'***REMOVED***
***REMOVED***

    var triggers = this.options.trigger.split(' '***REMOVED***

    for (var i = triggers.length; i--;***REMOVED*** {
      var trigger = triggers[i***REMOVED***

      if (trigger == 'click'***REMOVED*** {
        this.$element.on('click.' + this.type, this.options.selector, $.proxy(this.toggle, this***REMOVED******REMOVED***
  ***REMOVED*** else if (trigger != 'manual'***REMOVED*** {
        var eventIn  = trigger == 'hover' ? 'mouseenter' : 'focusin'
        var eventOut = trigger == 'hover' ? 'mouseleave' : 'focusout'

        this.$element.on(eventIn  + '.' + this.type, this.options.selector, $.proxy(this.enter, this***REMOVED******REMOVED***
        this.$element.on(eventOut + '.' + this.type, this.options.selector, $.proxy(this.leave, this***REMOVED******REMOVED***
  ***REMOVED***
***REMOVED***

    this.options.selector ?
      (this._options = $.extend({***REMOVED***, this.options, { trigger: 'manual', selector: '' ***REMOVED******REMOVED******REMOVED*** :
      this.fixTitle(***REMOVED***
  ***REMOVED***

  Tooltip.prototype.getDefaults = function (***REMOVED*** {
    return Tooltip.DEFAULTS
  ***REMOVED***

  Tooltip.prototype.getOptions = function (options***REMOVED*** {
    options = $.extend({***REMOVED***, this.getDefaults(***REMOVED***, this.$element.data(***REMOVED***, options***REMOVED***

    if (options.delay && typeof options.delay == 'number'***REMOVED*** {
      options.delay = {
        show: options.delay,
        hide: options.delay
  ***REMOVED***
***REMOVED***

    return options
  ***REMOVED***

  Tooltip.prototype.getDelegateOptions = function (***REMOVED*** {
    var options  = {***REMOVED***
    var defaults = this.getDefaults(***REMOVED***

    this._options && $.each(this._options, function (key, value***REMOVED*** {
      if (defaults[key***REMOVED*** != value***REMOVED*** options[key***REMOVED*** = value
***REMOVED******REMOVED***

    return options
  ***REMOVED***

  Tooltip.prototype.enter = function (obj***REMOVED*** {
    var self = obj instanceof this.constructor ?
      obj : $(obj.currentTarget***REMOVED***.data('bs.' + this.type***REMOVED***

    if (!self***REMOVED*** {
      self = new this.constructor(obj.currentTarget, this.getDelegateOptions(***REMOVED******REMOVED***
      $(obj.currentTarget***REMOVED***.data('bs.' + this.type, self***REMOVED***
***REMOVED***

    if (obj instanceof $.Event***REMOVED*** {
      self.inState[obj.type == 'focusin' ? 'focus' : 'hover'***REMOVED*** = true
***REMOVED***

    if (self.tip(***REMOVED***.hasClass('in'***REMOVED*** || self.hoverState == 'in'***REMOVED*** {
      self.hoverState = 'in'
      return
***REMOVED***

    clearTimeout(self.timeout***REMOVED***

    self.hoverState = 'in'

    if (!self.options.delay || !self.options.delay.show***REMOVED*** return self.show(***REMOVED***

    self.timeout = setTimeout(function (***REMOVED*** {
      if (self.hoverState == 'in'***REMOVED*** self.show(***REMOVED***
***REMOVED***, self.options.delay.show***REMOVED***
  ***REMOVED***

  Tooltip.prototype.isInStateTrue = function (***REMOVED*** {
    for (var key in this.inState***REMOVED*** {
      if (this.inState[key***REMOVED******REMOVED*** return true
***REMOVED***

    return false
  ***REMOVED***

  Tooltip.prototype.leave = function (obj***REMOVED*** {
    var self = obj instanceof this.constructor ?
      obj : $(obj.currentTarget***REMOVED***.data('bs.' + this.type***REMOVED***

    if (!self***REMOVED*** {
      self = new this.constructor(obj.currentTarget, this.getDelegateOptions(***REMOVED******REMOVED***
      $(obj.currentTarget***REMOVED***.data('bs.' + this.type, self***REMOVED***
***REMOVED***

    if (obj instanceof $.Event***REMOVED*** {
      self.inState[obj.type == 'focusout' ? 'focus' : 'hover'***REMOVED*** = false
***REMOVED***

    if (self.isInStateTrue(***REMOVED******REMOVED*** return

    clearTimeout(self.timeout***REMOVED***

    self.hoverState = 'out'

    if (!self.options.delay || !self.options.delay.hide***REMOVED*** return self.hide(***REMOVED***

    self.timeout = setTimeout(function (***REMOVED*** {
      if (self.hoverState == 'out'***REMOVED*** self.hide(***REMOVED***
***REMOVED***, self.options.delay.hide***REMOVED***
  ***REMOVED***

  Tooltip.prototype.show = function (***REMOVED*** {
    var e = $.Event('show.bs.' + this.type***REMOVED***

    if (this.hasContent(***REMOVED*** && this.enabled***REMOVED*** {
      this.$element.trigger(e***REMOVED***

      var inDom = $.contains(this.$element[0***REMOVED***.ownerDocument.documentElement, this.$element[0***REMOVED******REMOVED***
      if (e.isDefaultPrevented(***REMOVED*** || !inDom***REMOVED*** return
      var that = this

      var $tip = this.tip(***REMOVED***

      var tipId = this.getUID(this.type***REMOVED***

      this.setContent(***REMOVED***
      $tip.attr('id', tipId***REMOVED***
      this.$element.attr('aria-describedby', tipId***REMOVED***

      if (this.options.animation***REMOVED*** $tip.addClass('fade'***REMOVED***

      var placement = typeof this.options.placement == 'function' ?
        this.options.placement.call(this, $tip[0***REMOVED***, this.$element[0***REMOVED******REMOVED*** :
        this.options.placement

      var autoToken = /\s?auto?\s?/i
      var autoPlace = autoToken.test(placement***REMOVED***
      if (autoPlace***REMOVED*** placement = placement.replace(autoToken, ''***REMOVED*** || 'top'

      $tip
        .detach(***REMOVED***
        .css({ top: 0, left: 0, display: 'block' ***REMOVED******REMOVED***
        .addClass(placement***REMOVED***
        .data('bs.' + this.type, this***REMOVED***

      this.options.container ? $tip.appendTo(this.options.container***REMOVED*** : $tip.insertAfter(this.$element***REMOVED***
      this.$element.trigger('inserted.bs.' + this.type***REMOVED***

      var pos          = this.getPosition(***REMOVED***
      var actualWidth  = $tip[0***REMOVED***.offsetWidth
      var actualHeight = $tip[0***REMOVED***.offsetHeight

      if (autoPlace***REMOVED*** {
        var orgPlacement = placement
        var viewportDim = this.getPosition(this.$viewport***REMOVED***

        placement = placement == 'bottom' && pos.bottom + actualHeight > viewportDim.bottom ? 'top'    :
                    placement == 'top'    && pos.top    - actualHeight < viewportDim.top    ? 'bottom' :
                    placement == 'right'  && pos.right  + actualWidth  > viewportDim.width  ? 'left'   :
                    placement == 'left'   && pos.left   - actualWidth  < viewportDim.left   ? 'right'  :
                    placement

        $tip
          .removeClass(orgPlacement***REMOVED***
          .addClass(placement***REMOVED***
  ***REMOVED***

      var calculatedOffset = this.getCalculatedOffset(placement, pos, actualWidth, actualHeight***REMOVED***

      this.applyPlacement(calculatedOffset, placement***REMOVED***

      var complete = function (***REMOVED*** {
        var prevHoverState = that.hoverState
        that.$element.trigger('shown.bs.' + that.type***REMOVED***
        that.hoverState = null

        if (prevHoverState == 'out'***REMOVED*** that.leave(that***REMOVED***
  ***REMOVED***

      $.support.transition && this.$tip.hasClass('fade'***REMOVED*** ?
        $tip
          .one('bsTransitionEnd', complete***REMOVED***
          .emulateTransitionEnd(Tooltip.TRANSITION_DURATION***REMOVED*** :
        complete(***REMOVED***
***REMOVED***
  ***REMOVED***

  Tooltip.prototype.applyPlacement = function (offset, placement***REMOVED*** {
    var $tip   = this.tip(***REMOVED***
    var width  = $tip[0***REMOVED***.offsetWidth
    var height = $tip[0***REMOVED***.offsetHeight

    // manually read margins because getBoundingClientRect includes difference
    var marginTop = parseInt($tip.css('margin-top'***REMOVED***, 10***REMOVED***
    var marginLeft = parseInt($tip.css('margin-left'***REMOVED***, 10***REMOVED***

    // we must check for NaN for ie 8/9
    if (isNaN(marginTop***REMOVED******REMOVED***  marginTop  = 0
    if (isNaN(marginLeft***REMOVED******REMOVED*** marginLeft = 0

    offset.top  += marginTop
    offset.left += marginLeft

    // $.fn.offset doesn't round pixel values
    // so we use setOffset directly with our own function B-0
    $.offset.setOffset($tip[0***REMOVED***, $.extend({
      using: function (props***REMOVED*** {
        $tip.css({
          top: Math.round(props.top***REMOVED***,
          left: Math.round(props.left***REMOVED***
    ***REMOVED******REMOVED***
  ***REMOVED***
***REMOVED***, offset***REMOVED***, 0***REMOVED***

    $tip.addClass('in'***REMOVED***

    // check to see if placing tip in new offset caused the tip to resize itself
    var actualWidth  = $tip[0***REMOVED***.offsetWidth
    var actualHeight = $tip[0***REMOVED***.offsetHeight

    if (placement == 'top' && actualHeight != height***REMOVED*** {
      offset.top = offset.top + height - actualHeight
***REMOVED***

    var delta = this.getViewportAdjustedDelta(placement, offset, actualWidth, actualHeight***REMOVED***

    if (delta.left***REMOVED*** offset.left += delta.left
    else offset.top += delta.top

    var isVertical          = /top|bottom/.test(placement***REMOVED***
    var arrowDelta          = isVertical ? delta.left * 2 - width + actualWidth : delta.top * 2 - height + actualHeight
    var arrowOffsetPosition = isVertical ? 'offsetWidth' : 'offsetHeight'

    $tip.offset(offset***REMOVED***
    this.replaceArrow(arrowDelta, $tip[0***REMOVED***[arrowOffsetPosition***REMOVED***, isVertical***REMOVED***
  ***REMOVED***

  Tooltip.prototype.replaceArrow = function (delta, dimension, isVertical***REMOVED*** {
    this.arrow(***REMOVED***
      .css(isVertical ? 'left' : 'top', 50 * (1 - delta / dimension***REMOVED*** + '%'***REMOVED***
      .css(isVertical ? 'top' : 'left', ''***REMOVED***
  ***REMOVED***

  Tooltip.prototype.setContent = function (***REMOVED*** {
    var $tip  = this.tip(***REMOVED***
    var title = this.getTitle(***REMOVED***

    $tip.find('.tooltip-inner'***REMOVED***[this.options.html ? 'html' : 'text'***REMOVED***(title***REMOVED***
    $tip.removeClass('fade in top bottom left right'***REMOVED***
  ***REMOVED***

  Tooltip.prototype.hide = function (callback***REMOVED*** {
    var that = this
    var $tip = $(this.$tip***REMOVED***
    var e    = $.Event('hide.bs.' + this.type***REMOVED***

    function complete(***REMOVED*** {
      if (that.hoverState != 'in'***REMOVED*** $tip.detach(***REMOVED***
      if (that.$element***REMOVED*** { // TODO: Check whether guarding this code with this `if` is really necessary.
        that.$element
          .removeAttr('aria-describedby'***REMOVED***
          .trigger('hidden.bs.' + that.type***REMOVED***
  ***REMOVED***
      callback && callback(***REMOVED***
***REMOVED***

    this.$element.trigger(e***REMOVED***

    if (e.isDefaultPrevented(***REMOVED******REMOVED*** return

    $tip.removeClass('in'***REMOVED***

    $.support.transition && $tip.hasClass('fade'***REMOVED*** ?
      $tip
        .one('bsTransitionEnd', complete***REMOVED***
        .emulateTransitionEnd(Tooltip.TRANSITION_DURATION***REMOVED*** :
      complete(***REMOVED***

    this.hoverState = null

    return this
  ***REMOVED***

  Tooltip.prototype.fixTitle = function (***REMOVED*** {
    var $e = this.$element
    if ($e.attr('title'***REMOVED*** || typeof $e.attr('data-original-title'***REMOVED*** != 'string'***REMOVED*** {
      $e.attr('data-original-title', $e.attr('title'***REMOVED*** || ''***REMOVED***.attr('title', ''***REMOVED***
***REMOVED***
  ***REMOVED***

  Tooltip.prototype.hasContent = function (***REMOVED*** {
    return this.getTitle(***REMOVED***
  ***REMOVED***

  Tooltip.prototype.getPosition = function ($element***REMOVED*** {
    $element   = $element || this.$element

    var el     = $element[0***REMOVED***
    var isBody = el.tagName == 'BODY'

    var elRect    = el.getBoundingClientRect(***REMOVED***
    if (elRect.width == null***REMOVED*** {
      // width and height are missing in IE8, so compute them manually; see https://github.com/twbs/bootstrap/issues/14093
      elRect = $.extend({***REMOVED***, elRect, { width: elRect.right - elRect.left, height: elRect.bottom - elRect.top ***REMOVED******REMOVED***
***REMOVED***
    var isSvg = window.SVGElement && el instanceof window.SVGElement
    // Avoid using $.offset(***REMOVED*** on SVGs since it gives incorrect results in jQuery 3.
    // See https://github.com/twbs/bootstrap/issues/20280
    var elOffset  = isBody ? { top: 0, left: 0 ***REMOVED*** : (isSvg ? null : $element.offset(***REMOVED******REMOVED***
    var scroll    = { scroll: isBody ? document.documentElement.scrollTop || document.body.scrollTop : $element.scrollTop(***REMOVED*** ***REMOVED***
    var outerDims = isBody ? { width: $(window***REMOVED***.width(***REMOVED***, height: $(window***REMOVED***.height(***REMOVED*** ***REMOVED*** : null

    return $.extend({***REMOVED***, elRect, scroll, outerDims, elOffset***REMOVED***
  ***REMOVED***

  Tooltip.prototype.getCalculatedOffset = function (placement, pos, actualWidth, actualHeight***REMOVED*** {
    return placement == 'bottom' ? { top: pos.top + pos.height,   left: pos.left + pos.width / 2 - actualWidth / 2 ***REMOVED*** :
           placement == 'top'    ? { top: pos.top - actualHeight, left: pos.left + pos.width / 2 - actualWidth / 2 ***REMOVED*** :
           placement == 'left'   ? { top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left - actualWidth ***REMOVED*** :
        /* placement == 'right' */ { top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left + pos.width ***REMOVED***

  ***REMOVED***

  Tooltip.prototype.getViewportAdjustedDelta = function (placement, pos, actualWidth, actualHeight***REMOVED*** {
    var delta = { top: 0, left: 0 ***REMOVED***
    if (!this.$viewport***REMOVED*** return delta

    var viewportPadding = this.options.viewport && this.options.viewport.padding || 0
    var viewportDimensions = this.getPosition(this.$viewport***REMOVED***

    if (/right|left/.test(placement***REMOVED******REMOVED*** {
      var topEdgeOffset    = pos.top - viewportPadding - viewportDimensions.scroll
      var bottomEdgeOffset = pos.top + viewportPadding - viewportDimensions.scroll + actualHeight
      if (topEdgeOffset < viewportDimensions.top***REMOVED*** { // top overflow
        delta.top = viewportDimensions.top - topEdgeOffset
  ***REMOVED*** else if (bottomEdgeOffset > viewportDimensions.top + viewportDimensions.height***REMOVED*** { // bottom overflow
        delta.top = viewportDimensions.top + viewportDimensions.height - bottomEdgeOffset
  ***REMOVED***
***REMOVED*** else {
      var leftEdgeOffset  = pos.left - viewportPadding
      var rightEdgeOffset = pos.left + viewportPadding + actualWidth
      if (leftEdgeOffset < viewportDimensions.left***REMOVED*** { // left overflow
        delta.left = viewportDimensions.left - leftEdgeOffset
  ***REMOVED*** else if (rightEdgeOffset > viewportDimensions.right***REMOVED*** { // right overflow
        delta.left = viewportDimensions.left + viewportDimensions.width - rightEdgeOffset
  ***REMOVED***
***REMOVED***

    return delta
  ***REMOVED***

  Tooltip.prototype.getTitle = function (***REMOVED*** {
    var title
    var $e = this.$element
    var o  = this.options

    title = $e.attr('data-original-title'***REMOVED***
      || (typeof o.title == 'function' ? o.title.call($e[0***REMOVED******REMOVED*** :  o.title***REMOVED***

    return title
  ***REMOVED***

  Tooltip.prototype.getUID = function (prefix***REMOVED*** {
    do prefix += ~~(Math.random(***REMOVED*** * 1000000***REMOVED***
    while (document.getElementById(prefix***REMOVED******REMOVED***
    return prefix
  ***REMOVED***

  Tooltip.prototype.tip = function (***REMOVED*** {
    if (!this.$tip***REMOVED*** {
      this.$tip = $(this.options.template***REMOVED***
      if (this.$tip.length != 1***REMOVED*** {
        throw new Error(this.type + ' `template` option must consist of exactly 1 top-level element!'***REMOVED***
  ***REMOVED***
***REMOVED***
    return this.$tip
  ***REMOVED***

  Tooltip.prototype.arrow = function (***REMOVED*** {
    return (this.$arrow = this.$arrow || this.tip(***REMOVED***.find('.tooltip-arrow'***REMOVED******REMOVED***
  ***REMOVED***

  Tooltip.prototype.enable = function (***REMOVED*** {
    this.enabled = true
  ***REMOVED***

  Tooltip.prototype.disable = function (***REMOVED*** {
    this.enabled = false
  ***REMOVED***

  Tooltip.prototype.toggleEnabled = function (***REMOVED*** {
    this.enabled = !this.enabled
  ***REMOVED***

  Tooltip.prototype.toggle = function (e***REMOVED*** {
    var self = this
    if (e***REMOVED*** {
      self = $(e.currentTarget***REMOVED***.data('bs.' + this.type***REMOVED***
      if (!self***REMOVED*** {
        self = new this.constructor(e.currentTarget, this.getDelegateOptions(***REMOVED******REMOVED***
        $(e.currentTarget***REMOVED***.data('bs.' + this.type, self***REMOVED***
  ***REMOVED***
***REMOVED***

    if (e***REMOVED*** {
      self.inState.click = !self.inState.click
      if (self.isInStateTrue(***REMOVED******REMOVED*** self.enter(self***REMOVED***
      else self.leave(self***REMOVED***
***REMOVED*** else {
      self.tip(***REMOVED***.hasClass('in'***REMOVED*** ? self.leave(self***REMOVED*** : self.enter(self***REMOVED***
***REMOVED***
  ***REMOVED***

  Tooltip.prototype.destroy = function (***REMOVED*** {
    var that = this
    clearTimeout(this.timeout***REMOVED***
    this.hide(function (***REMOVED*** {
      that.$element.off('.' + that.type***REMOVED***.removeData('bs.' + that.type***REMOVED***
      if (that.$tip***REMOVED*** {
        that.$tip.detach(***REMOVED***
  ***REMOVED***
      that.$tip = null
      that.$arrow = null
      that.$viewport = null
      that.$element = null
***REMOVED******REMOVED***
  ***REMOVED***


  // TOOLTIP PLUGIN DEFINITION
  // =========================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.tooltip'***REMOVED***
      var options = typeof option == 'object' && option

      if (!data && /destroy|hide/.test(option***REMOVED******REMOVED*** return
      if (!data***REMOVED*** $this.data('bs.tooltip', (data = new Tooltip(this, options***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***(***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.tooltip

  $.fn.tooltip             = Plugin
  $.fn.tooltip.Constructor = Tooltip


  // TOOLTIP NO CONFLICT
  // ===================

  $.fn.tooltip.noConflict = function (***REMOVED*** {
    $.fn.tooltip = old
    return this
  ***REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: popover.js v3.3.7
 * http://getbootstrap.com/javascript/#popovers
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // POPOVER PUBLIC CLASS DEFINITION
  // ===============================

  var Popover = function (element, options***REMOVED*** {
    this.init('popover', element, options***REMOVED***
  ***REMOVED***

  if (!$.fn.tooltip***REMOVED*** throw new Error('Popover requires tooltip.js'***REMOVED***

  Popover.VERSION  = '3.3.7'

  Popover.DEFAULTS = $.extend({***REMOVED***, $.fn.tooltip.Constructor.DEFAULTS, {
    placement: 'right',
    trigger: 'click',
    content: '',
    template: '<div class="popover" role="tooltip"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>'
  ***REMOVED******REMOVED***


  // NOTE: POPOVER EXTENDS tooltip.js
  // ================================

  Popover.prototype = $.extend({***REMOVED***, $.fn.tooltip.Constructor.prototype***REMOVED***

  Popover.prototype.constructor = Popover

  Popover.prototype.getDefaults = function (***REMOVED*** {
    return Popover.DEFAULTS
  ***REMOVED***

  Popover.prototype.setContent = function (***REMOVED*** {
    var $tip    = this.tip(***REMOVED***
    var title   = this.getTitle(***REMOVED***
    var content = this.getContent(***REMOVED***

    $tip.find('.popover-title'***REMOVED***[this.options.html ? 'html' : 'text'***REMOVED***(title***REMOVED***
    $tip.find('.popover-content'***REMOVED***.children(***REMOVED***.detach(***REMOVED***.end(***REMOVED***[ // we use append for html objects to maintain js events
      this.options.html ? (typeof content == 'string' ? 'html' : 'append'***REMOVED*** : 'text'
    ***REMOVED***(content***REMOVED***

    $tip.removeClass('fade top bottom left right in'***REMOVED***

    // IE8 doesn't accept hiding via the `:empty` pseudo selector, we have to do
    // this manually by checking the contents.
    if (!$tip.find('.popover-title'***REMOVED***.html(***REMOVED******REMOVED*** $tip.find('.popover-title'***REMOVED***.hide(***REMOVED***
  ***REMOVED***

  Popover.prototype.hasContent = function (***REMOVED*** {
    return this.getTitle(***REMOVED*** || this.getContent(***REMOVED***
  ***REMOVED***

  Popover.prototype.getContent = function (***REMOVED*** {
    var $e = this.$element
    var o  = this.options

    return $e.attr('data-content'***REMOVED***
      || (typeof o.content == 'function' ?
            o.content.call($e[0***REMOVED******REMOVED*** :
            o.content***REMOVED***
  ***REMOVED***

  Popover.prototype.arrow = function (***REMOVED*** {
    return (this.$arrow = this.$arrow || this.tip(***REMOVED***.find('.arrow'***REMOVED******REMOVED***
  ***REMOVED***


  // POPOVER PLUGIN DEFINITION
  // =========================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.popover'***REMOVED***
      var options = typeof option == 'object' && option

      if (!data && /destroy|hide/.test(option***REMOVED******REMOVED*** return
      if (!data***REMOVED*** $this.data('bs.popover', (data = new Popover(this, options***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***(***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.popover

  $.fn.popover             = Plugin
  $.fn.popover.Constructor = Popover


  // POPOVER NO CONFLICT
  // ===================

  $.fn.popover.noConflict = function (***REMOVED*** {
    $.fn.popover = old
    return this
  ***REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: scrollspy.js v3.3.7
 * http://getbootstrap.com/javascript/#scrollspy
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // SCROLLSPY CLASS DEFINITION
  // ==========================

  function ScrollSpy(element, options***REMOVED*** {
    this.$body          = $(document.body***REMOVED***
    this.$scrollElement = $(element***REMOVED***.is(document.body***REMOVED*** ? $(window***REMOVED*** : $(element***REMOVED***
    this.options        = $.extend({***REMOVED***, ScrollSpy.DEFAULTS, options***REMOVED***
    this.selector       = (this.options.target || ''***REMOVED*** + ' .nav li > a'
    this.offsets        = [***REMOVED***
    this.targets        = [***REMOVED***
    this.activeTarget   = null
    this.scrollHeight   = 0

    this.$scrollElement.on('scroll.bs.scrollspy', $.proxy(this.process, this***REMOVED******REMOVED***
    this.refresh(***REMOVED***
    this.process(***REMOVED***
  ***REMOVED***

  ScrollSpy.VERSION  = '3.3.7'

  ScrollSpy.DEFAULTS = {
    offset: 10
  ***REMOVED***

  ScrollSpy.prototype.getScrollHeight = function (***REMOVED*** {
    return this.$scrollElement[0***REMOVED***.scrollHeight || Math.max(this.$body[0***REMOVED***.scrollHeight, document.documentElement.scrollHeight***REMOVED***
  ***REMOVED***

  ScrollSpy.prototype.refresh = function (***REMOVED*** {
    var that          = this
    var offsetMethod  = 'offset'
    var offsetBase    = 0

    this.offsets      = [***REMOVED***
    this.targets      = [***REMOVED***
    this.scrollHeight = this.getScrollHeight(***REMOVED***

    if (!$.isWindow(this.$scrollElement[0***REMOVED******REMOVED******REMOVED*** {
      offsetMethod = 'position'
      offsetBase   = this.$scrollElement.scrollTop(***REMOVED***
***REMOVED***

    this.$body
      .find(this.selector***REMOVED***
      .map(function (***REMOVED*** {
        var $el   = $(this***REMOVED***
        var href  = $el.data('target'***REMOVED*** || $el.attr('href'***REMOVED***
        var $href = /^#./.test(href***REMOVED*** && $(href***REMOVED***

        return ($href
          && $href.length
          && $href.is(':visible'***REMOVED***
          && [[$href[offsetMethod***REMOVED***(***REMOVED***.top + offsetBase, href***REMOVED******REMOVED******REMOVED*** || null
  ***REMOVED******REMOVED***
      .sort(function (a, b***REMOVED*** { return a[0***REMOVED*** - b[0***REMOVED*** ***REMOVED******REMOVED***
      .each(function (***REMOVED*** {
        that.offsets.push(this[0***REMOVED******REMOVED***
        that.targets.push(this[1***REMOVED******REMOVED***
  ***REMOVED******REMOVED***
  ***REMOVED***

  ScrollSpy.prototype.process = function (***REMOVED*** {
    var scrollTop    = this.$scrollElement.scrollTop(***REMOVED*** + this.options.offset
    var scrollHeight = this.getScrollHeight(***REMOVED***
    var maxScroll    = this.options.offset + scrollHeight - this.$scrollElement.height(***REMOVED***
    var offsets      = this.offsets
    var targets      = this.targets
    var activeTarget = this.activeTarget
    var i

    if (this.scrollHeight != scrollHeight***REMOVED*** {
      this.refresh(***REMOVED***
***REMOVED***

    if (scrollTop >= maxScroll***REMOVED*** {
      return activeTarget != (i = targets[targets.length - 1***REMOVED******REMOVED*** && this.activate(i***REMOVED***
***REMOVED***

    if (activeTarget && scrollTop < offsets[0***REMOVED******REMOVED*** {
      this.activeTarget = null
      return this.clear(***REMOVED***
***REMOVED***

    for (i = offsets.length; i--;***REMOVED*** {
      activeTarget != targets[i***REMOVED***
        && scrollTop >= offsets[i***REMOVED***
        && (offsets[i + 1***REMOVED*** === undefined || scrollTop < offsets[i + 1***REMOVED******REMOVED***
        && this.activate(targets[i***REMOVED******REMOVED***
***REMOVED***
  ***REMOVED***

  ScrollSpy.prototype.activate = function (target***REMOVED*** {
    this.activeTarget = target

    this.clear(***REMOVED***

    var selector = this.selector +
      '[data-target="' + target + '"***REMOVED***,' +
      this.selector + '[href="' + target + '"***REMOVED***'

    var active = $(selector***REMOVED***
      .parents('li'***REMOVED***
      .addClass('active'***REMOVED***

    if (active.parent('.dropdown-menu'***REMOVED***.length***REMOVED*** {
      active = active
        .closest('li.dropdown'***REMOVED***
        .addClass('active'***REMOVED***
***REMOVED***

    active.trigger('activate.bs.scrollspy'***REMOVED***
  ***REMOVED***

  ScrollSpy.prototype.clear = function (***REMOVED*** {
    $(this.selector***REMOVED***
      .parentsUntil(this.options.target, '.active'***REMOVED***
      .removeClass('active'***REMOVED***
  ***REMOVED***


  // SCROLLSPY PLUGIN DEFINITION
  // ===========================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.scrollspy'***REMOVED***
      var options = typeof option == 'object' && option

      if (!data***REMOVED*** $this.data('bs.scrollspy', (data = new ScrollSpy(this, options***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***(***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.scrollspy

  $.fn.scrollspy             = Plugin
  $.fn.scrollspy.Constructor = ScrollSpy


  // SCROLLSPY NO CONFLICT
  // =====================

  $.fn.scrollspy.noConflict = function (***REMOVED*** {
    $.fn.scrollspy = old
    return this
  ***REMOVED***


  // SCROLLSPY DATA-API
  // ==================

  $(window***REMOVED***.on('load.bs.scrollspy.data-api', function (***REMOVED*** {
    $('[data-spy="scroll"***REMOVED***'***REMOVED***.each(function (***REMOVED*** {
      var $spy = $(this***REMOVED***
      Plugin.call($spy, $spy.data(***REMOVED******REMOVED***
***REMOVED******REMOVED***
  ***REMOVED******REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: tab.js v3.3.7
 * http://getbootstrap.com/javascript/#tabs
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // TAB CLASS DEFINITION
  // ====================

  var Tab = function (element***REMOVED*** {
    // jscs:disable requireDollarBeforejQueryAssignment
    this.element = $(element***REMOVED***
    // jscs:enable requireDollarBeforejQueryAssignment
  ***REMOVED***

  Tab.VERSION = '3.3.7'

  Tab.TRANSITION_DURATION = 150

  Tab.prototype.show = function (***REMOVED*** {
    var $this    = this.element
    var $ul      = $this.closest('ul:not(.dropdown-menu***REMOVED***'***REMOVED***
    var selector = $this.data('target'***REMOVED***

    if (!selector***REMOVED*** {
      selector = $this.attr('href'***REMOVED***
      selector = selector && selector.replace(/.*(?=#[^\s***REMOVED****$***REMOVED***/, ''***REMOVED*** // strip for ie7
***REMOVED***

    if ($this.parent('li'***REMOVED***.hasClass('active'***REMOVED******REMOVED*** return

    var $previous = $ul.find('.active:last a'***REMOVED***
    var hideEvent = $.Event('hide.bs.tab', {
      relatedTarget: $this[0***REMOVED***
***REMOVED******REMOVED***
    var showEvent = $.Event('show.bs.tab', {
      relatedTarget: $previous[0***REMOVED***
***REMOVED******REMOVED***

    $previous.trigger(hideEvent***REMOVED***
    $this.trigger(showEvent***REMOVED***

    if (showEvent.isDefaultPrevented(***REMOVED*** || hideEvent.isDefaultPrevented(***REMOVED******REMOVED*** return

    var $target = $(selector***REMOVED***

    this.activate($this.closest('li'***REMOVED***, $ul***REMOVED***
    this.activate($target, $target.parent(***REMOVED***, function (***REMOVED*** {
      $previous.trigger({
        type: 'hidden.bs.tab',
        relatedTarget: $this[0***REMOVED***
  ***REMOVED******REMOVED***
      $this.trigger({
        type: 'shown.bs.tab',
        relatedTarget: $previous[0***REMOVED***
  ***REMOVED******REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  Tab.prototype.activate = function (element, container, callback***REMOVED*** {
    var $active    = container.find('> .active'***REMOVED***
    var transition = callback
      && $.support.transition
      && ($active.length && $active.hasClass('fade'***REMOVED*** || !!container.find('> .fade'***REMOVED***.length***REMOVED***

    function next(***REMOVED*** {
      $active
        .removeClass('active'***REMOVED***
        .find('> .dropdown-menu > .active'***REMOVED***
          .removeClass('active'***REMOVED***
        .end(***REMOVED***
        .find('[data-toggle="tab"***REMOVED***'***REMOVED***
          .attr('aria-expanded', false***REMOVED***

      element
        .addClass('active'***REMOVED***
        .find('[data-toggle="tab"***REMOVED***'***REMOVED***
          .attr('aria-expanded', true***REMOVED***

      if (transition***REMOVED*** {
        element[0***REMOVED***.offsetWidth // reflow for transition
        element.addClass('in'***REMOVED***
  ***REMOVED*** else {
        element.removeClass('fade'***REMOVED***
  ***REMOVED***

      if (element.parent('.dropdown-menu'***REMOVED***.length***REMOVED*** {
        element
          .closest('li.dropdown'***REMOVED***
            .addClass('active'***REMOVED***
          .end(***REMOVED***
          .find('[data-toggle="tab"***REMOVED***'***REMOVED***
            .attr('aria-expanded', true***REMOVED***
  ***REMOVED***

      callback && callback(***REMOVED***
***REMOVED***

    $active.length && transition ?
      $active
        .one('bsTransitionEnd', next***REMOVED***
        .emulateTransitionEnd(Tab.TRANSITION_DURATION***REMOVED*** :
      next(***REMOVED***

    $active.removeClass('in'***REMOVED***
  ***REMOVED***


  // TAB PLUGIN DEFINITION
  // =====================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this = $(this***REMOVED***
      var data  = $this.data('bs.tab'***REMOVED***

      if (!data***REMOVED*** $this.data('bs.tab', (data = new Tab(this***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***(***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.tab

  $.fn.tab             = Plugin
  $.fn.tab.Constructor = Tab


  // TAB NO CONFLICT
  // ===============

  $.fn.tab.noConflict = function (***REMOVED*** {
    $.fn.tab = old
    return this
  ***REMOVED***


  // TAB DATA-API
  // ============

  var clickHandler = function (e***REMOVED*** {
    e.preventDefault(***REMOVED***
    Plugin.call($(this***REMOVED***, 'show'***REMOVED***
  ***REMOVED***

  $(document***REMOVED***
    .on('click.bs.tab.data-api', '[data-toggle="tab"***REMOVED***', clickHandler***REMOVED***
    .on('click.bs.tab.data-api', '[data-toggle="pill"***REMOVED***', clickHandler***REMOVED***

***REMOVED***(jQuery***REMOVED***;

/* ========================================================================
 * Bootstrap: affix.js v3.3.7
 * http://getbootstrap.com/javascript/#affix
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE***REMOVED***
 * ======================================================================== */


+function ($***REMOVED*** {
  'use strict';

  // AFFIX CLASS DEFINITION
  // ======================

  var Affix = function (element, options***REMOVED*** {
    this.options = $.extend({***REMOVED***, Affix.DEFAULTS, options***REMOVED***

    this.$target = $(this.options.target***REMOVED***
      .on('scroll.bs.affix.data-api', $.proxy(this.checkPosition, this***REMOVED******REMOVED***
      .on('click.bs.affix.data-api',  $.proxy(this.checkPositionWithEventLoop, this***REMOVED******REMOVED***

    this.$element     = $(element***REMOVED***
    this.affixed      = null
    this.unpin        = null
    this.pinnedOffset = null

    this.checkPosition(***REMOVED***
  ***REMOVED***

  Affix.VERSION  = '3.3.7'

  Affix.RESET    = 'affix affix-top affix-bottom'

  Affix.DEFAULTS = {
    offset: 0,
    target: window
  ***REMOVED***

  Affix.prototype.getState = function (scrollHeight, height, offsetTop, offsetBottom***REMOVED*** {
    var scrollTop    = this.$target.scrollTop(***REMOVED***
    var position     = this.$element.offset(***REMOVED***
    var targetHeight = this.$target.height(***REMOVED***

    if (offsetTop != null && this.affixed == 'top'***REMOVED*** return scrollTop < offsetTop ? 'top' : false

    if (this.affixed == 'bottom'***REMOVED*** {
      if (offsetTop != null***REMOVED*** return (scrollTop + this.unpin <= position.top***REMOVED*** ? false : 'bottom'
      return (scrollTop + targetHeight <= scrollHeight - offsetBottom***REMOVED*** ? false : 'bottom'
***REMOVED***

    var initializing   = this.affixed == null
    var colliderTop    = initializing ? scrollTop : position.top
    var colliderHeight = initializing ? targetHeight : height

    if (offsetTop != null && scrollTop <= offsetTop***REMOVED*** return 'top'
    if (offsetBottom != null && (colliderTop + colliderHeight >= scrollHeight - offsetBottom***REMOVED******REMOVED*** return 'bottom'

    return false
  ***REMOVED***

  Affix.prototype.getPinnedOffset = function (***REMOVED*** {
    if (this.pinnedOffset***REMOVED*** return this.pinnedOffset
    this.$element.removeClass(Affix.RESET***REMOVED***.addClass('affix'***REMOVED***
    var scrollTop = this.$target.scrollTop(***REMOVED***
    var position  = this.$element.offset(***REMOVED***
    return (this.pinnedOffset = position.top - scrollTop***REMOVED***
  ***REMOVED***

  Affix.prototype.checkPositionWithEventLoop = function (***REMOVED*** {
    setTimeout($.proxy(this.checkPosition, this***REMOVED***, 1***REMOVED***
  ***REMOVED***

  Affix.prototype.checkPosition = function (***REMOVED*** {
    if (!this.$element.is(':visible'***REMOVED******REMOVED*** return

    var height       = this.$element.height(***REMOVED***
    var offset       = this.options.offset
    var offsetTop    = offset.top
    var offsetBottom = offset.bottom
    var scrollHeight = Math.max($(document***REMOVED***.height(***REMOVED***, $(document.body***REMOVED***.height(***REMOVED******REMOVED***

    if (typeof offset != 'object'***REMOVED***         offsetBottom = offsetTop = offset
    if (typeof offsetTop == 'function'***REMOVED***    offsetTop    = offset.top(this.$element***REMOVED***
    if (typeof offsetBottom == 'function'***REMOVED*** offsetBottom = offset.bottom(this.$element***REMOVED***

    var affix = this.getState(scrollHeight, height, offsetTop, offsetBottom***REMOVED***

    if (this.affixed != affix***REMOVED*** {
      if (this.unpin != null***REMOVED*** this.$element.css('top', ''***REMOVED***

      var affixType = 'affix' + (affix ? '-' + affix : ''***REMOVED***
      var e         = $.Event(affixType + '.bs.affix'***REMOVED***

      this.$element.trigger(e***REMOVED***

      if (e.isDefaultPrevented(***REMOVED******REMOVED*** return

      this.affixed = affix
      this.unpin = affix == 'bottom' ? this.getPinnedOffset(***REMOVED*** : null

      this.$element
        .removeClass(Affix.RESET***REMOVED***
        .addClass(affixType***REMOVED***
        .trigger(affixType.replace('affix', 'affixed'***REMOVED*** + '.bs.affix'***REMOVED***
***REMOVED***

    if (affix == 'bottom'***REMOVED*** {
      this.$element.offset({
        top: scrollHeight - height - offsetBottom
  ***REMOVED******REMOVED***
***REMOVED***
  ***REMOVED***


  // AFFIX PLUGIN DEFINITION
  // =======================

  function Plugin(option***REMOVED*** {
    return this.each(function (***REMOVED*** {
      var $this   = $(this***REMOVED***
      var data    = $this.data('bs.affix'***REMOVED***
      var options = typeof option == 'object' && option

      if (!data***REMOVED*** $this.data('bs.affix', (data = new Affix(this, options***REMOVED******REMOVED******REMOVED***
      if (typeof option == 'string'***REMOVED*** data[option***REMOVED***(***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED***

  var old = $.fn.affix

  $.fn.affix             = Plugin
  $.fn.affix.Constructor = Affix


  // AFFIX NO CONFLICT
  // =================

  $.fn.affix.noConflict = function (***REMOVED*** {
    $.fn.affix = old
    return this
  ***REMOVED***


  // AFFIX DATA-API
  // ==============

  $(window***REMOVED***.on('load', function (***REMOVED*** {
    $('[data-spy="affix"***REMOVED***'***REMOVED***.each(function (***REMOVED*** {
      var $spy = $(this***REMOVED***
      var data = $spy.data(***REMOVED***

      data.offset = data.offset || {***REMOVED***

      if (data.offsetBottom != null***REMOVED*** data.offset.bottom = data.offsetBottom
      if (data.offsetTop    != null***REMOVED*** data.offset.top    = data.offsetTop

      Plugin.call($spy, data***REMOVED***
***REMOVED******REMOVED***
  ***REMOVED******REMOVED***

***REMOVED***(jQuery***REMOVED***;
