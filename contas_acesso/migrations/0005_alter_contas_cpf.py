# Generated by Django 4.2.7 on 2024-01-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas_acesso', '0004_alter_contas_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
