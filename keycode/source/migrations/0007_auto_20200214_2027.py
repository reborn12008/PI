# Generated by Django 3.0.2 on 2020-02-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0006_auto_20200213_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='pincode',
            field=models.BinaryField(),
        ),
    ]