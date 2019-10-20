#!/bin/bash

set -eux
set -o pipefail

# makemigrations
python /app/manage.py makemigrations

# migrate
python /app/manage.py migrate

# start django: 
exec "$@"
