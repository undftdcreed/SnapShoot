# Generated by Django 4.2.3 on 2023-07-18 21:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_owner_listing_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_confirmed',
        ),
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_app.listing'),
        ),
        migrations.AddField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]