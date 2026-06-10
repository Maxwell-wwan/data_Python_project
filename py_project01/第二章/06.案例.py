# import numpy as np
# print(np.__version__)
# a = np.array()
# print(a)
# print(type(a))



"""
例题 教务管理系统
1.添加学生信息：录入学生姓名、语文、数学、英语成绩
2.修改学生信息：输入要修改的学生姓名，修改各科成绩
3.删除学生信息：输入要删除的学生姓名，删除信息
4.查询学生信息：
5.列出所有学生信息
6.统计班级成绩:统计各科成绩的最高分、最低分、平均分，以及其学生姓名
7.退出系统

格式:stu_info = {"name":{"chinese_score":100,"math_score":90,"english_score":90},,,}
"""
stu_info = {}
menu = """
---------学生教务系统----------
|       1.添加学生信息        |
|       2.修改学生信息        |
|       3.删除学生信息        |
|       4.查询学生信息        |
|       5.列出所有学生        |
|       6.统计班级成绩        |
|       7.退出教务系统        |
-----------------------------
"""
#1.教务系统操作界面




while True:
    print(menu)
    oper = int(input("请输入您的操作(1-7):"))
    match oper:
        case 1:  # 添加
            std_name = input("请输入需要录入的学生姓名:")
            std_chinese_score = input("请输入学生语文成绩:")
            std_math_score = input("请输入学生数学成绩:")
            std_english_score = input("请输入学生英语成绩:")
            stu_info[std_name] = {"chinese_score": std_chinese_score, "math_score": std_math_score,
                                  "english_score": std_english_score}
            print("录入成功~")
        case 2:  # 修改
            std_name = input("请输入需要修改的学生姓名:")
            if std_name not in stu_info:
                print("该学生不存在!请重新操作~")
                continue

            std_chinese_score = input("请输入新的学生语文成绩:")
            std_math_score = input("请输入新的学生数学成绩:")
            std_english_score = input("请输入新的学生英语成绩:")
            stu_info[std_name] = {"chinese_score": std_chinese_score, "math_score": std_math_score,
                                      "english_score": std_english_score}
            print("修改完毕~")
        case 3:  #删除
            std_name = input("请输入需要删除的学生姓名:")
            if std_name not in stu_info:
                print("该学生不存在!请重新操作~")
                continue
            del stu_info[std_name]
            print("删除完毕~")
        case 4:  #查询
            std_name = input("请输入需要查询的学生姓名:")
            if std_name not in stu_info:
                print("该学生不存在!请重新操作~")
                continue
            std_score = stu_info[std_name]     # 创建一个字典来接受内字典的信息
            print(f"学生姓名:{std_name}, 语文:{std_score["chinese_score"]},数学:{std_score["math_score"]}, 英语:{std_score["english_score"]} ")
        case 5:  #列出
            for k in stu_info.keys():
                std_score = stu_info[k]
                print(f"姓名:{k}\t语文:{std_score["chinese_score"]}\t数学:{std_score["math_score"]}\t英语:{std_score["english_score"]} ")

        case 6:  #统计
            ch_score = []   #列表
            ma_score = []
            en_score = []
            re_ch = {}    #字典
            re_ma = {}
            re_en = {}
            for k in stu_info.keys():
                std_score = stu_info[k]   #字典
                ch_score.append(int(std_score["chinese_score"]))
                ma_score.append(int(std_score["math_score"]))
                en_score.append(int(std_score["english_score"]))
                re_ch[std_score["chinese_score"]] = k
                re_ma[std_score["math_score"]] = k
                re_en[std_score["english_score"]] = k


            print(f"语文最高分是:{max(ch_score)}\t最低分是:{min(ch_score)}\t平均分是:{sum(ch_score)/len(ch_score):.1f}")
            print(f"数学最高分是:{max(ma_score)}\t最低分是:{min(ma_score)}\t平均分是:{sum(ma_score)/len(ma_score):.1f}")
            print(f"英语最高分是:{max(en_score)}\t最低分是:{min(en_score)}\t平均分是:{sum(en_score)/len(en_score):.1f}")
            print()
            print(f"语文最高分学生是:{re_ch[max(ch_score)]}  \t最低分的学生是:{re_ch[min(ch_score)]}")
            print(f"数学最高分学生是:{re_ch[max(ma_score)]}  \t最低分的学生是:{re_ch[min(ma_score)]}")
            print(f"英语最高分学生是:{re_ch[max(en_score)]}  \t最低分的学生是:{re_ch[min(en_score)]}")


        case 7:  #退出
            break
        case _:
            print("输入有误,请重新输入~")



