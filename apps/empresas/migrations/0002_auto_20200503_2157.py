# Generated by Django 3.0.5 on 2020-05-04 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(help_text='Nome da Empresa', max_length=100),
        ),
    ]
