# Generated by Django 3.0.2 on 2020-02-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0002_auto_20200213_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='tipo',
            field=models.CharField(choices=[('Auditorio', 'Auditorio'), ('Laboratorio', 'Laboratorio'), ('Normal', 'Normal')], max_length=25),
        ),
    ]