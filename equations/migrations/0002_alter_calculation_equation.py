# Generated by Django 4.1.2 on 2022-10-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='equation',
            field=models.CharField(choices=[('FIB', 'Fibonacci')], default='FIB', max_length=4),
        ),
    ]
