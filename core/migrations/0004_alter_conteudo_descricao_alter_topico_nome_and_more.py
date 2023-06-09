# Generated by Django 4.0.1 on 2022-10-31 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_conteudo_topico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudo',
            name='descricao',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='topico',
            name='nome',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='topico',
            name='ordem',
            field=models.IntegerField(blank=True),
        ),
    ]
