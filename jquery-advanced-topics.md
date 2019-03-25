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
