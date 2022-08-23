from email import message
from http.client import HTTPResponse
from itertools import count
from django.http import HttpResponse
from lib2to3.pgen2 import token
from random import randint, random
from sqlite3 import paramstyle
from telnetlib import LOGOUT
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Blogpost
from django.views.generic import ListView
from .models import contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def index(request):
    blogs = Blogpost.objects.all()
    limit_max=30
    n=len(blogs)
    params={'blogs':blogs,'strlen':n,'lim':limit_max}
    return render(request,"blogapp/index.html",params)

def search(request):
    if request.method =="GET":
        k = request.GET.get('key')
        blogs = Blogpost.objects.all()
        msg="search result IS:"
        for blog in blogs:
            temp_tags = blog.tags.names()
            for t in temp_tags:
                # print(t,end="\t")
                if t.lower() == k.lower() :
                    tar = blog.id
                    blog=Blogpost.objects.filter(id=tar)
                    # params = {'msg' :msg }
                    return render ( request, 'blogapp/searchview.html',{ 'blog':blog[0] ,'msg':msg} )
        return render(request,"blogapp/index.html")


def contact_view(request):
    if request.method =="POST":
        name = request.POST.get('name')
        # print(name)
        return render(request,"blogapp/contact.html")
    else:
        return render(request, "blogapp/contact.html")

def feed(request):
    name=request.POST.get('name')
    qstn=request.POST.get('querry')
    mail=request.POST.get('email')
    phone=request.POST.get('phone')
    temp_contact = contact(name = name , phonenum = phone , email = mail , querry = qstn )
    temp_contact.save()
    params={'username':name,'question':qstn,'mail':mail,'contact_number':phone}
    return render(request,"blogapp/feedgone.html",params)


def about(request):
    return render(request,"blogapp/about.html")

def donation(request):
    return render(request,"blogapp/donation.html")

def faqs(request):
    return render(request,"blogapp/faqs.html")

def userlogin(request):
    return render(request,"blogapp/login.html")

def signup(request):
    return render(request,"blogapp/signup.html")

def aboutblogs(request):
    return render(request,"blogapp/aboutblogs.html")

def topbloggers(request):
    return render(request,"blogapp/topbloggers.html")

def password_strength(pp):
    return 45
def postablog(request):
    return render (request, 'blogapp/postablog.html')

def blogbeforeview(request,myid):
    blog=Blogpost.objects.filter(id=myid)
    return render ( request, 'blogapp/blogbeforeviewview.html',{ 'blog':blog[0] })

def handle_sign_up(request):
    if request.method =="POST":
        mail=request.POST.get('mail')
        passkey1=request.POST.get('abc')
        passkey2=request.POST.get('abcd')
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        u=request.POST.get('username')
        role=request.POST.get('role')
        permi=request.POST.get('permi')

        #checking / validating the form 
        if passkey1!=passkey2:
            messages.error(request,'passwords dont match')
            return redirect('/blog/signup')
            # return render(request,'blogapp/sign-up.html',{'any_warning1':'passwords dont match'})
        elif len(passkey1) <= 8:
            messages.error(request,'password too short minimum characters are 8')
            return redirect('/blog/signup')
        elif password_strength(passkey1) < 40:
            messages.error(request,'passwords weak')
            # return redirect('/blog/signup')
        
        elif len(u) > 8:
            messages.error(request,'password too short')
            return redirect('/blog/signup')
            # return render(request,'blogapp/sign-up.html',{'any_warning1':'username too long'})
        
        else:
            myuser = User.objects.create_user(u,mail,passkey1)
            myuser.first_name=f
            myuser.last_name =l
            myuser.role=role
            myuser.permissons=permi
            myuser.save()
            messages.success(request,"Profile created succesfully , ")
            return redirect('/blog/home')
    else:
        return HTTPResponse('error - 404 not found')


def accopen(request):
    if request.method =="POST":
        loginpasskey=request.POST.get('passkey')
        loginusername=request.POST.get('username')
        user=authenticate(username=loginusername,password=loginpasskey)
        if user is not None:
            login(request,user)
            messages.success(request,"profile is opened")
            return redirect('/blog/home')
        else:
            return  redirect('/blog/userlogin')


def accclose(request):
    if request.method =="POST":
        logout(request)
        messages.success(request,"see u again ")
        return redirect('/blog/home')
    else:
        logout(request)
        messages.success(request,"see u again ")
        return redirect('/blog/home')