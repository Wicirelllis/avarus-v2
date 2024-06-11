# Generated by Django 5.0.4 on 2024-06-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('feedback', models.TextField()),
            ],
            options={
                'verbose_name': 'Feedback',
            },
        ),
    ]
