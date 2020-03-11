from django.db import models

# Create your models here.

class userinfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=16,null=True,blank=True,db_index=True)
    age=models.IntegerField(default=1,unique=True)
    current_date=models.DateField(auto_now=True)

