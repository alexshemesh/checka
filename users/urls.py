from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
   # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('regitser/', views.register, name='register'),
]


