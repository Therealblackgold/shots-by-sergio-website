# Generated by Django 3.1.5 on 2021-01-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_post_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
