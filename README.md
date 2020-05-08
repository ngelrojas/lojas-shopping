### TRAVIS-CI

[![Build Status](https://travis-ci.com/ngelrojas/brasilprev-shopping.svg?branch=master)](https://travis-ci.com/ngelrojas/brasilprev-shopping)

# Brasil-prev shopping

### TLDR

Hello, brasilprev-team, it was funny develop this test, :D

Tools to development this project

-   Django
-   Django rest framework
-   Django rest framework JWT
-   RabbitMQ
-   Flower
-   PostgreSQL
-   PG-Admin
-   Supervisor

-   SERVER
-   AWS EC2
-   Docker
-   Docker-compose
-   NGINX

Brasil-prev shopping is based in 12 factor to good developing and use TRAVIS-CI to continuous integration.
It's a monolithic project

#### Configuration env files and description

-   remove prefix ".example" in all .env files
-   `.env` file is develop environment
-   `.env_prod` is production environment
-   `.env.prod.db` is database production environment
-   `.env.prod.pgadmin` is pg-admin panel production
-   `.env.prod.rabbitmq` is to connect rabbitmq and celery

#### API documentation

[api doc methods](https://github.com/ngelrojas/brasilprev-shopping/blob/master/APIDOC.md)

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

#### panel pgadmin

[panel pgadmin](http://3.87.243.115:5051)

-   user = admin@brasilprev.com
-   password = admin2020

#### Collection files API

for a good test api in production
import in your postman file called BrasilPrev-API.json, that is in CollectionBrasilPrev folder.

following the link: https://learning.postman.com/docs/postman/variables-and-environments/variables/#environments-in-postman

-   in the variable `{{url_prod}}` put the url API production `3.87.243.115:1337`

and testing API.
