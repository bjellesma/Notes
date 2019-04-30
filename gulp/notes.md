# Things a task runner can do

* Minify code
* Concatenate code into one file so that we don't have references to several JS files
* SASS -> CSS
  * Write code in SASS and have it compiled to CSS
 * Cache busting
  * When we put new files out to a server, we want to ensure that the files are not cached on the server
 * Unit testing front end code
 * Injecting HTML
  * Automatically including script and link tags so that we don't need to remember them
 
 # Gulp APIs
 
 Gulpfiles really use only 4 simple APIs.
 
 ## gulp.task
 
 A typical task can be defined like so: `gulp.task(name, [dependancies], function)`
 
 dependancies are optional to pass in
 
 ```js
 gulp.task('js', function() {
            return gulp
                .src('./src/**/*.js')
                .pipe(concat('all.js'))
                .pipe(uglify())
                .pipe(gulp.dest('./build/'));
        });
 ```
 
 In the above example, we are creating a task called js (The name of the task must be unique in the gulpfile). This task will take all js files in the `./src/**/` folders and do the following actions
 
1. Concatenate the files into one js file called `all.js`
2. Uglify (minify) the code
3. Send the file to out `./build/` folder

However, with the optional dependancies parameter, we can define tasks that are to happen before the js task runs.

```js
gulp.task('js', ['jscs', 'jshint'], function() {
        return gulp
            .src('./src/**/*.js')
            .pipe(concat('all.js'))
            .pipe(uglify())
            .pipe(gulp.dest('./build/'));
    });
```

In the above example, jscs and jshint are to run before the js task runs. These tasks will run in parallel so that they will both run at the same time and js will run ONLY after both of these previous tasks finish.
 
 ## gulp.src
 
 Specify a glob pattern matching the files that you want to emit. `gulp.src(glob, [options])`
 
 ```js
gulp.task('js', ['jscs', 'jshint'], function() {
        return gulp
            .src('./src/**/*.js')
            .pipe(concat('all.js'))
            .pipe(uglify())
            .pipe(gulp.dest('./build/'));
    });
```
 
 For example, in the above example, we are matching all subfolders in `./src` with `**` and any js file within those subfolders with `*.js`
 
 The below tasks will be needed for future examples
 
 ```js
 var jshint = require('gulp-jshint');
        var jscs = require('gulp-jscs');
        var concat = require('gulp-concat');
        var uglify = require('gulp-uglify');


        gulp.task('jshint', function() {
            return gulp
                .src('./src/**/*.js')
                .pipe(jshint());
        });

    gulp.task('jscs', function() {
        return gulp
            .src('./src/**/*.js')
            .pipe(jscs());
    });
 ```
 
 Note that we will need plugins for jshint and jscs
 
 ## gulp.dest
 
 ```js
gulp.task('js', ['jscs', 'jshint'], function() {
        return gulp
            .src('./src/**/*.js')
            .pipe(concat('all.js'))
            .pipe(uglify())
            .pipe(gulp.dest('./build/'));
    });
```

 `gulp.dest(folder, [options])` is where you specify the folder that you want to output your files to. In the above example, we are outputing our files to `./build/`
 
 ## gulp.watch
  
 `gulp.watch(glob, [options], tasks)`. `tasks` is to be an array of tasks to watch for. This allows to watch a certain glob pattern
 
 ```js
gulp.task('lint-watcher', function() {
    gulp.watch('./src/**/*.js', [
        'jshint',
        'jscs'
    ]);
});
 ```
 
 In above example, we're watching `./src/**/*.js` and will perform `jshint` and `jscs` in parallel when any file in that glob pattern is changed.
 
# Project

1. Install gulp
 * Task runner
2. Install NPM
 * Package Manager
3. Install Webpack
 * Front end Package Management
 
 The following is a sample gulpfile.js
 
 ```js
 var gulp = require('gulp');

gulp.task('hello-world', function(){
    console.log('hello world');
});
 ```
