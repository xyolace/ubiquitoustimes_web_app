# Generated by Django 4.2.5 on 2024-02-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0078_a1navbar_link_href'),
    ]

    operations = [
        migrations.AddField(
            model_name='a1navbar',
            name='Tag_line',
            field=models.CharField(default='INFO AROUND', max_length=50),
            preserve_default=False,
        ),
    ]
