.. highlight:: python

Символы и строки
================

До сих пор наши программы работали только с числами. Но многим
программам надо работать с текстовыми данными. Для этого есть два
основных объекта — *символы* и *строки*.

Символьный тип данных
-----------------------------

В питоне, чтобы сохранить символ в переменной, надо просто написать

::

    ch1 = "a"
    ch2 = "$"

и т.п. В итоге в переменной ``ch1`` хранится символ ``a``, а в ``ch2`` — символ ``$``.

Вводить символы можно обычной командой ``input()``:

::

    ch = input()

(именно прямо так), выводить — обычным ``print``:

::

    print(ch)

(На самом деле, в питоне нет отдельного "типа" для символов, символ в
питоне — это просто строка длины 1, про строки см. ниже. Но часто удобно
думать про символы отдельно от строк.)

Коды символов
-------------------------------------------------

На самом деле, конечно, в памяти компьютера хранятся не символы (т.е.
если мы написали ``ch="$"``, то нигде
в памяти не будет *нарисован доллар*). Компьютер умеет работать только с
числами, и вместо символов он хранит тоже числа.

Есть общепринятая договоренность, которая каждому числу от 0 до 255
ставит в соответствие некоторый символ. Точнее, таких договоренностей
есть несколько, они называется *кодировки*, но для латинских букв, цифр
и частоупотребимых символов типа того же доллара, запятой или плюса, во
всех кодировках соответствующие числа одинаковы. Для русских букв это не
так: в разных кодировках им соответствуют разные числа, но это отдельная
тема.

.. _ascii_table:

Эта общепринятая сейчас кодировка для латинских букв, цифр и
частоупотребимых символов называется ASCII, иногда говорят *таблица
ASCII*. Основная часть этой таблицы выглядит так:

=====  =======  ==  =====  =======  ==  =====  =======  ==  =====  =======  ==  =====  =======  ==  =====  =======
  32   |space|        48    ``0``         64    ``@``         80    ``P``         96    |back|       112    ``p``       
  33    ``!``         49    ``1``         65    ``A``         81    ``Q``         97    ``a``        113    ``q``       
  34    ``"``         50    ``2``         66    ``B``         82    ``R``         98    ``b``        114    ``r``       
  35    ``#``         51    ``3``         67    ``C``         83    ``S``         99    ``c``        115    ``s``       
  36    ``$``         52    ``4``         68    ``D``         84    ``T``        100    ``d``        116    ``t``       
  37    ``%``         53    ``5``         69    ``E``         85    ``U``        101    ``e``        117    ``u``       
  38    ``&``         54    ``6``         70    ``F``         86    ``V``        102    ``f``        118    ``v``       
  39    ``'``         55    ``7``         71    ``G``         87    ``W``        103    ``g``        119    ``w``       
  40    ``(``         56    ``8``         72    ``H``         88    ``X``        104    ``h``        120    ``x``       
  41    ``)``         57    ``9``         73    ``I``         89    ``Y``        105    ``i``        121    ``y``       
  42    ``*``         58    ``:``         74    ``J``         90    ``Z``        106    ``j``        122    ``z``       
  43    ``+``         59    ``;``         75    ``K``         91    ``[``        107    ``k``        123    ``{``       
  44    ``,``         60    ``<``         76    ``L``         92    ``\``        108    ``l``        124    ``|``       
  45    ``-``         61    ``=``         77    ``M``         93    ``]``        109    ``m``        125    ``}``       
  46    ``.``         62    ``>``         78    ``N``         94    ``^``        110    ``n``        126    ``~``       
  47    ``/``         63    ``?``         79    ``O``         95    ``_``        111    ``o``        127    —       
=====  =======  ==  =====  =======  ==  =====  =======  ==  =====  =======  ==  =====  =======  ==  =====  =======

Здесь символ номер 32 — это пробел.

Символы с номерами от 0 до 31 — это так называемые *управляющие* символы, они нам пока не очень интересны (равно как и символ 127),
поэтому в таблице они не показаны. Символы с кодами больше 128 зависят от кодировки, мы пока это не будем обсуждать.
(См. подробнее в разделе :ref:`про кодировки<encodings>`, но пока вам это не нужно.)

.. |space| raw:: html

    <code class="docutils literal notranslate"><span class="pre"> </span></code>

.. |back| raw:: html

    <code class="docutils literal notranslate"><span class="pre">&#96;</span></code>

Например, символ доллар имеет номер (говорят *код*) 36, а символ ``N`` — 78.



Обратите внимание, что все цифры идут подряд, все заглавные буквы идут
подряд, и все маленькие буквы идут подряд. Это нам будет очень полезно.
(Для русских букв это выполняется не всегда.)

Узнать код символа в питоне можно операцией ord, а
узнать символ по коду можно операцией chr. Например:

::                                   

    ch = input()         # считали символ...
    print(ord(ch))       # и вывели его код

    i = ord('$')         # записали в i код доллара
    print(i)

    i = int(input())     # считали код
    print(chr(i))       # и вывели соответствующий символ

    ch = chr(ord('$') + 1)
    print(ch)            # вывели символ, следующий за долларом


В большинстве случаев точное знание кодов символов вам не надо — вы
всегда можете что надо вычислить через ``ord``. Например, если мы знаем, что
в переменной ``ch`` у нас цифра (т.е. символ, соответствующий цифре) — как в
переменную ``i`` записать значение этой цифры (т.е. 0, 1, 2, ..., или 9)?
Т.е. как перевести цифру-символ в число?

Нам поможет то, что все цифры идут подряд. Поэтому достаточно из кода
цифры вычесть код нуля:

::

    i = ord(ch) - ord('0')

Обратите внимание: нам не надо знать, что код нуля — 48. Мы прямо пишем
``ord('0')``, а не 48, компьютер сам вычислит код нуля за нас!

Сравнения символов
---------------------------------------

Символы можно сравнивать операторами =, >, <, >=, <=. На самом деле
сравниваются их коды:

::

    if ch1 == ch2:  # если два символа совпадают...
        ....
    if ch1>ch2:  # если код первого символа больше кода второго
        ....

Благодаря тому, что однотипные символы идут подряд, очень легко можно
проверять тип символа. Например, чтобы проверить, является ли символ
цифрой, можно написать:

::

    if ch>='0' and ch<='9': 
        ... 

Массивы и циклы
-----------------------

Если вам надо сделать массив, в
элементах которого хранить что-то, связанное с цифрами, то надо
переходить к кодам:

::

    a = [0] * 256  # у нас всего 256 символов
    a[ord('d')] = 10  # в элемент, соответствующий d, записали 10
    ...
    for x in range(ord('a'), ord('z')+1):
        ch = chr(x)
        print(ch)  # выводим все символы от a до z

Но вообще это продвинутая тема, сейчас пока вам не особо нужная.

Строки
------

Строка — это последовательность символов. Поэтому представляется
естественным использовать для хранения строк массив символов:

::

    s = ["T", "e", "s", "t"]
    # Но так делать не надо!


Но так делать не надо! Чтобы записать строку в переменную, надо просто записать
строку в переменную:

::

    s = "Test"

В питоне строка — это *массив*, каждым элементом
которого является символ, но это не просто массив, а массив с
дополнительными функциями.

Длину строки, как и у массива, можно узнать командой ``len(s)``:

::

    print(len(s))

Далее, строки, конечно, можно считывать и выводить. На питоне это
делается стандартными командами: вывод обычным ``print``, а ввод — обычным ``input()``,
никакой лишней конвертации не надо, пишете ``s = input()``:

::

    s = input()
    print(s)

В-третьих, строки можно складывать. Сложить две строки — значит
приписать к одной строке другую:

::

    s1 = input()
    s2 = input()
    s = s1 + s2
    print(s)  # выведет две строки одну за другой

Прибавлять можно и символы:

::

    s = s + 'A'

Наконец, *строковые константы* — это уже привычные вам
последовательности символов в кавычках:

::

    s = "Test"
    s = s + '2'
    print(s)  # выводит Test2

На самом деле, в питоне можно использовать как апострофы (символы
``'``), так и кавычки (символы ``"``)

Может возникнуть вопрос, как в строковой константе ввести собственно
символ апостроф или кавычку. Просто так написать ``'It's a string'`` не
получится, т.к.питон подумает, что строка закончилась
на втором апострофе; аналогично не сработает ``"Text"Text"``.
Поэтому надо приписывать символ ``\`` перед апострофом или кавычкой.
Например, чтобы записать в переменную строку ``It's a string``, надо
написать так:

::

    s = 'It\'s a string'
    # или так
    s = "It's a string"
    # а если нужны и апострофы, и кавычки:
    s = "It's a \"string\""

Аналогично для записи символа "апостроф"/"кавычка" в переменную типа
char:

::

    ch = '\''
    ch = "'"
    ch = "\""
    ch = '"'

Поскольку символ ``\`` имеет такой особый смысл, то чтобы записать в строку
прямо этот символ, его надо написать два раза::

    s = "test\\test\\\\test"

получится строка ``test\test\\test``.

Еще частный случай строки — *пустая* строка, т.е. строка длины ноль:

::

    s = ""  # питон

Ну и наконец, строка — это все-таки массив символов. Можно использовать
все известные вам операции над массивами (писать s[i], чтобы получить
доступ к i-му символу строки, и т.д.). Например, так можно проверить, есть ли в
строке пробелы:

::

    # питон
    for i in range(len(s)):
        if s[i] == ' ':
            ...

int и т.п.
------------------

Есть еще три полезных команды:

::

    int
    float
    str

Они переводят числа в строки и обратно, с ``int`` вы уже сталкивались.

::

    print(str(23) + 'abc' + str(45));     # выводит 23abc45
    print(float('2.5') * 2);              # выводит 5.0000e0
    print(str(2.5) + 'a');                # выводит 2.5000e0a

Другие операции
---------------

Вы знаете ряд хитрых команд работы с массивами, и иногда будет
возникать желание их использовать при работе со строками. Лучше их не
используйте, пока вы точно не будете понимать не только что, но и
насколько быстро они работают. В большинстве случаев можно обойтись без
них (и так даже будет проще!), плюс вы точно не знаете, как долго они
работают. 

Аналогично есть другие функции специально для строк, про которые вы 
можете где-то еще прочитать, например, ``find``.
Я не советую их использовать, пока вы не понимаете, как конкретно они работают
и насколько долго.

Например, пусть вам надо из строки удалить все
пробелы. Можно писать примерно так (считаем, что у вас уже есть исходная
строка ``s``):

::

    while s.find(" ") != -1:
        s = s[:s.find(" ")] + s[s.find(" ")+1:]  # вырезаем этот символ

Но это работает долго (поверьте мне :) ) и требует от вас помнить все
эти команды, а еще и осознавать не самый тривиальный код. Проще так:

::

    s1 = '';
    for i in range(len(s)):
        if s[i] != ' ':
            s1 = s1 + s[i]; 

Результат лежит в ``s1``. Поймите, как это работает.


Примеры решения задач
---------------------

Приведу несколько примеров задач, аналогичных тем, которые встречаются на олимпиадах
и в моем курсе.

.. task::

    Дан символ. Определите, верно ли, что он является маленькой латинской буквой.

    **Входные данные**: Вводится один символ.

    **Входные данные**: Выведите ``yes``, если это маленькая латинская буква, и ``no`` в противном случае.

    **Пример**:

    Входные данные::

        t

    Выходные данные::

        yes
    |
    |
    |

Считаем символ::

    ch = input()

Далее надо проверить, является ли этот символ маленькой латинской буквой. Тут (как и в других аналогичных примерах)
нужно воспользоваться тем, что символы в таблице ASCII идут подряд. Поэтому достаточно проверить ``'a' <= ch and ch <='z'``. 
Итоговый код::

    ch = input()
    if 'a' <= ch and ch <='z':
        print('yes')
    else:
        print('no')

.. task::

    Дана цифра. Считайте ее как символ, и переведите в число (в ``int``), не пользуясь стандартными функциями типа ``int``.

    **Входные данные**: Вводится один символ — цифра.

    **Входные данные**: Выведите число.

    **Пример**:

    Входные данные::

        1

    Выходные данные::

        1
    |
    |
    |

Конечно, чтобы чисто пройти все тесты, в этой задаче можно просто вывести то же самое, что и вводится. Но давайте честно научимся превращать цифру в число.
Считываем символ::

    ch = input()

и дальше надо понять, какая это цифра. Все цифры в таблице ASCII идут подряд, поэтому достаточно из кода символа вычесть код нуля. В итоге получаем

::

    ch = input()
    print(ord(ch) - ord('0'))

.. task::

    Дана строка. Посчитайте, сколько в ней маленьких латинских букв.

    **Входные данные**: Вводится одна строка.

    **Входные данные**: Выведите одно число — ответ на задачу.

    **Пример**:

    Входные данные::

        foo bar 123

    Выходные данные::

        6
    |
    |
    |

Давайте считаем строку::

    s = input()

Далее надо пройтись по строке::

    for i in range(len(s)):

и очередной символ (:math:`s[i]`) проверить: буква это или нет. Как проверять, мы уже знаем: ``if s[i] >= 'a' and s[i] <= 'z'``.
Если буква, то увеличиваем счетчик, надо еще этот счетчик заранее завести. Итоговый код::

    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            ans += 1
    print(ans)