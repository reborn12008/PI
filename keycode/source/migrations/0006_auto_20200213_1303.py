# Generated by Django 3.0.2 on 2020-02-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0005_auto_20200213_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]