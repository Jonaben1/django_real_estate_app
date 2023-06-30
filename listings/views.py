from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm, RegisterForm, ContactForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'retrieve.html', context)


def create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
             form.save()
             return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'create.html', context)



def update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("contact")
            else:
                messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})





def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("home")
    return render(request, 'logout.html')




@login_required(login_url='login')
class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact.html'
    success_message = 'Your message was submitted successfully'

    def form_invalid(self, form):
        message.error(self.request, 'An unknown error has occurred!')
        return HttpResponseRedirect('')



@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

