#! /bin/bash

pyenv local 3.11.6

# Verify if there's a folder named .venv, if yes activate it if not first run python -m venv .venv 
if [ -d .venv ]; then
    echo "Found virtual environment... activating it"

    source .venv/bin/activate
else
    echo "creating virtual environment"
    python -m venv .venv
    ./.venv/bin/activate
    # Install dependencies
    pip install -r app/requirements.txt
fi

# Add folder root to PYTHONPATH
export PYTHONPATH=$PWD:$PYTHONPATH

