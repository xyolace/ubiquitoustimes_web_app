# Generated by Django 4.2.5 on 2024-01-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0040_a3topfeatured_delete_a3topslider_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='A4NEWPOST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Text', models.TextField()),
                ('Image', models.ImageField(upload_to='New Post')),
            ],
        ),
        migrations.AlterField(
            model_name='a3topfeatured',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Top Featured'),
        ),
    ]
