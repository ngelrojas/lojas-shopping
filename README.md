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
-   Supervisor

-   Server
-   AWS EC2
-   Docker
-   Docker-compose

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

[production file](https://github.com/ngelrojas/brasilprev-shopping/blob/master/PRODUCTION.md)

#### url production

[admin-panel-aws](http://3.87.243.115:1337/admin/)

#### url production doc

[documentation-api](http://3.87.243.115:1337/api/v1/brasilprev/)

#### panel flower and celery

[panel flower celery](http://3.87.243.115:5555)

#### pangel pgadmin

[pangel pgadmin](http://3.87.243.115:5051)
user = admin@brasilprev.com
password = admin2020

#### Collection files API

for a test api in production
import in your postman file called BrasilPrev-API.json, that is in CollectionBrasilPrev folder

-   in the variable `{{url_prod}}` put the url API production `3.87.243.115:1337`

and testing the API.
