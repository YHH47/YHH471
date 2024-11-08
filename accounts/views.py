from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from accounts.form import UserCreateForm, UserloginForm
from django.contrib.auth.forms import AuthenticationForm

def signupaccount(request) :
    if request.method == 'GET':
        return render(request,'signupaccount.html',{'form':UserCreateForm})
    else:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        if len(password1)<8:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': '你的密码必须包含至少 8 个字符。'})
        if password1.isdigit():
            return render(request, 'signupaccount.html',{'form': UserCreateForm, 'error': '你的密码不能全都是数字。' })
        common_passwords = ["12345678", "password", "abcdefgh"]
        if password1.lower() in common_passwords:
            return render(request, 'signupaccount.html',{'form': UserCreateForm, 'error': '你的密码不能是一个常见密码。' })
        for info in username:
            if password1.lower() in info.lower():
                return render(request, 'signupaccount.html',{'form': UserCreateForm, 'error': '你的密码不能与你的其他个人信息太相似。' })
        if password1 and password2 and password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('moviehome')
            except IntegrityError:
                return render(request, 'signupaccount.html',{'form': UserCreateForm, 'error': '用户已存在' })
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': '输入的密码不一致'})
def logoutaccount(request):
    logout(request)
    return redirect('loginaccount')
def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': UserloginForm})
    else:
        user = authenticate(request,
        username=request.POST['username'] ,
        password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form':UserloginForm, 'error':'用户名或密码错误' })
        else:
            login(request, user)
            return redirect('moviehome')
