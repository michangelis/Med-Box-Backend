from django.urls import path
from . import views


urlpatterns = [
    path('user_list/', views.user_list),
    path('get_user_pills/', views.get_user_pills),
    path('get_next_user/', views.get_next_user),
    path('getUserCards/', views.getUserCards),
    path('count_taken/', views.count_taken),
    path('get_user_p/', views.get_user_p),
    path('get_user/<int:user_id>/', views.get_user),
    path('get_pills/', views.get_pills),
    path('get_pill/<int:pill_id>/', views.get_pill),
    path('get_comments/<int:pill_id>/', views.get_comments),

]