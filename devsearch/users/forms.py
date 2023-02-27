from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']

        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        for k, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})