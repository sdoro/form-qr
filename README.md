
## Working with forms (and QR code)

### Init

    # make/edit README.md
    echo "*.py[cod]" > .gitignore
    echo "Django==1.10.4" > requirements.txt

### build a virtual environment with django 1.10.4 (and verify)

    sudo pip install virtualenv
    virtualenv $HOME/.env
    source $HOME/.env/bin/activate
    pip install -r requirements.txt
    pip freeze

### create a project named timeTracker (and verify)

    django-admin.py startproject timeTracker
    cd timeTracker
    # edit timeTracker/settings.py and change ALLOWED_HOSTS
    ./manage.py runserver $IP:$PORT
    firefox https://form-qr-sdoro.c9users.io/

### create the puncher app

    ./manage.py startapp puncher
    # edit timeTracker/url.py
    > puncher/url.py
    # edit puncher/url.py
    mkdir -p puncher/templates/puncher
    > puncher/templates/puncher/index.html
    mkdir -p puncher/static/puncher/images
    # edit puncher/templates/puncher/index.html
    # edit puncher/settings.py
    # edit puncher/views.py
    # firefox https://form-qr-sdoro.c9users.io/puncher/

### setup database and create table

    # edit puncher/models.py
    ./manage.py makemigrations puncher
    ./manage.py migrate
    ./manage.py createsuperuser
    # Username: admin
    # Email address: admin@example.com
    # Password: not24get
    # Password (again): not24get

### some changes to database models

    # edit puncher/models.py
    ./manage.py makemigrations puncher
    ./manage.py migrate

### write a simple forms
    
    > puncher/templates/puncher/punch.html
    # edit puncher/templates/puncher/punch.html
    > puncher/templates/puncher/accepted.html
    # edit puncher/templates/puncher/accepted.html
    # edit puncher/admin.py
    # edit puncher/models.py
    # timeTracker/settings.py
    > puncher/templates/puncher/accepted.html
    # edit puncher/templates/puncher/accepted.html
    > puncher/templates/puncher/punch.html
    # edit puncher/templates/puncher/punch.html
