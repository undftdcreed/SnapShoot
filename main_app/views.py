from typing import Any, Dict
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Listing
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    
class About(TemplateView):
    template_name = "about.html"


class ListingList(TemplateView):
    template_name = "listing_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("title")
        if name != None:
            context["listings"] = Listing.objects.filter(name__icontains=name)
            context["header"] = f"searching for {name}"
        else:
            context["listings"] = Listing.objects.all()
            context["header"] = "Hot Locations"
        return context
    

    
class ListingCreate(CreateView):
    model= Listing
    fields = {'name', 'img', 'description', 'price'}
    template_name = "listing_create.html"
    success_url="/listings/"


class ListingDetail(DetailView):
    model=Listing
    template_name = "listing_detail.html"