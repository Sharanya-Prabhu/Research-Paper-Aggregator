from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [ path('', views.index_view, name='index_view'),
                path('login/', views.login_view, name='login'),
                path('signup/', views.signup_view, name='signup'),
                path('search/', views.query_handler, name='user_search'),
                path('save_preferences/', views.save_preferences, name='save_preferences'),
                path('show_preferences/', views.show_preferences, name='show_preferences'),
                path('logout/', views.user_logout, name='logout'),]