from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import csv

def home(request):
    if(request.user.is_authenticated):
        return render(request, 'home.html')
    else:
        return render(request,'index.html')

def tos(request):
    return render(request,'tos.html')
# matches certain parameters given by search
@login_required(login_url='/accounts/signup')
def search(request):
    if(request.method == 'POST'):
        first_name = request.POST['inputfirstname']
        last_name = request.POST['inputlastname']
        grad_year = request.POST['inputyear']
        college = request.POST['inputcollege']
        major = request.POST['inputmajor']
        city = request.POST['inputcity']
        state = request.POST['inputstate']
        country = request.POST['inputcountry']
        zip = request.POST['inputzip']
        employer = request.POST['inputemployer']
        job = request.POST['inputjobtitle']
        field = request.POST['inputfield']
        hs_activities = request.POST['inputclubs']
    else:
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
