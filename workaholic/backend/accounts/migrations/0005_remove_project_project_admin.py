# Generated by Django 3.0.6 on 2020-05-28 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_project_project_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_admin',
        ),
    ]
