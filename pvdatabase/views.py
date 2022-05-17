from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

        # 1. get all profiles
        # 2. check which of the filtering paramters are not null
        # 3.filter the list of profiles by the parameters
        profiles = AlumniProf.objects.all()
        matched_profiles = []
        for profile in profiles: # filtering profiles
            if( \\
            (first_name == "" || profile.first_name == first_name) && \
            (last_name == "" || profile.last_name == last_name) && \
            (grad_year == "" || profile.grad_year == grad_year) && \
            (college == "" || profile.college == college) && \
            (major == "" || profile.major == major) && \
            (city == "" || profile.city == city) && \
            (state == "" || profile.state == state) &&  \
             (country == "" || profile.country == country) && \
            (zip == "" || profile.zip == zip) && \
            (job == "" || profile.job == job) &&) \
            (employer == "" || profile.job == employer)):
                # add sorting by field and hs_activities
                matched_profiles.append(profile)

        return render(request,'buddyrequest/database.html',{'profiles':matched_profiles})
    else:
        return render(request, 'search.html')
