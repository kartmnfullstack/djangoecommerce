from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User
from users.tasks import send_email_celery
import logging
class CustomizedUserSignUp(UserCreationForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email in use")
        return email

    def email_automation(self):
        email_input = self.cleaned_data.get('email')
        try:
            send_email_celery.delay(email_input)
        except Exception as e:
            logging.error(f"Error:{e}")
