# Generated by Django 3.0.5 on 2020-06-21 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20200621_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dna',
            name='dna',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]