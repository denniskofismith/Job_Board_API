from django.shortcuts import render
from .serializers import ApplicationsSerializers
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import Applications
from rest_framework.views import APIView
from jobs.models import Job
from django.shortcuts import get_object_or_404
# Create your views here.


class ApplicationAPIView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get(self,request):
        
        if request.user.user_type != 'employer':
            
            return Response({"error": "Only employers can view applications"},status=status.HTTP_403_FORBIDDEN)
        
        applications = Applications.objects.filter(job__employer=request.user)
        serializer = ApplicationsSerializers(applications,many=True)
        return Response(serializer.data)
    
class ApplyForJobAPIView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request,job_id):
        
        if request.user.user_type != 'job-seeker':
            return Response({"error":"Only Job Seeker can apply for Jobs"})
        
        job = get_object_or_404(Job,job_id)
        
        serializer = ApplicationsSerializers(request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save(job=job,applicant=request.user)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class ApplicationDetailAPIView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request,application_id):
        
        application = get_object_or_404(Applications,application_id)
        
        if application:
            return Response({"error":"Application Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        if request.user != application.applicant and request.user != application.job.employer:
            
            return Response({'error':'Not authorized to view this application'},status=status.HTTP_403_FORBIDDEN)
        
        serializer = ApplicationsSerializers(application)
        
        return Response(serializer.data)
    
    def put(self,request,application_id):
        
        application = get_object_or_404(Applications,application_id)
        
        if application:
            return Response({"error":"Application Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        if request.user != application.job.employer:
            return Response({'error':'Not authorized to view this application'},status=status.HTTP_403_FORBIDDEN)
         
        serializer = ApplicationsSerializers(application,request.data,partial=True)
        
        serializer.is_valid(raise_exception=True)
          
        serializer.save()
        
        return Response(serializer.data)
         
        
    
        
        
    
    