from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from .models import Post, Category, Author
from .filters import PostFilter
from .forms import PostForm  # импортируем нашу форму
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin





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