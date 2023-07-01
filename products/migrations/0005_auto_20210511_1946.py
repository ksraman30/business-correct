# Generated by Django 3.0.8 on 2021-05-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200825_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='content_loc',
            field=models.CharField(choices=[('AboutContent', 'About'), ('HomeCarousel', 'Carousel'), ('HomeMarketing', 'Marketing'), ('ProductContent', 'Products'), ('CertContent', 'Certification')], default='HomeMarketing', max_length=100),
        ),
    ]
