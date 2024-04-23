from django.db import models
from django.urls import reverse

from apps.publications.models import Publication
from apps.authors.models import Author
from apps.datasets.models import Dataset

import pandas as pd
import os
import json

from django.contrib.postgres.fields import JSONField


class MapLocation(models.Model):
    ''' Location that displayed on map. Each locatio belong to one dataset, but in the future it is possible that one dataset will have multiple locations '''
    name = models.CharField('Location name', max_length=120, null=True)
    num = models.CharField('Number', max_length=120, null=True)
    authors = models.CharField('Authors', max_length=120, null=True)
    longitude = models.CharField('Longitude', max_length=120, null=True)
    latitude = models.CharField('Latitude', max_length=120, null=True)
    photo = models.FileField(upload_to='pictures', blank=True)
    url_photo = models.CharField('URL photo', max_length=120, null=True)
    url_page = models.CharField('URL page', max_length=120, null=True)
    plots = models.CharField('Number of plots', max_length=120, null=True)

    # name = models.CharField('Location name', max_length=120, null=True)
    # authors = models.CharField('Authors', max_length=120, null=True)
    # longitude = models.FloatField('Longitude', null=True)
    # latitude = models.FloatField('Latitude', null=True)
    # dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)

    # photo = models.FileField(upload_to='pictures', blank=True)
    # url_photo = models.CharField('URL photo', max_length=120, null=True)
    # url_page = models.CharField('URL page', max_length=120, null=True)
    # plots = models.CharField('Number of plots', max_length=120, null=True)
    # num = models.CharField('Number', max_length=120, null=True)

    def get_absolute_url(self):
        return ""

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Location'
