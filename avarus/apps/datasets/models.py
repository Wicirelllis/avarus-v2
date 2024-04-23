from django.db import models
from django.urls import reverse

from apps.publications.models import Publication
from apps.authors.models import Author

import pandas as pd
import os
import json

from django.contrib.postgres.fields import JSONField

from apps.datasets.parse import ParseDataset


class Dataset(models.Model):
    LOAN_STATUS = (
        ('pu', 'Public'),
        ('pr', 'Private')
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book", blank=True)

    env = models.FileField(upload_to='datasets/env/', blank=True)
    spp = models.FileField(upload_to='datasets/spp/', blank=True)

    dataset = models.CharField(max_length=200, blank=True)
    dataset_env = models.CharField(blank=True, max_length=200)
    status = models.CharField(max_length=5, choices=LOAN_STATUS, blank=True, default='pr', help_text='Book availability')
    image = models.ImageField(upload_to='datasets/img/', blank=True)

    authors = models.ManyToManyField(Author, related_name='datasets', null=True, blank=True)
    publications = models.ManyToManyField(Publication, related_name='datasets', null=True, blank=True)

    name = models.CharField(max_length=200, blank=True, null=True, help_text='Name of dataset', verbose_name='Verbose')
    year = models.CharField(max_length=200, blank=True, null=True, help_text='Year of creation')
    n_plots = models.CharField(max_length=200, blank=True, null=True, help_text='Number of plots')
    coverscale = models.CharField(max_length=200, blank=True, null=True, help_text='')
    coordinates = models.CharField(max_length=200, blank=True, null=True, help_text='Key site coordinates')
    geotagged = models.CharField(max_length=200, blank=True, null=True, help_text='')
    region = models.CharField(max_length=200, blank=True, null=True, help_text='')
    location = models.CharField(max_length=200, blank=True, null=True, help_text='')
    subzone = models.CharField(max_length=200, blank=True, null=True, help_text='')
    permafrost_type = models.CharField(max_length=200, blank=True, null=True, help_text='')
    permafrost_data = models.CharField(max_length=200, blank=True, null=True, help_text='')
    additional_data = models.CharField(max_length=200, blank=True, null=True, help_text='')
    mosses = models.CharField(max_length=200, blank=True, null=True, help_text='')
    liverworts = models.CharField(max_length=200, blank=True, null=True, help_text='')
    liches = models.CharField(max_length=200, blank=True, null=True, help_text='')
    vascular = models.CharField(max_length=200, blank=True, null=True, help_text='')
    cryptogam = models.CharField(max_length=200, blank=True, null=True, help_text='')

    # data for charts
    disturban = JSONField(blank=True, default={})
    position = JSONField(blank=True, default={})
    soil_text = JSONField(blank=True, default={})

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dataset-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Dataset'

    
    def save(self, *args, **kwargs):
        super(Dataset, self).save(*args, **kwargs)
        parse = ParseDataset(self)
        if not self.n_plots:
            parse._fill_n_plots()
        if not self.disturban:
            parse._fill_disturban()
        if not self.position:
            parse._fill_position()
        if not self.soil_text:
            parse._fill_soil_text()
        if not self.year:
            parse._fill_year()
        if not self.coverscale:
            parse._fill_coverscale()
        if not self.region:
            parse._fill_region()
        if not self.location:
            parse._fill_location()
        if not self.subzone:
            parse._fill_subzone()
        if not self.mosses:
            parse._fill_mosses()
        if not self.liverworts:
            parse._fill_liverworts()
        if not self.liches:
            parse._fill_liches()
        if not self.vascular:
            parse._fill_vascular()
        if not self.cryptogam:
            parse._fill_cryptogam()

        super(Dataset, self).save(*args, **kwargs)
