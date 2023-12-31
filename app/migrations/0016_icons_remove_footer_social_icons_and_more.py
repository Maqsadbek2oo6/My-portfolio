# Generated by Django 4.2.5 on 2023-09-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_powered_by_footer_company_footer_company_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_icons', models.CharField(max_length=128)),
                ('social_icons_link', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='social_icons',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='social_icons_link',
        ),
    ]
