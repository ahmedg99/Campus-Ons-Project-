# Generated by Django 3.1.7 on 2021-03-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0015_auto_20210324_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='photo',
            field=models.ImageField(upload_to='annonce/'),
        ),
    ]