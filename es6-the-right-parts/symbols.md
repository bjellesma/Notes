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

There is also a for in loop but that acts on keys of an iterable.

This is not as useful because we're often not interested in keys. However, it's good to be aware of this

```js
var str = 'hello'

for(var v of str){
    console.log(v)
}
//0
//1
//2
//3
//4
```

## Generator

The `yield` keyword can be useful in iterators:

```js
function uniqID(){
    while(true){
        yield Math.random();
    }
}

var numbers = uniqID()

numbers.next().value
```

You can imagine using the above function to iterate over the results of a database query.

