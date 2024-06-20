from django.contrib import admin

from .models import Dataset, DatasetRequest
from .parse import ParseDataset


class DatasetAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'description': 'Main fields. While they are optional it is recommended to fill them.',
                'fields': [
                    'in_preparation',
                    'title',
                    'summary',
                    'number',
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
    list_display = ['__str__', 'status', 'in_preparation']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.in_preparation:
            return
        if 'env' in form.changed_data:
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
            ParseDataset(obj).fill_fields(fields)
            super().save_model(request, obj, form, change)
        if 'spp' in form.changed_data:
            # currently there are no fields that are computed based on spp-file
            pass

admin.site.register(Dataset, DatasetAdmin)
admin.site.register(DatasetRequest)
