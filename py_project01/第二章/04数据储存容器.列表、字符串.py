#1.列表list 元组tuple 集合set 字典dict 字符串str(有序,不可修改)
#列表名称 = [元素1,元素2,...]   列表三大特点:元素有序,可重复,可修改
# shopping_list = [1,2,3,4,5,6,7]
# print(shopping_list)
# print(type(shopping_list))
#shopping_list[2] = "abc"  #修改列表指定位置元素
#del shopping_list[3]      #输出列表指定位置元素
#for item in shopping_list:  #遍历
#   print(item)

#***切片***
#shopping_list[:3:1]  #[开始索引:结束索引:步长]不包含结束索引

#列表的常见方法
# list.append()在列表尾部添加元素
# insert(索引,)在指定元素之前插入元素
# remove()删除第一个匹配的值
# pop()删除指定索引的元素,默认最后一个
# sort()对;列表进行排序
# reverse()反转列表元素位置
# shopping_list.append(5)  # shopping_list.insert(0,5)  # shopping_list.remove(3)  #shopping_list.pop(0)




# #列表案例1
# num_list = []  #定义空列表
# for i in range(10):
#     num = int(input("请输入一个有效数字:"))
#     num_list.append(num)   #添加进入空列表
# print("数字列表为:",num_list)
#
# num_list.reverse()  #反转
# print("反转后的数字列表为:",num_list)
# num_list.sort()     #排序(升序)
# print("排序后的数字列表为:",num_list)
#
# print("最大值为:",num_list[-1])  #max()
# print("最小值为:",num_list[0])   #min()
# print("平均值为:",sum(num_list)/len(num_list)) #len()求列表长度,获取元素个数

#列表案例2
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,28,95]
#
# for i in num_list2:
#     num_list1.append(i)  #列表合并
########## num_list = [*num_list1,*num_list2]      #######解包,*list解开成一个个独立元素,再合并; 组包
# #num_list = num_list1 + num_list2        # 列表合并
# print("合并后的列表为:",num_list1)
#
# new_list = []
# for i in num_list1:
#     if i not in new_list:  # in;not in 判断元素是否存在于列表中
#         new_list.append(i)
# print("合并去重后的列表为:",new_list)

#列表案例3
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)
#

#**************************列表推导式************************
# ###******推荐*****列表推导式-->快速生成列表-->语法格式:[要插入的值 for i in 序列/列表 if 条件]
# num_list2 = [i for i in range(1,21) ]
# print(num_list2)
# num_list3 = [i**2 for i in num_list2 if i%2==0]
# print(num_list3)







# 字符串str (有序,不可修改)
#切片 s[::-1] 倒过来
# 常用方法:
# s.find('') 查找子串
# s.count('') 统计子串出现次数
# s.upper() 所有字母转为大写,   括号内没有参数
# s.lower() 所有字母转为小写
# s.split('') 按照指定分隔符分割成 列表
# s.strip()/s.strip('*')  去除字符串两端空白字符或指定字符
# s.replace('','')替换子串
# s.startwith()/s.endwith() 是否以指定子串开头结尾,返回布尔值
#
# mail = input("请输入邮箱:")
# if mail.count("@") == 1 and "." in mail:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")


s = input("请输入回文:")
while True:
    if s == s[::-1]:
        print("输入正确")
        s1 = s.upper()
        for i in s1:
            print(i)
        break
    else:
        print("输入错误")













