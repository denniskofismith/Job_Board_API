from django.db import models
from jobs.models import Job
from users.models import CustomUser

# Create your models here.

class Applications(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    ]
    
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='apllications')
    status = models.CharField(choices=STATUS_CHOICES,max_length=10,default='pending')
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default='applicants')
    
    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"
    
