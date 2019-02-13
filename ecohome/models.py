
from django.db import models
import datetime

now = datetime.datetime.now()


class UserDetail(models.Model):
	user = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	zipcode = models.IntegerField()
	state = models.CharField(max_length=70)
	phone_number = models.IntegerField()

	def __str__(self):
		return self.user


class BannerProduct(models.Model):
	GENDER_CATEGORY = (
		(f'WOMEN COLLECTION {now.year} ' , 'WOMEN'),
		(f'MALE COLLECTION {now.year} ', 'MALE'),
		)

	banner_product_image = models.ImageField(upload_to='UpImg')
	banner_product_category = models.CharField(max_length=30, choices=GENDER_CATEGORY)
	banner_product_description = models.TextField()

	def __str__(self):
		return self.banner_product_description[:16]


class HomeProductDisplay(models.Model):
	PRODUCT_CATEGORY = (
		('SUNGLASSES', 'SUNGLASSES'),
		('DRESSES', 'DRESSES'),
		('FOOTWEAR', 'FOOTWEAR'),
		('WATCHES', 'WATCHES'),
		('BAGS', 'BAGS'),
		)
	home_product_image = models.ImageField(upload_to='HomeUpImg')
	home_product_category = models.CharField(max_length=40, choices=PRODUCT_CATEGORY)

	def __str__(self):
		return self.home_product_category