from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

class Author (models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    raiting_Author = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_raiting = self.post_set.aggregate(post_raiting_=Sum('raiting_article'))
        p_r = 0
        p_r += post_raiting.get('post_raiting_')

        comment_raiting = self.author.comment_set.aggregate(comment_raiting_=Sum('reating_comment'))
        c_r = 0
        c_r += comment_raiting.get('comment_raiting_')

        self.raiting_Author = p_r * 3 + c_r
        self.save()

    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        # ordering = ['-price']


class Category (models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post (models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    category_Type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    date_create_post = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text_article = models.TextField()
    raiting_article = models.SmallIntegerField(default=0)

    def like(self):
        self.raiting_article += 1
        self.save()

    def dislike(self):
        self.raiting_article -= 1
        self.save()

    def preview(self):
        return "{} ...".format(self.text_article[0:123])

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'

class PostCategory (models.Model):
    post_Through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_Through = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment (models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    data_create_comment = models.DateTimeField(auto_now_add=True)
    reating_comment = models.SmallIntegerField(default=0)

    def like(self):
        self.reating_comment += 1
        self.save()

    def dislike(self):
        self.reating_comment -= 1
        self.save()