from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeview(request):
    return render(request, 'testapp/index.html')


def aboutview(request):
    return render(request, 'testapp/about.html')

def clippingpathsview(request):
    return render(request, 'testapp/clipping_path.html')

def background_remover_view(request):
    return render(request, 'testapp/background_remover.html')

def color_correction_view(request):
    return render(request, 'testapp/color_correction.html')

def drop_shadow_view(request):
    return render(request, 'testapp/drop_shadow.html')

def image_retuch_view(request):
    return render(request, 'testapp/image_retuch.html')

def invisible_mannequine_view(request):
    return render(request, 'testapp/invisible_mannequin.html')


def portfolio(request):
    return render(request, 'testapp/portfolio.html')

def pricing(request):
    return render(request, 'testapp/pricing.html')

def faq(request):
    return render(request, 'testapp/faq.html')


def contact(request):
    return render(request, 'testapp/contact.html')


def getfredemo(request):
    return render(request, 'testapp/get_free_demo.html')


def bloglist(request):
    return render(request, 'testapp/blog_list.html')


def blogdetails(request):
    return render(request, 'testapp/blog_detail.html')



