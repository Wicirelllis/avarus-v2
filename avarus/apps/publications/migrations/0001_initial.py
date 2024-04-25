# Generated by Django 3.2.25 on 2024-04-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Title of the publication.', max_length=200, null=True)),
                ('abstract', models.TextField(blank=True, help_text='Abstract')),
                ('DOI', models.CharField(blank=True, max_length=200, null=True)),
                ('URL', models.URLField(blank=True, null=True)),
                ('authors', models.ManyToManyField(related_name='publications', to='authors.Author')),
            ],
            options={
                'verbose_name': 'Publication',
            },
        ),
    ]
