# Let

Previously, we've had situations like this

```js
function foo() {
  for (var i = 0; i < 10; i++) {
    console.log(i);
  }
  console.log("outside of loop")
  console.log(i);
}
```

would yield

```
1
2
3
4
5
6
7
8
9
outside of loop
10
```

In this scenerio, the variable i is available to the entire scope of `foo` even though we are using `var`. Developers would use this as a visual indicator to not use the variable i.

Instead, you can use `let` to enforce that this variable is block scoped ONLY to this view

```js
function foo() {
  for (let i = 0; i < 10; i++) {
    console.log(i);
  }
  console.log("outside of loop")
  console.log(i);
}
```

```
1
2
3
4
5
6
7
8
9
outside of loop
(index):37 Uncaught ReferenceError: i is not defined
    at foo ((index):37)
    at HTMLButtonElement.onclick ((index):46)
```

So `let` is useful when you want a variable to be available ONLY to that loop so that other developers are free to use that variable name in other areas.

This does come with one caveat in that you can't redeclare a variable with `let`

```
function foo() {
  for (var i = 0; i < 10; i++) {
    console.log(i);
  }
  let i = 6
  console.log("outside of loop")
  console.log(i);
}
```

This will actually lead to a syntax error that i has already been declared. Keep in mind that you can redeclare with `var`

```
function foo() {
  for (var i = 0; i < 10; i++) {
    console.log(i);
  }
  var i = 6
  console.log("outside of loop")
  console.log(i);
}
```

# Const

`const` is like `let` in that it's a block scope variable declaration.

The `const` keyword has nothing to do with the value being constant but is the fact that the variable cannot be reasigned.

```js
function foo() {
  const x = [0,1,2];
  x = 3;
}
```

The above results in a syntax error because x cannot be reasigned. However, we're still able to dynamically assign to that array.

```js
function foo() {
  const x = [0,1,2];
  x[0] = 4;
}

```

The most useful uses for `const` are for variables that are constant such as

```js
const PI = 3.14
```

Any other use of `const` may lead to confusion.

# Summary

Therefore, we should still use `var` for variable declaration, `let` for block scope declaration, `const` for block scope declaration where the value will never change. `const` can be confusing as other developers might think that the value is constant which it is not.

