# Generated by Django 3.0.8 on 2021-05-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_applcontent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='applcontent',
            name='button_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='applcontent',
            name='load_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='applcontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
