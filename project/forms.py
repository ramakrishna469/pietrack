from django import forms
from piebase.models import Project
class CreateProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name','description']