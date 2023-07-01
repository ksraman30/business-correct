# Generated by Django 3.0.8 on 2021-05-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(blank=True, max_length=100)),
                ('main_text', models.CharField(blank=True, max_length=2000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('subtitle_text', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
