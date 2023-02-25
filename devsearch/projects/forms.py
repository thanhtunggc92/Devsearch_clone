from django import forms

from .models import Projects


class ProjectForm(forms.ModelForm):
    class Meta:

        model = Projects
        # fields = ['title','descriptions','demo_link','source_link','tags','vote_total','vote_ratio']
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for k, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        # self.fields['title'].widget.attrs.update({'class':'input'})