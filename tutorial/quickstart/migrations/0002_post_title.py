# Generated by Django 3.2.6 on 2021-10-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
