# Generated by Django 4.2.5 on 2024-01-19 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0026_a2_navbar_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='A3_NAVBAR_MAIN_LINKS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='a1_top_header_right',
            name='Link',
            field=models.URLField(default='/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='a2_navbar_title',
            name='Link',
            field=models.URLField(default='/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='A3_NAVBAR_DROPDOWN_LINKS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('main_nav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dropdown_menus', to='xyolace_app.a3_navbar_main_links')),
            ],
        ),
        migrations.CreateModel(
            name='A3_NAVBAR_DEEPDROPDOWN_LINKS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('dropdown_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deep_dropdown_menus', to='xyolace_app.a3_navbar_dropdown_links')),
            ],
        ),
    ]