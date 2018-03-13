import random


def pasd():
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    p = ''
    for i in range(16):
        a = random.randrange(0, len(s))
        p += s[a]
    print('密码更新为:%s' % p)


pasd()

print('通知：xubiao直播将于4月1日开播')


def xubiao():
    a = input("请输入密码：")
    if a == 'xubiao':
        pasd()
        return '你真是个小天才'
    else:
        return '请访问www.xubioa.com,xubiao手把手教你成为小天才'


xubiao()
