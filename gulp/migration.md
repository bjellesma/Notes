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
If we do have a dependency, we'll use `gulp.series()`. For example, if we have a styles task that has a dependency of `clean-styles`, in gulp 3, it'd be:

```js
gulp.task('styles', ['clean-styles'], function() {

});
```

In gulp 4, we now have this:

```js
gulp.task('styles', gulp.series('clean-styles', function() {

}));
```

Notice how gulp series is now passed as the callback to styles task

If we had more than one task to run as a dependency, we'd use `gulp.parallel()`. So instead of:

```js
gulp.task('inject', ['wiredep', 'styles', 'templatecache'], function() {

});
```

We'd now use:

```js
gulp.task('inject', gulp.series(
    gulp.parallel('wiredep', 'styles', 'templatecache'),
    function() {
        log('Wire up the app css into the html, and call wiredep ');

        return gulp
            .src(config.index)
            .pipe($.inject(gulp.src(config.css)))
            .pipe(gulp.dest(config.client));
    }));
```

Notice how we're using `gulp.series()` as our dependency holder still because we want the callback to be on `gulp.series`

You also need to make sure that tasks defined in `gulp.series` or `gulp.parallel` are already defined further up in the file.
