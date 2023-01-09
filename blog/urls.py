from django.urls import path
from blog import views

urlpatterns = [
    path('aboutus/', views.aboutus,name='aboutus'),
    path('home/', views.home,name='home'),
    path('contactus/', views.contactus,name='contactus'),
    path('signuppage/', views.signuppage,name='signuppage'),
    path('loginpage/', views.loginpage,name='loginpage'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('logoutpage/', views.logoutpage,name='logoutpage'),
    

    

]
