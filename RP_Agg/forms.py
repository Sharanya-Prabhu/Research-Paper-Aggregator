from django import forms
from .models import UserPaperPreference

class UserPaperPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPaperPreference
        exclude = ('user',)
