# On() instead of bind()

The bind() method is older
```jquery
$('#buttong').bind('click', function(){
  console.log('hello world')
});
```
The newer (since 1.7) way of doing things is on()
```jquery
$('#buttong').on('click', function(){
  console.log('hello world')
});
```

The on() method also has can use a newer third parameters to better optimize performance

# On() instead of live() and delegate()

instead of 

```jquery
$('#members').find('la a').on('click', function(){
  console.log('hello world')
});
```

You can use 

```jquery
$('#members').on('click', 'la a', function(){
  console.log('hello world')
});
```

# Event Delegation

if the parent element also has an  event attached to it, you can use 

```jquery
$('#members').on('click', 'la a', function(e){
  e.stopProgration();
  console.log('hello world')
});
```

**NOTE: e is also included as a parameter to the callback function**

# Namespacing your events 

You are able to namespace your events by appending `.name` to the end of the event like so:


```jquery
$('#members').on('click.members', 'la a', function(e){
  e.stopProgration();
  console.log('hello world')
});
```

*Notice `click.members` instead of `click`*

# Creating custom events

you can use the `trigger()` method to create custom events that you can later listen to

# Determining user input

The parameter passed to the callback function on an event handler has a pleathera of information attached to it such as the pageX location and the key pressed

```jquery
$('#members').on('click.members', 'la a', function(e){
  console.log('keycode: ' + e.which);
  console.log('hello world')
});
```

# Determing if event was triggered by user

As before with the parameter passed to the callback function, the parameter has a property called `originalEvent`, which will only be set if the event
was triggered through user interaction rather than programatically.

