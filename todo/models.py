from django.db import models

# Create your models here.

class ToDo(models.Model):
   Title = models.CharField(max_length=15, blank=False) 
   Description = models.TextField(max_length=250, blank=True)
   Date = models.DateField(auto_now_add=True, blank=False)
   Completed = models.BooleanField(default=False)
   
   def __str__(self):
       return self.Title  
   
