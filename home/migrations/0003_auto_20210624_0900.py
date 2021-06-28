# Generated by Django 3.2 on 2021-06-24 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210624_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddata',
            name='disc',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='adddata',
            name='image',
            field=models.FileField(default='', max_length=255, upload_to=''),
        ),
        migrations.AddField(
            model_name='adddata',
            name='place',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='adddata',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]