from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutMe/', views.aboutMe, name="aboutMe"),
    path('myWorks/', views.myWorks, name="myWorks"),
    path('myResume/', views.myResume, name="myResume"),
    path('contactMe/', views.contactMe, name="contactMe"),

]
