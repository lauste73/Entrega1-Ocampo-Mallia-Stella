# Generated by Django 4.1.2 on 2022-10-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('chasis', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('kilometros', models.IntegerField()),
            ],
        ),
    ]
