# Generated by Django 2.2 on 2023-03-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.png', upload_to='profile_pictures'),
        ),
    ]
