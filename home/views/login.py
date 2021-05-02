from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from home.models.customer import Customer
from django.contrib.auth.hashers import check_password

class Login(View):
    
    def get(self, request):
        return render(request, "login.html") 

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        customer = Customer.get_customer_by_username(username)

        error_message = None
        
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session["customer"] = customer.id
                #print(customer.id)
                return redirect("/")
            else:
                error_message = "Email or Password invalid !!!..."
        else:
            error_message = "Email or Password invalid !!!..."
        
        return render(request, "login.html", {"error" : error_message})


def Logout(request):
    request.session.clear()
    return redirect("/")