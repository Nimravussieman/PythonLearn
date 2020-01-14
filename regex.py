import re

def f1():
    """
    Извлечь все слова, которые начинаются на гласную букву
    """
    with open('Lorem.txt') as f:
        text = f.read()
        res = re.findall(r'\b[eyuioa][a-zA-Z]*',text, flags=0)#\b[eyuioa]+([a-zA-Z]+)
        print(res)
#f1()
def f2():
    '''
    Извлечь все слова, которые начинаются на согласную букву из текста
    '''
    with open('Lorem.txt') as f:
        text = f.read()
        res = re.findall(r' ([^eyuioa][a-zA-Z]*)', text, flags=0)  # \b[eyuioa]+([a-zA-Z]+)
        print(res)
#f2()
def f3(number):
    '''
    Сделать валидацию строки по шаблону номера телефона, номер должен быть длинной 13 символов
    и начинаться с кода страны
    '''
    res = re.fullmatch(r'\+?\d{2}[ ]*\(? *(\d{3} *\)?[ -]*\d){7} ?', number)#'+?\d[ ]*\(? *\d{3} *\)?[ -]*\d{7}# #\+?\d[ ]*\(? *\d{3} *\)?([ -]*\d){7}
    if res:
        print(res.group())
f3('+38(068)44 66 -2 4 0')
def f4(L):
    '''
    Провалидировать список емейлов, в каждом эмейле должен присутствовать символ @ и
    доменное имя после точки
    '''
    s=' '.join(L)
    res = re.findall(r'\b\w+@(?:\w+.)+[a-zA-Z]{2,3}', s, flags=0)#@[a-zA-Z]*$\.[a-z]{2,4}
    print(res)
#f4(['abc.test@gmail.com', 'xyz@test.in', 'test.first@analyticsvidhya.com', 'first.test@rest.biz'])
def f5():
    '''
    Разбить строку по нескольким разделителям : , пробел
    '''
    with open('Lorem.txt') as f:
        text = f.read()
        res = re.findall(r'[^ ,]\w+', text, flags=0)
        print(res)
#f5()
def f6():
    '''
    найти следующую информацию:
    '''
    L = ['domain_name', 'domain__id', 'registrar', 'registrar_url', 'registrar_id',
    'registrar_email', 'registrar_phone', 'status', 'registrant_id', 'registrant_name',
    'registrant_address', 'registrant_city', 'registrant_state_province', 'registrant_postal_code',
    'registrant_country']
    d = {
        "domain_name": ""
    }
    with open('cybercity.txt') as f:
        text=f.read()
        res=''
        for l in L:
            s=re.sub(r'_',r'.',l)
            temp = re.search(r'%s ?:(.*)\n'%s, text, re.IGNORECASE)
            if temp:
                res+=temp.group()
        print(res)
#f6()
