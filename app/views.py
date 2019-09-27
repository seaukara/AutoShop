import django.core
from django.urls import reverse, path
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, CreateAccountForm
from django.core.mail import send_mail, BadHeaderError
from .models import User, Appointment
import datetime

def homeView(request):
    if request.method == 'GET':
        email=request.GET['email']
        if User.objects.all().filter(user_email=email).exists()==False:
            if request.method == 'GET':

                form = CreateAccountForm(initial={'Email':email})
        else:
            cur_user = User.objects.all().filter(user_email=email)[0]
            cur_apt = Appointment.objects.all().filter(apt_email=cur_user)[0]
            return render(request, "app/detail.html", {"user":cur_user, "apt": cur_apt})
    else:
        email = request.GET['email']
        if User.objects.all().filter(user_email=email).exists() == False:
            form = CreateAccountForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                u = User()
                u.user_email = form.cleaned_data['Email']
                u.user_fname = form.cleaned_data['FirstName']
                u.user_lname = form.cleaned_data['LastName']
                u.user_phone = form.cleaned_data['Phone']
                u.user_year = form.cleaned_data['Year']
                u.user_make = form.cleaned_data['Make']
                u.user_model = form.cleaned_data['Model']
                u.save()
                apt = Appointment()
                apt.apt_email = u
                try:
                    apt.apt_pref = str(form.cleaned_data['Date']) +" "+ datetime.time.strftime(((form.cleaned_data['Time'])))
                except:
                    apt.apt_pref = str(form.cleaned_data['Date'])
                apt.apt_type = form.cleaned_data['Service']
                apt.apt_ip = request.META['REMOTE_ADDR']
                apt.save()
                to_email = form.cleaned_data['Email']
                subject="Appointment Confirmation"
                message = "Your appointment has been confirmed! Please see the " \
                          "below details regarding your scheduled appointment.\n"
                message += "Appointment Time: " + apt.apt_pref

                try:
                    send_mail(subject, message, 'karamanseau@gmail.com',
                              [to_email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')


                to_email = "repairs@example.com"
                subject = "Car Repair Appointment"

                message = "New Appointment Confirmed!\n\nUser Information\n"
                message += "Name: " + u.user_fname + " " + u.user_lname + "\n"
                message += "Email: " + u.user_email + "\n"
                message += "Phone: " + str(u.user_phone) + "\n\n"
                message += "Vehicle Information\n"
                message += u.user_make + " "
                message += u.user_model +" (" +str(u.user_year)+")\n\n"

                message += "Appointment Information \n"
                message += "Time: " + apt.apt_pref + "\n"
                message += "Service Description: " + apt.apt_type + "\n"
                message += "IP: " + apt.apt_ip
                try:
                    send_mail(subject, message, 'karamanseau@gmail.com',
                              [to_email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return render(request, "app/detail.html", {"user": u,
                                                           "apt": apt})
            else:
                return HttpResponse('Invalid header found.')
    return render(request, "app/index.html", {'form': form})



def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']

            if User.objects.all().filter(user_email=email).exists() == False:
                link = request.build_absolute_uri() + "home/?email=" + form.cleaned_data['Email']
                subject = "Welcome!"
                to_email = form.cleaned_data['Email']
                message = "Hi, thank you for contacting us! Please click the below link for additional details." + link
                try:
                    send_mail(subject, message, 'karamanseau@gmail.com', [to_email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
            else:
                cur_user = User.objects.all().filter(user_email=email)[0]
                cur_apt = Appointment.objects.all().filter(apt_email=cur_user)[0]
                return render(request, "app/detail.html", {"user": cur_user, "apt": cur_apt})
    return render(request, "app/home.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')