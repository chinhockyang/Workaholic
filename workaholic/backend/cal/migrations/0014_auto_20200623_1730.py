# Generated by Django 3.0.6 on 2020-06-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0013_auto_20200623_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
    ]
