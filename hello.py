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



print('李大钊同志辛苦啦')