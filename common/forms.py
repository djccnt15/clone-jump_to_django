from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


class UserForm(UserCreationForm):
    """
    form for creating user
    inherit UserCreationForm to add custom fields
    """

    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class CheckPasswordForm(forms.Form):
    """
    form for validation by checking password
    """

    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())

    def __init__(self, user, *args, **kwargs):
        """
        inherit __init__ from base form and add self.user
        """

        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        """
        clean() runs to_python(), validate(), run_validators() for checking
        field validation of input data and propagate errors from APIs

        if there is no field validation error, check_password() compares input
        password to the hashed password in the database
        """

        cleaned_data = super().clean()  # input data for validation
        password = cleaned_data.get('password')  # get password from input data
        confirm_password = self.user.password  # get password from user model

        if password:  # if input password get through validation APIs
            if not check_password(password, confirm_password):  # if input/hashed passwords are not equal
                self.add_error('password', '비밀번호가 일치하지 않습니다.')  # return error msg