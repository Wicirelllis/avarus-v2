from django.db import models
from django.urls import reverse

from apps.authors.models import Author
from apps.datasets.models import Dataset

from apps.datasets.models import Dataset


class MapLocation(models.Model):
    ''' Location that displayed on map. Each location belong to one dataset, but in the future it is possible that one dataset will have multiple locations '''
    name = models.CharField('Location name', max_length=120, null=True)
    dataset = models.ForeignKey(Dataset, null=True, blank=True, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='map_locationsq', null=True, blank=True)


    def get_absolute_url(self):
        return ""

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Location'
