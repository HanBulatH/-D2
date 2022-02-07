from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from celery.schedules import crontab


# task для отправки писем подписчикам при создании новой статьи
@shared_task
def send_mail_after_creat(sub_username, sub_useremail, html_content, sub_title, sub_text):
    msg = EmailMultiAlternatives(
            # Заголовок письма, тема письма
            subject=f'Здравствуй, {sub_username}. Новая статья в вашем разделе!',
            # Наполнение письма
            body=f'{sub_title}, {sub_text[:50]}',
            # От кого письмо (должно совпадать с реальным адресом почты)
            from_email='bulmiftahoff@yandex.ru',
            # Кому отправлять, конкретные адреса рассылки, берем из переменной, либо можно явно прописать
            to=[sub_useremail],
        )


    msg.attach_alternative(html_content, 'text/html')

    msg.send()


# task для еженедельной рассылки писем
@shared_task
def send_mail_for_every_week_after_sub(sub_username, sub_useremail, html_content):



    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}, новые статьи за прошлую неделю в вашем разделе!',
        from_email='bulmiftahoff@yandex.ru',
        to=[sub_useremail]
    )

    msg.attach_alternative(html_content, 'text/html')

    msg.send()
