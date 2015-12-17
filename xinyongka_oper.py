def judge():
    op_file = open("use_information.txt",'r+')
    op_read = op_file.read()
    user_input = input("请输入用户名：")
    while user_input not in op_read:
        print("输入的用户不存在，请重新输入！")
        user_input = input("请输入用户名：")
judge()
