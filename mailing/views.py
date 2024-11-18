from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from mailing.forms import MailingForm, MessageForm, RecipientForm
from mailing.mixins import OwnerRequiredMixin

from .models import Mailing, MailingAttempt, Message, Recipient


class HomeView(ListView):
    model = Mailing
    template_name = 'mailing/home.html'


class RecipientListView(ListView):
    model = Recipient
    template_name = 'recipient_list.html'
    context_object_name = 'recipients'


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'recipient_create.html'
    success_url = reverse_lazy('mailing:home')


class RecipientUpdateView(OwnerRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'recipient_update.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientDeleteView(OwnerRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Recipient
    template_name = 'recipient_delete.html'
    success_url = reverse_lazy('mailing:recipient_list')


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = 'recipient_detail.html'
    context_object_name = 'recipient'


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_create.html'
    success_url = reverse_lazy('mailing:home')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(OwnerRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_update.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(OwnerRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    context_object_name = 'mailings'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_create.html'
    success_url = reverse_lazy('mailing:home')


class MailingUpdateView(OwnerRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_update.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(OwnerRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing_detail.html'
    context_object_name = 'mailing'
