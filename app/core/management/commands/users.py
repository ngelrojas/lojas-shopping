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
                User.objects.create_user(
                    email='jhon@yopmail.com',
                    password='me123',
                    first_name='jhon',
                    last_name='Doe',
                    is_activate=False)
                self.success('user created.')
            except Exception:
                self.error('please provide email and password')
