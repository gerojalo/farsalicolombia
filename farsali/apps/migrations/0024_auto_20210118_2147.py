# Generated by Django 3.1.3 on 2021-01-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0023_auto_20210118_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constante',
            name='nombre',
            field=models.CharField(choices=[('None', 'Ninguno'), ('contacto_email', 'Email'), ('contacto_telefono1', 'Teléfono'), ('contacto_telefono2', 'Télefono 2'), ('contacto_direccion', 'Dirección')], default='None', max_length=45, verbose_name='Codigo'),
        ),
    ]
