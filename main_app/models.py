from django.db import models

# Create your models here.
class Listing(models.Model):

    title = models.CharField(max_length=200)
    img = models.CharField(max_length=250, default='default.jpg')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['title']
