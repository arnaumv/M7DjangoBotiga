# Generated by Django 5.0.2 on 2024-04-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_categoria_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cistella',
            name='producte',
        ),
        migrations.AddField(
            model_name='cistella',
            name='producte',
            field=models.ManyToManyField(to='shop.producte'),
        ),
    ]
