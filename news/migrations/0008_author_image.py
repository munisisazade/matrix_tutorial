# Generated by Django 2.0.4 on 2018-07-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180710_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]
