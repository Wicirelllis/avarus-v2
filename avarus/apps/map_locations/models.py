from apps.authors.models import Author
from apps.datasets.models import Dataset
from django.db import models


class MapLocation(models.Model):
    ''' Location that displayed on map. Each location belong to one dataset, but in the future it is possible that one dataset will have multiple locations '''
    name = models.CharField('Location name', max_length=120, null=True)
    dataset = models.ForeignKey(Dataset, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Location'
