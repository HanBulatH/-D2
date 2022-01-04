from django.views.generic import ListView, DetailView
from .models import Post, Category


# Create your views here.
class PostsList (ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'flatpages/posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')


class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'flatpages/post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет
