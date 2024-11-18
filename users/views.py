import secrets
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
from .models import CustomUser
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponseForbidden


class RegisterView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users: login')

    def form_invalid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'

        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения почты перейдите по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return super().form_invalid(form)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect('users: login')


class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return CustomUser.objects.all()


class UserDetailList(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user_detail'


class BlockUserView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        if not request.user.has_perm('users.can_block_user'):
            return HttpResponseForbidden('Недостаточно прав для блокировки.')
        return render(request, 'user_block.html', {'user': user})

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)

        if not request.user.has_perm('users.can_block_user'):
            return HttpResponseForbidden('Недостаточно прав для блокировки.')

        user.is_block = not user.is_block
        user.save()

        return redirect('users:user_list')
