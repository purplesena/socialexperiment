# Generated by Django 4.0.4 on 2022-10-06 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_post_dislikes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='uploads/event_images/default.jpg', upload_to='uploads/event_images'),
        ),
    ]
