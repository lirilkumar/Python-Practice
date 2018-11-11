# def print_args(function):
#     def wrapper(*args, **kwargs):
#         print ('Arguments:', args, kwargs)
#         return function(*args, **kwargs)
#     return wrapper
#
# def second(function):
#     def wrapper(*args, **kwargs):
#         print ('second:', args, kwargs)
#         return function(*args, **kwargs)
#     return wrapper
#
# @print_args
# @print_args
# @second
# def write(text,a,c,d):
#     print(text)
#
# write('foo',10,11,d=11)
#


