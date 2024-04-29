from apps.datasets.models import DatasetRequest
from django import forms
from django.utils.translation import gettext_lazy as _


class DatasetRequestForm(forms.ModelForm):
     class Meta:
          model = DatasetRequest
          fields = ['name', 'organization', 'position', 'email', 'purpose', 'dataset', 'user']
          widgets = {
               'purpose': forms.Textarea(attrs={'placeholder': "Please describe your plans for using the data"}),
               'dataset': forms.HiddenInput(),
               'user': forms.HiddenInput(),
          }
