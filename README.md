# guava

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/nicolaskiprop/guava.git
```

### Create and activate a virtual environment

    virtualenv env --python=python3.6

    source env/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

## Running the application

```bash
$ export FLASK_APP=main.py

$ export MODE=development

$ flask run
```

## Endpoints Available
| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   | /api/v2/auth/signup             | sign up a user                        | users         |
| POST   | /api/v2/auth/login              | login a user                          | users         |

### Testing

    nosetests

    - Testing with coverage

    nosetests --with-coverage --cover-package=app

### Author
Nick

















