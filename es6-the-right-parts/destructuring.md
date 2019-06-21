# Array Destructuring

In ES5, the way that you would unpack values from a variable is you create variables to reference the array indices.

```js
function foo(){
    return [1,2,3];
}

var arr = foo();
var a = arr[0];
var b = arr[1];
var c = arr[2];
```

With ES6, you're now able to do something like this:

```js
function foo(){
    return [1,2,3,4];
}

var [
    a,
    b,
    c
] = foo();
```

In the above case, 4 will just be left unassigned as we didn't assign a variable to that specifically.

Furthermore, we can specify default values for these variable for the cases where we don't have enough values to match alll of the variables.

```js
function foo(){
    return [1,2];
}

var [
    a,
    b,
    c = 42
] = foo();
```

In the above case, 42 is assigned to c because there is no corresponding value in the array.

You can use this technique to assign multiple variables at once in a similar fashion to tuple unpacking in python

```js
var [a,b,c] = ["jeff", "likes", "toenails"]
```

You can use object destructing as function assignments to mimic the effect of having named parameters:

```js
function foo({a,b,c}){
	console.log(a,b,c)
}

foo({
  a:1,
  b:2,
  c:3
})
```

This would give the values 1,2,3 while if you use the wrong names for parameters

```js
function foo({d,e,f}){
	console.log(d,e,f)
}

foo({
  a:1,
  b:2,
  c:3
})
```

You'll get undefined, undefined, undefined
