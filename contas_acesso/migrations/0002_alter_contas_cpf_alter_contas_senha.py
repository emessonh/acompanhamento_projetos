# Generated by Django 4.2.7 on 2024-01-11 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0003_alter_pessoa_cpf'),
        ('contas_acesso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='cpf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, serialize=False, to='pessoas.pessoa', to_field='cpf'),
        ),
        migrations.AlterField(
            model_name='contas',
            name='senha',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
