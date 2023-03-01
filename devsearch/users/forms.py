from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']

        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs) #style all field on sigup form
        for k, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','short_intro','bio','profile_image','social_github','social_twitter',
                  'social_linkedin','social_youtube','social_website']
        

    def __init__(self, *args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)  #style editform
        for k, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class UserSkill(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude =['owner']

    def __init__(self, *args,**kwargs):
        super(UserSkill,self).__init__(*args,**kwargs)  #style editform
        for k, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
