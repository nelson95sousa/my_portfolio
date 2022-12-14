from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mainpage/index.html')

def about(request):
    return render(request,'mainpage/about.html')

def my_gear(request):
    return render(request,'mainpage/my_gear.html')

def techniques(request):
    return render(request,'mainpage/techniques.html')

def long_exposure(request):
    return render(request,'mainpage/long_exposure.html')

def panorama(request):
    return render(request,'mainpage/panorama.html')

def post_processing(request):
    return render(request,'mainpage/post_processing.html')

def contact(request):
    return render(request,'mainpage/contact.html')