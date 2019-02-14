
from django.shortcuts import render, redirect

from products.models import Product

from .models import ProductCart

def cart_page(request):
	filter_data = ProductCart.objects.filter(cart_product_buyer=request.user)
	#print(dir(filter_data))
	#print(filter_data.cart_product_id)
	if filter_data.exists():
		for x in filter_data:	# WHY? because the atribute which I want is not present in filter_data but when we use a loop we get it 
			pass				# It is not the best but figure it out later(EXPERIENCE)
	show_product = Product.objects.filter(id=x.cart_product_id)

	return render(request, 'cart.html',{'show_product':show_product})

def adding_item(request, pk):
	product = Product.objects.filter(id=pk)
	if product.exists():
		ProductCart.objects.create(cart_product_id=pk, cart_product_buyer=request.user)
	return render(request, 'cart.html')

def product_quantity(request, pk):
	print(pk)
	print(request.POST.get("num-product"), "Printing here!!!!!")
	return redirect("/cart")

def delete_item(request, pk):
	print(pk)
	#return redirect("%s"%())
	return render(request, 'cart.html')