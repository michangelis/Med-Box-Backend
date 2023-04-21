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
    path('get_per_pills/', views.get_per_pills),
    path('get_pill/<int:pill_id>/', views.get_pill),
    path('get_comments/<int:pill_id>/', views.get_comments),
    path('take_medication/<int:alarm_id>/', views.take_medication),
    path('register_user/', views.register_user, name='register_user'),
    path('create_pill/', views.create_pill, name='create_pill'),
    path('create_alarms/', views.create_alarms, name='create_alarms'),
    path('login/', views.login, name='login'),
    path('post_pill_comment/', views.post_pill_comment, name='post_pill_comment'),
    path('take_pill/', views.take_pill, name='take_pill'),
    path('deload/', views.deload, name='deload'),
    path('get_disable/<int:pill_id>/', views.get_disable),
    path('get_user_alarms/<int:user_id>/', views.get_user_alarms),

]