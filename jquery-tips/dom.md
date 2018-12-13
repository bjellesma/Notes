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

# Limit DOM Interactions

# Check if an element exists

# end()

# filter() vs find()

# Using objects with setters

# Use class over styles
