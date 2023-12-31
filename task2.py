# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.(Может помочь метод translate из модуля string)


import string


my_str = "Антисоветское восстание в Дагестане, возглавляемое Нажмудином Гоцинским, проходило с сентября 1920 года по май 1921 года. \
На пике восстания повстанцы практически полностью контролировали три округа Дагестана из девяти: Аварский, Андийский и Гунибский, \
а ещё в трёх шли боевые действия: Даргинском, Кази-Кумухском и Темир-Хан-Шуринском. \
После опустошительной для горского населения Гражданской войны в Дагестане установилась советская власть. \
Причинами восстания в нагорной части региона называются низкое качество работы новых властей, их злоупотребления, \
политика продразвёрстки и террора. Руководство повстанческим движением осуществлялось религиозными исламскими деятелями, \
имеющими авторитет у населения, и местными представителями бывшего имперского офицерства. Восстание охватило половину Дагестана, \
а в январе 1921 года распространилось на горную часть соседней Чечни. До февраля 1921 года восстание шло с переменным успехом для \
повстанцев, горцы активно использовали незнание местности красноармейцами, которые несли ощутимые потери. Переломным моментом  \
стал захват Грузии большевиками, дагестанские повстанцы были отрезаны и остались без поддержки с тыла. Красная армия провела мобилизацию, \
задействовав большие силы из других регионов, и имела военно-техническое преимущество в виде артиллерии, броневиков, авиации и химического оружия. \
Мятеж был подавлен, боевые действия повлекли негативные последствия для местных жителей, было уничтожено около сотни сёл."

prepositions = ['в', 'без', 'до', 'из', 'к', 'на', 'по', 'о', 'от', 'перед',
                'при', 'через', 'для', 'с', 'у', 'за', 'над', 'об', 'под', 'про', 'а', 'и']

my_dict = {}
word_list = []

my_str = my_str.lower().translate(str.maketrans('', '', string.punctuation)
                                  )  # Убираем служебные символы из текста
my_str = my_str.split()

for word in my_str:  # Убираем предлоги из текста
    if word not in prepositions:
        word_list.append(word)


for elem in word_list:
    my_dict.setdefault(elem, word_list.count(elem))


max_len = len(max(my_str, key=len))

num_words = 1
while num_words <= 10:
    num_words += 1
    max_key = max(my_dict,  key=my_dict.get)
    print(f'{max_key:>{max_len}}  =  {my_dict[max_key]}')
    my_dict.pop(max_key)