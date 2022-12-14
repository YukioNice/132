# Generated by Django 4.1.3 on 2022-11-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(db_index=True, max_length=200),
        ),
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
