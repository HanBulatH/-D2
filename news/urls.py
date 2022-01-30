from django.urls import path
from .views import PostsList, PostDetail, PostsSeach, PostCreate, PostEdit, PostDelete, CategoryList, subscribe_me # add_subscribe, del_subscribe #add_del_subscribe    импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', PostsList.as_view()),
    path ('<int:pk>', PostDetail.as_view(), name='post'),
    path ('search/', PostsSeach.as_view(), name='search_post'),
    path ('add/', PostCreate.as_view(), name='post_add'),
    path('<int:pk>/edit', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delet', PostDelete.as_view(), name='post_delet'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/category', PostsSeach.as_view(), name='post_category'),
    path('subscribed/<int:news_category_id>', subscribe_me, name='subscribed'),
    # path('<int:pk>/add_subscribe/', add_subscribe, name='add_subscribe'),
    # path('<int:pk>/del_subscribe/', del_subscribe, name='del_subscribe'),
    # path('', add_del_subscribe, name='add_del_subscribe'),











    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]