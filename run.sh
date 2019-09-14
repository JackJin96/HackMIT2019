#!/bin/bash

find . -name '*.pyc' -delete

export FLASK_APP=App
export FLASK_ENV=development
# remove when in development
export OAUTHLIB_INSECURE_TRANSPORT=1

echo $FLASK_APP
echo $FLASK_ENV

pip3 install -e .

# flask run --host=localhost --port=8080
flask run
