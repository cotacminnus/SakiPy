import os
import random
import discord

SAKI_SOYO_0 = "真是会虚情假意呢"
SAKI_SOYO_1 = "想演奏是你们的自由，你们就请便吧"
SAKI_SOYO_2 = "到现在都还执着于过去，真难看"
SAKI_SOYO_3 = "你也差不多该忘记了吧"
SAKI_SOYO_4 = "那么那个乐团算什么"
SAKI_SOYO_5 = "你讲的话和做的事全都互相矛盾"
SAKI_SOYO_6 = "CRYCHIC已经毁了"
SAKI_SOYO_7 = "绝对不可能再复活了"
SAKI_SOYO_8 = "我已经亲手将它结束了"
SAKI_SOYO_9 = "没有人那样拜托你"
SAKI_SOYO_A = "这是最后的警告"
SAKI_SOYO_B = "今后不要再和我扯上关系了"
SAKI_SOYO_C = "你是抱着多大的觉悟说出这种话的"
SAKI_SOYO_D = "你只不过是一个学生，有办法背负其他人的人生吗"
SAKI_SOYO_E = "「什么都愿意做」就是这么沉重的话"
SAKI_SOYO_F = "做不来的事就别轻易说出口"
SAKI_SOYO_10=  "你这个人，满脑子都只想到自己呢"

SAKI_SOYO_123 = "想演奏是你们的自由，你们就请便吧\n到现在都还执着于过去，真难看\n你也差不多该忘记了吧"
SAKI_SOYO_45678 = "那么那个乐团算什么\n你讲的话和做的事全都互相矛盾\nCRYCHIC已经毁了\n绝对不可能再复活了\n我已经亲手将它结束了"
SAKI_SOYO_9AB = "没有人那样拜托你\n这是最后的警告\n今后不要再和我扯上关系了"
SAKI_SOYO_CDEF = "你是抱着多大的觉悟说出这种话的\n你只不过是一个学生，有办法背负其他人的人生吗\n「什么都愿意做」就是这么沉重的话\n做不来的事就别轻易说出口"

UNSEI_0 = "fusaki.png"
UNSEI_1 = "shousaki.png"
UNSEI_2 = "chusaki.png"
UNSEI_3 = "daisaki.png"
UNSEI_U = "亲，今天已经抽过签了呢。"

TOUSAKI_BENE = "投祥成功！"
TOUSAKI_MALE = "亲，今天已经投过祥了呢。祝你幸福。"

UNSEI = {UNSEI_0, UNSEI_1, UNSEI_2, UNSEI_3}

class Staff:
    local_dir = ""

    def __init__(self, dir):
        self.local_dir = dir
        #投不投祥？
        if os.path.isfile(self.local_dir + "tousaki.saki") == False:
            f = open(self.local_dir + "tousaki.saki", "x")
            f.close()
        #每日算命
        if os.path.isfile(self.local_dir + "unsei.saki") == False:
            f = open(self.local_dir + "unsei.saki", "x")
            f.close()

    def tousaki(self, user):
        with open(self.local_dir + "tousaki.saki", "a+") as t:
            if user.id in t.readlines():
              return TOUSAKI_MALE
            else:
                t.write(user.id + "\n")
        return TOUSAKI_BENE
    
    def unsei(self, user):
        with open(self.local_dir + "unsei.saki", "a+") as t:
            if user.id in t.readlines():
              return UNSEI_U
            else:
                t.write(user.id + "\n")
        return random.choice(UNSEI)