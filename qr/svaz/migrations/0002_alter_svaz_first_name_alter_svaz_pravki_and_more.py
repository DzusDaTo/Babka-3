# Generated by Django 4.0.3 on 2022-10-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svaz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svaz',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='svaz',
            name='pravki',
            field=models.TextField(max_length=1000, verbose_name='Предложенные правки'),
        ),
        migrations.AlterField(
            model_name='svaz',
            name='sposob',
            field=models.CharField(max_length=100, verbose_name='Способ обратной связи'),
        ),
    ]
