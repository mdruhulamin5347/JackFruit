# Generated by Django 5.0.2 on 2024-02-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_profile_update_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_update',
            name='image',
            field=models.ImageField(default='profile/default.png', upload_to='profile/'),
        ),
    ]