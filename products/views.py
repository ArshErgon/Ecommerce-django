
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductReview
from .forms import ReviewForm

def product_display_view(request):
	product_context = Product.objects.all()
	print(product_context)
	product_review_context = ProductReview.objects.all()
	return render(request, 'product.html', {'product_context':product_context})

def product_detail_view_data_input_display(request, pk):
	product_view = get_object_or_404(Product, pk=pk)
	review_form = ReviewForm(request.POST)
	reviewer_name = request.POST.get('name')
	reviewer_review = request.POST.get("user_review")	
	show_reviews = ProductReview.objects.filter(product_id=pk)
	length_of_review = len(show_reviews)
	print(length_of_review)
	
	url = request.path
#	print(url, 'its working now ?')
	if review_form.is_valid():
		ProductReview.objects.create(product_id=pk, product_reviewer_name=reviewer_name, product_review=reviewer_review)
		return redirect('%s'%(url))
	return render(request, 'product-detail.html',{'product_view':product_view, 'review_form':review_form, "show_reviews":show_reviews, 'length_of_review':length_of_review})
