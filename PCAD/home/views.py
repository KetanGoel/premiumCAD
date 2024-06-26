from django.shortcuts import render, get_object_or_404
from .models import blog
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
    blogs = blog.objects.all()
    return render(request, 'blog.html' , {'blogs' : blogs})

def blogdetails(request, id):
    blog = get_object_or_404(blog, id=id)
    return render(request, 'blogdetails.html', {'blog': blog})
