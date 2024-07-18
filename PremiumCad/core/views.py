from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pathways(request):
    return render(request, 'pathways.html')

def services(request):
    return render(request, 'services.html')

def career(request):
    return render(request, 'career.html')

def cadservices(request):
    return render(request, 'cadservices.html')

def gisservices(request):
    return render(request, 'gisservices.html')

def telecomservices(request):
    return render(request, 'telecomservices.html')

def solardesign(request):
    return render(request, 'solardesign.html')

def blogs(request):
    return render(request, 'blogs.html')

# def blogdetails(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     return render(request, 'blogdetails.html', {'blog': blog})
