# Generated by Django 4.0.3 on 2022-10-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0002_alter_video_options_video_is_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
    ]