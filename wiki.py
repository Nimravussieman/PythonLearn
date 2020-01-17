import wikipedia,re,os
attempt=0
# win_page = input('final page: ')
with open('url.txt') as f:
    win_page = f.readline()
    print(win_page)

def ex_m(message = 'error'):
    print(message)
    os._exit(0)

def choice(list_):
    global attempt
    attempt += 1
    if attempt > 7:        ex_m('you have exhausted your attempts')

    print('\n\n')
    [print('{}: {}'.format(i + 1, x)) for i, x in enumerate(list_[0:7])]
    print('\n\n')
    while True:
        index = input('choice one of them: ')
        try:
            index=int(index)-1
            if index>len(list_): continue
            return list_[index]
        except:
            ex_m()


def equals(pattern):
    page = wikipedia.page(pattern)
    split = re.split(r'//\w*\.', win_page)[1]
    print(page.url)

    try:
        if re.fullmatch(r'https://\w+\.%s[^./]*' % split, page.url).group():  # ny.url == win_page:
            ex_m('Win')
    except:
        pass
    return page


def serch(string):
    try:
        res = wikipedia.search(string)
        if not res:    ex_m('Links not found exception')
        ny = equals(choice(res))
        ch = choice(ny.links)
        equals(ch)
        serch(ch)
    except Exception as ex:
        ex_m(ex)

s=input("search pattern: ")
if not s or not win_page:    ex_m()
serch(s)
