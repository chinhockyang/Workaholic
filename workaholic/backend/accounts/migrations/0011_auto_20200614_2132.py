# Generated by Django 3.0.6 on 2020-06-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_project_calendar_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='calendar_month',
            field=models.DateTimeField(),
        ),
    ]
