from django.db.utils import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
import pyautogui
from .form import *
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
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
                return redirect('/home/')
            else:
                messages.warning(request,"Wrong password!")
                return render(request,'index.html')

        else:
            messages.warning(request,"Enter valid username/password")
            return render(request,'index.html')


    else:
        return render(request,'index.html')


def home(request):
    if request.user.is_authenticated:
        return redirect('/display/')
    else:
        return redirect('/signIn/')
    


def signUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password1']
        print(username,email,password1,password2)
        if(re.match(regex,email)):
            if password1 != password2:
                messages.warning(request,"Please check your password")
                return render(request,'signup.html')
            else:
                try:
                    myuser = User.objects.create_user(username,email,password1)
                    myuser.save()

                except IntegrityError as e:
                    messages.warning(request,"Username already exists!")
                    return render(request,'signUp.html')

                return redirect('/')
        else:
            messages.warning(request,"Please enter a valid Email ID")
            return render(request,'signUp.html')


    else:
        return render(request,'signUp.html')
    


def signInAgain(request):
    request.redirect('/signIn/')


def display(request):
    context = {'blogs':BlogModel.objects.all()}
    return render(request,'home.html',context)


def addBlog(request):
    context = {'form': BlogForm}
    try:
        if request.method =="POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']



            BlogModel.objects.create(user= user, title = title, content = content, image=image)

            return redirect('/display/')

    except Exception as e:
        print(e)

    return render(request,'addBlog.html',context)


def viewFullBlog(request):
    return render(request,'fullBlog.html')


def blog_detail(request,slug):
    context ={}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj

    except Exception as e:
        print(e)
    return render(request,'blog_detail.html',context)



def view_blog(request):
    context={}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user )
        context['blog_objs'] = blog_objs


    except Exception as e:
        print(e)
    return render(request,'view_blog.html',context)


def blog_delete(request,id):
    try:
        blog_obj = BlogModel.objects.get(id=id)
        if(blog_obj.user==request.user):
            blog_obj.delete()


    except Exception as e:
        print(e)

    return redirect('/view_blog/')


def blog_update(request,slug):
    context ={}
    try:
        blog_obj = BlogModel.objects.get(slug = slug)
        
        if(blog_obj.user!=request.user):
            return redirect('/')
        inital_dict ={'content': blog_obj.content}
        form = BlogForm(initial = inital_dict)
        if request.method =="POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']


            blog_obj = BlogModel.objects.get(slug=slug)
            blog_obj.delete()
            BlogModel.objects.create(user= user, title = title, content = content, image=image)

            return redirect("/display/")


        context['blog_obj'] = blog_obj
        context['form'] = form


    except Exception as e:
        print(e)

    return render(request,'update_blog.html',context)





def logout_view(request):
    logout(request)
    return redirect('/')
    
    
