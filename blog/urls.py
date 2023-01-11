from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/', views.aboutus,name='aboutus'),
    path('home/', views.home,name='home'),
    path('contactus/', views.contactus,name='contactus'),
    path('signuppage/', views.signuppage,name='signuppage'),
    path('loginpage/', views.loginpage,name='loginpage'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('logoutpage/', views.logoutpage,name='logoutpage'),  
    path('addpost/', views.addpost,name='addpost'),
    path('editpage/<int:id>', views.edit_page,name='editpage'),
    path('deletepage/<int:id>', views.delete_page,name='deletepage'),

    

]
