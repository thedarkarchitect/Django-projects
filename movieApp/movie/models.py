from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    review = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0, 
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    description = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.title