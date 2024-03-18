# Generated by Django 4.2.5 on 2024-01-31 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0052_b3othernews'),
    ]

    operations = [
        migrations.CreateModel(
            name='B4POPULARNEWS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Text', models.TextField()),
                ('Image', models.ImageField(upload_to='Popular News')),
            ],
        ),
        migrations.CreateModel(
            name='B5TRENDINGTAGS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='B6STOREADS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Text', models.TextField()),
                ('Image', models.ImageField(upload_to='Popular News')),
            ],
        ),
    ]