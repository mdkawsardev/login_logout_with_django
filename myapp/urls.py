from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.logoutuser, name='logout'),
]
