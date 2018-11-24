* [caniuse.com](caniuse.com) is a resource to tell if a feature is going to be available for an older browser
* [Modernizr](https://modernizr.com/) is a javascript library to tell you if the user's browser is going to support new features

In the following example, if there is no support for the css3 border-radius, then we will use jquery, migrate, and imgr plugins to attain the same effect.

```js
Modernizr.load({
  test: Modernizr.borderradius,
  nope: ['/js/jquery-1.10.2.min.js', '/js/jquery-migrate-1.2.1.min.js', '/js/jquery.imgr.min.js'],
  complete: function(){
    if(!Modernizr.borderradius){
      $("#imgFlag").imgr({
        size: "3px",
        color: "red",
        radius: "25px"
      })
    }
  }
})
```

* If you control the server that is hosting the web files, you are able to control how long the user will cache your files so that the you don't have to unneccessarily use bandwith to serve files that may not have changed

In IIS, you can control how long files from a folder will take until they expire.

* Using a CDN is much better for performance
  * A CDN may be closer in proximity to the user than your datacenter may be so it would be faster for the user to go out to the CDN

The following can be used as a fallback technique if the CDN is not able to load the file

```html
<script src="http://ajax.microsoft.com/ajax/jquery/jquery-1.10.2.min.js"></script>

<!-- Fallback to use a local copy if the CDN does not load Properly -->
<!-- The statement will only execute if js is not loaded -->
<script>
  !window.jQuery && document.write('<script src="/js/jquery-1.10.2.min.js"></script>');
</script>
```
