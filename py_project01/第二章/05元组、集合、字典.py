# # #案例
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# #1. 生成示例销售数据
# data = {
#     'OrderID': range(1, 11),
#     'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
#     'Quantity': [5, 2, 0, 3, 1, 4, 6, 7, 0, 2],
#     'Price': [10.0, 20.0, 15.0, 10.0, 20.0, 15.0, 10.0, 20.0, 15.0, 10.0],
#     'Date': pd.date_range(start='2023-01-01', periods=10, freq='D')
# }
# sales_data = pd.DataFrame(data)
#
# # 2. 数据预处理
# # 检查缺失值
# print(sales_data.isnull().sum())
#
# # 填充缺失值（若有）
# sales_data['Quantity'].fillna(0, inplace=True)
# sales_data['Price'].fillna(sales_data['Price'].median(), inplace=True)
#
# # 3. 计算总销售额
# sales_data['TotalSales'] = sales_data['Quantity'] * sales_data['Price']
#
# # 4. 按产品分组计算总销售额
# product_sales = sales_data.groupby('Product')['TotalSales'].sum().reset_index()
#
# # 5. 数据可视化
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Product', y='TotalSales', data=product_sales)
# plt.title('Total Sales by Product')
# plt.xlabel('Product')
# plt.ylabel('Total Sales ($)')
# plt.xticks(rotation=45)
# plt.show()




#2.元组  ***元组一旦定义完成,不可修改(列表可修改),只能查询***    元组:有序,可重复,不可修改
# tup = (1,2,3,4,5,6,7,8,9) 或 tup = 1,2,3,4,5,6,7,8,9
#t = () #定义空元组    单个元素 t=(100,)
# print(type(tup))
#t1.count() 统计元素个数
#t1.index() 获取元素索引(第一个位置)
#解包  x,*y,z = tup   #*表示收集所有剩余元素
#a,b = 1,2
#a,b = b,a  #元组的组包与解包 -->交换变量值

# #元组案例
# students = (
#     ("s001","张三",85,98,78),
#     ("s002","李四",68,98,68),
#     ("s003","王五",98,98,89),
#     ("s004","赵六",98,98,98)
# )  # 元组嵌套元组
# #计算每个学生总分,平均分
# print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# # #方式一
# # for s in students:
# #     total = s[2]+s[3]+s[4]
# #     average = total/3
# #     print(f"{s[0]}\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{average:.1f}")  #设置格式,保留一位小数
# #方式二-----------元组解包----------
# for id,name,chinese,ma,en in students:
#     total = chinese + ma + en
#     average = total / 3
#     print(f"{id}\t{name}\t\t{chinese}\t\t{ma}\t\t{en}\t\t{total}\t\t{average:.1f}")  # 设置格式,保留一位小数
#
# #统计各科成绩最低分,最高分,平均分
# # ch = []
# # ma = []
# # en = []
# # for s in students:
# #     ch.append(s[2])
# #     ma.append(s[3])
# #     en.append(s[4])   #---优化后如下:
#
# ch = [s[2] for s in students]   #-------列表推导式---------
# ma = [s[3] for s in students]
# en = [s[4] for s in students]
#
# ch.sort()
# ma.sort()
# en.sort()
#
# print()
# print(f"语文最低分为{min(ch)},最高分为{max(ch)},平均分为{sum(ch)/len(ch)}")
# print(f"数学最低分为{ma[0]},最高分为{ma[-1]},平均分为{sum(ma)/len(ma)}")
# print(f"英语最低分为{en[0]},最高分为{en[-1]},平均分为{sum(en)/len(en)}")
# print()
# #查找平均分大于90的学生为优秀
# print("优秀学生名单如下:")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     average = total / 3
#     if average > 90:
#         print(f"学号:{s[0]}\t姓名:{s[1]}\t平均分:{average:.1f}")




#3.集合set--------无序，不可重复，可修改-------
# names = {'张三','李四','王五'}  #花括号
#s1 = {1,3,8,5,2,7,7,6,6}
#  #定义空集合 s2 = set()    #定义空字典 s2 = {}
# print(names)
#常见方法
#s1.add()添加;s1.remove()删除 ;s1.pop()随机删除并返回 ;s1.clear()清空集合;s1.difference(s2)差集,在s1不在s2 ;s1.union()并集;s1.intersection()交集

#集合案例
#s1 & s2 --->求交集,同s1.intersection(s2)
#s1 - s2 --->求差集,同s1.difference(s2)
#s1 | s2 | s3 | s4  --->竖线|求并集,同s1.union(s2).union(s3).union(s4)
#*****集合推导式*******, 语法 :{要往集合中添加的元素 for s in set1 if 条件}
#fb_set3 = {s for s in football_set if s not in basketball_set}   #求差集
# all_list = [*s1,*s2,*s3,*s4]   #集合解包,放在列表里面




#4.字典dict   键值对key:value类型的数据   没有索引下标,由key找到value,一一映射
#字典名称 = {key:value, key:value, key:value}  #key不可变(str,int,float,tuple)(不能是list,set,dict),不可重复(如果重复,后面的值会覆盖前面的)
#定义空字典  dict2 = {}
#访问   dict[key]     #value可修改
# contact = {"小明":"18300000000" ,
#            "小光":"18300000001" ,
#            "小花":"18300000002"
#           }
# print(len(contact))
# print(contact["小明"])
# print("小明" in contact)


#常用方法
# 添加 : dict1[key]=value   ; contact["小强"] = "18888886666"
# 修改(赋值) : dict1[key] = new_value
# 删除 :del dict1[key]  或  value1 = dict1.pop[key]
# 查询 : dict1.keys()获取所有key; dict1.values()获取所有value ; dict1.items()获取所有键值对
#遍历
# for k in contact.keys():
#     print(f"{k}: {contact[k]}")
#
# for item in contact.items():
#     print(f"{item[0]}: {item[1]}")
#
# for k,v in contact.items():
#     print(f"{k}: {v}")


"""
#------------案例  购物车管理系统-------------
增删改查,退出
结构: shopping_cart = {"Meta80":{"price":"6999","num":2},"鼠标":{...},...}
"""
shopping_cart = {}
menu = """
#########购物车系统#########
#       1.添加购物车       #
#       2.修改购物车       #
#       3.删除购物车       #
#       4.查询购物车       #
#       5.退出购物车       #
###########################
"""
print("欢迎使用购物车系统 ~ ")


while True:
    # 1.制作菜单
    print(menu)

    # 2.执行具体操作
    choice = input("请输入要执行的操作(1-5):")
    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品名称:")
            goods_price = float(input("请输入商品价格:"))
            goods_num = int(input("请输入商品数量:"))
            # 如果商品存在,则提示信息
            if goods_name in shopping_cart:
                print("该商品已存在,请重新选择~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕~")

        case "2":  # 修改购物车
            goods_name = input("请输入要修改的商品名称:")
            # 如果商品不存在,提示错误信息
            if goods_name not in shopping_cart:
                print("该商品不存在,请重新选择~")
                continue

            goods_price = float(input("请输入商品新的价格:"))
            goods_num = int(input("请输入商品新的数量:"))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("修改完毕~")

        case "3":  # 删除购物车
            goods_name = input("请输入要修改的商品名称:")

            if goods_name not in shopping_cart:
                print("该商品不存在,请重新选择~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕~")

        case "4":  # 查询购物车
            for goods_name in shopping_cart:
                goods_info = shopping_cart[goods_name]
                print(f"商品名称:{goods_name}, 商品价格:{goods_info["price"]}, 商品数量:{goods_info["num"]}")

        case "5":  # 退出购物车
            print("Bye~")
            break

        case _:  # 匹配其他所有情况
            print("非法操作,不支持!!!")