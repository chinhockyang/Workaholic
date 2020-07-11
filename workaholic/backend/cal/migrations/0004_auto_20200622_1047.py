# Generated by Django 3.0.6 on 2020-06-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20200614_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='label',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Meeting', 'Meeting'), ('Submission', 'Submission'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]