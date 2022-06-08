# Generated by Django 4.0.5 on 2022-06-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0007_remove_likes_unique_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='author',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(upload_to='image/'),
        ),
    ]