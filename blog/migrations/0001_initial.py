# Generated by Django 4.1.4 on 2023-01-11 11:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imagefields', models.FileField(upload_to='images/')),
                ('describe', ckeditor.fields.RichTextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
