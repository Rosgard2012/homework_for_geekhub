from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('detail/', views.product_detail, name='product_detail'),
]