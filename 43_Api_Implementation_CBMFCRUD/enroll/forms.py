from django import forms
from .models import StudentInfo


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
