from django.core.management.base import BaseCommand
from django.db import transaction
from core.models.user import User
from core.models.profile import ProfileBuyer
from core.models.profile import ProfileSeller
from core.models.product import Product
from core.models.order import Order


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
                # jhon = User.objects.get(id=2)
                xavier = User.objects.get(id=3)
                # mery = User.objects.get(id=4)
                # get orders
                orders_xavier = Order.objects.create(
                    title='fist order',
                    description='first order description',
                    users=xavier)
                # create products
                product_xavier_one = Product.objects.create(
                        title="fist product",
                        excerpt="fist product excerpt",
                        description="first product description",
                        price=54.25,
                        descount=5,
                        coupon="125adsd",
                        stock=20,
                        stock_min=5,
                        stock_max=50,
                        users=xavier)
                product_xavier_two = Product.objects.create(
                        title="second product",
                        excerpt="second product excerpt",
                        description="second product description",
                        price=54.25,
                        descount=5,
                        coupon="125adsd",
                        stock=20,
                        stock_min=5,
                        stock_max=50,
                        users=xavier)
                orders_xavier.products.add(product_xavier_one, product_xavier_two)
                self.success(f'product for  {xavier.first_name} created.')
            except Exception as err:
                self.error(f'{err}')
