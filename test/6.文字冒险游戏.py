# 尽量参考回合制RPG游戏的模式，游戏剧情自编，要有战斗模式，主角有HP属性，战斗和吃东西会对HP有相应的增减效果。
import time
import random


class Person:
    def __init__(self, name, level, school=1):
        self.name = name
        self.level = level
        self.school = school


class Protagonist(Person):
    # equipment=[武器，防具]
    # items=[金币，药剂，，]
    # state=[血量，攻击，防御%]
    def __init__(self, name, level, school, equipment, items):
        self.state = []
        Person.__init__(self, name, level, school)
        self.equipment = equipment
        self.items = items
        self.state.append(int(self.level * 10))
        self.state.append(int(self.level * 2 + self.equipment[0]))
        self.state.append(1 - (1 / (self.level + self.equipment[1]) ** (1 / 4)))

    def update(self):
        self.state[0] = (int(self.level * 10))
        self.state[1] = (int(self.level * 5 + self.equipment[0]))
        self.state[2] = (1 - (1 / (self.level + self.equipment[1]) ** (1 / 4)))


class Enemy(Person):
    # items=[金币，药剂，武器掉落，防具掉落]
    # state=[血量，攻击，防御%]
    def __init__(self, name, level, school):
        Person.__init__(self, name, level, school)
        self.state = []
        self.items = []
        self.state.append(self.level * 10)
        self.state.append(self.level * 3)
        self.state.append(1 - (1 / (self.level) ** (1 / 4)))
        self.items.append(int(self.level * 0.5 * (random.randint(1, 9))))
        self.items.append(random.randint(1, 2))
        self.items.append(int(self.level * 0.5 * (random.randint(0, 5))))
        self.items.append(int(self.level * 0.5 * (random.randint(0, 5))))


def Fight(Protagonist, Enemy):
    print('敌人%s出现,等级%s' % (Enemy.name, Enemy.level))
    DefenseTemp = Protagonist.state[2]
    BloodTemp = Protagonist.state[0]
    while (Protagonist.state[0] > 0 and Enemy.state[0] > 0):
        action = input('选择你的动作:1.攻击.2.防御.3.喝药.4.逃跑.')
        if action == '1' or action == '':
            Enemy.state[0] = (int(Enemy.state[0] - (Protagonist.state[1] * (1 - Enemy.state[2]))))
            print('敌人血量剩余%d' % (Enemy.state[0]))
        elif action == '2':
            DefenseTemp = DefenseTemp * 1.2
            if DefenseTemp > 0.95:
                DefenseTemp = 0.95
        elif action == '3':
            if Protagonist.items[1] > 0:
                Protagonist.state[0] = Protagonist.state[0] + BloodTemp * 0.2
                print('你的血量剩余%d' % (Protagonist.state[0]))
            else:
                print('没药了')
        else:
            if (random.randint(0, 10)) > 5:
                Protagonist.update()
                print('逃跑成功')
                return 1
            else:
                print('逃跑失败')
        if Enemy.state[0] > 0:
            print('你的敌人出手了')
            Protagonist.state[0] = int(Protagonist.state[0] - (Enemy.state[1] * (1 - DefenseTemp)))
            DefenseTemp = Protagonist.state[2]
            time.sleep(0.5)
            print('你的血量剩余%d' % (Protagonist.state[0]))
        else:
            print('你的敌人已阵亡')
            time.sleep(0.5)
    print('战斗结束')
    if Protagonist.state[0] > 0:
        Protagonist.level += (Enemy.level * 0.1)  # 等级增长
        print('你的当前等级:', Protagonist.level)
        Protagonist.items[0] += Enemy.items[0]  # 金币掉落
        print('你的当前金币:', Protagonist.items[0])
        Protagonist.items[1] += Enemy.items[1]  # 药剂掉落
        print('你的当前药剂数:', Protagonist.items[1])
        if Enemy.items[2] > Protagonist.equipment[0]:
            Protagonist.equipment[0] = Enemy.items[2]
            print('你的武器提升为：', Protagonist.equipment[0])
        if Enemy.items[3] > Protagonist.equipment[1]:
            Protagonist.equipment[1] = Enemy.items[3]
            print('你的防具提升为：', Protagonist.equipment[1])
        Protagonist.update()
        return 1
    else:
        print('大侠请重新来过')
        return 2


a = Protagonist('lin', 10, 1, [10, 10], [35, 10])
b = Enemy('chen', 10, 1)
c = Enemy('hen', 13, 1)

Fight(a, b)
Fight(a, c)








