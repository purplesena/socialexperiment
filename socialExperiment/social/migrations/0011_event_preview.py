# Generated by Django 4.0.4 on 2022-07-20 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_alter_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='preview',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
