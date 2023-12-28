from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def faqs_view(request):
    return render(request, 'faqs.html')

def contact_view(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        return HttpResponse('register URL with POST method')
        # create one row in db table
        # add user in our db


def header_view(request):
    return render(request, 'header.html')