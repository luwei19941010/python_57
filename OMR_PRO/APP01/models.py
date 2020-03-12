from django.db import models

# Create your models here.

# class user(models.Model):
#     name=models.CharField(max_length=16,null=True,blank=True,db_index=True)
#     age=models.IntegerField(default=1,unique=True)
#
#     def __str__(self):
#         return self.name

class data(models.Model):
    name=models.CharField(max_length=16)
    data=models.DateField()

    def __str__(self):
        return self.name
