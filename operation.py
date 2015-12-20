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

if __name__ == '__main__':
    get = Operation()
    get.get_user('王鹏飞')
    print('a->还款')
