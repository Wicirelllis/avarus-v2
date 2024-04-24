from apps.authors.models import Author
from apps.datasets.parse import ParseDataset
from apps.publications.models import Publication
from django.db import models
from django.urls import reverse


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
    disturban = models.JSONField(blank=True, null=True, default=dict)
    position = models.JSONField(blank=True, null=True, default=dict)
    soil_text = models.JSONField(blank=True, null=True, default=dict)
    ecotope = models.JSONField(blank=True, null=True, default=dict)
    phytocoenosis = models.JSONField(blank=True, null=True, default=dict)
    phytocoenosis_cover = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dataset-detail', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        ''' Overrie save method to automatically generate ddescription of dataset '''
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
            'cryptogam'
        ]
        ParseDataset(self).fill_fields(fields)
        super(Dataset, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Dataset'
