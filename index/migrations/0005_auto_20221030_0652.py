# Generated by Django 3.2 on 2022-10-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20221030_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='category',
            field=models.ManyToManyField(to='index.Category'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='category_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
