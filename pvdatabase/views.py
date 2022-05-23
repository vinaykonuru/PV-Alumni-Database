from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from alumniprof.models import AlumniProf

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
        state = request.POST.getlist('inputstate')
        country = request.POST['inputcountry']
        zip = request.POST['inputzip']
        employer = request.POST['inputemployer']
        job = request.POST['inputjobtitle']
        field = request.POST.getlist('inputfield')
        hs_activities = request.POST.getlist('inputclubs')

        print(state)
        if not state:
            state = ""
        else:
            state = state[0];
        # 1. get all profiles
        # 2. if filter is empty or if the profile matches the filter, include
        # it in search results
        profiles = AlumniProf.objects.all()
        matched_profiles = []
        for profile in profiles: # filtering profiles
            if( \
            (first_name == '' or profile.first_name == first_name) & \
            (last_name == '' or profile.last_name == last_name) & \
            (grad_year == '' or profile.grad_year == grad_year) & \
            (college == '' or profile.college == college) & \
            (major == '' or profile.major == major) & \
            (city == '' or profile.city == city) & \
            (state == '' or profile.state == state) &  \
            (country == '' or profile.country == country) & \
            (zip == '' or profile.zip == zip) & \
            (job == '' or profile.job == job) & \
            (employer == '' or profile.job == employer)):
                # add sorting by field and hs_activities
                matched_profiles.append(profile)

        return render(request,'results.html', {'profiles':matched_profiles})
    else:
        return render(request, 'search.html')
