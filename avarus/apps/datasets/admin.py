from django.contrib import admin

from .models import Dataset, DatasetRequest


class DatasetAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'description': 'Main fields. While they are optional it is recommended to fill them.',
                'fields': [
                    'title',
                    'summary',
                    'env',
                    'spp',
                    'download_url',
                    'image',
                    'authors',
                    'publications',
                    'status',
                    'permafrost_type',
                    'permafrost_data',
                    'additional_data',
                    'available_to',
                ],
            },
        ),
        (
            'Optional fields',
            {
                'description': 'Fields below autofill based on dataset files content. But feel free to fill / edit if necessities arise.',
                'classes': [
                    'collapse',
                ],
                'fields': [
                    'year',
                    'n_plots',
                    'coverscale',
                    'longitude',
                    'latitude',
                    'geotagged',
                    'region',
                    'location',
                    'subzone',
                    'mosses',
                    'liverworts',
                    'liches',
                    'vascular',
                    'cryptogam'
                ],
            },
        ),
    ]

admin.site.register(Dataset, DatasetAdmin)
admin.site.register(DatasetRequest)
