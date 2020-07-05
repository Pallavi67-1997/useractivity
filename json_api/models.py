from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User1(models.Model):
    UserID = models.CharField(max_length = 50)
    Real_name = models.CharField(max_length = 50)
    tz = models.CharField(max_length = 50)
    
   
    class Meta:
        db_table = "AAA"

class Activity_period1(models.Model):
    user = models.ForeignKey('User1',related_name='activity_period',on_delete=models.CASCADE)
    start_time = models.CharField(max_length = 100)
    end_time = models.CharField(max_length = 100)
   
    class Meta:
        db_table = "BBB"
