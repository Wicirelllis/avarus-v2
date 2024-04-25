from apps.datasets.models import Dataset
from apps.map_locations.models import MapLocation
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Dataset)
def create_map_location(sender, instance, created, **kwargs):
    ''' Create corresponding map location on dataset creation '''
    if created:
        MapLocation.objects.create(name=instance.title, dataset=instance)
        # TOOO authors are not set bc it's m2m field and post_save don't track them
