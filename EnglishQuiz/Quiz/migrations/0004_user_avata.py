# Generated by Django 3.2.8 on 2021-10-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avata',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]