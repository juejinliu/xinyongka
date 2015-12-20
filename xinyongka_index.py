from operation import Operation
import os
print(os.getcwd())

user = input("请输入用户名：")
passwd = input("请输入密码：")
while user != 'wpf' or passwd != '123456':
    print("用户名或密码错误，请重新输入！")
    user = input("请输入用户名：")
    passwd = input("请输入密码：")
user_info = open("use_information.txt", 'r', encoding='utf8').readlines()
for user in user_info:
    print(user.strip('\n'))
operation_dict = {'s':"查询", 'a':"添加", 'd':"删除"}
for d, x in operation_dict.items():
    print(d+"->"+x)
def judge(user_input):
    op_file = open("use_information.txt", 'r+', encoding='utf8')
    op_read = op_file.read()
    # user_input = input("请输入用户名：")
    while user_input not in op_read:
        print("输入的用户不存在，请重新输入！")
        user_input = input("请输入用户名：")
a = input("请选择功能：")
while a == 's':
    user_input = input("输入用户名：")
    judge(user_input)
    get = Operation()
    get_info = get.get_user(user_input)
    for i in range(len(get_info)):
        print(get_info[i])
    print('a->还款')

