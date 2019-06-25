# Computed Properties

If you ever have instances where you want to set a variable value to be a property name, ES6 fixes this with **computed properties**

Let's say that we want a property with the name "hello" which is currently set by c. In ES5, we would do the following:

```js
"use strict";

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var c = "hello";

var obj = _defineProperty({
  a: "hello",
  b: "world"
}, c, "yo");
```

If we type `obj.hello` we would get the words Yo

In ES6, we can greatly reduce this syntax with:

```js
let c = "hello";

var obj = {
 a: "hello",
	b: "world",
  [c]:"yo"
}
```
