from django import forms
from .models import Request
class requestForm(forms.ModelForm):
    desc =forms.CharField(label='Description',widget=forms.Textarea())
    class Meta:
        model = Request
        fields = ['name','courseName','desc']