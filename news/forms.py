from django.forms import ModelForm, BooleanField
from .models import Post, PostCategory



# Создаём модельную форму
class PostForm(ModelForm):

    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post

        fields = ['author', 'category_Type','post_category', 'title', 'text_article', 'raiting_article',]