# server
Django + React

## Description
Simple Django web application built with Webpack and Yarn. Based on the work
given by Angela Branaes:
[Building a Python ReactJS web application](https://www.youtube.com/watch?v=nfi0hX-F8Zo "Youtube: Angela Branaes")

## Setup
PyEnv was used to select the proper Python version to be used along with
VirtualEnv. The React part was integrated using NodeEnv.

## Prerrequisites
Make sure to install and have a working Git and PyEnv environment
and then with the help of PyEnv install Python version 3.6.3.

### Git
In our case, with Windows 10 WSL with Ubuntu:

    sudo apt-get install git

### PyEnv
Copy and paste the following in the console/terminal:

    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

Edit your .bashrc file and add the following at the end of the file:

    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

To continue, refresh/rehash the shell.

### Install Python 3.6.3
Install in case this particular version is not readily available; otherwise,
skip to the next section:

    pyenv install 3.6.3

Verify the installation went through:

    pyenv versions

You should see something like this after executing the previous command:

    * system (set by /home/<user>/.pyenv/version)
    3.6.3

## Installation
Please follow the next recommended sequence of general instructions to install
this application:

    git clone
    cd school
    pyenv virtualenv 3.6.3 school
    pyenv activate school
    pip install -r requirements.txt

### Tie nodeenv with pyenv

    nodeenv -p

### Install yarn
We proceed to install the yarn node package manager, and also make sure the
proper settings have been applied to the end of the bash setup (.bashrc file):

    curl -o- -L https://yarnpkg.com/install.sh | bash

    export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

To continue, refresh/rehash the shell.

### Install Node packages via yarn
Proceed to install all needed React dependencies:

    cd school/static
    yarn install
    yarn build
    cd ../../

### React autobuild
While developing React components, you can use the auto build feature by:

    cd application/templates/static
    yarn watch

## Run server
To run the server, make sure you have the instance folder with the config.py
file settings needed, before you start the sever:

    mkdir instance
    cd instance
    touch config.py

With your favorite editor add the following settings accordingly:

    CONFIG = 'INSTANCE'
    SECRET_KEY = 'some-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/server.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'some-password-salt'

    SUPER_ROLE = 'super'
    SUPER_ROLE_DESCRIPTION = 'Super User'
    SUPER_PASSWORD = 'superuser'
    SUPER_EMAIL = 'super@localhost.com'
    ADMIN_ROLE = 'admin'
    ADMIN_ROLE_DESCRIPTION = 'Administrador'
    ADMIN_PASSWORD = 'adminuser'
    ADMIN_EMAIL = 'admin@localhost.com'

    SECURITY_EMAIL_SENDER = 'no-reply@localhost'
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = some-user
    MAIL_PASSWORD = some-password

Then start the server:

    ./start



## Logging
The built in logging feature using JSON can be monitered as well:

    tail -f /tmp/server_development_json.log

## NOTES
The SQLite file location is setup via the instance configuration settings.
The logging file location is setup via the different config files for:

    - development
    - stagging
    - production
