from django.core.management.base import BaseCommand
from django.db import transaction
from core.models.user import User
from core.models.profile import ProfileBuyer
from core.models.profile import ProfileSeller


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
                # get users
                jhon = User.objects.get(id=2)
                xavier = User.objects.get(id=3)
                mery = User.objects.get(id=4)
                # create profile users buyer
                jhon_pro = ProfileBuyer.objects.get(users=jhon)
                jhon_pro.typeuser = False
                jhon_pro.save()
                self.success(f' profile buyer to users {jhon.first_name} updated')
                xavier_pro = ProfileBuyer.objects.get(users=xavier)
                xavier_pro.typeuser = False
                xavier_pro.save()
                self.success(f' profile buyer to users {xavier.first_name} updated.')
                ProfileSeller.objects.create(
                    dni='123456',
                    cnpj='123456',
                    address_company="beyond there",
                    phone_company="123654",
                    email_company="me@mery.com",
                    typeuser=True,
                    users=mery)
                self.success(f' profile buyer  {jhon.first_name} created.')
            except Exception as err:
                self.error(f'{err}')
