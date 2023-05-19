from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        lname = request.POST.get('lname','')
        password = request.POST.get('lpass','')
        if lname == '':
            messages.error(request,'Username cannot be empty')
            return redirect('/accounts/login/')
        if password == '':
            messages.error(request,'Password cannot be empty')
            return redirect('/accounts/login/')
        user = auth.authenticate(username=lname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Login details doesn\'t exists')
            return redirect('/accounts/login/')


    return render(request,'login.html')

def signin(request):
    if request.method == 'POST':
        sname = request.POST.get('sname','')
        semail = request.POST.get('semail', '')
        spass1 = request.POST.get('spass1', '')
        spass2 = request.POST.get('spass2', '')
        if sname == '':
            messages.error(request,'Username can\'t be empty')
            return redirect('/accounts/signin/')
        if semail == '':
            messages.error(request,'E-mail can\'t be empty')
            return redirect('/accounts/signin/')
        if spass1 == '':
            messages.error(request,'Password can\'t be empty')
            return redirect('/accounts/signin/')
        if spass1 == spass2:
            collect_1 = User.objects.filter(username=sname)
            if len(collect_1) == 0:
                collect_2 = User.objects.filter(email=semail)
                if len(collect_2) == 0:
                    user = User.objects.create_user(username=sname,email=semail,password=spass1)
                    messages.success(request,'success')
                    return redirect('/accounts/login/')
                else:
                    messages.error(request,'E-mail already exists')
                    return redirect('/accounts/signin/')
            else:
                messages.error(request, 'Username already exists')
                return redirect('/accounts/signin/')
        else:
            messages.error(request, 'Password mismatches')
            return redirect('/accounts/signin/')


    else:
        return render(request,'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')





