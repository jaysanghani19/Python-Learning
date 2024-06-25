from django.urls import path

from products.views import create_product,dyanmic_product,product_page,update_product

urlpatterns = [
    path('',product_page),
    path('create/',create_product),
    path('<int:id>/',dyanmic_product,name="product-detail"),
    path('<int:id>/update/',update_product),

]
