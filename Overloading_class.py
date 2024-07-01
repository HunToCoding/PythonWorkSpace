# 일반 유닛
class Unit :
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향 [속도 {2}]"\
              .format(self.name, location, self.speed))

# 공격 유닛
class Attackunit(Unit) :
     def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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

# 다중 상속
# Dropship Attack X

class Flyable(Unit):
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향 [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttack(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Attackunit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# # 벌쳐 : 지상, 기동성이 좋음
# Vulture = Attackunit("Vulture", 80, 10, 20)

# # 배틀 크루져 : 공중, 체력, 공격력
# BattleCruiser = FlyableAttack("BattleCruiser", 500, 25, 3)

# Vulture.move("11시")
# BattleCruiser.fly(BattleCruiser.name ,"9시")

# # Overloading
# BattleCruiser.move("9시")

# def game_start():
#     print("[알림] 새로운 게임")

# def game_over():
#     pass

# game_start()
# game_over()

# 서플라이 디폿 : 건물, 1개 건물 = 8인구
# supply_depot = Building("서플라이 디폿", 500, "7시")

# pass 아무것도 안하고 넘어간다 - 건물 만들기
# super()
class Building(Unit):
    def __init__(self, name, hp, location):
    # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location


