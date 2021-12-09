class Car:
    ##field属性定义
    name:str
    id:str
    year:str
    age:str
    area:str

    ##初始化信息
    def __init__(self,name:str,id:str,year:str,
    age:str,area:str):
        self.name=name
        self.id=id
        self.year=year
        self.age=age
        self.area=area


class CarSystem:
    ##信息以字典的形式储存
    data:dict={}


    #欢迎界面
    def welcome(self):
        print(
        '''
        *********欢迎使用车辆信息管理系统**********
                    1.添加信息
                    2.查询信息
                    3.删除信息
                    4.修改信息
                    5.退出系统
        ****************************************
        '''
        )


    #1.添加信息
    def addInfo(self):
        ##输入信息
        name: str=input('请输入车名: ')
        id: str=input('请输入编号: ')
        year: str=input('请输入年份: ')
        age: str=input('请输入车龄: ')
        area: str=input('请输入产地: ')
        car = self.data.get(id)
        if car == None:
            newCar = Car(name, id, year, age, area)
            self.data.update({id: newCar})
            print('添加成功！^_^')
            return newCar
        else:
            print('添加失败，该编号车辆已存在！')

    #2.查询信息
    def selectInfo(self):
        print(self.data)
        while True:
            try:
                id: str = input('请输入编号: ')
                car:Car=self.data.get(id)
                print('车名:',car.name)
                print('编号:', car.id)
                print('年份:', car.year)
                print('车龄:', car.age)
                print('产地:', car.area)
            except:
                print('您输入的车辆不存在！')
            else:
                return car

    #3.删除信息
    def delInfo(self):
        id: str = input('请输入编号: ')
        car: Car = self.data.get(id)
        if car==None:
            print('您输入的车辆本来就不存在！')
        else:
            self.data.pop(id)
            print('删除成功')

    def updateInfo(self):
        car=self.selectInfo()
        print('1.修改车名 2.修改编号 3.修改年份 4.修改车龄 5.修改产地 6.退出')
        while 1:
            select=input('请输入选项: ')
            if select.__eq__('1'):
                str = input('修改为: ')
                car.name = str
                self.data.update({car.id:car})
                print('修改成功')
                break
            elif select.__eq__('2'):
                self.data.pop(car.id)
                str = input('修改为: ')
                car.id = str
                self.data.update({car.id: car})
                print('修改成功')
                break
            elif select.__eq__('3'):
                str = input('修改为: ')
                car.year = str
                self.data.update({car.id: car})
                print('修改成功')
                break
            elif select.__eq__('4'):
                str = input('修改为: ')
                car.age = str
                self.data.update({car.id: car})
                print('修改成功')
                break
            elif select.__eq__('5'):
                str = input('修改为: ')
                car.area = str
                self.data.update({car.id: car})
                print('修改成功')
                break
            elif select.__eq__('6'):
                break
            else:
                print('您输入有误！')




    def run(self):
        while 1:
            self.welcome()
            select=input('请输入选项: ')
            if select.__eq__('1'):
                self.addInfo()
            elif select.__eq__('2'):
                self.selectInfo()
            elif select.__eq__('3'):
                self.delInfo()
            elif select.__eq__('4'):
                self.updateInfo()
            elif select.__eq__('5'):
                break
            else:
                print('您输入有误！')


carSystem = CarSystem()
carSystem.run()

