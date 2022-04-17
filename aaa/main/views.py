from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from aaa.settings import EMAIL_HOST_USER
from django.core import serializers
from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import NewUserForm, CustomAuthForm
from .models import *

def index(request):
    categories = Category.objects.all()
    staffs = Staff.objects.all()
    services = Service.objects.filter(order_service__is_available=True).prefetch_related(Prefetch(
        'order_service', Order.objects.all()
    )).distinct()
    return render(request, 'main.html', context={'staffs': staffs, 'categories': categories, 'services': services})

def contacts(request):
    return render(request, "contacts.html", context={})

def about_us(request):
    return render(request, "blog.html", context={})

def register(request):
    form = NewUserForm()
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_urls')
    return render(request, "registration.html", context={'register_form': form})

def login_request(request):
    if request.POST:
        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index_urls')
            else:
                return redirect('login_urls')
    form = CustomAuthForm()
    return render(request, "login.html", context={'login_form': form})


def logout_request(request):
    logout(request)
    return redirect('login_urls')

def staff_info(request, id):
    staff = Staff.objects.get(id=id)
    return render(request, 'staff_info.html', context={'staff': staff})

def mission(request):
    return render(request, "mission.html", context={})

def history(request):
    return render(request, "history.html", context={})

def laws(request):
    return render(request, "laws.html", context={})

def rights(request):
    return render(request, "rights.html", context={})

def questions(request):
    return render(request, "questions.html", context={})

def services(request):
    category = Category.objects.all()
    service = Service.objects.all()
    return render(request, "services.html", context={'category': category, 'service': service})

def get_service_time(request, id):
    if not id:
        return
    times = Order.objects.filter(service_id=id).filter(is_available=True).select_related('service')
    data = serializers.serialize('json', times)
    return HttpResponse(data, content_type="application/json")

def send_message(request):
    full_name = request.POST.get("full_name")
    phone = request.POST.get("phone")
    message = request.POST.get("message")
    Message.objects.create(full_name=full_name, phone=phone, message=message)
    return redirect('index_urls')

def order_online(request):
    service = Service.objects.get(id=request.POST.get('service'))
    time = request.POST.get('time')
    full_name = request.POST.get('full_name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    OnlineOrder.objects.create(service=service, time=time, full_name=full_name, phone=phone, message=message)
    order = Order.objects.get(time=time)
    order.is_available = False
    order.save()
    subject = 'Медицинский центр MEDIXO'
    message = f'Здравствуйте, уведомляем вас об успешной записи на ПРИЁМ -  { service.name } ВРЕМЯ - { time }'
    recipient = str(request.POST.get('email'))
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
    return redirect('index_urls')


def feedback(request):
    if request.method == 'POST':
        Feedback.objects.create(full_name=request.POST.get('full_name'),
                                phone=request.POST.get('phone'),
                                email=request.POST.get('email'),
                                comment=request.POST.get('comment'))
        return redirect('index_urls')
    return redirect('index_urls')