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

RELATIONSLIST = ['Student (Current/Former)',
                 'Teacher (Current/Former)',
                 'Administration (Current/Former)',
                 'Parent of Current/Former Student']

DEGREESLIST = ['Associate of Arts (A.A.)',
               'Associate of Science (A.S.)',
               'Bachelor of Arts (B.A.)',
               'Bachelor of Science (B.S.)',
               'Bachelor of Fine Arts (B.F.A.)',
               'Master of Arts (M.A.)',
               'Master of Science (M.S.)',
               'Master of Business Administration (M.B.A.)',
               'Doctor of Philosophy (Ph.D.)',
               'Doctor of Education (Ed.D.)',
               'Doctor of Dental Surgery (D.D.S.)',
               'Doctor of Optometry (O.D.)',
               'Doctor of Osteopathic Medicine (D.O.)',
               'Doctor of Podiatric Medicine (D.P.M)',
               'Doctor of Medicine (M.D.)',
               'Juris Doctor (J.D.)'
               ]

# Reg expression for validating email
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Reg expression for validating password 
regex_password = r'^(?=.*[A-Z])(?=.*[0-9]).{8,32}$'

# server-side email and password validator
def check(email, password):
    if(re.fullmatch(regex_email, email) and re.fullmatch(regex_password, password)):
        return False
    else:
        return True

# server-side length of fields validator
def checklengths(firstname, lastname, email, password1, password2, year, college, major, city, country, zip, employer, job):
    if (len(firstname) > 30 or
        len(lastname) > 30 or
        len(email) > 30 or
        len(password1) > 30 or
        len(password2) > 30 or
        len(year) > 4 or
        len(college) > 30 or
        len(major) > 30 or
        len(city) > 30 or
        len(country) > 30 or
        len(zip) > 10 or
        len(employer) > 30 or
        len(job) > 30):
            return True
    return False

# server-side validation for fields
def checkfields(fields, activities, state, relation, degrees):
    fieldset1 = set(fields)
    fieldset2 = set(FIELDSLIST)

    activityset1 = set(activities)
    activityset2 = set(HSACTIVITIESLIST)

    degreeset1 = set(degrees)
    degreeset2 = set(DEGREESLIST)

    if ((bool(fields) and not fieldset1.issubset(fieldset2)) or (bool(activities) and not activityset1.issubset(activityset2)) or (state is not None and state not in STATESLIST) or (relation is not None and relation not in RELATIONSLIST) or (bool(degrees) and not degreeset1.issubset(degreeset2))):
        return True
    return False

def login(request):
    if request.method=='POST':
        # server-side validation
        if (
                len(request.POST['inputemail']) > 30 or
                len(request.POST['inputpassword']) > 30
            ):
                return render(request, 'login.html', {'error':'One of your fields is longer than its character limit. Try again.', 
                                                      "email":request.POST['inputemail'], "password":request.POST['inputpassword']})

        if check(request.POST['inputemail'], request.POST['inputpassword']):
            return render(request, 'login.html', {'error':'Enter a valid email and password.', 
                                                  "email":request.POST['inputemail'], "password":request.POST['inputpassword']})
                    
        user=auth.authenticate(username=request.POST['inputemail'], password=request.POST['inputpassword'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Enter a valid email and password.', 
                                                "email":request.POST['inputemail'], "password":request.POST['inputpassword']})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        if request.POST['inputpassword1']==request.POST['inputpassword2']:
            # server-side validation for same first and last name as another user
            try:
                user=User.objects.get(first_name = request.POST.get('inputfirstname'), last_name = request.POST.get('inputlastname'))
                return render(request, 'signup.html', {'error':'Your first and last name already match an account in the database.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})
            except:
                pass

            try:
                user=User.objects.get(username = request.POST['inputemail'])
                return render(request, 'signup.html', {'error':'This email has already been taken.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})
            except User.DoesNotExist:
                # Server-side validation for lengths
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
                    return render(request, 'signup.html', {'error':'One of your fields is longer than its character limit. Try again.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})

                # Server side validation for email and password using regex's
                if check(request.POST['inputemail'], request.POST['inputpassword1']):
                    return render(request, 'signup.html', {'error':'Enter a valid email and password.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})

                # Server-side validation for firstname, lastname (required fields)
                if request.POST['inputfirstname'] == "" or request.POST['inputlastname'] == "":
                    return render(request, 'signup.html', {'error':'Please make sure to input a first name and/or last name.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})
                
                # Server-side validation for Terms of Service
                if request.POST.get('tos') != "on":
                    return render(request, 'signup.html', {'error':'Please make sure to agree to the Terms of Service.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})

                # Server-side validation for fields, activities, and state
                if checkfields(request.POST.getlist('inputfield', None), request.POST.getlist('inputclubs', None), request.POST.get('inputstate', None), request.POST.get('inputrelation', None), request.POST.getlist('inputdegrees', None)):
                    return render(request, 'signup.html', {'error':'Please enter valid state, fields, and activities.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})

                user=User.objects.create_user(username = request.POST['inputemail'],password=request.POST['inputpassword1'], first_name=request.POST['inputfirstname'], last_name=request.POST['inputlastname'])
                auth.login(request,user)
                relation = request.POST.get('inputrelation', None)
                first_name = request.POST['inputfirstname']
                last_name = request.POST['inputlastname']
                grad_year = request.POST['inputyear']
                college = request.POST.get('inputcollege', "")
                major = request.POST.get('inputmajor', "")
                degrees = request.POST.getlist('inputdegrees', None)
                city = request.POST.get('inputcity', "")
                state = request.POST.get('inputstate', None)
                country = request.POST.get('inputcountry', "")
                zip = request.POST['inputzip']
                employer = request.POST.get('inputemployer', "")
                job = request.POST.get('inputjobtitle', "")
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
                relation = relation, 
                first_name = first_name, last_name = last_name,
                grad_year = grad_year, college = college,
                major = major, degrees = degrees, city = city,
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
            return render(request,'signup.html',{'error':'Passwords must match',"states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                        "activerelation":request.POST.get('inputrelation', None),
                                                        "firstname":request.POST['inputfirstname'],
                                                        "lastname":request.POST['inputlastname'],
                                                        "email":request.POST['inputemail'],
                                                        "password1":request.POST['inputpassword1'],
                                                        "password2":request.POST['inputpassword2'],
                                                        "year":request.POST['inputyear'],
                                                        "college":request.POST['inputcollege'],
                                                        "major":request.POST['inputmajor'],
                                                        "activedegrees":request.POST.getlist('inputdegrees', None),
                                                        "city":request.POST['inputcity'],
                                                        "country":request.POST['inputcountry'],
                                                        "zip":request.POST['inputzip'],
                                                        "employer":request.POST['inputemployer'],
                                                        "jobtitle":request.POST['inputjobtitle'],
                                                        "activefields":request.POST.getlist('inputfield', None),
                                                        "activeactivities":request.POST.getlist('inputclubs', None),
                                                        "activestate":request.POST.get('inputstate', None),
                                                        "newsletter":request.POST.get('newsletter'),
                                                        "interview":request.POST.get('interview')})
    else:
        return render(request, 'signup.html', {"states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST})

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
        # Server-side validation for fields, activities, and state
        if checkfields(request.POST.getlist('inputfield', None), request.POST.getlist('inputclubs', None), request.POST.get('inputstate', None), request.POST.get('inputrelation', None), request.POST.getlist('inputdegrees', None)):
            return render(request, 'editprofile.html', {'error':'Please enter valid state, fields, and activities.', "states":STATESLIST, "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                "activerelation":request.POST.get('inputrelation', None),
                                                "firstname":request.POST['inputfirstname'],
                                                "lastname":request.POST['inputlastname'],
                                                "year":request.POST['inputyear'],
                                                "college":request.POST['inputcollege'],
                                                "major":request.POST['inputmajor'],
                                                "activedegrees":request.POST.getlist('inputdegrees', None),
                                                "city":request.POST['inputcity'],
                                                "country":request.POST['inputcountry'],
                                                "zip":request.POST['inputzip'],
                                                "employer":request.POST['inputemployer'],
                                                "jobtitle":request.POST['inputjobtitle'],
                                                "activefields":request.POST.getlist('inputfield', None),
                                                "activeactivities":request.POST.getlist('inputclubs', None),
                                                "activestate":request.POST.get('inputstate', None),
                                                "newsletter":request.POST.get('newsletter'),
                                                "interview":request.POST.get('interview')})

        # Server-side validation of lengths
        if checklengths(
                request.POST['inputfirstname'],
                request.POST['inputlastname'],
                '',
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
                    return render(request, 'editprofile.html', {'error':'One of your fields is longer than its character limit. Try again.',"states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                "activerelation":request.POST.get('inputrelation', None),
                                                "firstname":request.POST['inputfirstname'],
                                                "lastname":request.POST['inputlastname'],
                                                "year":request.POST['inputyear'],
                                                "college":request.POST['inputcollege'],
                                                "major":request.POST['inputmajor'],
                                                "activedegrees":request.POST.getlist('inputdegrees', None),
                                                "city":request.POST['inputcity'],
                                                "country":request.POST['inputcountry'],
                                                "zip":request.POST['inputzip'],
                                                "employer":request.POST['inputemployer'],
                                                "jobtitle":request.POST['inputjobtitle'],
                                                "activefields":request.POST.getlist('inputfield', None),
                                                "activeactivities":request.POST.getlist('inputclubs', None),
                                                "activestate":request.POST.get('inputstate', None),
                                                "newsletter":request.POST.get('newsletter'),
                                                "interview":request.POST.get('interview')})
        
        # Server-side validation for firstname, lastname (required fields)
        if request.POST['inputfirstname'] == "" or request.POST['inputlastname'] == "":
            return render(request, 'editprofile.html', {'error':'Please make sure to input a first name and/or last name.', "states":STATESLIST, "fields":FIELDSLIST, "activities":HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST,
                                                "activerelation":request.POST.get('inputrelation', None),
                                                "firstname":request.POST['inputfirstname'],
                                                "lastname":request.POST['inputlastname'],
                                                "year":request.POST['inputyear'],
                                                "college":request.POST['inputcollege'],
                                                "major":request.POST['inputmajor'],
                                                "activedegrees":request.POST.getlist('inputdegrees', None),
                                                "city":request.POST['inputcity'],
                                                "country":request.POST['inputcountry'],
                                                "zip":request.POST['inputzip'],
                                                "employer":request.POST['inputemployer'],
                                                "jobtitle":request.POST['inputjobtitle'],
                                                "activefields":request.POST.getlist('inputfield', None),
                                                "activeactivities":request.POST.getlist('inputclubs', None),
                                                "activestate":request.POST.get('inputstate', None),
                                                "newsletter":request.POST.get('newsletter'),
                                                "interview":request.POST.get('interview')})
        
        relation = request.POST.get('inputrelation', None)
        first_name = request.POST['inputfirstname']
        last_name = request.POST['inputlastname']
        grad_year = request.POST['inputyear']
        college = request.POST['inputcollege']
        major = request.POST['inputmajor']
        degrees = request.POST.getlist('inputdegrees', None)
        print(degrees)
        city = request.POST['inputcity']
        state = request.POST.get('inputstate', None)
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

        AlumniProf.objects.get(user=request.user).delete()
        alumniprof = AlumniProf(
        relation = relation,
        first_name = first_name, last_name = last_name,
        grad_year = grad_year, college = college,
        major = major, degrees = degrees, city = city,
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

        relation = alumniprof.relation
        first_name = alumniprof.first_name
        last_name = alumniprof.last_name
        grad_year = alumniprof.grad_year
        college = alumniprof.college
        major = alumniprof.major
        degrees = alumniprof.degrees
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

        return render(request, 'editprofile.html',{'activerelation':relation, 'firstname':first_name, 'lastname':last_name, 'year':grad_year, 'college':college, 'major':major, 'activedegrees':degrees, 'city':city, 'activestate':state, 'country':country,'zip':zip, 'employer':employer, 'jobtitle':job,'activefields':field, 'activeactivities':hs_activities, 'newsletter':newsletter, 'interview':interview, 'states':STATESLIST, 'fields':FIELDSLIST, 'activities':HSACTIVITIESLIST, "relations":RELATIONSLIST, "degrees":DEGREESLIST})

@login_required(login_url='/accounts/signup')
def changelogin(request):
    if request.method == 'POST':
        # server-side validation for lengths and regex expressions
        if (
                len(request.POST['inputemail']) > 30 or
                len(request.POST['inputpassword']) > 30
            ):
                return render(request, 'changelogin.html', {'error':'One of your fields is longer than its character limit. Try again.', 
                                                      "email":request.POST['inputemail'], "password":request.POST['inputpassword']})

        if check(request.POST['inputemail'], request.POST['inputpassword']):
            return render(request, 'changelogin.html', {'error':'Enter a valid email and password.', 
                                                  "email":request.POST['inputemail'], "password":request.POST['inputpassword']})

        if request.POST["inputemail"] != "" and request.POST["inputpassword"] != "":
            oldAlumniProf = AlumniProf.objects.get(user=request.user)
            current_user = request.user
            oldusername = current_user.username
            oldfirstname = current_user.first_name
            oldlastname = current_user.last_name
            newusername = request.POST["inputemail"]
            try:
                request.user.delete()
                User.objects.get(username = newusername)
                request.user = User.objects.create_user(username = oldusername, password=request.POST["inputpassword"], first_name=oldfirstname, last_name=oldlastname)
                request.user.save()
                alumniprof = AlumniProf(
                relation = oldAlumniProf.relation,
                first_name = oldAlumniProf.first_name, last_name = oldAlumniProf.last_name,
                grad_year = oldAlumniProf.grad_year, college = oldAlumniProf.college,
                major = oldAlumniProf.major, degrees = oldAlumniProf.degrees, city = oldAlumniProf.city,
                state = oldAlumniProf.state, country = oldAlumniProf.country,
                zip = oldAlumniProf.zip, employer = oldAlumniProf.employer,
                job = oldAlumniProf.job, field = oldAlumniProf.field,
                hs_activities = oldAlumniProf.hs_activities, 
                newsletter = oldAlumniProf.newsletter,
                interview = oldAlumniProf.interview,
                user = request.user
                )
                oldAlumniProf.delete()
                alumniprof.save()
                return render(request, 'login.html', {"error": "Your new email has already been taken. Please log in again with your original credentials."})
            except User.DoesNotExist:
                request.user = User.objects.create_user(username = newusername ,password=request.POST["inputpassword"], first_name=oldfirstname, last_name=oldlastname)
                request.user.save()
                alumniprof = AlumniProf(
                relation = oldAlumniProf.relation,
                first_name = oldAlumniProf.first_name, last_name = oldAlumniProf.last_name,
                grad_year = oldAlumniProf.grad_year, college = oldAlumniProf.college,
                major = oldAlumniProf.major, degrees = oldAlumniProf.degrees, city = oldAlumniProf.city,
                state = oldAlumniProf.state, country = oldAlumniProf.country,
                zip = oldAlumniProf.zip, employer = oldAlumniProf.employer,
                job = oldAlumniProf.job, field = oldAlumniProf.field,
                hs_activities = oldAlumniProf.hs_activities, 
                newsletter = oldAlumniProf.newsletter,
                interview = oldAlumniProf.interview,
                user = request.user
                )
                oldAlumniProf.delete()
                alumniprof.save()
                return render(request, 'login.html', {'error':'Please login again with your new email and password.', 'email':newusername})
    else:
        return render(request, 'changelogin.html')