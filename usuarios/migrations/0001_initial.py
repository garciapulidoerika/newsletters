# Generated by Django 3.2.9 on 2021-11-23 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('correo', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
