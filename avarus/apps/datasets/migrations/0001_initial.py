# Generated by Django 3.2.25 on 2024-04-22 00:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('summary', models.TextField(blank=True, help_text='Enter a brief description of the book', max_length=1000)),
                ('env', models.FileField(blank=True, upload_to='')),
                ('spp', models.FileField(blank=True, upload_to='')),
                ('dataset', models.CharField(blank=True, max_length=200)),
                ('dataset_env', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(blank=True, choices=[('pu', 'Public'), ('pr', 'Private')], default='pr', help_text='Book availability', max_length=5)),
                ('image', models.ImageField(blank=True, upload_to='img/')),
                ('name', models.CharField(blank=True, help_text='Name of dataset', max_length=200, null=True, verbose_name='Verbose')),
                ('year', models.CharField(blank=True, help_text='Year of creation', max_length=200, null=True)),
                ('n_plots', models.CharField(blank=True, help_text='Number of plots', max_length=200, null=True)),
                ('coverscale', models.CharField(blank=True, max_length=200, null=True)),
                ('coordinates', models.CharField(blank=True, help_text='Key site coordinates', max_length=200, null=True)),
                ('geotagged', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('subzone', models.CharField(blank=True, max_length=200, null=True)),
                ('permafrost_type', models.CharField(blank=True, max_length=200, null=True)),
                ('permafrost_data', models.CharField(blank=True, max_length=200, null=True)),
                ('additional_data', models.CharField(blank=True, max_length=200, null=True)),
                ('mosses', models.CharField(blank=True, max_length=200, null=True)),
                ('liverworts', models.CharField(blank=True, max_length=200, null=True)),
                ('liches', models.CharField(blank=True, max_length=200, null=True)),
                ('vascular', models.CharField(blank=True, max_length=200, null=True)),
                ('cryptogam', models.CharField(blank=True, max_length=200, null=True)),
                ('disturban', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('position', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('soil_text', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('authors', models.ManyToManyField(blank=True, null=True, related_name='datasets', to='authors.Author')),
                ('publications', models.ManyToManyField(related_name='datasets', to='publications.Publication')),
            ],
            options={
                'verbose_name': 'Dataset',
            },
        ),
    ]
