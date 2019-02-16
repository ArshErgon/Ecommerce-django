
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
	else:
		show_product = ''

	return render(request, 'cart.html',{
										'show_product'			:			show_product
										}
				)

def product_quantity(request, pk):
	print(pk)
	a = Product.objects.filter(id=pk)
	#print(dir(a))
	filter_data = ProductCart.objects.filter(cart_product_buyer=request.user)
	total_price = x.product_price		
	if filter_data.exists():
		for data in filter_data:	# WHY? because the atribute which I want is not present in filter_data but when we use a loop we get it 
			pass				# It is not the best but figure it out later(EXPERIENCE)
		show_product = Product.objects.filter(id=data.cart_product_id)
	else:
		show_product = ''
	num_product = request.POST.get("num-product")
	if num_product == "0":
		pass

	for x in a:
		pass
	try:
		total_price = x.product_price * int(request.POST.get("num-product"))
	except TypeError:
			total_price = x.product_price		

	quality_price = request.POST.get("num-product")
	
#	tem_price = int(request.POST.get("num-product"))
#	q = x.product_price
#	print("---00"*10, sep="*"*10)
#	print(q)
#	print(tem_price)
#	print(q*tem_price)
	return render(request, 'cart-detail.html', {
										'total_price'			:			total_price,
										'show_product'			:			show_product,
										'quality_price'			:			quality_price,
										}
				 )

def adding_item(request, pk):
	product = Product.objects.filter(id=pk)
	if product.exists():
		ProductCart.objects.create(cart_product_id=pk, cart_product_buyer=request.user)
		return redirect("/cart")
	return render(request, 'cart.html')

def delete_item(request, pk):
	
	return render(request, "cart.html")
	