from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    #we set null to True so that if field is empty no error is generated
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)#this means a customer can have one user and user can have only one customer so there is no confusion between user and customer
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    #to see the name of the customer instead of object we using string function

    def __str__(self):
        return self.name


class Tag(models.Model):#this just shows the tag a product can be
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)#different products can have more than one tag so we use a many to many relationship

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    #foreign keys are justs parents of the child model being created 
    cutomer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)#when order is deleted the customer will stay in the database but with a null value for order
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
