from django.urls import path
from .views import PostsList, PostDetail, PostsSeach, PostCreate, PostEdit, PostDelete, CategoryList, CategoryDetail  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', PostsList.as_view()),
    path ('<int:pk>', PostDetail.as_view(),name='post'),
    path ('search/', PostsSeach.as_view(), name='search_post'),
    path ('add/', PostCreate.as_view(), name='post_add'),
    path('<int:pk>/edit', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delet', PostDelete.as_view(), name='post_delet'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path ('category/', CategoryDetail.as_view(),name='post_category'),




    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]