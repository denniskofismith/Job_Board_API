
from django.urls import path
from .views import RegisterView,LoginView,ProfileView,LogoutAPIView,RefreshTokenAPIView


urlpatterns = [
    path('register/',RegisterView.as_view(),name='Register'),
    path('login/',LoginView.as_view(),name='LogIn'),
    path('profile/',ProfileView.as_view(),name='Pofile'),
      path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', RefreshTokenAPIView.as_view(), name='token_refresh'),
]