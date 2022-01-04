from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются.......

@register.filter(name='Censor')
def Censor (word):
    word_list = []
    word_list = word.split()
    cencor_word = ['Россия', 'федерализма', 'МИД']
    if str(word) in cencor_word:
        word = 'xxxx'
        return word
