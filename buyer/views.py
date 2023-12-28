from django.shortcuts import render

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
    return render(request, 'register.html')

def header_view(request):
    return render(request, 'header.html')