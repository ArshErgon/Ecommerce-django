
from django.urls import path
from . import views

urlpatterns = [
	path('', views.ecommerce_home, name='home'),
	path('ecommerce/sign/', views.signpage, name='signin'),
]