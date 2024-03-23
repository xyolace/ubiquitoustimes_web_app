# Generated by Django 4.2.5 on 2024-01-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0018_nav_title_remove_nav_image_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='slider')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]