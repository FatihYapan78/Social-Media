from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
import string
# Kayıt Ol
def Register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        dogumt = request.POST.get('date')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if password == password2:
            Upchar = False
            Numchar = False
            Specialchar = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~."
            char = False
            for i in password:
                if i.isupper():
                    Upchar = True
                if i.isnumeric():
                    Numchar = True
                for s in Specialchar:
                    if i == s:
                        char = True
            if Upchar:
                if Numchar:
                    if char:
                        if len(password) >= 6:
                            if not User.objects.filter(email=email).exists():
                                if not UserInfo.objects.filter(tel=tel).exists():
                                    user = User.objects.create_user(first_name = name, last_name = surname,username = name,email=email,password=password)
                                    user.save()
                                    userinfo = UserInfo(user=user,tel=tel,password=password, dogumt= dogumt)
                                    userinfo.save()
                                    return redirect('login')
                                else:
                                    messages.warning(request, "Bu Telefon Numarası Kullanılıyor!")
                                    return redirect('register')
                            else:
                                messages.warning(request, "Bu E-Posta Adresi Kullanılıyor!")
                                return redirect('register')
                        else:
                            messages.warning(request, "Şifre En Az 6 Karakterden Oluşmalıdır!")
                            return redirect('register')
                    else:
                        messages.warning(request, "Şifre en az bir tane özel karakter !#$%&'()*+,-./:;<=>?@[\]^_`{|}~. içermelirdir!")
                        return redirect('register')
                else:
                    messages.warning(request, 'Şifre en az bir tane rakam içermelirdir!')
                    return redirect('register')
            else:
                messages.warning(request, 'Şifre en az bir tane büyük harf içermelirdir!')
                return redirect('register')
        else:
            messages.warning(request, 'Şifreler Uyumsuz!')
            return redirect('register')
    return render(request, 'User/register.html')
# Giriş Yap 
def Login(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('emailandtel')
        password = request.POST.get('password')


        mail = False
        for i in username:
            if i == "@":
                mail = True
        if username[-4:] == ".com" and mail:
            username = User.objects.get(email=username)
            user = authenticate(username = username, password= password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('anasayfa')        
        telnumber = False
        for i in username:
            if i.isnumeric():
                telnumber = True
        if telnumber:
            username = UserInfo.objects.get(tel = username)
            username = username.user
            user = authenticate(username = username, password= password)
            if user is not None:
                login(request, user)
                return redirect('anasayfa')
    return render(request, 'User/login.html')
# Çıkış Yap
def Logout(request):
    logout(request)
    return redirect('login')