# Generated by Django 5.0.3 on 2024-08-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_alter_articles_imagealaune_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
