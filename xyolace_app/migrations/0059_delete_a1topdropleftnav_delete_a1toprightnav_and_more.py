# Generated by Django 4.2.5 on 2024-02-03 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xyolace_app', '0058_remove_a1topdropleftnav_dropdown_menu_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='A1TOPDROPLEFTNAV',
        ),
        migrations.DeleteModel(
            name='A1TOPRIGHTNAV',
        ),
        migrations.RemoveField(
            model_name='a2maindropitems',
            name='dropdown_menu',
        ),
        migrations.DeleteModel(
            name='A2MAINNAV',
        ),
        migrations.DeleteModel(
            name='A2MAINNAVAFTER',
        ),
        migrations.DeleteModel(
            name='A2NAVLOGO',
        ),
        migrations.DeleteModel(
            name='A2NAVTITLE',
        ),
        migrations.DeleteModel(
            name='A2MAINDROPITEMS',
        ),
        migrations.DeleteModel(
            name='A2MAINDROPNAV',
        ),
    ]
