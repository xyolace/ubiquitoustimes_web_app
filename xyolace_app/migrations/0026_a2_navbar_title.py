# Generated by Django 4.2.5 on 2024-01-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0025_a2_navbar_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='A2_NAVBAR_TITLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Link', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
