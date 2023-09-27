from django.shortcuts import render,redirect
from .models import studentSignup
from .forms import StudentSignupForm,StudentUpdateForm,StudentQueryform
from django.contrib.auth import logout
from django.core.mail import send_mail
from institutemanagement import settings
# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
    cuser=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=StudentSignupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                #Email Sending
                sub="Thank you"
                msg=f"Hello Student!\n\n Thanks For Login Our Site\n\n institute Management Team\n +91 7046297375 "
                from_ID=settings.EMAIL_HOST_USER
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']
            
            userid=studentSignup.objects.get(username=unm)
            print("Current User:",userid.id)

            user=studentSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm #create a session
                request.session['userid']=userid.id
                return redirect('studentQuery')
            else:
                print("Error! Username or Password invalid...")
    return render(request,'student.html',{'cuser':cuser})

def studentQuery(request):
    cuser=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=StudentSignupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']
            
            userid=studentSignup.objects.get(username=unm)
            print("Current User:",userid.id)

            user=studentSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm #create a session
                request.session['userid']=userid.id
                return redirect('studentQuery')
            else:
                print("Error! Username or Password invalid...")
    if request.method=='POST':
        newnotes=StudentQueryform(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request,'studentquery.html',{'cuser':cuser})


def studentprofile(request):
    cuser=request.session.get('user')
    userid=request.session.get('userid')
    data=studentSignup.objects.get(id=userid)
    if request.method=='POST':
        update=StudentUpdateForm(request.POST,instance=data)
        if update.is_valid():
            update.save()
            print("Your profile has been updated!")
            return redirect('student')
        else:
            print(update.errors)
    return render(request,'studentprofile.html',{'cuser':cuser,'userid':data})

def userlogout(request):
    logout(request)
    return redirect('student')