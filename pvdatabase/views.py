from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import csv

def home(request):
    return render(request,'home.html')
def search(request):
    return render(request, 'search.html')
# def about(request):
#     return render(request,'about.html')
#
# def contacts(request):
#     return render(request,'contact.html')
#
# @login_required(login_url='/accounts/login')
# def find(request):
#     return render(request,'find.html')
#
#
# def excercise_guide(request):
#     return render(request,'excercise_guide.html')
