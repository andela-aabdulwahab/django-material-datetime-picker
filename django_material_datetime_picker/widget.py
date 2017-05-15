from django.forms.widgets import (DateInput, DateTimeInput, TimeInput, Media,
                                  MultiWidget)
import uuid
from django.utils import formats
from django.forms.utils import to_current_timezone


class MdPickerMixin(object):

    format_type = None

    format_map = (
        # Date
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
        context = super(MdPickerMixin, self).get_context(name, value, attrs)
        context['widget']['attrs']['id'] = 'id_' + uuid.uuid4().hex
        format = self.format or formats.get_format(self.format_key)[0]
        context['widget']['attrs']['format'] = \
            self.conv_datetime_format_py2js(format)
        return context


class DateWidget(MdPickerMixin, DateInput):
    template_name = 'date_picker.html'


class TimeWidget(MdPickerMixin, TimeInput):
    template_name = 'time_picker.html'


class DateTimeWidget(MultiWidget):

    def __init__(self, attrs=None, date_format=None, time_format=None,
                 date_attrs=None, time_attrs=None):
        widgets = (
            DateWidget(
                attrs=attrs if date_attrs is None else date_attrs,
                format=date_format,
            ),
            TimeWidget(
                attrs=attrs if time_attrs is None else time_attrs,
                format=time_format,
            ),
        )
        super().__init__(widgets)

    def decompress(self, value):
        if value:
            value = to_current_timezone(value)
            return [value.date(), value.time().replace(microsecond=0)]
        return [None, None]
