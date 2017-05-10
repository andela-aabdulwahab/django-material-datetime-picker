from django.shortcuts import render
from django.views.generic import FormView
from .forms import DateTimeForm

from django.utils.formats import get_format
# Create your views here.


class TestFormView(FormView):
    form_class = DateTimeForm
    template_name = "example_form.html"
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(form.is_valid())
        print(get_format('DATETIME_INPUT_FORMATS'))
        return super(TestFormView, self).post(request, *args, **kwargs)
