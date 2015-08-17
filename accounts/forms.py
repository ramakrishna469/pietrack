import re
from django import forms
from piebase.models import User

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'username']

#class ProductForm(forms.Form):
#    product_name = forms.CharField()
#    category = forms.ModelChoiceField(queryset = Category.objects.all())
#
#class CategoryForm(forms.ModelForm):
#    
#    class Meta:
#        model = Category
#        fields = '__all__'
#
#    def clean_category_name(self):
#        category_name_str = self.cleaned_data['category_name']
#        if category_name_str[0].isupper():
#            if re.findall(r'\d+', category_name_str):
#                return category_name_str
#            else:
#                raise forms.ValidationError('Required atleast one numeric value')
#        else:
#            raise forms.ValidationError('First letter should be caps')
#
#class LoginForm(forms.Form):
#    username = forms.CharField()
#    password = forms.CharField(widget = forms.PasswordInput)
#
#class RegistrationForm(forms.Form):
#    username = forms.CharField()
#    password = forms.CharField(widget = forms.PasswordInput)
#
#class FileUploadForm(forms.Form):
#    file_upload = forms.FileField(label = 'Select File')
