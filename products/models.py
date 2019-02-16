from django.db import models


class Product(models.Model):
	GENDER = (
		('male', 'MALE'),
		('female', 'FEMALE'),
		)
	PRODUCT_TAGES = (
		("new", "NEW"),
		('sale', 'SALE'),
		)
	PRODUCT_CATEGORY = (
		('SUNGLASSES', 'SUNGLASSES'),
		('DRESSES', 'DRESSES'),
		('FOOTWEAR', 'FOOTWEAR'),
		('WATCHES', 'WATCHES'),
		('BAGS', 'BAGS'),
		)
	PRODUCT_COLOR = (
		('RED','RED'),
		('BLUE','BLUE'),
		('GREEN', 'GREEN'),
		)
	product_name = models.CharField(max_length=50)
	product_image = models.ImageField(upload_to='ProImg')
	product_image_second  = models.ImageField(upload_to='ProImg')
	product_image_third = models.ImageField(upload_to='ProImg')
	product_description = models.CharField(max_length=100)
	product_addition_detail = models.TextField(blank=True)
	product_eye_catcher = models.CharField(max_length=100)
	product_category = models.CharField(max_length=15, choices=PRODUCT_CATEGORY)
	product_color_by_user = models.CharField(max_length=10, choices=PRODUCT_COLOR, blank=True)
	product_gender = models.CharField(max_length=10, choices=GENDER)
	product_price = models.IntegerField()
	product_quantity_total_price = models.IntegerField( blank=True, default=1)
	product_tage = models.CharField(max_length=10, choices=PRODUCT_TAGES, blank=True)


	def __str__(self):
		return self.product_name[:50]



class ProductReview(models.Model):
	product_id = models.IntegerField()
	product_reviewer_name = models.CharField(max_length=50)
	product_review = models.TextField()

	def __str__(self):
		return "ID: %s by  %s" %(str(self.product_id), self.product_reviewer_name)
