from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('organization'))
    position = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('position'))
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, verbose_name=_('photo'))

    def __str__(self):
        return f'{self.user} ({self.organization})'
