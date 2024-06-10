from apps.feedback.models import Feedback
from django import forms
from django.utils.translation import gettext_lazy as _


class FeedbackForm(forms.ModelForm):
     class Meta:
          model = Feedback
          fields = ['name', 'email', 'feedback']
          labels = {
               'name': _('Name'),
               'email': _('Email'),
               'feedback': _('Feedback')
          }
          # help_texts = {
          #      'name': _('Some useful help text.'),
          #      'email': _('Email'),
          #      'feedback': _('Feedback')
          # }
