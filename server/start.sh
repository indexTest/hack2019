#!/bin/bash

export FLASK_APP=flaskr
export FLASK_ENV=development
pip install -r requirement.txt

flask run -h 0.0.0.0
