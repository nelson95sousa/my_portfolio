from django.shortcuts import render
from portfolio.models import Portfolio_Picture

# Create your views here.
def city(request):
    img = Portfolio_Picture.objects.filter(image_category='city')
    return render(request,'portfolio/portfolio_template.html',{'img':img,'category':'CITY'})

def nature(request):
    img = Portfolio_Picture.objects.filter(image_category='nature')
    return render(request,'portfolio/portfolio_template.html',{'img':img,'category':'NATURE'})

def panorama(request):
    img = Portfolio_Picture.objects.filter(image_category='panorama')
    return render(request,'portfolio/portfolio_template.html',{'img':img,'category':'PANORAMA'})

def long_exposure(request):
    img = Portfolio_Picture.objects.filter(image_category='long_exposure')
    return render(request,'portfolio/portfolio_template.html',{'img':img, 'category':'LONG EXPOSURE'})
