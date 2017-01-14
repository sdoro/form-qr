
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

### create the pucher app

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
