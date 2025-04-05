from django.db import models
from django.forms import ValidationError
from jobs.models import Job
from users.models import CustomUser

# Create your models here.

def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        
        raise ValidationError("Only PDF files are allowed.")

class Applications(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    ]
    
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='apllications')
    status = models.CharField(choices=STATUS_CHOICES,max_length=10,default='pending')
    resume = models.FileField(upload_to='resumes/',validators=[validate_pdf])
    created_at = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default='applicants')
    
    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"
    
