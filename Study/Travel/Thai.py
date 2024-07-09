class ThaiPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
    print("Thai Module 직접 실행")
    print("이 문장은 모듈 직접 실행 할때만 실행 됨")
    trip_to = ThaiPackage()
    trip_to.detail()
else:
    print("Thai 모듈 외부 호출 ")