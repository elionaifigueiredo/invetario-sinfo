# Generated by Django 4.0.2 on 2022-04-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_alter_material_bmp_alter_material_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='bmp',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='material',
            name='serie',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
