# Generated by Django 2.1.5 on 2019-02-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_product_image', models.ImageField(upload_to='CartImg')),
                ('cart_product_name', models.CharField(max_length=100)),
                ('cart_product_id', models.IntegerField()),
                ('cart_product_price', models.IntegerField()),
            ],
        ),
    ]
