from django.db import models
from django.urls import reverse

from apps.authors.models import Author

class Publication(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, help_text='Title of the publication.')
    abstract = models.TextField(help_text="Abstract", blank=True)
    DOI = models.CharField(max_length=200, blank=True, null=True)
    URL = models.URLField(max_length=200, blank=True, null=True)

    authors = models.ManyToManyField(Author, related_name='publications')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Publication'
