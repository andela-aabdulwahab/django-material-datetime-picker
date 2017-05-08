from django import forms
from django_material_datetime_picker.widget import SelectDateWidgetTest


class DateTimeForm(forms.Form):
    date = forms.DateField(widget=SelectDateWidgetTest)
    time = forms.TimeField()
    datetime = forms.DateTimeField()
