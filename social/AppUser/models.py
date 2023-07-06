from django.db import models
from django.contrib.auth.models import User
class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    tel = models.CharField(("Telefon Numarası"), max_length=50)
    password = models.CharField(("Parola"), max_length=50)
    dogumt = models.DateField(("Doğum Tarihi"))
