# Generated by Django 4.2.6 on 2023-10-23 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0002_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='curriculo',
            field=models.ImageField(upload_to='static/ofertas/img'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='static/ofertas/img'),
        ),
    ]
