from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from alumniprof.models import AlumniProf
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is not correct'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        if request.POST['inputpassword1']==request.POST['inputpassword2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['inputpassword1'])
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
                first_name = firstname, last_name = last_name,
                grad_year = grad_year, college = college,
                major = major, city = city,
                state = state, country = country,
                zip = zip, employer = employer,
                job = job, field = field,
                hs_activities = hs_activities, user = user
                )
                alumniprof.save()
                return redirect('home')

        else:
            return render(request,'signup.html',{'error':'Passwords must match'})
    else:
        return render(request, 'signup.html')

def logout(request):
    print('hello1')
    if request.method=='POST':
        print('hello')
        auth.logout(request)
        return redirect('home')

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
    else:
        return render(request, 'editprofile.html')
