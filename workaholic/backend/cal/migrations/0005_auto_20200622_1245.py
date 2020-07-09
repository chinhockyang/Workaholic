# Generated by Django 3.0.6 on 2020-06-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0004_auto_20200622_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='label',
            field=models.CharField(choices=[('Meeting', 'Meeting'), ('Submission', 'Submission'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]