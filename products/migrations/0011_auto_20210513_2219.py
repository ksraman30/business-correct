# Generated by Django 3.0.8 on 2021-05-13 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productcontent_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ButtonContent',
            new_name='ProductButton',
        ),
    ]
