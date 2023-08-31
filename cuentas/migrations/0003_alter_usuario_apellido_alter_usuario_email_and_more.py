# Generated by Django 4.2.3 on 2023-08-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_remove_usuario_nombreusuario_usuario_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='', max_length=40),
        ),
    ]
