# from allauth.account.forms import SetPasswordField, PasswordField
from django import forms
from apply import models

# from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


COUNTRY = (
    ('SELECT', _('Select Country'))
)

STATE = (
    ('SELECT', _('Select State'))
)

CITY = (
    ('SELECT', _('Select City'))
)


class StudentRegisterForm(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = '__all__'
        exclude = ['student', 'nationality']

    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget = forms.Select(attrs={
            'id': 'countryId',
            'class': 'countries'})
        self.fields['state'].widget = forms.Select(attrs={
            'id': 'stateId',
            'class': 'states'})
        self.fields['city'].widget = forms.Select(attrs={
            'id': 'cityId',
            'class': 'cities'})


class DocumentsForm(forms.ModelForm):

    class Meta:
        model = models.Document
        fields = '__all__'
        exclude = ['student', 'nationality', 'entry_date']

    def __init__(self, *args, **kwargs):
        super(DocumentsForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget = forms.Select(attrs={
            'id': 'countryId',
            'class': 'countries'})
        self.fields['state'].widget = forms.Select(attrs={
            'id': 'stateId',
            'class': 'states'})
        self.fields['city'].widget = forms.Select(attrs={
            'id': 'cityId',
            'class': 'cities'})
