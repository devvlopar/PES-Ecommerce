from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from buyer.models import Buyer

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
        # email validation
        form_email = request.POST['email']
        try:
            user_obj = Buyer.objects.get(email = form_email)
            return render(request, 'register.html', {'msg': 'This email is already in Use.'})

        except:
            # error occurred while finding that email in DB
            # it means entered email is completely new
            # we can create a new account for it..


            # password & confirm password validation
            if request.POST['password'] == request.POST['cpassword']:
                global c_otp
                c_otp = randint(100_000, 999_999)
                global user_data
                user_data = {
                    'full_name': request.POST['full_name'],
                    'email': request.POST['email'],
                    'password':request.POST['password'],
                    'mobile': request.POST['mobile'],
                    'address': request.POST['address'],
                    'cpassword': request.POST['cpassword']
                }

                subject = 'Ecommerce Registration'
                message = f'Hello!! your OTP is {c_otp}'
                sender = settings.EMAIL_HOST_USER
                rec = [request.POST['email']]
                send_mail(subject, message, sender, rec)
                return render(request, 'otp.html')
            else:
                return render(request, 'register.html', {'msg': 'BOTH passwords do not matchh!!!'})
        
        
def otp_view(request):
    pass
    # compare otp entered by user and generated otp
    # c_otp = 315308 INTEGER
    # request.POST['u_otp'] = '315308' STRING

    if str(c_otp) == request.POST['u_otp']:
        # create a row in db
        Buyer.objects.create(
            full_name = user_data['full_name'],
            email = user_data['email'],
            password = user_data['password'],
            address = user_data['address'],
            mobile = user_data['mobile']
        )
        return render(request, 'register.html', {'msg': 'Account Created Successfully!!!'})

    else:
        return render(request, 'otp.html', {'msg': "entered OTP is INVALID"})


def header_view(request):
    return render(request, 'header.html')