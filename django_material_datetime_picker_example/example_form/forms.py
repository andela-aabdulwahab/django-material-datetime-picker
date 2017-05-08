from django import forms


class DateTimeForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
    datetime = forms.DateTimeField()
