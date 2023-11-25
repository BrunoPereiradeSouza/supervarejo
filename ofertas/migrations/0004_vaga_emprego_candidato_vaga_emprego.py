# Generated by Django 4.2.6 on 2023-11-21 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0003_alter_candidato_curriculo_alter_produto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga_emprego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vaga', models.CharField(max_length=50)),
                ('carga_horaria', models.FloatField()),
                ('salario', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='candidato',
            name='vaga_emprego',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ofertas.vaga_emprego'),
        ),
    ]
