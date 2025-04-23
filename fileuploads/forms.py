from django import forms
from fileuploads.models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'