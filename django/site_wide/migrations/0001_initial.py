# Generated by Django 2.1.2 on 2018-10-20 19:52

from django.db import migrations, models
import site_wide.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=site_wide.models.image_upload_path_handler)),
            ],
        ),
    ]