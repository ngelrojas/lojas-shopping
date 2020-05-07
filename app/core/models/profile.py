from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .abstract import AbstractProfile
from .user import User


class ProfileBuyer(AbstractProfile):
    """create a profile buyer user"""
    typeuser = models.BooleanField(default=False)
    users = models.OneToOneField(
        User,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.users.first_name


@receiver(post_save, sender=User)
def buyer_profile(sender, instance, created, **kwargs):
    if created:
        ProfileBuyer.objects.create(users=instance)


class ProfileSeller(AbstractProfile):
    """create a profile user"""
    typeuser = models.BooleanField(default=True)
    cnpj = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    address_company = models.CharField(max_length=50)
    phone_company = models.CharField(max_length=15)
    email_company = models.CharField(max_length=250)
    users = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.users.first_name
