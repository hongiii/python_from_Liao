# -*- coding: utf-8 -*-
# 试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
dic = {"Mary": 12, (1, 2, 3): 10}
print(dic)

# dic = {"Mary": 12, (1, [2, 3]): 10}
# dic = {1: 12, [2, 3]: 10}
# print(dict)

s = set((1, 2, 3))
print(s)

# s = set((1, [2, 3]))
# print(s)

# 解释：dict和set都不能放入可变对象。


# 额外demo练习
data = {"Mary": 100, "Bob": 81, "Tracy": 72, "Ted": 91}
stu_name = input("Please input the name you want to query:")
if stu_name in data:
    print(("%s get %d in the exam.") % (stu_name, data[stu_name]))
else:
    print("Sorry, it doesn't exist. Add new data into the database.")
    stu_grade = int(input("Please input the grade of this student: "))
    data[stu_name] = stu_grade
    print(("%s get %d in the exam.") % (stu_name, data[stu_name]))
