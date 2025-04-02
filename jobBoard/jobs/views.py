from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.shortcuts import get_object_or_404
from .models import Job
from .serializers import JobSerializer
# Create your views here.

class JobViewSet(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,requst):
        
        jobs = Job.objects.all().order_by('-created_at')
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
    
    def post(self,requst):
        
        if requst.user.user_type != 'employer':
            
            return Response({"error":"Only employer can post jobs."})
        
        serializer = JobSerializer(data=requst.data)
        
        if serializer.is_valid():
            serializer.save(employer=requst.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class JobDetailView(APIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        
        job = get_object_or_404(Job,pk=pk)
        
        jobserializer = JobSerializer(job)
        
        return Response(jobserializer.data)
    
    def put(self,request,pk):
        
        
        job = get_object_or_404(Job,pk=pk)
        
        if request.user != job.employer:
            
            return Response({"error": "You can Only edit your own Job Postings."})
        
        serializer = JobSerializer(job, data=request.data,partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        
        job = get_object_or_404(Job,pk)
        
        if request.user != job.employer:
            
            return Response({'error':'You can only delete your own job posting.'},status=status.HTTP_403_FORBIDDEN)
        
        job.delete()
        return Response({'message':"Job deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
    
        