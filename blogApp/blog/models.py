from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

class Post(models.Model):
    #this is the choices user will see and the values will be what is shown in the database
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        #these will be seen in the admin parnel
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()#this is an internet address for titles in the url
    intro = models.TextField()
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    def __str__(self):
        return self.title

    #if you want to order the blog in the views you use the class meta
    class Meta:
        ordering = ('-created_at', )#the "-"prefix takes the latest entry and puts on top and the old ones at he bottom

class Comment(models.Model):
    #the related_name allows us to have access to the POST db in html 
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)#this will shoow that comments belog to a certain post
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name