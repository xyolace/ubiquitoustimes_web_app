# Generated by Django 4.2.5 on 2024-01-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0053_b4popularnews_b5trendingtags_b6storeads'),
    ]

    operations = [
        migrations.CreateModel(
            name='B7BOTTOMNAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, null=True)),
                ('Link', models.URLField(default=None)),
            ],
        ),
    ]