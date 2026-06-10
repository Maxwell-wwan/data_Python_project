#定义匿名函数(没有名字)(单行表达式)(通常作为高阶函数的参数)
# lambda 参数列表:函数体
# line = lambda   : print("-----------")
# add = lambda x,y : x+y
# line()
from os import name


#递归调用-----自己调用自己(层层递进,再逐层回归)----->一定要有终结点
# def jc(n):
#     """
#     求n的阶乘
#     :param n:
#     :return:
#     """
#     if n == 1:
#         return 1
#     else:
#         return n*jc(n-1)
#
# print(jc(3))



#类型注解----->指定变量类型    会自动推断
# a2 :int = 344
# ee = False
# names2 :list[str|int] = ["1","2",3]
# oper1: dict[str,int] = {"cads":23,"dsf":23}