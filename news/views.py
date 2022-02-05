from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from .models import Post, Category, Author, PostCategory, User
from .filters import PostFilter
from .forms import PostForm  # импортируем нашу форму
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import mail_admins
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.




class PostsList (ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'flatpages/posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')
    paginate_by = 10  # поставим постраничный вывод в 10 элементов


class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'flatpages/post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет

# дженерик для поиска
class PostsSeach(ListView):
    model = Post
    template_name = 'flatpages/search_post.html'
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        # context['categories'] = Category.objects.all()
        # context['form'] = PostForm()
        return context

# дженерик для создания
class PostCreate( PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    model = Post
    template_name = 'flatpages/post_add.html'
    form_class = PostForm



    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        category_pk = request.POST.get('post_category')
        sub_text = request.POST.get('text_article')
        sub_title = request.POST.get('title')
        category = Category.objects.get(pk=category_pk)
        subscribers = category.subscribers.all()
        # получаем адрес хоста и порта (в нашем случае 127.0.0.1:8000), чтоб в дальнейшем указать его в ссылке
        # в письме, чтоб пользователь мог с письма переходить на наш сайт, на конкретную новость
        host = request.META.get('HTTP_HOST')

        # валидатор - чтоб данные в форме были корректно введены, без вредоносного кода от хакеров и прочего
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            print('Статья:', news)

        for subscriber in subscribers:
            print('Адреса рассылки:', subscriber.email)

            # (6)
            html_content = render_to_string(
                'mail_creat.html', {'user': subscriber, 'text': sub_text[:50], 'post': news, 'host': host})

            # (7)
            msg = EmailMultiAlternatives(
                # Заголовок письма, тема письма
                subject=f'Здравствуй, {subscriber.username}. Новая статья в вашем разделе!',
                # Наполнение письма
                body=f'{sub_title}, {sub_text[:50]}',
                # От кого письмо (должно совпадать с реальным адресом почты)
                from_email='bulmiftahoff@yandex.ru',
                # Кому отправлять, конкретные адреса рассылки, берем из переменной, либо можно явно прописать
                to=[subscriber.email],
            )

            msg.attach_alternative(html_content, "text/html")

            msg.send()

        return redirect('/news/')


# class Post_Add(CreateView):
#     model = Post
#     template_name = 'flatpages/post_add.html'
#     context_object_name = 'posts'
#     form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
#
#         context['categories'] = Category.objects.all()
#         context['form'] = PostForm()
#         return context
#
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
#
#         if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
#             form.save()
#
#         return super().get(request, *args, **kwargs)


# дженерик для удаления
class PostDelete( PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'flatpages/post_delet.html'
    queryset = Post.objects.all()
    success_url = '/posts/'

# дженерик для редактирования объекта
class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    model = Post
    template_name = 'flatpages/post_edit.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class CategoryList (ListView):
    model = Category
    template_name = 'flatpages/category_list.html'
    context_object_name = 'categories'
    # queryset = Post.objects.order_by('-id')
    # для отображения кнопок подписки (если не подписан: кнопка подписки - видима, и наоборот)



# class CategoryDetail(DetailView):
#     model = Category  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
#     template_name = 'flatpages/post_category.html'  # название шаблона будет product.html
#     context_object_name = 'post_category'  # название объекта. в нём будет

@login_required
def subscribe_me(request, news_category_id):
    user = request.user
    my_category = Category.objects.get(id=news_category_id)
    sub_user = User.objects.get(id=user.pk)
    if my_category.subscribers.filter(id=user.pk):
        my_category.subscribers.remove(sub_user)
        return redirect('/news/')
    else:
        my_category.subscribers.add(sub_user)
        return redirect('/news/')

# @login_required
# def add_subscribe(request, **kwargs):
#     pk = request.GET.get('pk', )
#     print('Пользователь', request.user, 'добавлен в подписчики категории:', Category.objects.get(pk=pk))
#     Category.objects.get(pk=pk).subscribers.add(request.user)
#     return redirect('/news/')
#
#
# # функция отписки от группы
# @login_required
# def del_subscribe(request, **kwargs):
#     pk = request.GET.get('pk', )
#     print('Пользователь', request.user, 'удален из подписчиков категории:', Category.objects.get(pk=pk))
#     Category.objects.get(pk=pk).subscribers.remove(request.user)
#     return redirect('/news/')


# def add_del_subscribe(request, **kwargs):
#     pk = request.GET.get('pk',)
#     user = request.user
#     my_category = Category.objects.get(pk=pk)
#     sub_user = User.objects.get(pk=user.pk)
#     print('Пользователь', user, 'додписался на категории:', my_category)
#
#     if my_category.subscribers.filter(pk=user.pk):
#         my_category.subscribers.remove(sub_user)
#         return redirect('/news/')
#     else:
#         my_category.subscribers.add(sub_user)
#         return redirect('/news/')
    # # category_object = PostCategory.objects.get(postThrough=pk)
    # # category_object_name = category_object.categoryThrough
    # print('Пользователь', user, 'добавлен в подписчики категории:', category_object_name.objects.get(pk=pk))
    # # category_object_name.objects.get(pk=pk).subscribers.add(user)
    # return redirect('/categories/')

# Первый способ отправки сообщений подписчику (второй через сигналы сделан)
