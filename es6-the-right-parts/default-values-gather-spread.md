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

# Gather Operator

ES6 allows you insert a variable number of parameters as an array like object using `...`

```js
function countArguments(...args) {  
   alert(args[2]);
}
```

If we call this with `countArguments('welcome', 'to', 'Earth');`, We will receive an alert of the third index of the array, `Earth`

# Spread Operator

ES6 provides us with the spread operator to easily concat arrays

Previously, we'd use

```js
var x = [1,2,3];
var y = [4,5];
var z = [0].concat(x,y,[6]);
```

To give us `[0,1,2,3,4,5,6]`

With the spread operator, we'll use

```js
var x = [1,2,3];
var y = [4,5];
var z = [0, ...x, ...y,6];
```

## Exercise

We want to make the following code return true when we do our console.log

```js
function foo() { }

function bar() {
	var a1 = [ 2, 4 ];
	var a2 = [ 6, 8, 10, 12 ];

	return foo();
}

console.log(
	bar().join("") === "281012"
);

```

Using a combination of our gather/spread operators

```js
function foo(x,y,z,...args) {
	 return [
   	x,
    ...args
   ]
 }

function bar() {
	var a1 = [ 2, 4 ];
	var a2 = [ 6, 8, 10, 12 ];
	return foo(...a1,...a2);
}

function end(){
	alert(
		bar().join("") === "281012"
	);
}


```
