from django.urls import path
from .views import index, about, menu, cart, edit_product, delete_product, add_product

urlpatterns = [
    path('', index, name='index'),
    path('about.html', about, name='about'),
    path('menu.html', menu, name='menu'),
    path('cart/', cart, name='cart'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),  # URL for editing a product
    path('delete/<int:product_id>/', delete_product, name='delete_product'),  # URL for deleting a product
    path('add/', add_product, name='add_product'),  # URL for adding a product
    # Add other URL patterns as needed
]
