from django.urls import path
from . import views

urlpatterns = [
    path('applications/',views.ApplicationAPIView.as_view(),name='application-list'),
    path('jobs/<int:job_id>/apply/',views.ApplyForJobAPIView.as_view(),name='apply-for-job'),
    path('applications/<int:application_id>',views.ApplicationDetailAPIView.as_view(),name='applicant')
    
    
]