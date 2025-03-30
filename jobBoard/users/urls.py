
from django.urls import path
from .views import RegisterView,LoginView,ProfileView


urlpatterns = [
    path('register/',RegisterView.as_view(),name='Register'),
    path('login/',LoginView.as_view(),name='LogIn'),
    path('profile/',ProfileView.as_view(),name='Pofile')
]