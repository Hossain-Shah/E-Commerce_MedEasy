# E-Commerce

## Project Setup for Development

Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

Run the development server using the command:

```bash
python manage.py runserver
```

To migrate database run the command:

```bash
python manage.py makemigrations
python manage.py migrate
```

## API documentation

```bash
Get API token:  http://127.0.0.1:8000/api/token/
Refresh API token:  http://127.0.0.1:8000/api/token/refresh/
Product list API: http://127.0.0.1:8000/product
Product order by name Get API: http://127.0.0.1:8000/api/product
Product order detail API: http://127.0.0.1:8000/product/<int:pk>
User registration API: http://127.0.0.1:8000/api/register/
Authorized user login API: http://127.0.0.1:8000/api/login/
Authorized user logout API: http://127.0.0.1:8000/api/logout/
```


