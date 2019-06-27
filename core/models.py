from django.db import models

from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from allauth.account.models import EmailAddress
from django.urls import reverse


# Create your models here.
from sai import settings


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_school_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    # username = None
    email = models.EmailField(
        unique=True, verbose_name='Email', help_text='Enter email')
    address = models.CharField(
        max_length=100, help_text='Enter your area of residence', verbose_name='Address')
    phone = PhoneNumberField(_('phone number'), blank=True, help_text=_(
        'Number must be in international format.'), null=True)
    nationality = CountryField(blank_label='select nationality')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    @property
    def email_addresses(self):
        return EmailAddress.objects.filter(user__pk=self.pk)

    @property
    def is_verified(self):
        return EmailAddress.objects.filter(verified=True).exists()


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, related_name='profile')
    image = models.ImageField(upload_to='profile/',
                              default='profile/default_profile.jpg')

    created_on = models.DateTimeField(_('added on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True)

    def __str__(self):
        return self.user.email
