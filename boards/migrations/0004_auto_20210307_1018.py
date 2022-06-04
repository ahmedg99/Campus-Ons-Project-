# Generated by Django 3.1.6 on 2021-03-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20210306_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_dt',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='post',
            name='distance',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='nbchambre',
            field=models.TextField(default='Test', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='surface',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(default='Test', max_length=250),
        ),
    ]