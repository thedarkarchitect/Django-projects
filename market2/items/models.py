from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300,blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)#when category is deleted all items to that category will be deleted
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image  = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)#this relates to the User class model already built in by django and shows when the items specific to a user were created 
    created_at = models.DateTimeField(auto_now_add=True)#this is specific to when the item is created    

    def __str__(self):
        return self.name