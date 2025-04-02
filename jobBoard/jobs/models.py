from django.db import models
from users.models import CustomUser

# Create your models here.

class Job(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(decimal_places=2,max_digits=8)
    location = models.CharField(max_length=300)
    employer = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    