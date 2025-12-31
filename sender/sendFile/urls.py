from django.urls import path
from sendFile import views, api_views


urlpatterns = [
    path('', views.home, name='home'),
    path('view_login/', views.view_login, name='view_login'),
    path('signup/', views.signup, name='signup'),
    path('view_logout/', views.view_logout, name='view_logout'),


    path('api/get/', api_views.userdetails_list),
    path('api/get/<int:pk>/', api_views.userdetails)
    
] 