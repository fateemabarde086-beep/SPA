from django.db import models

class booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    date = models.DateField()
    time = models.TimeField() 
    requirement = models.TextField()
    
    def __str__(self): 
         return self.name
    
