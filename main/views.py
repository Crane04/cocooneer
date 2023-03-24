from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        return redirect("/")
    else:
        features = Features.objects.all()
        return render(request, "index.html", {'features': features})
# 234106612910-ce4pfi564davssjkgdjhaajc7vs62n01.apps.googleusercontent.com