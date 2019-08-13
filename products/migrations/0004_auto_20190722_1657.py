# Generated by Django 2.2.2 on 2019-07-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190722_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='model_id',
            new_name='ph_id',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='model_id',
        ),
        migrations.AddField(
            model_name='laptop',
            name='lap_id',
            field=models.CharField(default='180', max_length=5),
        ),
    ]
