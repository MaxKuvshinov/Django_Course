from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users: login")
