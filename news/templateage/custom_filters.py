from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются.......

@register.filter(name='Censor')
def Censor (value):
    cencor_word = ['Россия', 'федерализма', 'МИД', 'Эфиопии']
    word_list = (str(value)).split()

    for i in cencor_word:
        for j in word_list:
            if j == i:
                a = word_list.index(j)
                word_list.insert(a, '***')
                word_list.remove(j)
                value = ' '.join(word_list)

    return value
