`virtualenvwrapper` is a package that will alow you to easily switch between virtual environments by using the `workon` command

### After installing virtualenvwrapper, you would do the following to work on a project from github
1. `git clone https://github.com/kennethreitz/requests.git`
2. `mkvirtualenv requests`

*Note that the above command will make the virtual env in the profile specified and your new requests virtualenv is immediatly activated*

3. when you're in the directory /requests, make sure to do `setvirtualenvproject`

This means that whenever you type `workon requests`, your virtual environment will be activated and your directory will immediatly change to /requests

### With virtualenvwrapper, you would also follow the following logic to make a project from scratch

1. `mkproject sample`

this command will immediatly create and activate a sample virtual environment
