from django.http import HttpResponse
from django.shortcuts import *

def about(request):
    #return HttpResponse("this is my site")
    return render(request,'about.html')
def home(request):
    #return HttpResponse("Homepage")
    return render(request,'index.html')
def posts(request):
    #return HttpResponse("Homepage")
    return render(request,'post.html')
def contact(request):
    #return HttpResponse("Homepage")
    return render(request,'contact.html')