

from django.urls import path

from . import views

urlpatterns = [
	path('', views.product_display_view, name='product_display'),
	path('detail/<int:pk>/', views.product_detail_view_data_input_display, name='product-detail'),

]