from django.shortcuts import render
from .models import Recipient, Message, Mailing, MailingAttempt
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView


class MessageHomeView(ListView):
    pass
