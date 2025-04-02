"""
URL configuration for jobBoard project.

"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs-board/token/', TokenObtainPairView.as_view()),
    path('jobs-board/refresh/',TokenRefreshView.as_view()),
    path('jobs-board/users/',include('users.urls')),
    path('jobs-board/jobs/',include('jobs.urls')),
    path('jobs-board/applications/',include('applications.url'))
]