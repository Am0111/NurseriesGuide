# Generated by Django 5.1 on 2024-08-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurseries', '0006_nursery_commercial_registry_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursery',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
