from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'



    