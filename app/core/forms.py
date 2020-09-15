from django import forms
from .models import TimesYouSaved


class TimesYouSavedModelForm(forms.ModelForm):
    class Meta:
        model = TimesYouSaved
        fields = ['when', 'how', 'thanks']