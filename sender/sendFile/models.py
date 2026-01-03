from django.db import models
from django.contrib.auth.models import User
from employes.models import Employes



class Userdetails(models.Model):
    user = models.ForeignKey(Employes, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email