## PRODUCTION

#### change file CELERY.PY to production

-   path: app/api/celery.py

```python
    from api.settings import production
```

```python
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings.production')
```

```python
    production.DEFAULT_FROM_EMAIL
```

#### change file SERIALIZERS.PY to production, module USERS

-   path: app/users/serializers.py

```python
    from api.settings import production
```

```python
    URL_TO_SEND = production.URL_PRODUCTION
```

#### change file MANAGE.PY to production

-   path: app/manage.py

```python
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.production")
```

# run production

```python
    docker-compose -f docker-compose.prod.yml up -d --build
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py migrate
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py users
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py profiles
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py product_orders
```

```python
    docker-compose -f docker-compose.prod.yml run api sh -c "python manage.py collectstatic --no-input --clear"
```

## run celery production

```python
    docker-compose -f docker-compose.prod.yml run api sh -c "celery -A api.celery worker -l info"
```

### Testing

-   Don't stop container
-   Run the testing

```python
    docker-compose -f docker-compose.prod run api api sh -c "python manage.py test && flake8"
```

#### troubleshooting

-   if the panel admin not working try this:

-   don't stop current container

-   edit docker-compose.prod.yml and add '/api/' in volumes like this:

```python
    static_volume: /home/app/api/api/staticfiles
```

-   save file docker-compose.prod.yml

-   run the script

```python
    docker-compose -f docker-compose.prod.yml run sh -c "python manage.py collectstatic --no-input --clear"
```

-   refresh panel admin
