# Generated by Django 4.2.5 on 2024-01-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0016_alter_nav_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav_image',
            name='image',
            field=models.ImageField(upload_to='navlogo'),
        ),
    ]
