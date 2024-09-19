from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name="home"),
    path('signup' , views.signup , name="signup"),
    path('login' , views.login , name="login"),
    path('logout' , views.logoutuser , name="logout"),
    path('generate' , views.generate , name="generate"),
    path('exam_portal' , views.portal , name="portal"),
]
