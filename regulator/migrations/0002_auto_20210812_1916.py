# Generated by Django 3.2.6 on 2021-08-12 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regulator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='inserted_at',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='updated_at',
        ),
    ]
