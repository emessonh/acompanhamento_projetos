# Generated by Django 4.2.7 on 2024-02-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_alter_projeto_link_alter_projeto_prazo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='ano_desenvolvimento',
            field=models.CharField(default=2024),
            preserve_default=False,
        ),
    ]