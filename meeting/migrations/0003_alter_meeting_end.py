# Generated by Django 4.2 on 2024-01-03 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_news_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
