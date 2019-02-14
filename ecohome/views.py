
from django.shortcuts import render, redirect

from .models import BannerProduct, HomeProductDisplay, UserDetail

from .forms import SignInForm, SignInDetail, TryForm

from products.forms import ReviewForm

from cart.models import ProductCart

from products.models import Product

from django.contrib.auth import  login, get_user_model

from django.contrib.auth.models import User


def ecommerce_home(request):
	banner_context = BannerProduct.objects.all()
	home_product_context = HomeProductDisplay.objects.all()
	return render(request, 'home.html', {
										'banner_context'			:			banner_context, 
										'home_product_context'		:			home_product_context
										}
				)

User = get_user_model()
def signpage(request):
	sign_form = SignInForm(request.POST or None)
	sign_detail = SignInDetail(request.POST or None)

	# ------------------------------------------------------
		
	# Sign form Data Enter here
	name = request.POST.get('name')
	email = request.POST.get('email')
	password = request.POST.get('password')
	# end sign form data end

	# ------------------------------------------------------

	# ------------------------------------------------------

	# Sign detail form starthere

	street_address = request.POST.get('street_address')
	zip_code = request.POST.get('zip_code')
	state = request.POST.get('state')
	phone_number = request.POST.get('phone_number')
	# end here
	# ------------------------------------------------------

	print(phone_number, zip_code, password, email)

	if request.method == "POST":

		if sign_form.is_valid():
			UserDetail.objects.create(user=name, address=street_address, zipcode=zip_code, state=state, phone_number=phone_number)
			new_sign_form = User.objects.create_user(name, email, password, is_staff=True)
			login(request, new_sign_form)
			return redirect('/')
			
	return render(request, 'sign.html', {
										'sign_form'			:		sign_form, 
										'sign_detail'		:		sign_detail
										}
				)



def trypage(request):
	a = ProductCart.objects.filter(cart_product_buyer='arsh')
	if a.exists():
		x = Product.objects.filter(id=1)
	else:
		x = 'A'
	print(request.path_info)
	return render(request, 'try.html', {'a':x})
