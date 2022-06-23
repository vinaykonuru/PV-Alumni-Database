from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from alumniprof.models import AlumniProf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import re

# Create your views here.
FIELDSLIST = ["Accounting",
                    "Advertising"
                    ,"Architecture"
                    ,"Building/Construction"
                    ,"Consulting"
                    ,"Energy Resources"
                    ,"Engineering-Chemical"
                    ,"Engineering-Civil"
                    ,"Engineering-Electrical"
                    ,"Engineering-Mech./Aerospace"
                    ,"Engineering-Other"
                    ,"Environmental Affairs"
                    ,"Finance-Asset Management"
                    ,"Finance-Corporate Finance"
                    ,"Finance-Hedge Funds"
                    ,"Finance-Investment Mngmt."
                    ,"Finance-Private Equity"
                    ,"Finance-Commercial Banking"
                    ,"Finance-Financial Planning"
                    ,"Finance-Investment Banking"
                    ,"Finance-Other"
                    ,"Finance-Securities/Commodities"
                    ,"Finance-Tax, Trust, & Estate"
                    ,"Finance-Venture Capital"
                    ,"Foreign Service"
                    ,"Fundraising"
                    ,"Government Departments & Agencies"
                    ,"Government-Cabinet Member"
                    ,"Government-Executive"
                    ,"Government-Legislator"
                    ,"Government-Other"
                    ,"Government-Policy Analysis"
                    ,"Government-Politics"
                    ,"Government-White House Staff"
                    ,"Health Care-Mental"
                    ,"Health Care-Other"
                    ,"Health Care-Physical"
                    ,"Human Resources"
                    ,"Insurance"
                    ,"Law-Corporate"
                    ,"Law-Criminal"
                    ,"Law-Intellectual Property"
                    ,"Law-Litigation"
                    ,"Law-Other"
                    ,"Law-Patent/Copyright"
                    ,"Law-Tax"
                    ,"Law-Trusts & Estates"
                    ,"Management/Admin"
                    ,"Marketing/Sales"
                    ,"Military"
                    ,"Other"
                    ,"Performing Arts"
                    ,"Printing/Publishing"
                    ,"Public Relations"
                    ,"Radio/TV/Film/Theater"
                    ,"Real Estate"
                    ,"Religious Services"
                    ,"Research & Development"
                    ,"Social Work"
                    ,"Sports/Recreation"
                    ,"Teaching-Arts"
                    ,"Teaching-Humanities"
                    ,"Teaching-Other"
                    ,"Teaching-Science/Engineering"
                    ,"Teaching-Social Science"
                    ,"Technology-Biotechnology"
                    ,"Technology-E-Commerce"
                    ,"Technology-Hardware/Software Dev."
                    ,"Technology-Info. Services/Systems"
                    ,"Technology-Telecommunications"
                    ,"Technology-Other"
                    ,"Transportation/Travel"
                    ,"Veterinary Medicine"
                    ,"Visual/Fine Arts"
                    ,"Writing/Editing"]

HSACTIVITIESLIST =  ["Academic Olympics"
                    ,"A.K.H.L. (Achieve, Know, Help, Lead)"
                    ,"Anime Club"
                    ,"Anime Pride"
                    ,"Artificial Intelligence and Machine Learning Club"
                    ,"Astronomy Club"
                    ,"Aviation Club"
                    ,"Basketball Group"
                    ,"Biology Olympiad"
                    ,"Biomedical Engineering Club (BMES)"
                    ,"Book Club"
                    ,"buildOn"
                    ,"Business Professionals of America"
                    ,"Chess Club"
                    ,"C2 Community Contributions"
                    ,"Chinese Club"
                    ,"Chinese National Honor Society"
                    ,"Ciao! - The Italian Club"
                    ,"Coexistence Club"
                    ,"Competitive Programming Club"
                    ,"Cosplay"
                    ,"Crate Diggers (A Vinyl Record Club)"
                    ,"Current Events Club"
                    ,"Desi Club (Indian & South Asian Cultural Club)"
                    ,"Disc Golf Club"
                    ,"Dive Club"
                    ,"Diversifying & Integrating Gifted Schools (DIGS)"
                    ,"Doodle Club"
                    ,"Drama Club"
                    ,"Drone Club"
                    ,"Elementary Music Club"
                    ,"Elementary Student Council"
                    ,"Entrepreneur Club"
                    ,"Film Club"
                    ,"FIRST Robotics"
                    ,"Florida Future Educators of America (FFEA)"
                    ,"Gender & Sexuality Alliance (GSA)"
                    ,"National French Honor Society"
                    ,"Gardening Club"
                    ,"Health and Education Initiatives (HEI)"
                    ,"History Bowl"
                    ,"History Club"
                    ,"HOSA (Future Health Professionals)"
                    ,"Interact Club"
                    ,"International Current Events Debate (ICED)"
                    ,"Investors Club"
                    ,"Key Club"
                    ,"Linguistics Club"
                    ,"Luminary Magazine"
                    ,"Magic the Gathering"
                    ,"Marine Science Club"
                    ,"Math Club"
                    ,"MATHCOUNTS"
                    ,"MathWorks Math Modeling Challenge"
                    ,"Mock Trial"
                    ,"Model United Nations"
                    ,"MS Literary Magazine Club"
                    ,"National Art Honor Society"
                    ,"National French Honor Society"
                    ,"National Honor Society"
                    ,"National Junior Honor Society"
                    ,"Nature Club"
                    ,"Neuroscience Club"
                    ,"Odyssey of the Mind"
                    ,"Outreach for Impact"
                    ,"Overbooked"
                    ,"Peace Jam"
                    ,"Peer Mentoring"
                    ,"Philosophy Club"
                    ,"Photography"
                    ,"Poet Society"
                    ,"Political Action"
                    ,"Psi Alpha (Psychology Honor Society)"
                    ,"Puzzle Club"
                    ,"Red Cross Club"
                    ,"Rho Kappa Honor Society"
                    ,"Run Club"
                    ,"Russian Cultural Heritage"
                    ,"SAT Prep Club"
                    ,"Scholars 4 Scholars"
                    ,"Science National Honor Society"
                    ,"Science Olympiad"
                    ,"Signing @ PV - American Sign Language Club"
                    ,"Smash Club"
                    ,"Soccer Club"
                    ,"Spanish National Honor Society"
                    ,"Speech & Debate"
                    ,"Students for Asian Advocacy"
                    ,"Students Organized for Animal Rights (SOAR)"
                    ,"Students Working Against Tobacco (SWAT)"
                    ,"Technology Student Association (TSA)"
                    ,"Together Women Rise (TWR)"
                    ,"Tri-M Music Honor Society"
                    ,"Tree Huggers Environmental Club"
                    ,"UNICEF Club"
                    ,"Ultimate Frisbee Club"
                    ,"Unidos Now at Pine View"
                    ,"Uno Club"
                    ,"VEX Robotics"
                    ,"Women in Literature"
                    ,"Young Investors Society"
                    ,"Weight Lifting Club"]

STATESLIST = [  "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"]

# Reg expression for validating email
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Reg expression for validating password 
regex_password = r'^(?=.*[A-Z])(?=.*[0-9]).{8,32}$'

# server-side email and password validator
def check(email, password):
    if(re.fullmatch(regex_email, email) and re.fullmatch(regex_password, password)):
        pass
    else:
        return True

# server-side length of fields validator
def checklengths(firstname, lastname, email, password1, password2, year, college, major, city, country, zip, employer, job):
    if (len(firstname) > 30 or
        len(lastname) > 30 or
        len(email) > 30 or
        len(password1) > 30 or
        len(password2) > 30 or
        len(year) != 4 or
        len(college) > 30 or
        len(major) > 30 or
        len(city) > 30 or
        len(country) > 30 or
        len(zip) > 10 or
        len(employer) > 30 or
        len(job) > 30):
            return True
    return False

def login(request):
    if request.method=='POST':
        # server-side validation
        if (
                len(request.POST['inputemail']) > 30 or
                len(request.POST['inputpassword']) > 30
            ):
                return render(request, 'login.html', {'error':'One of your fields is longer than its character limit. Try again.'})

        if check(request.POST['inputemail'], request.POST['inputpassword']):
            return render(request, 'login.html', {'error':'Enter a valid email and password.'})
                    
        user=auth.authenticate(username=request.POST['inputemail'],password=request.POST['inputpassword'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Enter a valid email and password.'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        if request.POST['inputpassword1']==request.POST['inputpassword2']:
            try:
                user=User.objects.get(first_name = request.POST.get('inputfirstname'), last_name = request.POST.get('inputlastname'))
                return render(request, 'signup.html', {'error':'Your first and last name already match an account in the database.'})
            except:
                pass

            try:
                user=User.objects.get(username = request.POST['inputemail'])
                # Fix error message to render HTML template instead
                return render(request, 'signup.html', {'error':'This email has already been taken.'})
            except User.DoesNotExist:
                # Server-side validation 
                if checklengths(
                request.POST['inputfirstname'],
                request.POST['inputlastname'],
                request.POST['inputemail'],
                request.POST['inputpassword1'],
                request.POST['inputpassword2'],
                request.POST['inputyear'],
                request.POST['inputcollege'],
                request.POST['inputmajor'],
                request.POST['inputcity'],
                request.POST['inputcountry'],
                request.POST['inputzip'],
                request.POST['inputemployer'],
                request.POST['inputjobtitle']
                ):
                    return render(request, 'signup.html', {'error':'One of your fields is longer than its character limit. Try again.'})
                if check(request.POST['inputemail'], request.POST['inputpassword1']):
                    return render(request, 'signup.html', {'error':'Enter a valid email and password.'})

                user=User.objects.create_user(username = request.POST['inputemail'],password=request.POST['inputpassword1'], first_name=request.POST['inputfirstname'], last_name=request.POST['inputlastname'])
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
            return render(request,'signup.html',{'error':'Passwords must match',"states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST})
    else:
        return render(request, 'signup.html', {"states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST})

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
        if checklengths(
                request.POST['inputfirstname'],
                request.POST['inputlastname'],
                request.POST['inputemail'],
                '',
                '',
                request.POST['inputyear'],
                request.POST['inputcollege'],
                request.POST['inputmajor'],
                request.POST['inputcity'],
                request.POST['inputcountry'],
                request.POST['inputzip'],
                request.POST['inputemployer'],
                request.POST['inputjobtitle']
                ):
                    return render(request, 'signup.html', {'error':'One of your fields is longer than its character limit. Try again.'})
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
        'job':job,'field':field, 'hs_activities':hs_activities, 'newsletter':newsletter, 'interview':interview, 
        'fields_list':FIELDSLIST, 'hs_activities_list':HSACTIVITIESLIST})
