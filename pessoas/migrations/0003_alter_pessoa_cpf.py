# Generated by Django 4.2.7 on 2024-01-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_pessoa_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(default=0, max_length=11, unique=True),
        ),
    ]
