from django import forms
from .models import Applicant, Application


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('__all__')

    def clean_skills(self):
        skills = self.cleaned_data.get('skills')
        app = self.cleaned_data.get('Applying_for')
        if skills != app.skills_required:
            raise forms.ValidationError('You dont have the required skills')
        return skills


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('__all__')
