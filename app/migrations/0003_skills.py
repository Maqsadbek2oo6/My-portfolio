# Generated by Django 4.2.5 on 2023-09-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_detals_alter_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_skill', models.CharField(max_length=32)),
                ('direction_name', models.CharField(max_length=32)),
                ('percent', models.CharField(max_length=32)),
            ],
        ),
    ]
