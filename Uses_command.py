# # # # user_1 = User.objects.create_user('Пушкин А. С.')
# # # # user_2 = User.objects.create_user('Есенин С. А.')
# # # # Author.objects.create(author = user_1)
# # # # Author.objects.create(author=user_2)
# # # # Category.objects.create(category_name='SPORT')
# # # # Category.objects.create(category_name='SCIENCE')
# # # # Category.objects.create(category_name = 'ART')
# # # # Category.objects.create(category_name = 'POLITIC')
# # # # author = Author.objects.get (id =1)
# # # #  Post.objects.create(author = author, category_Type = 'AR', title = 'Зимнее утро', text_article = 'Мороз и солце день чудесный, Еще ты дремлтшь друг прелестный ...
# # # # ')
# # # # author = Author.objects.get(id=2)
# # # # Post.objects.create(author = author,  category_Type = 'AR', title = 'Шигане',  text_article = 'Шигане ты моя Шигане ...')
# # # # Post.objects.create(author=author, category_Type='NW', title='Смерть поэта',
# # # #                     text_article='Повесился знаменитый поэт ...')
# # # # Post.objects.get(id=1).post_category.add(Category.objects.get(id=3))
# # # # Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))
# # # # Post.objects.get(id = 2).post_category.add(Category.objects.get (id = 3))
# # # # >>> Post.objects.get(id = 2).post_category.add(Category.objects.get (id = 2))
# # # # >>> Post.objects.get(id = 3).post_category.add(Category.objects.get (id = 1))
# # # # >>> Post.objects.get(id = 3).post_category.add(Category.objects.get (id = 4))
# # # #  Comment.objects.create(comment_post = Post.objects.get (id = 1), comment_user = Author.objects.get (id = 1).author, text_comment = 'Данное произвидение было напис
# # # # ано мною ....')
# # # #  Comment.objects.create(comment_post = Post.objects.get (id = 1), comment_user = Author.objects.get (id = 2).author, text_comment = 'Вы слишком рамантичный Пушкин'
# # # # )
# # # # Comment.objects.create(comment_post = Post.objects.get (id = 2), comment_user = Author.objects.get (id = 2).author, text_comment = 'Это стихотворение я написал на
# # # # ...')
# # # Comment.objects.create(comment_post = Post.objects.get (id =3), comment_user = Author.objects.get (id = 1).author, text_comment = 'это ужасная утрата')
# # # Comment.objects.get (id = 1).like()
# # # >>> Comment.objects.get (id = 1).like()
# # # >>> Comment.objects.get (id = 1).like()
# # # >>> Comment.objects.get (id = 1).dislike()
# # # Comment.objects.get (id = 2).like()
# # # >>> Comment.objects.get (id = 2).like()
# # # >>> Comment.objects.get (id = 2).like()
# # # >>> Comment.objects.get (id = 2).like()
# # # >>> Comment.objects.get (id = 2).like()
# # # Comment.objects.get (id = 2).dislike()
# # # Comment.objects.get (id = 3).like()
# # # >>> Comment.objects.get (id = 3).like()
# # # Comment.objects.get (id = 3).dislike()
# # Comment.objects.get (id = 4).like()
# # >>> Comment.objects.get (id = 4).like()
# # >>> Comment.objects.get (id = 4).like()
# # Post.objects.get(id = 1).like()
# # >>> Post.objects.get(id = 2).like()
# # >>> Post.objects.get(id = 3).like()
# # Author.objects.get(id = 1)
# # a = Author.objects.get(id = 1)
# # a.update_rating()
# # Author.objects.get(id = 2)
# # b = Author.objects.get(id = 2)
# # >>> b.update_rating()
# a = Author.objects.order_by('-raiting_Author')[:1]
#  for i in a:
# ...     i.author.username
# ...     i.raiting_Author
# ...
# 'Есенин С. А.'
# 12
# a = Post.objects.order_by('-raiting_article')[:1]
# for i in a:
# ...     i.date_create_post
# ...     i.author.username
# ...     i.raiting_article
# ...     i.title
# ...     i.preview()


# b = Comment.objects.order_by('comment_post_id')[1:2]
# for i in b:
# ...     i.data_create_comment
# ...     i.comment_user
# ...     i.reating_comment
# ...     i.text_comment
