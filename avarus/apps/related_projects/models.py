from django.db import models
from django.urls import reverse

from apps.authors.models import Author

class RelatedProject(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, help_text='Title of the project.')
    url = models.URLField(max_length=200, blank=True, null=True, help_text='URL of the project.')
    url_text = models.CharField(max_length=200, blank=True, null=True, help_text='Masking text for URL.')
    short_description = models.TextField(max_length=1000, blank=True, help_text='Short description that is displayed on the all-projects page.')
    long_description = models.TextField(blank=True, help_text='Long description that is discplayed on this project\'s page.')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('related-project-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Related Project'
