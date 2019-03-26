You can add a utility method to jquery like

```jquery
(function($){
  $.extended_function = function(){
    //blah
  }
})(jQuery)
```
This construct

```js
(function ($) {

})(jQuery);
```

is called an **Immediately Invoked Function Expression (IIFE)**. Jquery is always the first parameter to the IIFE. The `$` as an actual parameter to the function makes it a reserved jquery object. Any functions listed inside of this IIFE is immediately excuted after the IIFE is created. Any variables created in this IIFE are scoped in this IIFE just like any function; this prevents pollution of the global namespace.

Pass in a map to a jquery plugin and extend the default functionality to include default option.

```jquery
// Plugin definition.
$.fn.hilight = function( options ) {
 
    // Extend our default options with those provided.
    // Note that the first argument to extend is an empty
    // object – this is to keep from overriding our "defaults" object.
    var opts = $.extend( {}, $.fn.hilight.defaults, options );
 
    // Our plugin implementation code goes here.
 
};
 
// Plugin defaults – added as a property on our plugin function.
$.fn.hilight.defaults = {
    foreground: "red",
    background: "yellow"
};
```

