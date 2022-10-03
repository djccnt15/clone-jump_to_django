from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserForm, CheckPasswordForm

# Create your views here.


login_view = auth_views.LoginView.as_view(template_name='common/login.html')
logout_view = auth_views.LogoutView.as_view()


def user_signup(request):
    """
    function for sign up user
    """

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # user authentication
            login(request, user)  # login(create user session)
            return redirect('/')  # redirection after sign up
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/user_signup.html', context)


def user_drop(request):
    """
    function for drop user
    """

    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        if password_form.is_valid():
            request.user.delete()
            logout(request)
            return redirect('/common/login/')
    else:
        password_form = CheckPasswordForm(request.user)
    context = {'password_form':password_form}
    return render(request, 'common/user_drop.html', context)