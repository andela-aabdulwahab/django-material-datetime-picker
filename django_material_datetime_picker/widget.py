from django.forms.widgets import (DateInput, DateTimeInput, TimeInput,
                                  SelectDateWidget, Media)
import uuid
from django.utils import formats


class MediaMixin(object):

    format_type = None

    format_map = (
        #Date
        ('DD', r'%d'),
        ('dddd', r'%A'),
        ('ddd', r'%a'),
        ('MMMM', r'%B'),
        ('MMM', r'%b'),
        ('MM', r'%m'),
        ('YYYY', r'%Y'),
        ('YY', r'%y'),

        # Time
        ('A', r'%p'),
        ('ss', r'%S'),
        ('mm', r'%M'),
        ('HH', r'%H'),
        ('hh', r'%I'),
    )

    @classmethod
    def conv_datetime_format_py2js(cls, format):
        for js, py in cls.format_map:
            format = format.replace(py, js)
        return format

    @classmethod
    def conv_datetime_format_js2py(cls, format):
        for js, py in cls.format_map:
            format = format.replace(js, py)
        return format

    def _media(self):
        _js = ['md-date-time-picker/dist/js/moment.min.js',
               'md-date-time-picker/dist/js/draggabilly.pkgd.min.js',
               'js/draggabillyfix.js',
               'md-date-time-picker/dist/js/mdDateTimePicker.js']
        _css = {'all': ('md-date-time-picker/dist/css/mdDateTimePicker.css',)}
        return Media(css=_css, js=_js)
    media = property(_media)

    def get_context(self, name, value, attrs):
        context = super(MediaMixin, self).get_context(name, value, attrs)
        context['widget']['attrs']['id'] = 'id_' + uuid.uuid4().hex
        context['widget']['attrs']['format'] = self.conv_datetime_format_py2js(formats.get_format(self.format_key)[0])
        return context


class MdDateInput(MediaMixin, DateInput):
    template_name = 'date_picker.html'

class MdTimeInput(MediaMixin, TimeInput):
    template_name = 'time_picker.html'
