# Generated by Django 3.2.8 on 2021-11-03 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_auto_20211102_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='mail',
        ),
    ]
