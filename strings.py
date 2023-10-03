"=====Строки======"
# строки-неизменяемые тип данных. который предназначен для хранения текста( послевовательности символов), заключенного в одинарные или двойные кавычки

string ='Hello World'
string1 ="Hello World"
string = " Don't" # внутри двойных ковычек все одинарные - просто символы
string = ' "   ' # внури одинарных все двойные - просто симыволы

''' Don't   "Hello"  '''
""" Don't  "Hello" """

print('asdf' + '2') #asdf2
print('asdf' * '2') # asdfasdf
string = 'Hello'
string2= 'World'
print=(string+' ' +string2) # Hello World
print(string / string2) # Error

# Конкатенация - склеивание строк


"==============Экранизация строк==========="
'\n' # перенос на новую строку
print('hello\nwor\nld')
#hello
#world

'\t' # табуляция
print('hello\tworld') # hello    world
print('Don\'t')
print("Don\"t")
print("hello\\nero") 
# hello nero

'\v' # перенрс на новую строку со смешением впрво на длину предыдущей строки
print('hello\vworld\vmakers\bootcamp')
#hello
#     world
#          makers
#               bootcamp

"========Форматирование строк========="
title = 'plov'
price = 200

#название: plov
# цена: 201
print(f'название: {title}) \nцена: {price}')
# надо принять с терминала название блюда и вывести такое сообщение:
# название блюда был вкусный
title =input('Введите название блюда:')
print=(f'{title} был вкусный')





"=====Методы строк======"
# методы- функции, который относится к определенному классу (типу данных). к ним мы обращаемся чз точку
#print(dir(str#))
'HELLO' . lower() # hello
'hello'. upper() # HELLO

'HELLO'. swapcase() #hello
'hello world'. capitalize() #Hello world
'hello world'. title() #Hello World  все буквы после пробела заглавной 

'hello'.count('l') #2
'hello'.count('ll') #1
'hello world'.count('oo') #0

'hello world'.startwith('he') # True
'hello world'.startswith('Hello') # False
'hello world'.endswith('ld') #True

'hello world'.islower() #True
'HELLO'.islower() #True
'1234'.isdigit() #True
'hello !'.isalpha() #True
'hello !'.isalnum() #False
'1234 ,'.isalnum() #False
'h1'.isalnum() #True

'hello world'.split(' ') #['hello', 'world']
'hello world'.split('o') #['hell', 'w', 'rld']
'hello world'.split('makers') #['hello world']

' 1'.join(['hello', 'world', 'rt']) # 'hello1world
'hello'+'1'+'world'+'1'+'rt'

string = '                hello world               '
print(string.strip()) #'hello world'
print(string.lstrip()) # 'hello world         '
print(set.rstrip()) # '          hello world'

string = '$$$$$$$$df$$$$$$$'
string.strip('$') #as$df

string = '$$as$df$$$$'
string.replace('$', '') # asdf
string.replace('$', '', 2) # as$df$$$$




'=============Индексы==========='
# индекс- порядковый номер элемента в последовательности (символ в строке) ( индексация начинается с 0)

'h e l l o  w o r l d '
#0 1 2 3 4 5 6 7 8 9 10
#       . . . -3 -2  -1
string = 'hello world'
string[2] # 'l'
string{0} # 'h'
string[6] # 'w'
string[10] # 'd'
string[=1] # 'd'


# срез - подстрака строки
string[0:5] # hello
string[0:4] # hell
string[6:10] # worl
string[6:-1] # world
string[6:] # world
string[:5] #hello
string[:] # hello world
 
string [:2] + string[-2:] # he + ld = held

'hello world' 
string[::2] #hlowrd
string[1:5] # ello
string[1:5:2] # el
string[::-1] # dlrow olleh
string[::-2] # drwolh
string[::3] # hlwl

# question isnumeric|isdigit|isdecimal ?

immutable_string = 'hello'
immutable_string = immutable_string.upper() # HELLO
immutable_string = immutable_string[::-1] # OLLEH
print(immutable_string) # OLLEH

string = 'world'
string[:-3] # wo
print(string) # world
