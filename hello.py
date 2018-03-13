import random


def pasd():
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    p = ''
    for i in range(16):
        a = random.randrange(0, len(s))
        p += s[a]
    print('update password:%s' % p)


pasd()

print('徐彪通知：我是李大钊')


def xubiao():
    a = input("请输入能输入的东西：")
    if a == 'xubiao':
        return '你真是个小天才'
    else:
        return '%s真是个小天才' % a
