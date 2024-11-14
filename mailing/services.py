from config.settings import CACHE_ENABLED
from django.core.cache import cache
from .models import Recipient, Mailing, Message


def get_recipient_from_cache():
    """Получение данных из кеша, если кеш пуст, то получает данные из БД."""
    if not CACHE_ENABLED:
        return Recipient.objects.all()
    key = 'recipients_list'
    recipient = cache.get(key)
    if recipient is not None:
        return recipient
    recipient = Recipient.objects.all()
    cache.set(key, recipient)
    return recipient


def get_mailing_from_cache():
    """Получает данные из кеша, если кеш пуст, то получает данные из БД."""
    if not CACHE_ENABLED:
        return Mailing.objects.all()
    key = 'mailing_list'
    mailing = cache.get(key)
    if mailing is not None:
        return mailing
    mailing = Mailing.objects.all()
    cache.set(key, mailing)
    return mailing


def get_message_from_cache():
    """Получает данные из кеша, если кеш пуст, то получает данные из БД."""
    if not CACHE_ENABLED:
        return Message.objects.all()
    key = 'message_list'
    message = cache.get(key)
    if message is not None:
        return message
    message = Message.objects.all()
    cache.set(key, message)
    return message
