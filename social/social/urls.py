from django.contrib import admin
from django.urls import path
from AppUser.views import *
from AppSocial.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Anasayfa/', Anasayfa, name='anasayfa'),
    path('', Login, name='login'),
    path('Register', Register, name='register'),
    path('Logout', Logout, name='logout'),
]
