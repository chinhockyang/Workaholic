# Generated by Django 3.0.6 on 2020-07-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
