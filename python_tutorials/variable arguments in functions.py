# def kuchibhikarega(a, b, *c, **d,):
#     print("a", type(a), a)
#     print("b", type(b), b)
#     print("c", type(c), c)
#     print("d", type(d), d)
#
#
# kuchibhikarega(a=2,b=1, j=6, k=7)
# kuchibhikarega(2,b=1, j=6, k=7)
# kuchibhikarega(2,1, j=6, k=7)
# # kuchibhikarega(a=2,1, j=6, k=7)
#
#
#
#


# abc="my name is liril. i am hungry? are you         ?"
#
# import re
# # lists=re.split('[.?]',abc)
# lists=re.findall('[\w\s]+',abc)
# print(lists)
#
# for i in lists:
#     print(len(i))
# aaa=lambda i:len(i)
#
# print(max(aaa(i) for i in lists))
#
# d={'a':10}
# print(d)



def draw_point(x, y):
    # do some magic
    print('abc')
    print(x,y)

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
draw_point(**point_bar)
