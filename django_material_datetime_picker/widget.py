from django.forms.widgets import (DateInput, DateTimeInput, TimeInput,
                                  SelectDateWidget, Media)


class MediaMixin(object):

    def _media(self):
        _js = ['md-date-time-picker/dist/js/moment.min.js',
               'md-date-time-picker/dist/js/draggabilly.pkgd.min.js',
               'js/draggabillyfix.js',
               'md-date-time-picker/dist/js/mdDateTimePicker.js']
        _css = {'all': ('md-date-time-picker/dist/css/mdDateTimePicker.css',)}
        return Media(css=_css, js=_js)
    media = property(_media)


class DateInput(MediaMixin, DateInput):
    pass
