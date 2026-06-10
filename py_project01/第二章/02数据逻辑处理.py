"""
while-->已知 循环开始和结束的条件;  for-->已知 循环次数或遍历
多行注释
三引号
大段注释
"""
# 流程控制语句  条件判断,模式匹配,循环
#1.条件判断
#条件语句 ==等于 !=不等于
# year = int(input("请输入需要判定的年份: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# mood_index = int(input("今天对象的心情指数是:"))#else if
# if 100 >= mood_index >= 80:
#     print("恭喜,去吧皮卡丘")
#     print("嘿嘿嘿")
# elif 80> mood_index >= 60:
#     print("赶紧去哄吧")
# else:
#     print("完蛋了")


# score = float(input("请输入您的成绩:"))
# if 0 <= score <= 100:
#     if score >= 92:
#         print("您的等级为A")
#     elif score >= 70:
#         print("您的等级为B")
#     elif score >= 60:
#         print("您的等级为C")
#     else:
#         print("您的等级为D")
# else:
#     print("输入错误!")



#2.模式匹配 match...case  匹配数据的结构和内容
# day = input("请输入星期几(1-7):")
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         pass#空语句,占位作用
#     case "6" | "7":    # | 表示或的意思
#         print("周末")
#     case _ :           # _ 匹配其他所有情况
#         print("输入错误")


# num1 = float(input("请输入第一个数:"))
# num2 = float(input("请输入第二个数:"))
# oper = input("请输入运算符:")
# match oper:
#     case "+":
#         print(f"{num1} + {num2}={num1+num2}")
#     case "-":
#         print(f"{num1} - {num2}={num1-num2}")
#     case "*":
#         print(f"{num1} * {num2}={num1*num2}")
#     case "/" if num2 != 0:#if条件成立时,才匹配这个case
#         print(f"{num1} / {num2}={num1/num2}")
#     case _:
#         print("输入有误")


#3.循环 while循环(条件)  for循环(迭代循环)轮询遍历机制,逐个处理  ;break语句,continue语句,pass语句
#
# num = int(input("请输入一个正整数:"))
# n = 0
# count = 0
# while n<=num:
#     if n%2==1:
#         print(n)
#         count += 1
#     else :
#         pass
#     n += 1
#else:
#     pass
# print(f'从0到{num}之间,有{count}个奇数')

#计算1-100所有偶数和
# n = 1
# sum = 0
# while n<=100:
#     if n%2==0:
#         sum += n
#     n += 1
# else :
#     print(f"1-100所有偶数和:{sum}")

# for 元素 in 待处理数据集:
#range(start,stop,[step])等差数列函数  range(stop)    ***包含start不包含stop
# for i in range(10):
#     if i % 3 == 0:
#         print(i)
#     else:
#         pass


# for i in range(5):
#     if i == 3:
#         continue ##表示直接进入下一次循环
#     else:
#         print(i)


sum = 0
for i in range(100,501):
    if i % 3 == 0:
        sum +=i
print(sum)



