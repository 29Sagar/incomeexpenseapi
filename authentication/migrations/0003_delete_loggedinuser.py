# Generated by Django 4.0.4 on 2022-05-11 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_loggedinuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoggedInUser',
        ),
    ]
