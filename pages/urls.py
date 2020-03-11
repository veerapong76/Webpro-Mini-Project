from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('login',views.my_login,name='login'),
    path('logout',views.my_logout,name='logout'),
    path('register',views.register,name='register'),
    path('detail/<int:id_event>',views.detail,name='detail'),
    path('profile/<int:id_user>',views.profile,name='profile'),
    path('edit_profile/<int:id_user>',views.edit_profile,name='edit_profile'),
    path('search/',views.search_event,name='search_event'),
    path('all_event/',views.all_event,name='all_event'),
    path('all_catagorie/',views.all_catagorie,name='all_catagorie'),
    path('search_catagorie/<str:name>',views.search_catagorie,name='search_catagorie'),
    
]