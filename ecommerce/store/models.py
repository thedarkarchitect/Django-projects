from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)#this will let us know if the product is a digital product or a physical product that needs to be shipped
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    #this help us to access images as attributes using the model method below to stop a front end error we will use a try/except block
    # the @property decorator will access the method like an attribut
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)#this is a one to one relationship
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)#will keep track of cart items if they have been bought or not
    transcation_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()#helps access the order items of an order
        total = sum([item.get_total for item in orderitems])#this is going to total the number of items and get the total price the customer want to pay 
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])#this will get the number of things in the cart using the quantity of items 
        return total    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)#this is a one to one relationship since and item need to align with  a product and order status
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)#this is a one to one relationship
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):#this will return the total price of the quantities interested in
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    @property
    def shipping(self):#this loops thru all orders and looks for physical and digital products to see which are for shipping and which don't need to be shipped
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping