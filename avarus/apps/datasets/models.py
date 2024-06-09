from apps.authors.models import Author
from apps.datasets.parse import ParseDataset
from apps.datasets.utils import _read_env, _read_spp
from apps.datasets.validators import env_validator
from apps.publications.models import Publication
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

LOAN_STATUS = (
    ('pu', 'Public'),
    ('pr', 'Private')
)


class Dataset(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text="A brief description of the dataset.", blank=True)

    env = models.FileField(upload_to='datasets/env/', validators=[env_validator])
    spp = models.FileField(upload_to='datasets/spp/', blank=True)
    image = models.ImageField(upload_to='datasets/img/', blank=True)
    download_url = models.URLField('Download link', blank=True)

    authors = models.ManyToManyField(Author, related_name='datasets', blank=True)
    publications = models.ManyToManyField(Publication, related_name='datasets', blank=True)

    status = models.CharField(max_length=5, choices=LOAN_STATUS, blank=True, default='pr', help_text='Availability.')
    permafrost_type = models.CharField(max_length=200, blank=True, help_text='')
    permafrost_data = models.CharField(max_length=200, blank=True, help_text='')
    additional_data = models.TextField(blank=True, help_text='Any additional info related to dataset.')

    available_to = models.ManyToManyField(User, related_name='available_datasets', blank=True)

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

    # statistics
    species_total = models.IntegerField(default=0)
    species_liches = models.IntegerField(default=0)
    species_liverworts = models.IntegerField(default=0)
    species_mosses = models.IntegerField(default=0)
    species_vascular = models.IntegerField(default=0)
    species_unknown = models.IntegerField(default=0)

    def get_col_names(self):
        return _read_spp(self.spp.path).columns.values

    def get_spp_rows(self):
        return _read_spp(self.spp.path)['PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)']

    def get_spp_cols(self):
        return _read_spp(self.spp.path).columns.values

    def get_env_rows(self):
        return _read_env(self.env.path)['FIELD_NR']

    def get_env_cols(self):
        return _read_env(self.env.path).columns.values

    def get_env_numeric_cols(self):
        return _read_env(self.env.path).columns.values

    def get_env_col_values(self, col: str) -> set:
        return set(_read_env(self.env.path)[col])


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
            'species_total',
            'species_liches',
            'species_liverworts',
            'species_mosses',
            'species_vascular',
            'species_unknown',
        ]
        ParseDataset(self).fill_fields(fields)
        super(Dataset, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Dataset'


ACCESS_STATUS = (
    ('g', 'Granted'),
    ('r', 'In review'),
    ('d', 'Denied')
)

class DatasetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, help_text='User that requested access')
    dataset = models.ForeignKey(Dataset, on_delete=models.PROTECT)
    name = models.CharField('Name', max_length=120)
    organization = models.CharField('Organization', max_length=120)
    position = models.CharField('Position', max_length=120)
    email = models.EmailField('Email', max_length=120)
    purpose = models.TextField('Purpose')
    status = models.CharField(max_length=1, choices=ACCESS_STATUS, blank=True, default='r')


    class Meta:
        verbose_name = 'Dataset access request'

    def __str__(self):
        return f'{self.dataset} | {self.user}'
