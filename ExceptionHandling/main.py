#exception handling

'''
while 1:
    a=int(input())
    b=int(input())
    print(a/b)
    '''
# 10
# 5
# 2.0
# 10
# 2
# 5.0
# 10
# 0
# Traceback (most recent call last):
#   File "/home/main.py", line 5, in <module>
#     print(a/b)
#           ~^~
# ZeroDivisionError: division by zero


# ...Program finished with exit code 1
# Press ENTER to exit console.

while 1:
    try:
        a=int(input())
        b=int(input())
        print(a/b)
    except Exception as e:
        print(e)
    