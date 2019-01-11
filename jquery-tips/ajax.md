# Promises

An example scenerio would be the following
1. Client calls an async function named getAccount()
2. getAccount() will immediately return a promise before it even returns from the server
3. The client can now use the promise object to wire up success/error callbacks
4. While this promise is being used by the client, getAccount() is still executing in the background
5. The callbacks setup by the promise will be run once getAccount() returns

The above scenerio may seem like a standard ajax call but the real advantage of promises are that they are reusable because you create the callbacks when you call the function

A typical ajax call may look like this:
```js
$.ajax({
                url: urlBase + '/' + cust.ID,
                data: cust,
                type: 'GET',
                success: function () {
                    //success
                }
            });
```

If we instead use a promise, we can make the code reusable and put it into a function

```js
getCustomers = function(){
    getCustomersData().done(function(custs){
        //successful call
    })
    .fail(function(){
        //fail
    })
},

getCustomersData = function(){
    return $.getJSON(urlBase)
}
```

For other http ops like POST, PUT, and DELETE, we can make the ajax call into the object to be returned making our code reusable

```js
updateCustomer = function () {
        var cust = (); //customer object
        updateCustomerData(cust)
            .done(function(){

            })
            .fail(function(){

            })
    },

    updateCustomerData = function(cust){
        return $.ajax({
            url: urlBase,
            data: cust,
            type: 'PUT'
        })
    }
```

We can take this a step further and place these promises in a seperate file or class (ES6+) and call that file or class.

If you have multiple related promises that you want to make a master callback for, we can use jquery's '$.when()' to pass an array of calls

```js
$.when(ajaxCall1(cust), ajaxCall2(order).done(function(customerData, orderData){

});
```

# Headers

You may also want to use HTTP headers in your request. You can send them to the server with the following:

```js
authenticate = function (authToken) {
        return $.ajax({
                    url: "/api/authentication",
                    type: "POST",
                    beforeSend: function (request) {
                        request.setRequestHeader("AuthToken", authToken);
                    }
                });
    }
```

You can then retreive the header like so

```js
$("#login").click(function () {
            var authToken = "123456ABCDEF";
            dataService.authenticate(authToken)
                .success(function (data, statusText, jqXHR) {
                    $("#authToken").html(jqXHR.getResponseHeader("AuthToken"));
                })
                .fail(function(jqXHR, statusText, err) {
                    alert("Error authenticating: " + err);
                });
        });
 ```
 
 # Use data() to store data
 
 If you don't have that much storage, you can use the `data()` function to cache the storage rather than needing to make
 another expensive call to your server
 
 ```js
 customersService.getCustomers()
            .success(function (data) {
                var $trs = [];
                for (var i = 0; i < data.length; i++) {
                    var cust = data[i];
                    var $tr = $("<tr>" + td(cust.ID) + td(cust.FirstName) + td(cust.LastName) + "</tr>");
                    $tr.data("orders", cust.Orders);
                    $tr.click(showOrders);
                    $trs.push($tr);
                }
                $("#customersTable tbody").append($trs);
            })
            .fail(function (jqXHR, statusText, err) {
                alert("Error getting customers: " + err);
            });


        function showOrders() {
            var $tbody = $("#ordersTable tbody");
            $tbody.html("");
            var orders = $(this).data("orders");
            var $trs = [];
            for (var i = 0; i < orders.length; i++) {
                var order = orders[i];
                var $tr = $("<tr>" + td(order.ID) + td(order.ProductTitle) + td(order.Total) + "</tr>");
                $trs.push($tr);
            }
            $tbody.append($trs);
        }

        function td(data) {
            return "<td>" + data + "</td>";
        }
 ```
