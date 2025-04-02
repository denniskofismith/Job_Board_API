from django.urls import path
from .views import JobDetailView,JobViewSet


urlpatterns = [
    path('',JobViewSet.as_view(),name='jobs'),
    path('<int:pk>',JobDetailView.as_view(),name='job-detail')
]