from django.views import View
from django.shortcuts import render, redirect
from home.models.orders import Order


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, "orders.html", {'orders' : orders})