- Most commonly, odoo is installed in a virtual machine on an ubuntu install for local testing
- All odoo data is stored inside of a PostGres database so install this with `sudo apt-get install postgres`
- Create a new PostGres user with the following commands
  - `sudo su - postgres`
    - This will switch users to the postgres account so that we can start writing commands for that
  - `createuser --createdb --username postgres --no-createrole --pwprompt <user>`
    - Where `<user>` is the user of the linux distro
    - This command will allow the `<user>` to be able to user PostGres so that we no longer need to use `sudo su - postgres`
- Installing Odoo Dependancies

  - The list of these dependencies are available on the odoo documentation [https://www.odoo.com/documentation/14.0/administration/install.html](https://www.odoo.com/documentation/14.0/administration/install.html)

    ```bash

    ```

  sudo apt install python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
   libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
   liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev

  ```

  ```

- Installing Odoo
  - Doing a source installation is the best for developers as it allows you to maintain multiple versions very easily
    `git clone https://github.com/odoo/odoo.git`
  - You'll need at least python 3.6 or higher installed on your system to run odoo
  * In the same directory with the `requirements.txt`, run the following commands
  ```bash
  pip3 install setuptools wheel
  pip3 install -r requirements.txt
  ```
  - Errors
    - While installing, I also found that I needed the following
    ```bash
    sudo apt-get install python3-pypdf2
    sudo apt-get install python3-decorator
    sudo apt-get install python3-polib
    sudo apt-get install python3-html2text
    sudo apt-get install python3-docutils
    sudo apt-get install python3-libsass
    ```

* If all works out properly, you will see messages in your terminal that the server is running at port 8069
* When you create a new database on Odoo, you will be asked if you wanted to create demo data that you can use.
* Run Odoo with `./odoo-bin`
  - This is the command line so Odoo will start in the background
