# from core.models import City, Pharmacy
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from django.db import models
from sai.settings import AUTH_USER_MODEL
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
# from cities_light.models import Country, City

# from core.models import User, Profile

# Create your models here.

User = AUTH_USER_MODEL


GENDER_CHOICE = (
    ('MALE', _('Male')),
    ('FEMALE', _('Female')),
    ('OTHER', _('Others'))
)

MODE = (
    ('Entrance Exam', _('Entrance Exam')),
    ('File Study', _('File Study'))
)

LEVEL = (
    ('BTS1', _('BTS 1')),
    ('BTS2', _('BTS 2')),
    ('LICENCE', _('Licence Pro')),
)


class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    nationality = CountryField(blank_label='select nationality')
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    created_on = models.DateTimeField(_('added on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True)

    def __str__(self):
        return self.student.email


class Session(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Session Name', help_text='Give the session a name')
    month = models.CharField(max_length=50)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')

    created_on = models.DateTimeField(_('added on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=200)

    created_on = models.DateTimeField(_('added on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=200)

    created_on = models.DateTimeField(_('added on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True)

    class Meta:
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return self.name


class Document(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    nationality = CountryField(blank_label='select nationality')
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    mode = models.CharField(max_length=20, choices=MODE,
                            verbose_name='Select Mode')
    level = models.CharField(
        max_length=20, choices=LEVEL, verbose_name='Select Level')
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    cni = models.FileField(upload_to='documents/',
                           verbose_name='National ID Card')
    birth_certificate = models.FileField(
        upload_to='documents/', verbose_name='Birth Certificate')
    gce = models.FileField(upload_to='documents/', verbose_name='GCE A-Levels')
    bts1 = models.FileField(upload_to='documents/',
                            verbose_name='BTS 1', blank=True, null=True)
    bts2 = models.FileField(upload_to='documents/',
                            verbose_name='BTS 2', blank=True, null=True)
    bachelor = models.FileField(
        upload_to='documents/', verbose_name='Bachelor', blank=True, null=True)

    entry_date = models.DateField()

    created_on = models.DateTimeField(_('added on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True)

    def __str__(self):
        return f'{self.student.email} | Files | {self.created_on.date()} | {self.created_on.time()}'
