# Generated by Django 3.0.6 on 2020-07-17 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20200711_1039'),
        ('cal', '0019_auto_20200711_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='todo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.Todo'),
        ),
    ]
