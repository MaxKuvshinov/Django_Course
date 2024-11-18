from django.urls import path
from django.views.decorators.cache import cache_page
from mailing.apps import MailingConfig
from mailing.views import (
    HomeView,
    MailingCreateView,
    MailingDeleteView,
    MailingDetailView,
    MailingListView,
    MailingUpdateView,
    MessageCreateView,
    MessageDeleteView,
    MessageDetailView,
    MessageListView,
    MessageUpdateView,
    RecipientCreateView,
    RecipientDeleteView,
    RecipientDetailView,
    RecipientListView,
    RecipientUpdateView,
)

app_name = MailingConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),

]
