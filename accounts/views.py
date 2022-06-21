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
                # Fix error message to render HTML template instead
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
                state = request.POST.get('inputstate', None)
                country = request.POST['inputcountry']
                zip = request.POST['inputzip']
                employer = request.POST['inputemployer']
                job = request.POST['inputjobtitle']
                # fixes MultiValueDictKey Error
                field = request.POST.getlist('inputfield', None)
                # fixes MultiValueDictKey Error
                hs_activities = request.POST.getlist('inputclubs', None)
                newsletter = request.POST.get('newsletter', False)
                if (newsletter == 'on'):
                    newsletter = True
                interview = request.POST.get('interview', False)
                if (interview == 'on'):
                    interview = True

                alumniprof = AlumniProf(
                first_name = first_name, last_name = last_name,
                grad_year = grad_year, college = college,
                major = major, city = city,
                state = state, country = country,
                zip = zip, employer = employer,
                job = job, field = field,
                hs_activities = hs_activities, 
                newsletter = newsletter,
                interview = interview,
                user = user
                )
                alumniprof.save()
                return redirect('home')
        else:
            # fix error message to render HTML template
            return render(request,'signup.html',{'error':'Passwords must match'})
    else:
        return render(request, 'signup.html')

@login_required(login_url='/accounts/signup')
def logout(request):
    if request.method=='POST':
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
        field = request.POST.getlist('inputfield', None)
        hs_activities = request.POST.getlist('inputclubs', None)
        newsletter = request.POST.get('newsletter', False)
        if (newsletter == 'on'):
            newsletter = True
        interview = request.POST.get('interview', False)
        if (interview == 'on'):
            interview = True

        # if not field:
        #     field = ""
        # else:
        #     field = field[0]

        # if not hs_activities:
        #     hs_activities = ""
        # else:
        #     hs_activities = hs_activities[0]

        AlumniProf.objects.get(user=request.user).delete()
        alumniprof = AlumniProf(
        first_name = first_name, last_name = last_name,
        grad_year = grad_year, college = college,
        major = major, city = city,
        state = state, country = country,
        zip = zip, employer = employer,
        job = job, field = field,
        hs_activities = hs_activities, 
        newsletter = newsletter,
        interview = interview,
        user = request.user
        )
        alumniprof.save()
        return render(request, 'home.html')
    else:
        alumniprof = AlumniProf.objects.get(user = request.user)
        if(alumniprof == None):
            return redirect('home')

        first_name = alumniprof.first_name
        last_name = alumniprof.last_name
        grad_year = alumniprof.grad_year
        college = alumniprof.college
        major = alumniprof.major
        city = alumniprof.city
        state = alumniprof.state
        country = alumniprof.country
        zip = alumniprof.zip
        employer = alumniprof.employer
        job = alumniprof.job
        field = alumniprof.field
        hs_activities = alumniprof.hs_activities
        newsletter = alumniprof.newsletter
        interview = alumniprof.interview

        return render(request, 'editprofile.html',{'first_name':first_name, 'last_name':last_name,'grad_year':grad_year,
        'college':college, 'major':major,'city':city,'state':state, 'country':country,'zip':zip, 'employer':employer,
        'job':job,'field':field, 'hs_activities':hs_activities, 'newsletter':newsletter, 'interview':interview})
