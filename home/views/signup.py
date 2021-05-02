from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from home.models.customer import Customer
from django.contrib.auth.hashers import make_password

class Signup(View):

    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        postData = request.POST

        fullname = postData.get("fullname")
        username = postData.get("username")
        email = postData.get("email")
        mobile = postData.get("mobile")
        password = postData.get("password")

        value = {
            'fullname': fullname,
            'username': username,
            'email': email,
            'mobile': mobile,
        }

        error_message = None

        customer = Customer(fullname = fullname,
                            username = username,
                            email = email,
                            mobile = mobile,
                            password = password)
        
        error_message = self.validateCustomer(customer)

        if not error_message:  
            customer.password = make_password(customer.password)
            customer.save()  
            return render(request, "login.html")      

        else:

            data = {
                'error': error_message,
                'values': value, 
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):

        error_message = None

        if (not customer.fullname):
            error_message = "fullname required !!!..."
        elif len(customer.fullname) < 4:
            error_message = "first name must be 4 character long !!!..."

        elif (not customer.username):
            error_message = "username required !!!..."
        elif len(customer.username) < 4:
            error_message = "username must be 4 character long !!!..."
        elif customer.userExists():
            error_message = "Username already taken!!!..."

        elif (not customer.mobile):
            error_message = "phone number required !!!..."
        elif len(customer.mobile) < 10:
            error_message = "phone number must be of 10 digits !!!..."

        elif (not customer.password):
            error_message = "password required !!!..."
        elif len(customer.password) < 5:
            error_message = "password must be 5 characters long !!!..."

        elif len(customer.email) < 5:
            error_message = "email must be 5 characters long !!!..."
        elif customer.isExists():
            error_message = "email already registered !!!..."

        return error_message      