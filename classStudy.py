#마린 : 공격, 군인, 총
# name = "마린"
# Hp = 40
# damage = 5
# 
# print("{0} 유닛 생성".format(name))
# print("체력 {0}, 공격력 {1}".format(Hp, damage))
# 
#탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# 
# print("{0} 유닛 생성".format(tank_name))
# print("체력 {0}, 공격력 {1}".format(tank_hp, tank_damage))
# 
# def attack(name, location, damage):
    # print("{0} : {1} 방향 공격 [공격력 : {2}]".format(name, location, damage))
# 
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# __init__ - Python 생성자
class Unit :
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛 생성".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
Tank    = Unit("Tank", 150, 35)
wraith = Unit("Wraith", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith.name, wraith.damage))

wraith2 = Unit("Wraith2", 80, 5)
wraith2.Clocking = True

if wraith2.Clocking == True:
    print("{0} 클로킹 상태".format(wraith2.name))