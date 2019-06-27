# from allauth.account.forms import SetPasswordField, PasswordField
from django import forms
from core.models import User, Profile

# from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


GENDER_CHOICE = (
    ('MALE', _('Male')),
    ('FEMALE', _('Female')),
    ('OTHER', _('Others'))
)


class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "input_text", }), required=True,)
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={"class": "input_text", }), required=True,)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={"class": "input_text", }), required=True)
    nationality = CountryField(blank_label='select nationality').formfield()
    address = forms.CharField()
    phone = forms.CharField(help_text="Number must be in format: +237654686473", label="Phone Number",
                            max_length=30, widget=forms.TextInput(attrs={"class": "input_text", }))

    class Meta:
        model = User

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']

    #     if type(phone) != 'int':
    #         # raise forms.ValidationError('Phone must be ')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.nationality = self.cleaned_data['nationality']
        user.address = self.cleaned_data['address']
        user.phone = self.cleaned_data['phone']
        user.save()


class UserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'address', 'nationality']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
