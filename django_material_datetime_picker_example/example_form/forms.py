from django import forms
from django_material_datetime_picker.widget import MdDateInput, MdTimeInput


class DateTimeForm(forms.Form):
    date = forms.DateField(widget=MdDateInput)
    time = forms.TimeField(widget=MdTimeInput(attrs={'placeholder': 'Select Time'}))
    # datetime = forms.DateTimeField(widget=forms.DateInput)
