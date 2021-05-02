from django.db import models

class Customer(models.Model):
    fullname = models.CharField(max_length = 500)
    username = models.CharField(max_length = 500)
    email = models.EmailField()
    mobile = models.CharField(max_length = 30)
    password = models.CharField(max_length = 300)

    def __str__(self):
        return self.fullname

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True 
        return False

    def userExists(self):
        if Customer.objects.filter(username = self.username):
            return True
        return False

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username = username)
        except:
            return False