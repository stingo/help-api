# Generated by Django 5.1.7 on 2025-04-01 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upfrica_backend', '0003_helparticle_category_alter_helparticle_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpcategory',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
