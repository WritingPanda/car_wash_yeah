from django.shortcuts import render


def index(request):
    return render(request, template_name='car_wash_manager/index.html')


def login(request):
    return render(request, template_name='car_wash_manager/login.html')