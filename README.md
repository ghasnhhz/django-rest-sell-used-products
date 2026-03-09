# SellAndSave

A REST api aimed to help people sell their assests. A guy who is very interested in learning programming has no laptop, but has $350 dollars, and he needs a stronger laptop. He can't buy a new stronger laptop, but do buy one which is used a little bit, and there are people who have these laptops, and trying to sell them. So, this easily solves this problem, being a bridge between people.

## Tech Stack: 
Django, DRF, SQLite3

## To install & run the project
1. Create a virtual environment -
  On Windows
```python3 -m venv .venv```
```source .venv\Scripts\activate```
  On Linux, macOS
```python3 -m venv .venv```
```source .venv/bin/activate```

3. Clone the repo - ```git clone https://github.com/ghasnhhz/django-rest-sell-used-products```
4. Install dependencies - ```pip install -r requirements.txt```
  
5. Run Migrations. Inside src folder: Run - 
  ```python manage.py makemigrations```
  ```python manage.py migrate```
6. Run the server - ```python manage.py runserver```

## URL Endpoints
```
POST    api/users/register/
POST    api/users/login/
POST    api/users/logout/
GET     api/users/<int:pk>/
GET     api/products/
POST    api/products/
GET     api/products/<int:pk>/
PUT     api/products/<int:pk>/
DELETE  api/products/<int:pk>/
```
