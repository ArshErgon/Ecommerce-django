# Generated by Django 2.1.5 on 2019-02-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_tage',
            field=models.CharField(blank=True, choices=[('New', 'NEW'), ('Sale', 'SALE'), ('Premiere', 'PREMIERE')], max_length=10),
        ),
    ]
