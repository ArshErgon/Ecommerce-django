
from django.urls import path

from . import views

urlpatterns = [
	path('', views.cart_page, name='cart'),
	path("add/<int:pk>/product/", views.adding_item, name='add-products'),
	path("delete/<int:pk>/item", views.delete_item, name='delete-item'),
	path("quantity/<int:pk>/", views.product_quantity, name='quantity'),
]