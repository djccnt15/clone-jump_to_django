from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('user_drop/', views.user_drop, name='user_drop'),
]