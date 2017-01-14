
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
