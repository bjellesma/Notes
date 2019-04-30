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
 
 ```js
 gulp.task('js', function() {
            return gulp
                .src('./src/**/*.js')
                .pipe(concat('all.js'))
                .pipe(uglify())
                .pipe(gulp.dest('./build/'));
        });
 ```
 
 ## gulp.src
 
 ## gulp.dest
 
 ## gulp.watch
  
  
