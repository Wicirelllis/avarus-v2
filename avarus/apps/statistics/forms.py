from django import forms
from django.utils.translation import gettext_lazy as _


class ChoiceFieldForm(forms.Form):
    def __init__(self, *args, **kwargs):
        field = kwargs.pop('field') if 'field' in kwargs else None
        choices = kwargs.pop('choices') if 'choices' in kwargs else []
        widget = kwargs.pop('widget') if 'widget' in kwargs else None
        super().__init__(*args, **kwargs)
        self.fields[field] = forms.ChoiceField(choices=choices, widget=widget)

class MultipleChoiceFieldForm(forms.Form):
    def __init__(self, *args, **kwargs):
        field = kwargs.pop('field') if 'field' in kwargs else None
        choices = kwargs.pop('choices') if 'choices' in kwargs else []
        widget = kwargs.pop('widget') if 'widget' in kwargs else None
        super().__init__(*args, **kwargs)
        self.fields[field] = forms.MultipleChoiceField(choices=choices, widget=widget)
