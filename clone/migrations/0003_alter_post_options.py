# Generated by Django 4.0.5 on 2022-06-05 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
