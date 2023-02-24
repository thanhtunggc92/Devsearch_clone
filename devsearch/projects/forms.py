from django import forms

from .models import Projects


class ProjectForm(forms.ModelForm):
    class Meta:

        model = Projects
        fields = ['title','descriptions','demo_link','source_link','tags','vote_total','vote_ratio']
        # fields = '__all__'