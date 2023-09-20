from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    """
    View for user registration and sign-up.

    This view class provides a user registration and sign-up form using Django's built-in
    UserCreationForm. It allows users to create a new account by providing a username and password.
    After successful registration, users are redirected to the login page.

    Attributes:
        form_class (Form): The form class used for user registration (UserCreationForm).
        success_url (str): The URL to redirect to after successful registration (login page).
        template_name (str): The HTML template used for rendering the sign-up form.

    Methods:
        The SignUpView class inherits methods from generic.CreateView for handling the registration
        process.

    """
    
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"