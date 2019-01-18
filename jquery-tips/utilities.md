# Map method

The map method in jquery is way to create a new array from an existing array. This can be useful if you need to change the keys around.

```js
var people = [
            { fn: "John", ln: "Doe", bday: "11/19/1977" },
            { fn: "Jane", ln: "Doe", bday: "10/12/1979" },
            { fn: "Joe",  ln: "Doe", bday: "07/05/2009" }
        ];

        people = $.map(people, function (person) {
            return {
                firstName: person.fn,
                lastName: person.ln,
                age: moment().diff(moment(person.bday), "years")
            };
        });
```

A use case for this could be if you get data in an unwanted format from the server. For example, in the above code, we are use momentjs to find the person's age from their birthday.

# Grep method

This is a quick way to search.

```js
people = $.grep(people, function (person) {
            return person.age > 18;
        });
```

# Type method

Rather than using the JS `typeof` operator, we can use the `$.type` jquery method

```js
if ($.type(items) === "array") {
                    for (i = 0; i < items.length; i++) {
                        result.push(callback(items[i], i));
                    }
                } else if (typeof items === "object") {
                    for (i in items) {
                        result.push(callback(items[i], i));
                    }
                }
```

In the above example, the `typeof` operator only says the value is an object, whereas the jquery `$.type()` method will get more information and tell you that the object is an array

# Brower Detection

JQuery has removed their `$.browser` method so you can't sniff a browser anymore. It's a better idea to use the **Modernizr** library to test to see

```js
//if the input type of date doesn't exist
if (!Modernizr.inputtypes.date) {
            $("link[rel='stylesheet']:last")
                .after("<link href='./ext/bootstrap-datepicker/css/datepicker.css' rel='stylesheet' />");
            $.getScript("./ext/bootstrap-datepicker/js/bootstrap-datepicker.js", function () {
                $("input[type=date]").datepicker();
            });
        }
```

This is such a common use of the library that they've made this even easier

```js
//here we're saying that if the browser doesn't support date for an input type, we want to load the datepicker stylesheet and js library
Modernizr.load({
            test: Modernizr.inputtypes.date,
            nope: [
                "./ext/bootstrap-datepicker/css/datepicker.css",
                "./ext/bootstrap-datepicker/js/bootstrap-datepicker.js"
            ],
            complete: function () {
                if (!Modernizr.inputtypes.date) {
                    $("input[type=date]").datepicker();
                }
            }
        });
```

# Extends method

Sometimes, it is useful to create your own jquery method rather than a function. Most often, this is useful in creating a jquery plugin. This can also be useful in creating a method that the user can override.
In the following example, we will make a jquery method that set the color of the text to red and increase its font to 16px. We have an object of default values, but the user may also specify an object of different values.

```js
$.fn.valentines = function (options) {
        //the second parameter is the object of default values
        //the third parameter is the options object that the user may specify to override the defaults
        //the first parameter is the object to extend which is why it is normally set to a blank object
    		var settings = $.extend({}, $.fn.valentines.defaults, options);

			return this.css(settings);
    	};
    	$.fn.valentines.defaults = { color: "red", fontSize: "16px" };

    	$("a").valentines({ color: "#A00000" });
    	$("a:last").valentines();
```

