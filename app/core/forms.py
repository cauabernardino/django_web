from django import forms
from django.forms import widgets
from django.forms.widgets import Select, SelectMultiple, TextInput
from .models import TimesYouSaved

class DateInput(forms.DateInput):
     input_type = 'date'


class TimesYouSavedModelForm(forms.ModelForm):
    class Meta:
        widgets = {'when':DateInput(), 'how':TextInput(attrs={'size':40}), 'thanks':SelectMultiple()}
        model = TimesYouSaved
        fields = ['when', 'how', 'thanks']
