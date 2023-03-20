# auth
This is the Authentication API for all users.
This API will manage the following things.

1. New User Registration

2. Email Verification

3. User Login

4. Forget Password

5. Admin User

This is created implementing the following libraries.

1. Django REST Framework

2. Django AUTH

3. Simple JWT

 

# Create the Virtual Environment
$ `python -m venv DEV`

Activate the Virtual Environment
$ `DEV\Scripts\activate`

 

Create the Django Project
Install Django
$ `pip install django`

Create the Django Project
$ `django-admin startproject auth`

Create the Application
$ `python manage.py startapp api`

# Add the Application api to installed apps in settings.py.

Create the urls.py file in Application and include that in urls.pyfile in Project.

Run the Project
$ `python manage.py runserver`

This command will run the Django Project on localhost:8000.

# Setup Django Rest Framework
Install Django REST Framework
$ `pip install djangorestframework`

Add `rest_framework` to your `INSTALLED_APPS` in settings.py


INSTALLED_APPS = [
    ...
    'rest_framework',
]
 

# Setup Simple JWT
Simple JWT can be installed with pip:

$ `pip install djangorestframework-simplejwt`

Django project must be configured to use the library. In settings.py, add rest_framework_simplejwt.authentication.JWTAuthentication to the list of authentication classes:


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
Add to Installed APPs in settings.py

INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]
Add definitions.py for Simple JWT configuration.

from datetime import timedelta
...

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5), #Lifetime can be anything of our choice.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1), #Lifetime can be anything of our choice.
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
}

# Installing Django CORS Headers
$ `pip install django-cors-headers`

add it to your installed apps:


INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
Will also need to add a middleware class to listen in on responses:


MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    ...,
]
Add all the desired domain from where you want to call this api in the below list in settings.py


CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
 
