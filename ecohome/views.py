from django.shortcuts import render


def ecommerce_home(request):
	return render(request, 'home.html')
