# Planaday Developer Test Project


[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## INSTRUCTIONS

Once docker is up and running, go to `localhost:8000` in order to access the projet instructions


## Basic Commands

### Using Docker

To set up the Docker Environment please use the following command to install, set up and start the app.
        
    docker-compose -f local.yml up

To create and run migrations

    docker-compose -f local.yml run --rm django python manage.py makemigrations
    docker-compose -f local.yml run --rm django python manage.py migrate


### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ docker-compose -f local.yml run --rm django coverage run -m pytest
    $ docker-compose -f local.yml run --rm django coverage html
    $ docker-compose -f local.yml run --rm django open htmlcov/index.html

#### Running tests with pytest

    $ docker-compose -f local.yml run --rm django pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
