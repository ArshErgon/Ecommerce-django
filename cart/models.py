from django.db import models

class ProductCart(models.Model):
	cart_product_id = models.IntegerField()
	cart_product_buyer = models.CharField(max_length=50)

	def __str__(self):
		return "ID: %s, %s" % (self.cart_product_id, self.cart_product_buyer)

