# Generated by Django 5.0.4 on 2024-07-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0004_rename_date_completed_project_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certification',
            name='date_issued',
        ),
        migrations.AddField(
            model_name='certification',
            name='date',
            field=models.TextField(blank=True, null=True),
        ),
    ]