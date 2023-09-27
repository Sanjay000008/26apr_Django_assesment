from django.shortcuts import render,redirect
from .forms import TeacherSignupForm,TeacherUpdateForm
from .models import teacherSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from institutemanagement import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def teacher(request):
    cuser=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=TeacherSignupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                sub="Thank you"
                msg=f"Hello Teacher!\n\n Thanks For Login Our Site\n\n institute Management Team\n +91 7046297375 "
                from_ID=settings.EMAIL_HOST_USER
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']
            
            userid=teacherSignup.objects.get(username=unm)
            print("Current User:",userid.id)

            user=teacherSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm #create a session
                request.session['userid']=userid.id
                return redirect('teachersprofile')
            else:
                print("Error! Username or Password invalid...")
    return render(request,'teacher.html',{'cuser':cuser})

def teachersprofile(request):
    cuser=request.session.get('user')
    userid=request.session.get('userid')
    data=teacherSignup.objects.get(id=userid)
    if request.method=='POST':
        update=TeacherUpdateForm(request.POST,instance=data)
        if update.is_valid():
            update.save()
            print("Your profile has been updated!")
            return redirect('student')
        else:
            print(update.errors)
    return render(request,'teachersprofile.html',{'cuser':cuser,'userid':data})

def userlogout(request):
    logout(request)
    return redirect('teacher')