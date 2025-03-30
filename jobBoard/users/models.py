from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES = (('employer','Employer'),('jobseeker','Job Seeker'))
    user_type = models.CharField(max_length=10,choices=USER_TYPES)
    
    def __str__(self):
        return f"{self.username}  - {self.user_type}"