# Generated by Django 2.2.1 on 2019-05-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.jpeg', upload_to='images/'),
        ),
    ]
