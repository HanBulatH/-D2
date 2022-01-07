from django_filters import FilterSet, DateFromToRangeFilter, DateFilter # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    # date_create_post = DateFromToRangeFilter()

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {

            'date_create_post': ['gt'],
            'title': ['icontains'],
            'author': ['exact']

        }