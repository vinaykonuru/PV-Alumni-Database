from sre_parse import SPECIAL_CHARS
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
        relation = request.POST.get('inputrelation', None)
        first_name = request.POST['inputfirstname']
        last_name = request.POST['inputlastname']
        grad_year = request.POST['inputyear']
        college = request.POST['inputcollege']
        major = request.POST['inputmajor']
        city = request.POST['inputcity']
        state = request.POST.getlist('inputstate')
        country = request.POST['inputcountry']
        employer = request.POST['inputemployer']
        job = request.POST['inputjobtitle']
        field = request.POST.getlist('inputfield', None)
        hs_activities = request.POST.getlist('inputclubs', None)
        newsletter = request.POST.get('newsletter', False)
        if (newsletter == 'on'):
            newsletter = True
        interview = request.POST.get('interview', False)
        if (interview == 'on'):
            interview = True

        print(state)
        if not state:
            state = ""
        else:
            state = state[0]
        # 1. get all profiles
        # 2. if filter is empty or if the profile matches the filter, include
        # it in search results
        profiles = AlumniProf.objects.all()
        matched_profiles = []

        # convert to sets to search subsets of lists
        if field != '':
            fieldset1 = set(field)
        else:
            fieldset1 = field
        if hs_activities != '':
            activityset1 = set(hs_activities)
        else:
            activityset1 = hs_activities

        for profile in profiles: # filtering profiles
            # convert to sets to search subsets of lists
            if profile.field != '':
                fieldset2 = set(profile.field)
            else: 
                fieldset2 = profile.field
            if profile.hs_activities != '':
                activityset2 = set(profile.hs_activities)
            else:
                activityset2 = profile.hs_activities

            if( \
            (relation == '' or relation in profile.relation) & \
            (first_name == '' or first_name.upper() in profile.first_name.upper()) & \
            (last_name == '' or last_name.upper() in profile.last_name.upper()) & \
            (grad_year == '' or profile.grad_year == grad_year) & \
            (college == '' or college.upper() in profile.college.upper()) & \
            (major == '' or major.upper() in profile.major.upper()) & \
            (city == '' or city.upper() in profile.city.upper()) & \
            (state == '' or state in profile.state) &  \
            (country == '' or country.upper() in profile.country.upper()) & \
            (job == '' or job in profile.job) & \
            (employer == '' or employer in profile.employer) & \
            (field == '' or fieldset1.issubset(fieldset2)) & \
            (hs_activities == '' or activityset1.issubset(activityset2)) & \
            (newsletter == False or newsletter == profile.newsletter) & \
            (interview == False or interview == profile.interview)):
                # add sorting by field and hs_activities
                matched_profiles.append(profile)

        return render(request,'results.html', {'profiles':matched_profiles})
    else:
        return render(request, 'search.html')

def profile(request, first_name, last_name):
    profiles = AlumniProf.objects.all()

    for profile in profiles:
        if (profile.first_name.upper() == first_name.upper()) and (profile.last_name.upper() == last_name.upper()):
            matched_profile = profile

            # put fields and activities in correct format to display
            if (matched_profile.field == "[]"):
                matched_profile.field == ''
            else:
                matched_profile.field = matched_profile.field.replace('[','')
                matched_profile.field = matched_profile.field.replace(']', '')
                matched_profile.field = matched_profile.field.replace("'", '')
            if (matched_profile.hs_activities == "[]"):
                matched_profile.hs_activities == ''
            else:
                matched_profile.hs_activities = matched_profile.hs_activities.replace('[','')
                matched_profile.hs_activities = matched_profile.hs_activities.replace(']', '')
                matched_profile.hs_activities = matched_profile.hs_activities.replace("'", '')

    return render(request, 'profile.html', {'profile':matched_profile})