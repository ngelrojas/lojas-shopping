## DEVELOPMENT

#### change file CELERY.PY to development

-   path: app/api/celery.py

```python
    from api.settings import development
```

```python
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings.development')
```

```python
    development.DEFAULT_FROM_EMAIL
```

#### change file SERIALIZERS.PY to production, module USERS

-   path: app/users/serializers.py

```python
    from api.settings import development
```

```python
    URL_TO_SEND = development.URL_PRODUCTION
```

#### change file MANAGE.PY to production

-   path: app/manage.py

```python
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.development")
```

# run production

```python
    docker-compose up -d --build
```

```python
    docker-compose exec api python manage.py migrate
```

```python
    docker-compose exec api python manage.py users
```

```python
    docker-compose exec api python manage.py profiles
```

```python
    docker-compose exec api python manage.py product_orders
```

```python
    docker-compose run api sh -c "python manage.py collectstatic --no-input --clear"
```

## if not running celery

## the script below fix the problem

```python
    docker-compose run api sh -c "celery -A api.celery worker -l info"
```

### Testing

-   Don't stop container
-   Run the testing

```python
    docker-compose run api api sh -c "python manage.py test && flake8"
```