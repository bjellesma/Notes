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

is called an **Immediately Invoked Function Expression (IIFE)**. Jquery is always the first parameter to the IIFE. The `$` as an actual parameter to the function makes it a reserved jquery object. Any functions listed inside of this IIFE is immediately excuted after the IIFE is created. Any variables created in this IIFE are scoped in this IIFE just like any function; this prevents pollution of the global namespace. The function expression is stored in parentheses because that makes it a function and tells the browser to immediately evaluate the function as an expression.

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
# Identifying performance problems

Use the profiler in your browser. In google chrome, this is found with performance -> record. This starts a profile. You can also run `profile()` in the console.

Whenever looping, always looks for results that you can cache to improve performance. For example,
```js
for(var j = 0; j<=divs.length; j++){

}
```

is less efficient than

```js
var len = divs.length
for(var j = 0; j<=len; j++){

}
```

Because the first example needs to requery the DOM every time while the second example only queries the DOM once, the second loop is exponentially more efficient.

Using DOM properties rather than jquery properties can help to speed up code signicantly. For example,
```js
var s = div.attr("id")
```
is much less efficient than
```js
var s = div.id
```

Many times, it may be necessary to use Jquery for things like chaining but using raw DOM properties can help to speed things up.

## Selector Performance

Using jquery `find()` can be fastest when selecting DOM elements because `find()` is fastest at grabbing the DOM element that it is chained onto

```js
$('#hello').find('.world')
``` 
is faster than

```js
$('#hello .world')
```

because jquery selects the rightmost element first (world) and looks through those elements to see which has #hello as its parent.

## Data method

You can store data directly in jQuery using the `data()` method rather than dirtying the HTML. Use the `data()` method to attach data to the DOM.

```js
div1.data("object1", {var1:1,var2:2});
```

