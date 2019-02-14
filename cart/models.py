from django.db import models

class ProductCart(models.Model):
	cart_product_image = models.ImageField(upload_to='CartImg')
	cart_product_name = models.CharField(max_length=100)
	cart_product_id = models.IntegerField()
	cart_product_price = models.IntegerField()

	def __str__(self):
		return "ID: %s, %s" % (self.cart_product_id, self.cart_product_name)

