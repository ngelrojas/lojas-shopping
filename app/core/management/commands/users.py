from django.core.management.base import BaseCommand
from django.db import transaction
from core.models.user import User


class Command(BaseCommand):
    help = 'provide user name and password'

    def success(self, message):
        return self.stdout.write(
            self.style.SUCCESS(message)
        )

    def warning(self, message):
        return self.stdout.write(
            self.style.WARNING(message)
        )

    def error(self, message):
        return self.stdout.write(
            self.style.ERROR(message)
        )

    def handle(self, *args, **options):
        self.warning('if something goes wrong after installations, \n'
                     'please use develop environment: \n'
                     'docker-compose exec api python manage.py flush')

        with transaction.atomic():
            try:
                # create super user
                User.objects.create_superuser(
                    'admin@brasilprev.com',
                    'admin2020'
                )
                self.success('admin user created.')
                # create user to re-send email confirmation
                jhon = User.objects.create_user(
                    email='jhon@yopmail.com',
                    password='me123',
                    first_name='jhon',
                    last_name='Doe')
                self.success(f'user seller {jhon.first_name} created\
                             activated={jhon.is_activate}')

                xavier = User.objects.create_user(
                    email='xavier@yopmail.com',
                    password='me123',
                    first_name='Xavier',
                    last_name='Doe')
                xavier = User.objects.get(id=xavier.id)
                xavier.is_activate = True
                xavier.save()
                self.success(f'user seller {xavier.first_name} created\
                             activated={xavier.is_activate}')

                mery = User.objects.create_user(
                    email='mery@yopmail.com',
                    password='me123',
                    first_name='Mery',
                    last_name='Doe')
                mery = User.objects.get(id=mery.id)
                mery.is_activate = True
                mery.save()
                self.success(f'user buyer {mery.first_name} created\
                             activated={mery.is_activate}')
            except Exception as err:
                self.error(f'{err}')
