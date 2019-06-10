The following two functions are equivalent but the first uses a fat arrow:

```js
foo = x => 2;
```

```js
function foo(){
    return 2;
}
```

`=>` implies the beggining of a function and no curly braces in that body means that x returns 2. If we need to create a function with more logic, we would have to specify the return keyword

```js
x => { return 3; }
```

If you need your function to return an object (objects also use curly braces, you'll need to wrap those in round braces 

```js
x => ({y:x})
```

