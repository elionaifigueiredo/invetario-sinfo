# Generated by Django 4.0.2 on 2022-04-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_material_bmp_alter_material_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
