# Generated by Django 4.0.2 on 2022-03-31 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repre',
            name='vFname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='repre',
            name='vLname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
