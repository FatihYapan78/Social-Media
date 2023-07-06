from django.shortcuts import render


def Anasayfa(request):
    return render(request, 'index.html')
