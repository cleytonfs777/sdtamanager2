# Generated by Django 4.1.6 on 2023-02-15 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torres', '0014_alter_torre_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torre',
            name='description',
        ),
    ]