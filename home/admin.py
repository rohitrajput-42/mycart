from django.contrib import admin
from .models.index import Filter, Deals, Ads, Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order 

class AdminFilter(admin.ModelAdmin):
    list_display = ["name"]

class AdminDeals(admin.ModelAdmin):
    list_display = ["name"]

class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "price", "description"]

class AdminCustomer(admin.ModelAdmin):
    list_display = ["fullname", "username", "email", "mobile"]

class AdminOrder(admin.ModelAdmin):
    list_display = ["product", "customer", "quantity", "price", "address", "phone", "date", "order_status"]  

admin.site.register(Filter, AdminFilter)
admin.site.register(Deals, AdminDeals)
admin.site.register(Ads)
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)