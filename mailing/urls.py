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
    BlockMailingView,
    MailingAttemptListView,
    SendMailingView,
)

app_name = MailingConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("recipient_create/", RecipientCreateView.as_view(), name="recipient_create"),
    path(
        "recipient/<int:pk>/delete/",
        RecipientDeleteView.as_view(),
        name="recipient_delete",
    ),
    path("recipient_list/", cache_page(30)(RecipientListView.as_view()), name="recipient_list"),
    path(
        "recipient_detail/<int:pk>/",
        RecipientDetailView.as_view(),
        name="recipient_detail",
    ),
    path(
        "recipient_update/<int:pk>/",
        RecipientUpdateView.as_view(),
        name="recipient_update",
    ),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),
    path("message_list/", cache_page(30)(MessageListView.as_view()), name="message_list"),
    path("message_detail/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message_update/<int:pk>/", MessageUpdateView.as_view(), name="message_update"),
    path("mailing_create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path("mailing_detail/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing_update/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"),
    path("<int:pk>", SendMailingView.as_view(), name="send_mailing"),
    path(
        "attempt_list/",
        MailingAttemptListView.as_view(),
        name="attempt_list",
    ),
    path(
        "mailing_block/<int:mailing_id>/block/",
        BlockMailingView.as_view(),
        name="mailing_block",
    ),
]
