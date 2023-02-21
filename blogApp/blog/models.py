from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()#this is an internet address for titles in the url
    intro = models.TextField()
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    #if you want to order the blog in the views you use the class meta
    class Meta:
        ordering = ('-created_at', )#the "-"prefix takes the latest entry and puts on top and the old ones at he bottom

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)#this will shoow that comments belog to a certain post
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)