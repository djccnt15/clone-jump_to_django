from django.contrib.auth import views as auth_views

# Create your views here.


login_view = auth_views.LoginView.as_view(template_name='common/login.html')
logout_view = auth_views.LogoutView.as_view()