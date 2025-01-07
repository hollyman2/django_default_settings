import logging
from celery import shared_task
from django.core.mail import send_mail

@shared_task(name='users.tasks.send_mail_task')
def send_mail_task(subject, message, from_email, recipient_list):
    print(f"Отправка письма: Тема: {subject}, Сообщение: {message}, От: {from_email}, Получатели: {recipient_list}")
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Письмо успешно отправлено")
        return True, None, None
    except Exception as e:
        print(f"Ошибка при отправке email: {e}")
        logger = logging.getLogger(__name__)
        logger.exception(f"Ошибка при отправке email: {e}")
        return False, None, None
   