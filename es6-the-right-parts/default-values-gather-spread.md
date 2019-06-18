# Default Values

Previously when trying to have default values in JS, you would use the following:

```js
function foo(x){
    x = x || 42
}
```

The problem with this is that the `||` operator does an operation of truthy/falsy so some values passed can not work as expected:

```js
foo(0)
```

to the above function still results in x being 42 because 0 is seen as a falsy value.

ES6 enables Javascript to have default values just like other programming languages

```js
function foo(x = 42){
    
}
```
