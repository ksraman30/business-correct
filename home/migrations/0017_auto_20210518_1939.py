# Generated by Django 3.0.8 on 2021-05-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210512_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselcontent',
            name='main_text',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='main_text',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='subtitle_text',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]