# Generated by Django 3.2.3 on 2021-05-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associado', '0002_auto_20210517_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associado',
            name='saida',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]