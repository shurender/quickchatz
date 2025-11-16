from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('rooms/', views.rooms, name='rooms'),
    path('create-room/', views.create_room, name='create_room'),
    path('room/<str:code>/', views.room, name='room'),

]