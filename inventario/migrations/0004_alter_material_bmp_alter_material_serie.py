# Generated by Django 4.0.2 on 2022-04-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_material_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='bmp',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='material',
            name='serie',
            field=models.CharField(max_length=30),
        ),
    ]