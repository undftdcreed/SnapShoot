from typing import Any, Dict
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Listing
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    
class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class ListingList(TemplateView):
    template_name = "listing_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("title")
        if name != None:
            context["listings"] = Listing.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"searching for {name}"
        else:
            context["listings"] = Listing.objects.filter(user=self.request.user)
            context["header"] = "Hot Locations"
        return context
    

    
class ListingCreate(CreateView):
    model= Listing
    fields = {'name', 'img', 'description', 'price'}
    template_name = "listing_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListingCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('listing_deatil', kwargs={'pk': self.object.pk})


class ListingDetail(DetailView):
    model=Listing
    template_name = "listing_detail.html"
    


class ListingUpdate(UpdateView):
    model=Listing
    fields =['name', 'img', 'description', 'price']
    template_name = "listing_update.html"

    def get_success_url(self):
        return reverse('listing_deatil', kwargs={'pk': self.object.pk})
    
class ListingDelete(DeleteView):
    model = Listing
    template_name = "listing_delete_confirmation.html"
    success_url = "/listing/"
    


class Signup(TemplateView):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("listing_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
