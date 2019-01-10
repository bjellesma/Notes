# Using a CDN

## CDN with fallback

* CDNs have servers all over the country so that scripts can be cached
* Support for http and https
* allows the browser to download in parellel

```html
<script src="//googleapis.com/ajax">
</script>
```

Notice that no protocol is specified so that either http or https can be used. The page automatically files the front with the protocol that it uses

You can use a fallback to a local version with the following code
if the window has a jquery property, then the cdn loaded correctly

```html
<script>window.jQuery || document.write('<script src="js/jquery.js"></script>')</script>
```


# Working with Selectors

It's a good idea to cache your selectors so that you don't need to keep requerying the DOM.

For example
```javascript
function processdata(){
  $(".display").addclass("processed");
  $(".display").fadeIn(500);
}
```
while this works find, we can help the performance slightly with 
```javascript
var $display = $(".display");

function processdata(){
  $display.addclass("processed");
  $display.fadeIn(500);
}
```
The $ on the variable is a convention to tell us that the variable holds jquery data

We can also chain these commands to futher help performance with
```javascript
var display = $(".display");

function processdata(){
  display.addclass("processed").fadeIn(500);
}
```

## Using custom selectors

jQuery will actually allow you to make your own selectors to do common tasks. For example, say that you want to find all classes with an arial font. You can use the following code to create a new selector:

```javascript
$.extend($.expr[":"], {
    hasArialFont: function (element){
      return $(element).css("font-family") === "Arial";
  }
 });
```
And use the code like so:
```javascript
$("div:hasArialFont").click(function(){
  //code
});
```

# Limit DOM Interactions

Minimize the number of times that you touch the DOM in your code. What I like to do is to use a temporary variable to append to and then I can append the variable to the content

# Check if an element exists

To find if an element exists, the easiest method is to check if the length propery is less than zero. For ease, you can create a custom jquery property to do this

```javascript
//returns true if the length of the element is greater than zero
jQuery.fn.exists = function(){ return this.length > 0 };
```
We can then use the function like this
```javascript
if(element.exists){ alert(exists);}
```

# end()

Sometimes during function chaining, you may end switching the context of the jquery selector inadvertedly. For this, you can use the end() function to switch back up to the original selector. 

```javascript
$('<div class="custom"><span /></div>'>
  .find("<span") //context is now switched to span element
  .end() //get back to the span's parent div
 .html("hello world")
```

# filter() vs find()

find() will look for child elements while filter() will use the current collection

# Using objects with setters

In order to be the most maintainable, you can add multiple attributes at once to an element without needing to make several calls. You can do this by passing in javascript objects.
```javascript
$("a.main").attr({
  "href": "http://pluralsight.com",
  "title": "Pluralsight Courses"
});
```

# Use class over styles

Rather than using the `css()` jquery function to set styles to your elements, it's a better idea to define a class in your stylesheet and then use `addClass()` to add the class when needed.

```javascript
//toggleClass will add the class if it's not there, and remove it if it is
//this is very useful for display:none and other types of classes
$("div").on("click", function(){
  $(this).toggleClass("highlight");
});
```
```
