from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Listing(models.Model):

    name = models.CharField(max_length=200)
    img = models.CharField(max_length=250, default='default.jpg')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['name']


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    # Additional fields specific to your booking requirements

    def __str__(self):
        return f"{self.user.username}'s Booking for {self.service.name}"