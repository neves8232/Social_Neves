# Generated by Django 4.2.2 on 2023-07-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_post_no_of_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank_profile.png', upload_to='profile_images'),
        ),
    ]
