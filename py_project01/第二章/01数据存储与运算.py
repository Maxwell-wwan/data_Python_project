# 1.字面量与变量
# print(100) # int
# print(3.14) # float
# print(True) # 布尔 bool
# print(False)
# print(None) #空值 None Type
# print("Hello Python") #字符串 str引号引起来的都是字符串
# print("---------------") # srt

#变量  命名规则 :1.只能包含字母,数字,下划线 2.不能以数字开头,3.不能用关键词True等,4.严格区分大小写
#变量标识符命名 规范 : 1.见名知意2.多个部分用下划线连接3.英文字母全小写
# num = 6666
#user1_age=22
# num,user1_age = 6666,"二十二" #一次性定义多个变量,逗号分隔
# print(num)
# num += 1
# print(num)

# 变量交换  需要一个临时变量
# a,b,c = 100,200,300
# t = c
# c = a
# a = b
# b = t
# print(a,b,c)


# 2.常见数据类型  int整数 float浮点数 str字符串 bool布尔 NoneType空值(只有一个None);type()查看
#type() 函数 获取字面量或变量的数据类型
#isinstance() 判断数据是否属于指定类型,返回一个bool值
# print(type("6666"))
# print(type(666))
# print(type(False))
# print(type(None))
# num = 3.14
# print(type(num))
# print(isinstance(num,int))

#字符串    转义字符\"表示引号为输出内容 ,定义字符串可以双引号,单引号,
# print("hello + '111' +  world")
# print("He said\"Let's go !\" ")
# print("\"Hello World\"  \n   你好    ")
# print('''君不见黄河之水天上来
# 奔流到海不复回
# 君不见高堂明镜悲白发
# 朝如青丝暮成雪
# ''') # 三引号,'''  '''三引号可以定义多行字符串,换行
# print("\t\n Hello \\\ world\n\n") # 转义字符 \n换行符;\t制表符;\'单引号;\"双引号

#字符串拼接    str(int型)-->可转化为字符串类型;int()-->可转化为int型;float();bool()
# s1,s2 = "人生苦短"   "ok","我用Python"
# print("吉多*范罗苏姆:" + s1 + "," + s2) # + 拼接多个字符串,只能拼接字符串类型,不能拼接其他类型
# user_name = "涛哥"
# age = 22
# hobby = "Python"
# print("大家好,\n\t我是"+user_name+",今年"+str(age)+"岁,我的兴趣爱好是"+hobby)

#占位符  字符串格式化
# print("大家好,我是%s,今年%s岁,我的兴趣爱好是%s" %(user_name,age,hobby))# 字符串格式化方法一 "%s,%s"   %(变量,变量)
# print(f"大家好,我是{user_name},今年{age}岁,我的兴趣爱好是{hobby}" )    # 字符串格式化方法二  f"内容{变量/表达式}"   **推荐**



#3.输入与输出 input语句  s = input(提示信息);print语句  print(数据..);# input获取键盘输入的数据都是字符串数据
# name = input("请输入您的姓名:")
# age = input("请输入您的年龄:")
# print(f"您的姓名为{name},年龄为{age}")

#BMI = 体重/(身高**2) # float 计算可能存在精度损失,除法运算结果为小数
# user_weight = float(input("请输入您的体重(单位kg): "))# float() -->将输入的字符串转化为float型数据
# user_height = float(input("请输入您的身高(单位m): "))
# BMI = user_weight / (user_height ** 2)
# print("您的BMI值为:" + str(BMI))
# print("您的BMI值为:" , str(BMI))
# print(f"您的BMI值为:{str(BMI)}" )
# print("您的BMI值为:%s"  %(str(BMI)))#光标放后面Ctrl+d快速复制一行代码


#4.运算符  算术,赋值,比较,逻辑; //整除   %求余求模  **幂指数
#4.1算术运算符的优先级: () --> ** --> * / // % --> + -
# import math
# a = math.pow(2,3)
# print(a*2)
# b = math.exp(1)
# print(math.log(b))
# print(3**3)

# print(len("hello world! \n 你好"))
# type(None)

#4.2赋值运算符 = += -= *= /= %= //= **=   ;# num **= 2 等效于 num = num**2
#4.3比较运算符 == !=不等于 > < >= <=
#4.4逻辑运算符  not非(取反);and且;or或;   连接多个布尔值

#非not 与and 或or
# print(not(False))
x = int(input("输入:"))
a = not(x>5 and( x<10 or x==100))
print(a)