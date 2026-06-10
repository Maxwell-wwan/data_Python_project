"""
break:只能出现在循环中,表示结束、跳出循环的含义（break跳出循环时,while后面的else将不会执行）
continue：只能出现在循环中，表示字段本次循环，直接进入下一次循环
"""


# m = int(input("请输入长方形长度:"))
# #shift键 + enter键 下一行
# n = int(input("请输入长方形宽度:"))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")# print("*")自带换行效果;end=""表示每次输出以什么结束,默认\n
#     print()



#案例 打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={i*j}",end="\t")#每次输出以空格结束;制表符
#     print()


#案例 打印国际象棋棋盘
# for i in range(8):
#     if i % 2 == 0:
#         for j in range(4):
#             print("■  □",end="  ")
#         print()
#     else:
#         for j in range(4):
#             print("□  ■",end="  ")
#         print()


#案例 B站登录页面
# while True:
#     username = input("请输入用户名:")
#     password = input("请输入用户密码:")
#
#     if username == "" or password == "":
#         print("输入的用户名或密码不能为空!请重新输入")
#         continue #结束当前循环,直接进入下一次循环
#
#     if username == "admin" and password == "666666":
#         print("登录成功,进入B站首页~")
#         break #结束循环
#     elif username == "admin1" and password == "88888":
#         print("登录成功,进入B站首页~")
#         break
#     else:
#         print("输入的用户名或密码错误!请重新输入")


#案例 猜数字游戏
import random #导入函数
random_number = random.randint(1,100) #生成随机数
while True:
    n = int(input("请输入数字:"))
    if  n > random_number:
        print("猜大了,请重新输入")
        #continue
    elif n < random_number:
        print("猜小了,请重新输入")
        #continue
    else:
        print("恭喜,猜对了!")
        break
print(f"随机生成的数字是{random_number}")


# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print(total)

# total = 0
# str1 = input("请输入一个字符串:")
# for i in str1:
#     if i == 'a' or i == 'b' :
#         total +=1
# print(f"一共有{total}个a和b")