# Generated by Django 3.1.5 on 2021-02-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210213_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.CharField(default=0, max_length=10),
        ),
    ]