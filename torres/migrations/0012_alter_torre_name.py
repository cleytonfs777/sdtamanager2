# Generated by Django 4.1.6 on 2023-02-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torres', '0011_alter_torre_energia_cedida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='name',
            field=models.CharField(max_length=25, verbose_name='nome'),
        ),
    ]