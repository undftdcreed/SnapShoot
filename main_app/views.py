from typing import Any, Dict
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import BaseModelForm
from .models import Booking, Listing
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    
class About(TemplateView):
    template_name = "about.html"


class ListingList(TemplateView):
    template_name_authenticated = "listing_list.html"
    template_name_unauthenticated = "listing_list_unauthenticated.html"

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return [self.template_name_authenticated]
        else:
            return [self.template_name_unauthenticated]

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

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated and 'listing_pk' in kwargs:
            # Redirect non-authenticated users to login if they try to access the BookingCreate view
            return redirect(reverse_lazy('signup'))
        return super().dispatch(request, *args, **kwargs)
    

    
class ListingCreate(CreateView):
    model= Listing
    fields = {'name', 'img', 'description', 'price'}
    template_name = "listing_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListingCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('listing_detail', kwargs={'pk': self.object.pk})


class ListingDetail(DetailView):
    model=Listing
    template_name = "listing_detail.html"
    


class ListingUpdate(UpdateView):
    model=Listing
    fields =['name', 'img', 'description', 'price']
    template_name = "listing_update.html"

    def get_success_url(self):
        return reverse('listing_detail', kwargs={'pk': self.object.pk})
    
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
        
@method_decorator(login_required, name='dispatch')       
class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        # Only return bookings that belong to the currently logged-in user
        return Booking.objects.filter(user=self.request.user)
    

class BookingCreate(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['start_datetime', 'end_datetime']
    template_name = 'booking_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.listing = get_object_or_404(Listing, pk=self.kwargs['listing_pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing_pk'] = self.kwargs['listing_pk']
        return context

    def get_success_url(self):
        return reverse('booking_detail', kwargs={'pk': self.object.pk})

class BookingDetail(DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    context_object_name = 'booking'


class BookingUpdate(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['start_datetime', 'end_datetime']
    template_name = 'booking_update.html'  # Create a new template for updating bookings

    def get_success_url(self):
        return reverse('booking_detail', kwargs={'pk': self.object.pk})
