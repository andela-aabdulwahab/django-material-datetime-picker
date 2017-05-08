from django.shortcuts import render
from django.views.generic import FormView
from .forms import DateTimeForm
# Create your views here.


class TestFormView(FormView):
    form_class = DateTimeForm
    template_name = "example_form.html"
