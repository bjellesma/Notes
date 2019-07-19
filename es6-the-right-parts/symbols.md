ES6 Introduces the for of loop

```js
var str = 'hello'

for(var v of str){
    console.log(v)
}
//H
//e
//l
//l
//o
```

This is similar to the array method foreach loop

```js
var arr = [1,2,3]

arr.forEach(element => {
    console.log(element)
})

//1
//2
//3
```

Notice however that the foreach loop requires a callback function and you use this only for arrays and not, more generally, iterables.


