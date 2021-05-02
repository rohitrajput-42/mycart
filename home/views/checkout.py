from django.views import View
from django.shortcuts import render, redirect
from home.models.index import Product
from home.models.customer import Customer
from home.models.orders import Order

class CheckOut(View):
    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_products_by_id(list(cart.keys()))
        
        for product in products:
            order = Order(customer = Customer(id = customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id)))
            order.placeOrder()

        request.session['cart'] = {}

        return redirect('cart')