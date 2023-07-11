from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    
class About(TemplateView):
    template_name = "about.html"


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
