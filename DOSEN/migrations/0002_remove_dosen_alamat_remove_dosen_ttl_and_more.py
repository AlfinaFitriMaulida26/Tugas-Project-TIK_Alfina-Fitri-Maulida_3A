# Generated by Django 4.1.1 on 2022-10-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSEN', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='ttl',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='unit',
        ),
        migrations.AlterField(
            model_name='dosen',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='nama',
            field=models.CharField(max_length=50),
        ),
    ]
