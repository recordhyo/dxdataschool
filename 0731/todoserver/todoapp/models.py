from django.db import models

# Create your models here.
class ToDo(models.Model) :
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    done = models.BooleanField()
    regdate = models.DateField(auto_now_add=True)
    moddate = models.DateField(null=True)