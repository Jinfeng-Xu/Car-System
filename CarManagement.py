class Carsselling(object):
    def __init__(self):
        self.cars = []

    # 菜单
    def print_menu(self):
        print("**************************************************** \
              \n----------------○ 汽车销售系统v1.0 ○--------------------- \
              \n\t\t● 1录入汽车信息\t● 2显示汽车信息 \
               \n\t\t● 3销售汽车\t\t● 4修改汽车信息 \
               \n\t\t● 5销售数据\t\t● 6退出系统 \
              \n*****************************************************")

    # 登录
    def login(self):
        user = []
        while True:
            print("========汽车销售系统=======")
            print("--------1.用户登录--------")
            print("--------2.用户注册-------")
            print("--------3.退出-----------")
            num = input("请输入你想要的功能：")
            if num == "1":
                f = open("E:\\汽车管理\\注册信息.txt", "a+")
                f.seek(0)
                a = f.read()
                f.close()
                name = input("请输入用户名：")
                pwd = input("请输入密码：")
                number = []
                number.extend([name, pwd])

                if str(number) == a:
                    print("登录成功！")
                    self.print_menu()
                    self.option()
                    break

                else:
                    print("登录失败！请重新输入密码！")


            elif num == "2":

                username = input("请输入用户名：")
                password = input("请输入密码")
                user.extend([username, password])
                file = open("E:\\汽车管理\\注册信息.txt", "w")
                file.write(str(user))
                file.close()
                print("注册成功！")

            elif num == "3":
                print("谢谢使用本系统，再见！")
                break

    # 录入汽车信息
    def car_add(self):
        while 1:
            car = {}
            num = input("请输入汽车的编号")
            name = input("请输入汽车的商标")
            address = input("请输入汽车的产地")
            price = input("请输入汽车的价格")
            car["num"] = num
            car["name"] = name
            car["address"] = address
            car["price"] = price
            self.cars.append(car)
            a = input("是否继续添加？输入y/n")
            if a == "n":
                print("录入成功")
                break
            elif a == "y":
                print("录入成功,请继续录入")
        self.save_info()  # 保存录入的信息

    # 显示汽车信息
    def car_display(self):

        print("\t\t\t\t当前车辆库存信息\n" + \
              "-" * 80 + "\n\t编   号\t\t商   标\t\t产   地\t\t价   格")
        for car in self.cars:
            print("\t  " + car["num"] + \
                  "\t\t\t" + car["name"] + \
                  "\t\t" + car["address"] + \
                  "\t\t" + car["price"]
                  )

        print("-" * 80, "\n")

    # 销售汽车
    def car_del(self):
        self.car_display()  # 先显示出库存车辆信息
        num = input("请输入要销售的车辆编号：")
        for car in self.cars:
            if num == car.get("num"):
                f = open("E:\\汽车管理\\销售数据.txt", "a+")
                f.write("\t车辆编号:" + str(car["num"]) + "\t" + \
                        "商标:" + str(car["name"]) + "\t" + \
                        "产地:" + str(car["address"]) + "\t" + \
                        "价格:" + str(car["price"]) + "\n")  # 保存
                f.close()  # 关闭资源
                self.cars.remove(car)
        self.car_display()  # 显示销售后的车辆库存信息
        print("此车已出售!")
        self.save_info()  # 保存销售汽车的信息

    # 修改汽车信息
    def car_modify(self):
        self.car_display()  # 显示修改前的车辆库存信息
        num = input("请输入想要修改的车辆信息所对应的编号")
        for car in self.cars:
            if num == car.get("num"):
                print("此车的车辆信息如下:\n-----------------------")
                print("编号:" + car["num"] + \
                      "商标:" + car["name"] + \
                      "产地:" + car["address"] + \
                      "价格:" + car["price"])
        new_num = input("请输入新的编号")
        car["num"] = new_num
        new_name = input("请输入新的商标")
        car["name"] = new_name
        new_address = input("请输入新的产地")
        car["address"] = new_address
        new_price = input("请输入新的价格")
        car["price"] = new_price
        print("修改信息成功！")
        self.save_info()  # 保存到车辆库存信息

    # 销售数据
    def car_sell(self):
        print("------------车辆销售数据------------")
        fo = open("E:\\汽车管理\\销售数据.txt", "a+")
        fo.seek(0)
        for line in fo:
            print(line)

    # 文件保存
    def save_info(self):
        f = open("E:\\汽车管理\\车辆库存信息.txt", "w")
        f.write(str(self.cars))  # 保存
        f.close()  # 关闭资源

    # 文件读取
    def load_info(self):
        fp = open("E:\\汽车管理\\车辆库存信息.txt", "a+")
        fp.seek(0)
        content = fp.read()
        if len(content) > 0:
            self.cars = eval(content)
        fp.close()  # 关闭资源

    # 操作指令
    def option(self):
        self.load_info()  # 在本地读取车辆库存信息
        while True:
            print("\n\t\t操作指令\n" + \
                  "~" * 50 + \
                  "\n 1：录入信息|2：显示信息|3：销售汽车|4：修改信息|5：销售数据|6：退出 \n" + \
                  "~" * 50)
            # 输入的内容都当做字符串
            input_num = input("请按照提示输入相应的指令：")

            # 判断用户输入的内容
            if input_num == "1":

                self.car_add()
            elif input_num == "2":

                self.car_display()
            elif input_num == "3":

                self.car_del()
            elif input_num == "4":

                self.car_modify()
            elif input_num == "5":

                self.car_sell()
            elif input_num == "6":
                print("感谢您使用本系统，再见！\n")
                break
            else:
                print("请不要瞎玩,这里需要输入对应的数字！\n")

    # 入口函数
    def main(self):
        self.login()

        # 创建实例对象，调用方法


car = Carsselling()
car.main()
