from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
	return render(request, 'blog/index.html')

def inicio(request):
	return render(request, 'blog/inicio.html')

def dark(request):
	return render(request, 'blog/dark_post.html')
# Create your views here.


