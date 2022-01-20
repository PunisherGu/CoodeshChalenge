# Coodesh Chaleng

This is a challenge proposed by coodesh, basically we are consuming and CRUDing articles consumed in the spaceflight API.

## Languages and Frameworks

* Python 3.6
* Django 3.2
* Django Rest Framework 3.13



## Getting Started

This project use Docker for run, so run commands bellow
```python
docker-compose up --build
```
##

If for some reason docker compose doesn't run, try:

```python
1 - Create a virtualenv (we recommend virtualenvwrapper)
2 - Clone this repository
3 - Run: pip install -r requirements.txt
4 - Run: python manage.py migrate
5 - Run: python manage.py runserver
```

For run tests run
```python
python manage.py test
```

##

PS: 
The credentials as well as the secret key are exposed in the code for easier evaluation, obviously in a real environment this would be stored in environment variables

##
This is a challenge by [Coodesh](https://coodesh.com/)