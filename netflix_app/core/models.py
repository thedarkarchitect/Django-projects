from django.db import models
from  django.contrib.auth.models import AbstractUser #this inherits from the User class and is used to add additional Fields required for your User in Database itself
import uuid 

AGE_CHOICES=(
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICE = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)

# Create your models here.
class CustomUser(AbstractUser):#this class inherits from the User Django class
    profiles = models.ManyToManyField('Profile', blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)#will add the date and time the movie is inserted
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=20, choices=MOVIE_CHOICE)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')#will store flyer for specific movie
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)

class Video(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='movies')
