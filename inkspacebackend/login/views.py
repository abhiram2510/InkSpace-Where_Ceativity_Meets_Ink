from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def index(request):
    return render(request,'index.html')
    
def signIn(request):
    if request.method == "POST":
        usern = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username=usern,password=passw)
        print(usern,passw)
        if user is not None:
            login(request,user)
            if request.user.is_authenticated:
                return redirect('home/')
            else:
                return render(request,'index.html')

        else:
            return render(request,'index.html')

    else:
        return render(request,'index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('signIn/')
    

def signUp(request):
    return render(request,'index.html')