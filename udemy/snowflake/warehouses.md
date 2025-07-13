A virtual warehouse is a named abstraction for a massively parallet processing compute cluster and are required for DQL operations (Select), DML operations (update), and Data Loading operations (copy into)

Virtual Warehouse configuration can be changed on the fly

Virtual Warehouses contain local SSD storage used to store raw data retrieved from the storage layer

suspend warehouse - `alter warehouse my_wh suspend`. This will suspend the warehouse after current queries are finished executing

you can auto suspend a warehouse - `create warehouse my_med_wh auto_suspend=300;`. This is useful for controlling costs as it says that a warehouse can shut down after so many second.

By default, a warehouse will auto resume. We can control this by manually setting auto resume `create warehouse MY_MED_WH AUTO_RESUME=FALSE`. This may be useful if we want to not have a warehouse auto turn on.

