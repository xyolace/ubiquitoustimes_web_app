# Generated by Django 4.2.5 on 2024-02-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0060_b9subscibenews'),
    ]

    operations = [
        migrations.CreateModel(
            name='B9SUBSCRIBENEWS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Text', models.TextField()),
                ('Button', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='B9SUBSCIBENEWS',
        ),
    ]