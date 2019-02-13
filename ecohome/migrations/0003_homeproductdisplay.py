# Generated by Django 2.1.5 on 2019-02-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohome', '0002_auto_20190212_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeProductDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_product_image', models.ImageField(upload_to='HomeUpImg')),
                ('home_product_category', models.CharField(choices=[('SUNGLASSES', 'SUNGLASSES'), ('DRESSES', 'DRESSES'), ('FOOTWEAR', 'FOOTWEAR'), ('WATCHES', 'WATCHES'), ('BAGS', 'BAGS')], max_length=40)),
            ],
        ),
    ]
