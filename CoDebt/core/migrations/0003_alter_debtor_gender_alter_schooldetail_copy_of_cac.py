# Generated by Django 4.0.6 on 2022-08-12 06:04

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_debtor_student_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtor',
            name='gender',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='schooldetail',
            name='copy_of_CAC',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='proof_of_CAC'),
        ),
    ]
