# Generated by Django 4.1.6 on 2023-02-15 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torres', '0008_alter_torre_propriedade_alter_torre_pte_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='description',
            field=models.CharField(max_length=2000, verbose_name='descricao'),
        ),
    ]
