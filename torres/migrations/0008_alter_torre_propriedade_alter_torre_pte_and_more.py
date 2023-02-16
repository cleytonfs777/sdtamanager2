# Generated by Django 4.1.6 on 2023-02-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torres', '0007_alter_torre_resp_nome_alter_torre_resp_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='propriedade',
            field=models.CharField(max_length=90, verbose_name='propriedade'),
        ),
        migrations.AlterField(
            model_name='torre',
            name='pte',
            field=models.CharField(max_length=15, verbose_name='projeto_tecnico_executivo'),
        ),
        migrations.AlterField(
            model_name='torre',
            name='seguranca',
            field=models.CharField(max_length=180, verbose_name='seguranca'),
        ),
    ]
