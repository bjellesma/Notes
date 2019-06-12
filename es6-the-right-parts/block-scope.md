Previously, we've had situations like this

```js
function foo(x,y){
    for(var i = 0; i<10; i++){
        console.log(i);
    }
    console.log(i);
}
```

In this scenerio, the variable i is available to the entire scope of `foo` even though we are using `var`. Developers would use this as a visual indicator to not use the variable i.
