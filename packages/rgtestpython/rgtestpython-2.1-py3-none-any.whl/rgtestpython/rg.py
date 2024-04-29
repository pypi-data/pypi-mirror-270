# coding=utf-8
import sys
import time


class Cmsg:

    login_menu='''
        ---菜单调用演示--
             1.登录
             2.查询
             3.修改
             4.删除
             0.退出
        ---结束演示请输入0-
        '''


    def login(self):
        print("您已经进入登录模块！")
        time.sleep(1) # 此行代码，为了演示，暂停了1秒，
                      # 实际调用，应该删除此行代码

    def query(self):
        print("您已经进入查询模块！")
        time.sleep(1) # 此行代码，为了演示，暂停了1秒，
                      # 实际调用，应该删除此行代码

    def modify(self):
        print("您已经进入修改模块！")
        time.sleep(1) # 此行代码，为了演示，暂停了1秒，
                      # 实际调用，应该删除此行代码

    def dele(self):
        print("您已经进入删除模块！")
        time.sleep(1) # 此行代码，为了演示，暂停了1秒，
                      # 实际调用，应该删除此行代码

    def exit1(self):
        sys.exit()

    login_choice={"1":login,"2":query,"3":modify,"4":dele,"0":exit1}

    # @classmethod
    def choice(self):
        while True:
            ch=input(Cmsg.login_menu+"\n请输入功能号（0-4）：")
            if ch in Cmsg.login_choice:
                # print(ch,type(ch))
                # print(login_choice,type(login_choice))
                # print(login_choice[ch],type(login_choice[ch]))
                # print(Cmsg.login_choice)
                Cmsg.login_choice[ch](self)
            else:
                print("输入错误，请输入，退出请输入0!")

    @classmethod
    def view(cls,msg):
        print(f'你想显示的信息是:{msg}')


# c1=Cmsg()
# c1.choice()