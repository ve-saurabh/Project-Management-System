from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('manager-register/', views.ManagerRegisterView.as_view(), name="manager-register"),
    # path('sendmail/', views.sendMail, name="sendmail"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('manager-dashboard/', views.ManagerDashboardView.as_view(), name="manager-dashboard"),
    path('developer-dashboard/', views.DeveloperDashboardView.as_view(),name="developer-dashboard"),
    path('logout/', LogoutView.as_view(next_page = "login"), name="logout"),
]