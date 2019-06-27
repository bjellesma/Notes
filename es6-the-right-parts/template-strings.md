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
# Template Strings

ES6 introduces a form of string interpolation they call **Template Strings**. In ES5, you would write 

```js
"use strict";

var firstName = "John";
var lastName = "Smith";
var msg = "Hello ".concat(firstName, " ").concat(lastName);
```

In ES6, you can now write

```js
let firstName = "John";
let lastName = "Smith";

let msg = `Hello ${firstName} ${lastName}`;
```

In order to span multiple lines (in the text editor and not the msg), you would do

```js
let firstName = "John";
let lastName = "Smith";

let msg = `Hello ${firstName} \
and ${lastName}`;
```

To get actual multiple lines in the outputted string, we would just remove the escape char

```js
let firstName = "John";
let lastName = "Smith";

let msg = `Hello ${firstName} 
and ${lastName}`;
```

Just as with jinja in python, any valid javascript is allowed in these template literals.

# Tag Functions

You can use tag functions as an abstracted way to format strings. For example, you can use a tag function to format a string with currency to automatically round to two decimal places.

```js
function currency(strings, ...values){
    var str = "";
    for(let i=0; i<strings.length; i++){
        if(i>0){
            if(typeof values[i-1] == "number"){
                str += values[i-1].toFixed(2);
            }else{
                str += values[i-1];
            }
        }
        str += strings[i];
    }
    return str;
}

var msg = currency`Hello ${name}, your \
order was $${total}.`;
````

In the above example, total is a number so it is formatted as currency. You've now extracted this functionality so that you don't need to manually remember to format.
