#调用csv模块
import csv

#调用open()函数打开csv文件，传入参数：文件名“student.csv”、追加模式“a”、newline=''。
with open('student.csv','a',newline='',encoding='GBK') as csvfile:
    # 用csv.writer()函数创建一个writer对象。
    writer = csv.writer(csvfile,dialect='excel')
    # 定义表头信息
    header = ['名字','入学时间','班级','性别','年龄','语文成绩','数学成绩','英语成绩']
    # 用writerow()函数将表头写进csv文件里
    writer.writerow(header)
    while True:
        name = input('请输入学生名字:')
        s_time = input('请输入入学时间:')
        class_ = input('请输入班级:')
        gender = input('请输入性别:')
        age = int(input('请输入与年龄:'))
        c_score = input('请输入语文成绩:')
        m_score = input('请输入数学成绩:')
        e_score = input('请输入英语成绩:')
        all_student_list = [name, s_time, class_, gender, age, c_score, m_score, e_score]

        writer.writerow(all_student_list)
        s = input('如果退出请按q,继续请回车!')

        if s == 'q':
            break
