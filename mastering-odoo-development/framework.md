- You can activate Odoo debug mode through settings -> activate developer mode
  _ [Odoo 14 Documentation](#https://www.odoo.com/documentation/14.0/applications/general.html#activate-the-developer-mode-debug-mode)
  _ You can now activate debug mode using the following screenshot
  ![Debug Mode](./images/debug_mode.png)
  - With debug mode, you're also able to hover over a field and see technical details
    ![Debug Hover](./images/debug_hover.png)
    - **Field** is the actual field name that you'll use when creating customization
    - The **Object** of product.template means that this and other objects are part of the product.template model
    - **Type** is the data type

* Database Structure is an option available under technical
  ![Database Structure](./images/database_structure.png) \* Looking at database structure, you're able to see `product.template` model which contains all of the associated object fields that we saw before
* Backup and Restore an Odoo database
    * Navigating to `/web/database/manager` brings you to a list of databases that are attached to your Odoo instance
![Database Manager](./images/database_manager.png)
    * Performing a backup/restore is as easy as clicking the buttons on the manager
    * It's always a good idea to use your backup/restore and ensure proper testing of them before modifying the database
* Add to a model by navigating to Settings -> Technical -> Database Structure => Models and choosing the model that you want to modify. In our example, we'll choose `product.template`. Scroll to the bottom of the page where you should see an option for "add a line"
![Add Field](./images/add-field.png)
* Notice that the field name begins with "x_". This is how Odoo denotes that the field is custom so they'll preserve this field through updates
![Add Field Example](./images/add-field-example.png)
* Make sure to also click save on the model in order to properly save it to the database
![Save Model](./images/save-model.png)
* Although this field is added to the model, it must still be added to the view