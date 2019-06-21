Instead of having a dependency task array in gulp 3, you'll now use `gulp.series()` in gulp 4.

We also now have a `gulp.parallel` command which will allow tasks to run in parallel (at the same time)

The biggest change is that the overall structure of `gulp.task` changed from being 3 params to 2

Instead of

```js
gulp.task(name, [,dep], fn)
```

Dependancies are removed and it is

```js
gulp.task(name, fn)
```
