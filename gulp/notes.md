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
 * Since this course is older, install older gulp with `npm install gulp@3.9.0 --save-dev`
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
 
 Run this task with `gulp hello-world`
 
# Linting Tools

jshint and jscs are popular linting tools with their own configurable json files on how to watch for your code changes.

1. Install these tools with `npm install --save-dev gulp-jshint gulp-jscs gulp-print gulp-if yargs`
2. Because they are new packages, we need to use node's require statement to include these
```js
var jshint = require('gulp-jshint')
var jscs = require('gulp-jscs')
var gulp-print = require('gulp-print')
var gulp-if = require('gulp-if')
var args = require('yargs').argv
```

You may also choose to load all plugins with 

```
var gulp = require('gulp`)
var $ = require('gulp-load-plugins')({lazy: true});
var args = require('yargs').argv
```

*Note that args is still defined seperately as it's called slightly differently*

*lazy:true will get the plugins only as they're used*

The above is a plugin that will automatically load all gulp plugins in your package.json file. You can now use plugins like `$.jscs()`

3. You can now create a gulp task called vet to automatically lint all of your js files

```js
gulp.task('vet', function() {

    return gulp
        .src([
            './src/**/*.js',
            './*.js'
        ])
        .pipe($.if(args.verbose, $.print()))
        .pipe($.jscs())
        .pipe($.jshint())
        .pipe($.jshint.reporter('jshint-stylish', {verbose: true}));
});
```

## Arguments

If we use the following 

```js
.pipe($.if(args.verbose, $.print()))
```

That will tell gulp to print verbose when verbose is passed on the cmd. So when we call this gulp task with `gulp vet --verbose`, we will get a lot more information about what the task is doing.

## gulp.config

To help make things more reuseable, we'll use a file that we'll export comonlly used strings called gulp.config.js

```js
module.exports = function() {
    var config = {

        // all js to vet
        alljs: [
            './src/**/*.js',
            './*.js'
        ]
    };

    return config;
};
```

We can now redefine our imports in our gulpfile slightly with

```js
var gulp = require('gulp');
var args = require('yargs').argv;
var config = require('./gulp.config')();
var $ = require('gulp-load-plugins')({lazy: true});
```

*Note: the parentheses are very important on the end of the import because that tells gulp to execute it right now*

We can redefine our task like so:

```js
gulp.task('vet', function() {

    return gulp
        .src([
            './src/**/*.js',
            './*.js'
        ])
        .pipe($.if(args.verbose, $.print()))
        .pipe($.jscs())
        .pipe($.jshint())
        .pipe($.jshint.reporter('jshint-stylish', {verbose: true}));
});
```
# CSS compilation

Install gulp tools for transforming LESS to CSS with `npm install --save-dev gulp-less gulp-autoprefixer`. This also installs an autoprefixer task which will automatically add vendor prefixes.

First, we'll update our config file to the following

```js
module.exports = function() {
    var config = {
        temp: './.tmp',
        // all js to vet
        alljs: [
            './src/**/*.js',
            './*.js'
        ],
        less:'./src/client/styles/styles.less'
    };

    return config;
};

```

Using the previous defined $, we can now run a task like so

```js
gulp.task('styles', function() {
    //log('Compile LESS to CSS');

    return gulp
        .src(config.less) //TODO add config
        .pipe($.less())
        .pipe($.autoprefixer())
        .pipe(gulp.dest(config.temp)); //TODO add config
});
```

Furthermore, rather than calling this gulp task every time, we can set gulp to watch for changes in our less with the following task using the watch api:

```js
gulp.task('less-watcher', function(){
    gulp.watch([config.less], ['styles'])
});
```

## Handle Errors Gracefully

To handle errors without stopping gulp and in order to give us better error handling, we can use a tool called plumber. We can install this tool by using `npm install --save-dev gulp-plumber`

We will pipe this into our task like any plugin with

```js
gulp.task('styles', function() {
    //log('Compile LESS to CSS');

    return gulp
        .src(config.less) //TODO add config
        .pipe($.plumber())
        .pipe($.less())
        .pipe($.autoprefixer())
        .pipe(gulp.dest(config.temp)); //TODO add config
});
```
