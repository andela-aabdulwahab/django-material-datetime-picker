from django import forms
from django_material_datetime_picker.widget import DateWidget, TimeWidget, SplitDateTimeWidget


class DateTimeForm(forms.Form):
    date = forms.DateField(widget=DateWidget)
    time = forms.TimeField(widget=TimeWidget(attrs={'placeholder': 'Select Time'}))
    datetime = forms.SplitDateTimeField(widget=SplitDateTimeWidget)
