# Generated by Django 4.2 on 2024-01-05 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0007_delete_meetingdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='summary',
            new_name='news_summary',
        ),
    ]
