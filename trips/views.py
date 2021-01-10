from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def hello(request):
    return render(request, 'hello.html', {
        'data': "Ohhoho",
    })

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
         'post_list': post_list,
    })