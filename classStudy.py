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
# 
# marine1 = Unit("Marine", 40, 5)
# marine2 = Unit("Marine", 40, 5)
# Tank    = Unit("Tank", 150, 35)
# wraith = Unit("Wraith", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith.name, wraith.damage))
# 
# wraith2 = Unit("Wraith2", 80, 5)
# wraith2.Clocking = True
# 
# if wraith2.Clocking == True:
    # print("{0} 클로킹 상태".format(wraith2.name))

# __init__ - Python 생성자

# 일반 유닛
class Unit :
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class Attackunit(Unit) :
     def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

     def attack(self, location) :   
        print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]"\
              .format(self.name, location, self.damage))
    
     def damaged(self, damage):
         print("{0} : {1} damaged".format(self.name, damage))
         self.hp -= damage
         print("{0} : {1} ".format(self.name, self.hp))
         if self.hp <= 0:
             print("{0} : 파괴".format(self.name))

# Medi

# 파이어뱃
firebat1 = Attackunit("FireMat", 50, 16)
firebat1.attack("5시")

# 공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속
# Dropship Attack X

class Flyable(Unit):
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향 [속도 : {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttack(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Attackunit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
