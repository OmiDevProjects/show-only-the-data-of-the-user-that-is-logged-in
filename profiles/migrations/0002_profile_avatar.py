# Generated by Django 3.0.8 on 2022-02-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='Profile'),
        ),
    ]
