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

def blogpage(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html' , {'blogs' : blogs})

def blogdetails(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blogdetails.html', {'blog': blog})
