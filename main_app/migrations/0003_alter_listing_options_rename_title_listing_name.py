# Generated by Django 4.2.3 on 2023-07-12 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_listing_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='title',
            new_name='name',
        ),
    ]
