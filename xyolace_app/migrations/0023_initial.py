# Generated by Django 4.2.5 on 2024-01-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xyolace_app', '0022_delete_basic_nav_remove_drop_nav_items_navbar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='A0_PAGE_LOGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Page_Logo')),
            ],
        ),
        migrations.CreateModel(
            name='A0_PAGE_TITLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='A1_TOP_HEADER_RIGHT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
            ],
        ),
    ]
