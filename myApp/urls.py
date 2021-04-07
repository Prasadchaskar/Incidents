from django.urls import path,include
from . import views
from . views import Create,Saved_Incidents
from django.contrib.auth import views as auth_view

urlpatterns = [
    
    path('',views.home,name="home"),
    path('create/',views.Create,name="create"),
    path('register/',views.register,name='register'),
    path('saved',views.Saved_Incidents,name="saved"),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_view.LoginView.as_view(template_name='logout.html'),name='logout'),
]