# Generated by Django 5.1 on 2024-08-21 01:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='contenu',
            field=ckeditor.fields.RichTextField(),
        ),
    ]