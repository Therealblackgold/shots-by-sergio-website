# Generated by Django 3.1.5 on 2021-01-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210129_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('pintrerest_url', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
