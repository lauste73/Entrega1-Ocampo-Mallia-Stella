# Generated by Django 4.1.2 on 2022-11-03 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0009_publicacion_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='avatar',
        ),
    ]