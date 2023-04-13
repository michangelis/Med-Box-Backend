from django.urls import path
from . import views


urlpatterns = [
    path('user_list/', views.user_list),
    path('get_user_pills/', views.get_user_pills),
    path('get_next_user/', views.get_next_user),
    path('getUserCards/', views.getUserCards),
    path('count_taken/', views.count_taken),
]