from django.urls import path
from . import views

urlpatterns = [
    path('product_listing_page/', views.product_listing_page),
    path('product_detail_page/', views.product_detail_page),
    path('search/', views.search),
]