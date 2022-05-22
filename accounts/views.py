from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from alumniprof.models import AlumniProf
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['inputemail'],password=request.POST['inputpassword'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Username or password is not correct'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        if request.POST['inputpassword1']==request.POST['inputpassword2']:
            try:
                user=User.objects.get(username = request.POST['inputemail'])
                return render(request, 'signup.html', {'error':'Email has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(username = request.POST['inputemail'],password=request.POST['inputpassword1'])
                auth.login(request,user)
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

                alumprof = AlumniProf(
                first_name = first_name, last_name = last_name,
                grad_year = grad_year, college = college,
                major = major, city = city,
                state = state, country = country,
                zip = zip, employer = employer,
                job = job, field = field,
                hs_activities = hs_activities, user = user
                )
                alumprof.save()
                return redirect('home')
        else:
            return render(request,'signup.html',{'error':'Passwords must match'})
    else:
        return render(request, 'signup.html')

@login_required(login_url='/accounts/signup')
def logout(request):
    if request.method=='POST':
        print('hello')
        auth.logout(request)
        return redirect('home')


def reset(request):
    if(request.method == 'POST'):
        email = request.POST['reset_email']
        return render(request, 'password_resent_sent.html')
    else:
        return render(request, 'forgotpassword.html')

@login_required(login_url='/accounts/signup')
def edit(request):
    if request.method == 'POST':
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

        alumprof = AlumniProf(
        first_name = firstname, last_name = last_name,
        grad_year = grad_year, college = college,
        major = major, city = city,
        state = state, country = country,
        zip = zip, employer = employer,
        job = job, field = field,
        hs_activities = hs_activities, user = user
        )
        alumniprof.save()
        return render(request, 'home.html')
    else:
        alumprof = AlumniProf.objects.get(user = request.user)
        if(alumprof == None):
            return redirect('home')

        first_name = alumprof.first_name
        last_name = alumprof.last_name
        grad_year = alumprof.grad_year
        college = alumprof.college
        major = alumprof.major
        city = alumprof.city
        state = alumprof.state
        country = alumprof.country
        zip = alumprof.zip
        employer = alumprof.employer
        job = alumprof.job
        field = alumprof.field
        hs_activities = alumprof.hs_activities

        return render(request, 'editprofile.html',{'first_name':first_name, 'last_name':last_name,'grad_year':grad_year,
        'college':college, 'major':major,'city':city,'state':state, 'country':country,'zip':zip, 'employer':employer,
        'job':job,'field':field, 'hs_activities':hs_activities})
