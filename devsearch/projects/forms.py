from django import forms

from .models import Project,Reviews


class ProjectForm(forms.ModelForm):
    class Meta:

        model = Project
        fields = ['title','descriptions','feature_image','demo_link','source_link','tags']
        # fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for k, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        # self.fields['title'].widget.attrs.update({'class':'input'})

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['value','body']
        labels ={
            'value':'Give a vote for the project',
            'body':'add comment to the project and vote it'
        }
        def __init__(self, *args,**kwargs):
            super(ReviewForm,self).__init__(*args,**kwargs)
            for k, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})