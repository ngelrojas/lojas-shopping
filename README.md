### TRAVIS-CI

[![Build Status](https://travis-ci.com/ngelrojas/brasilprev-shopping.svg?branch=master)](https://travis-ci.com/ngelrojas/brasilprev-shopping)

# Brasil-prev shopping

Tools to development this project

-   Django
-   Django rest framework
-   Django rest framework JWT
-   RabbitMQ
-   Flower
-   PostgreSQL
-   PG-Admin

Brasil-prev shopping is based in 12 factor to good developing and use TRAVIS-CI to continuous integration.

### Configuration env files and description

-   remove prefix ".example" in all .env files
-   `.env` file is develop environment
-   `.env_prod` is production environment
-   `.env.prod.db` is database production environment
-   `.env.prod.pgadmin` is pg-admin panel production
-   `.env.prod.rabbitmq` is to connect rabbitmq and celery

#### run mode development

[development file](https://github.com/ngelrojas/brasilprev-shopping/blob/master/DEVELOPMENT.md)

#### run mode production

[development file](https://github.com/ngelrojas/brasilprev-shopping/blob/master/PRODUCTION.md)

#### url production

[it's in aws](http//:35.25.125/)

#### url production doc

[documentation-api](http://35.225.25/api/v1/brasilprev)
