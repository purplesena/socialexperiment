# Generated by Django 4.0.4 on 2022-07-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_event_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pronouns',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]