from django.db import models


class Feedback(models.Model):
    name = models.CharField(blank=True)
    email = models.EmailField(blank=True)
    feedback = models.TextField()

    class Meta:
        verbose_name = 'Feedback'
