from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import AboutModel, ContactModel # I can you class meta also but I have never try that

def contact_page(request):
	contact_form =  ContactForm(request.POST or None)
	name = request.POST.get("full_name")
	phone_number = request.POST.get("phone_number")
	email = request.POST.get("email")
	message = request.POST.get("message")
	if contact_form.is_valid():
		ContactModel.objects.create(full_name=name, phone_number=phone_number, email=email, message=message)
		return redirect('/')
	return render(request, 'contact.html', {'contact_form':contact_form})

def about_page(request):
	about_context = AboutModel.objects.all()
	return render(request, 'about.html', {'about_context':about_context})