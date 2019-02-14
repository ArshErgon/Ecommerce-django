
from django.shortcuts import render

from products.models import Product

from .models import ProductCart

def cart_page(request):
#	print(dir(Product))
	return render(request, 'cart.html')

def adding_item(request, pk):
	product = Product.objects.filter(id=pk)
	if product.exists():
		ProductCart.objects.create(cart_product_id=pk, cart_product_buyer=request.user)
	return render(request, 'cart.html')

def delete_item(request, pk):
	print(pk)
	return render(request, 'cart.html')