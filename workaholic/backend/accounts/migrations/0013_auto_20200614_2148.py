# Generated by Django 3.0.6 on 2020-06-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200614_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='board_last_modified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='cal_last_modified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_modified',
            field=models.DateTimeField(null=True),
        ),
    ]
