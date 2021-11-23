# Generated by Django 3.2.9 on 2021-11-23 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=600)),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
