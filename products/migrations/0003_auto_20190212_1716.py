# Generated by Django 2.1.5 on 2019-02-12 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190212_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_tage',
            field=models.CharField(blank=True, choices=[('new', 'NEW'), ('sale', 'SALE'), ('premiere', 'PREMIERE')], max_length=10),
        ),
    ]