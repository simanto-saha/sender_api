from django.db import models

class Employes(models.Model):
    emp_id = models.IntegerField(null=False, unique=True)
    emp_name = models.CharField(max_length=100)
    disgination = models.CharField(max_length=100)


    def __str__(self):
        return self.emp_name
