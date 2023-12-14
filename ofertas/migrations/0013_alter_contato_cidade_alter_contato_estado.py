# Generated by Django 4.2.6 on 2023-12-14 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0012_cidade_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='cidade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ofertas.cidade'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='estado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ofertas.estado'),
        ),
    ]
