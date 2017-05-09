from django import forms
from django_material_datetime_picker.widget import DateInput


class DateTimeForm(forms.Form):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField()
    datetime = forms.DateTimeField(widget=forms.DateInput)
