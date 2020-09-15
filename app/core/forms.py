from django import forms
from django.forms import widgets
from django.forms.widgets import Select, SelectMultiple, TextInput
from .models import TimesYouSaved

class DateInput(forms.DateInput):
    """
    Updating for a date input.
    """
    input_type = 'date'


class TimesYouSavedModelForm(forms.ModelForm):
    """
    Form to get other people glories.
    """
    class Meta:
        widgets = {'when':DateInput(), 'how':TextInput(attrs={'size':40}), 'thanks':SelectMultiple()}
        model = TimesYouSaved
        fields = ['when', 'how', 'thanks']
