# Generated by Django 4.0.2 on 2022-04-12 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solucionador',
            fields=[
                ('data_termino', models.DateTimeField(auto_created=True)),
                ('data_inicio', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'solucionador',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('R', 'Resolvido'), ('C', 'Cancelado'), ('P', 'Processando')], max_length=1)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Chamados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('militar', models.CharField(max_length=30)),
                ('contato', models.CharField(max_length=11)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
                ('from_email', models.CharField(max_length=250)),
                ('recipient_list', models.CharField(max_length=250)),
                ('solucionador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chamados.solucionador')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chamados.status')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chamados',
            },
        ),
    ]