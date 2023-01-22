from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "websiteapp/index.html")

def projects(request):
    return render(request, "websiteapp/projects.html")

def links(request):
    return render(request, "websiteapp/links.html")