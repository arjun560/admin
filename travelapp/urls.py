from django.urls import path
from. import views

urlpatterns =[
    path('home/',views.home,name='home'),
    path('login_view/',views.login_view,name='login_view'),

    path('reg/',views.register_view,name='register_view'),
    

]