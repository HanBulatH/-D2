# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import post_save
# from django.dispatch import receiver  # импортируем нужный декоратор
# from django.shortcuts import redirect
# from django.template.loader import render_to_string
#
# from .models import Post, Category, PostCategory
# from .forms import PostForm
#
#
# # в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
# @receiver(post_save, sender=Post)
# def send_mail_after_create(sender, instance, created, **kwargs):
#
#     global subscriber
#     sub_text = instance.text_article
#     sub_title = instance.title
#     _category = instance.post_category.all()
#
#     for category in _category:
#
#
#         subscribers = category.subscribers.all()
#         post = instance
#
#         for subscriber in subscribers:
#             html_content = render_to_string(
#                 'mail_creat.html', {'user': subscriber, 'text': sub_text[:50], 'post': post})
#
#             msg = EmailMultiAlternatives(
#                 # Заголовок письма, тема письма
#                 subject=f'Здравствуй, {subscriber.username}. Новая статья в вашем разделе!',
#                 # Наполнение письма
#                 body=f'{sub_title}, {sub_text[:50]}',
#                 # От кого письмо (должно совпадать с реальным адресом почты)
#                 from_email='bulmiftahoff@yandex.ru',
#                 # Кому отправлять, конкретные адреса рассылки, берем из переменной, либо можно явно прописать
#                 to=[subscriber.email],
#             )
#
#             msg.attach_alternative(html_content, "text/html")
#
#             msg.send()
#
#         return redirect('/news/')