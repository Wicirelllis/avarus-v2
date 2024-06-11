# Generated by Django 5.0.4 on 2024-06-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Title of the project.', max_length=200, null=True)),
                ('url', models.URLField(blank=True, help_text='URL of the project.', null=True)),
                ('url_text', models.CharField(blank=True, help_text='Masking text for URL.', max_length=200, null=True)),
                ('short_description', models.TextField(blank=True, help_text='Short description that is displayed on the all-projects page.', max_length=1000)),
                ('long_description', models.TextField(blank=True, help_text="Long description that is discplayed on this project's page.")),
            ],
            options={
                'verbose_name': 'Related Project',
            },
        ),
    ]
