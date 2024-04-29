from apps.datasets.models import Dataset, DatasetRequest
from apps.map_locations.models import MapLocation
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Dataset)
def create_map_location(sender, instance, created, **kwargs):
    ''' Create corresponding map location on dataset creation '''
    if created:
        MapLocation.objects.create(name=instance.title, dataset=instance)
        # TOOO authors are not set bc it's m2m field and post_save don't track them

@receiver(post_save, sender=DatasetRequest)
def update_available_to(sender, instance, created, **kwargs):
    ''' Update available_to when status of request changes '''
    if instance.status == 'g':
        instance.dataset.available_to.add(instance.user)
    elif instance.status == 'd':
        instance.dataset.available_to.remove(instance.user)
