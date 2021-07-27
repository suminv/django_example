from django.urls import path
from app_users.views import another_register_view, login_view, logout_view
from app_users.views import AnotherLoginView, AnotherLogoutView
from app_users.views import register_view

urlpatterns = [
path('login/', login_view, name='login'),
path('logout/', logout_view, name='logout'),
path('another_login/', AnotherLoginView.as_view(), name='another_login'),
path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
path('register/', register_view, name='register'),
path('another_register/', another_register_view, name='another_register'),

]
