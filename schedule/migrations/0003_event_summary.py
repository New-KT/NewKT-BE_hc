# Generated by Django 4.2 on 2024-01-03 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
