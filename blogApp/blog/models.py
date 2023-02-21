from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()#this is an internet address for titles in the url
    intro = models.TextField()
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    #if you want to order the blog in the views you use the class meta
    class Meta:
        ordering = ('-create_at', )#subtracts the first order from the second and the first goes on top in html