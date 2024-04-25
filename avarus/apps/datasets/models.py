from apps.authors.models import Author
from apps.datasets.parse import ParseDataset
from apps.publications.models import Publication
from django.db import models
from django.urls import reverse

LOAN_STATUS = (
    ('pu', 'Public'),
    ('pr', 'Private')
)


class Dataset(models.Model):
    title = models.CharField(max_length=200, blank=True)
    summary = models.TextField(help_text="A brief description of the dataset.", blank=True)

    env = models.FileField(upload_to='datasets/env/', blank=True)
    spp = models.FileField(upload_to='datasets/spp/', blank=True)
    image = models.ImageField(upload_to='datasets/img/', blank=True)

    authors = models.ManyToManyField(Author, related_name='datasets', blank=True)
    publications = models.ManyToManyField(Publication, related_name='datasets', blank=True)

    status = models.CharField(max_length=5, choices=LOAN_STATUS, blank=True, default='pr', help_text='Availability.')
    permafrost_type = models.CharField(max_length=200, blank=True, help_text='')
    permafrost_data = models.CharField(max_length=200, blank=True, help_text='')
    additional_data = models.TextField(blank=True, help_text='Any additional info related to dataset.')


    year = models.CharField(max_length=200, blank=True, help_text='Year of creation')
    n_plots = models.CharField(max_length=200, blank=True, help_text='Number of plots')
    coverscale = models.CharField(max_length=200, blank=True, help_text='')
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geotagged = models.CharField(max_length=200, blank=True, help_text='')
    region = models.CharField(max_length=200, blank=True, help_text='')
    location = models.CharField(max_length=200, blank=True, help_text='')
    subzone = models.CharField(max_length=200, blank=True, help_text='')
    mosses = models.CharField(max_length=200, blank=True, help_text='')
    liverworts = models.CharField(max_length=200, blank=True, help_text='')
    liches = models.CharField(max_length=200, blank=True, help_text='')
    vascular = models.CharField(max_length=200, blank=True, help_text='')
    cryptogam = models.CharField(max_length=200, blank=True, help_text='')

    # data for charts
    disturban = models.JSONField(blank=True, default=dict)
    position = models.JSONField(blank=True, default=dict)
    soil_text = models.JSONField(blank=True, default=dict)
    ecotope = models.JSONField(blank=True, default=dict)
    phytocoenosis = models.JSONField(blank=True, default=dict)
    phytocoenosis_cover = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dataset-detail', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        ''' Overrie save method to automatically generate description of dataset '''
        super(Dataset, self).save(*args, **kwargs)
        fields = [
            'n_plots',
            'disturban',
            'position',
            'ecotope',
            'phytocoenosis',
            'phytocoenosis_cover',
            'soil_text',
            'year',
            'coverscale',
            'region',
            'location',
            'subzone',
            'mosses',
            'liverworts',
            'liches',
            'vascular',
            'cryptogam',
            'latitude',
            'longitude',
        ]
        ParseDataset(self).fill_fields(fields)
        super(Dataset, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Dataset'
