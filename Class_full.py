# from random import *

# # 일반 유닛
# class Unit :
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향 [속도 {2}]"\
#               .format(self.name, location, self.speed))

#     def damaged(self, damage):
#          print("{0} : {1} damaged".format(self.name, damage))
#          self.hp -= damage
#          print("{0} : {1} ".format(self.name, self.hp))
#          if self.hp <= 0:
#              print("{0} : 파괴".format(self.name))


# # 공격 유닛
# class Attackunit(Unit) :
#      def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#      def attack(self, location) :   
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]"\
#               .format(self.name, location, self.damage))

# # 마린
# class Marine(Attackunit):
#     def __init__(self):
#         Attackunit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10 :
#             self.hp -= 10
#             print("{0} : 스팀팩 사용 [체력 {1}]".format(self.name, self.hp))
#         else :
#             print("{0} : 체력 부족".format(self.name))

# # Tank
# class Tank(Attackunit):
#     seize_dev = False;

#     def __init__(self):
#         Attackunit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_dev == False :
#             return
        
#         if self.seize_dev == False:
#             print("{0} : 시즈 모드".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈 모드 해제".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# # 다중 상속
# # Dropship Attack X

# class Flyable(Unit):
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향 [속도 {2}]"\
#               .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttack(Attackunit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         Attackunit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # Wraith
# class Wraith(FlyableAttack):
#     def __init__(self):
#         FlyableAttack.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드".format(self.name))
#             self.clocked = True

# def game_Start():
#     print("[알림] 새로운 게임")
# def game_over():
#     print("Player : GG")
#     print("[Player] 님이 퇴장")

# game_Start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# # 유닛 일괄 관리
# attack_unit = []
# attack_unit.append(m1)
# attack_unit.append(m2)
# attack_unit.append(m3)
# attack_unit.append(t1)
# attack_unit.append(t2)
# attack_unit.append(w1)

# # 유닛 전체 이동
# for unit in attack_unit:
#     unit.move("1시")

# # Tank SeizeMode
# Tank.seize_dev = True
# print("[알림] 탱크 시즈 모드 개발 완료")

# # 공격 준비
# for unit in attack_unit:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 피해
# for unit in attack_unit:
#     unit.damaged(randint(5, 21))

# # 게임 종료
# game_over()

# Quiz 
class House:
    def __init__(self, location, house_type, deal_type, price, completion):
        self.location = location
        self.house_type = house_type
        self.dealtype = deal_type
        self.price = price
        self.completion = completion

    def Show_detail(self):
        print(self.location, self.house_type, self.dealtype\
              ,self.price, self.completion)

house = []
h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

house.append(h1)
house.append(h2)
house.append(h3)

print("총 {0} 대의 매물이 있습니다.".format(len(house)))

for home in house:
    home.Show_detail()


