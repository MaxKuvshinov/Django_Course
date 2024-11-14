from django.db import models


class Recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
        ordering = ['full_name']


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Тема письма')
    body_of_the_letter = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['subject']


class Mailing(models.Model):
    STATUS_CHOICES = [('Создана', 'Создана'), ('Запущена', 'Запущена'), ('Завершена', 'Завершена')]
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время первой отправки')
    end_time = models.DateTimeField(auto_now=True, verbose_name='Дата и время окончания отправки')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Создана', verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Recipient, verbose_name='Получатели')

    def __str__(self):
        return f'Рассылка сообщения: {self.message}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['start_time', 'status']


class MailingAttempt(models.Model):
    STATUS_CHOICES = [('Успешно', 'Успешно'), ('Не успешно', 'Не успешно')]
    date_time_of_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Не успешно', verbose_name='Статус')
    mail_server_response = models.TextField(verbose_name='Ответ почтового сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
        ordering = ['date_time_of_attempt']