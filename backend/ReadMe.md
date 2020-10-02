## This is the Anagram Checker application's backend.

## Setup

### Based python version = 3.6
### Install the python dependencies listed in `requirements.txt`

`pip install -r requirements.txt`

## Run
### Running the application
`python app.py`

### Runming the application with Gunicorn
`gunicorn wsgi:app -b 0.0.0.0:5000`

### Running test cases
`pytest`
