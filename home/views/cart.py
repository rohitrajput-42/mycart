from django.views import View
from django.shortcuts import render, redirect
from home.models.index import Product

class Cart(View):
    def get(self, request):
        
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)

        return render(request, "cart.html", {'products' : products})