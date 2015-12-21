class Operation:
    def get_user(self, user_name):
        self.user_neme = user_name
        get_file = open('user_consumption.txt', encoding='utf8')
        get_read = get_file.readlines()
        count_line = []
        for line in get_read:
            if self.user_neme in line:
                count_line.append(line.strip('\n'))
                # print(line)
        get_edu = count_line[len(count_line) - 1].split()
        get_pay = int(get_edu[1]) - int(get_edu[2])
        print("总额度：%s    应还款：%d" % (get_edu[1], get_pay))
        print(get_read[0].strip('\n'))
        for i in range(len(count_line)):
            return count_line
            # print(count_line[i])
    def user_pay(self, user_name):
        self.user_neme = user_name
        get_file = open('user_consumption.txt', 'r+', encoding='utf8')
        get_read = get_file.readlines()
        count_line = []
        for line in get_read:
            if self.user_neme in line:
                count_line.append(line.strip('\n'))
        get_edu = count_line[len(count_line) - 1].split()
        get_pay = int(get_edu[1]) - int(get_edu[2])
        if get_pay == 0:
            shuru = "没有要还的款"
            return shuru
        else:
            print("你用还款的金额为%d" % get_pay)
            user_input_pay = int(input("输入要还款的金额："))
            while user_input_pay > get_pay:
                print('输入的金额大于应还款金额，请重新输入！')
                user_input_pay = int(input("输入要还款的金额："))
            else:
                get_edu[-2] = '-'+str(user_input_pay)
                get_edu[2] = int(get_edu[2]) + user_input_pay
                print(get_edu)
                get_str = ' '.join(get_edu)
                # print(type(get_edu))
                print(get_str)
                n = '\t'
                new_user = n.join(str(get_edu))
                print(new_user)
                # get_file.write(new_user)
                # get_file.close()

if __name__ == '__main__':
    get = Operation()
    get.user_pay('王鹏飞')
    # print('a->还款')
