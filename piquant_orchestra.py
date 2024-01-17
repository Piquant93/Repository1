"""
> 변경점
1. 변수로 연주회 목록과 좌석 목록을 만들고
2. 관람할 연주회 목록을 확인 후 입력 값 받기
3. 관람할 연주회에 대한 좌석 목록 확인 후 입력 값 받기
--------------------------------------------
1. 클래스 내 메서드 매개 변수를 만들고
2. 그에 맞는 연주회 & 좌석 목록을 만들고
3. 입력 값 받은 후 입력 받은 값 확인.

스토리 설명(= orchestra)
1. 오케스트라(실내악) 종류 입력 받기
 > 연주회 목록 - [1. Brass_quintet 2. Symphony_student 3. Symphony_master]
2. 좌석 종류 입력 받기 
 > 좌석 목록 - ['4. 200,000 & A열', '5. 300,000 & S석', '6. 400,000 & VIP석', '7. 500,000 & VVIP석']
3. 오케스트라(실내악) 종류 + 좌석 종류 != 다시 입력 받기)
"""

import pickle
# 클래스
# 오케스트라의 값을 리턴받은 Brass/Symphony라는 객체
# Brass / Symphony 객체는 오케스트라의 인스턴스이다.
class Orchestra: # 오케스트라라는 클래스
    def __init__(self, type): # 메서드의 매개변수
        self.type = type
        self.type_all = [] # 저장

    def create_seat(self, seat):
        self.type_all.append(seat) # 뒤에 추가 저장

def select_seat(orchestra_type, type_all):
    print()
    print("============================================================================================================")
    print(type_all)
    print("============================================================================================================")
    print()

    seat1 = input("좌석을 선택해주세요. >>> ")
    seat1 = int(seat1)
    while True:

        if 4 <= seat1 <= 7:
            print("{0} 연주회 & {1} 관람석 선택되었습니다. :D".format(orchestra_type, seat1))
            print()
            break
        else:
            seat1 = int(input(">>> 관람석을 다시 선택해주세요. 선택 가능한 번호는 '4 ~ 7'입니다. >>>> "))
            print()
            print("-> 선택한 관람석은 '{0}'입니다.".format(seat1))

# 클래스에 오케스트라 타입 저장
orchestra_type1 = Orchestra("1. Brass_quintet > 금관 5중주")
orchestra_type2 = Orchestra("2. Symphony_student > 학생 오케스트라")
orchestra_type3 = Orchestra("3. Symphony_master > 마스터 오케스트라")
# 클래스 > 오케스트라 타입 별 좌석과 금액 저장
orchestra_type1.create_seat("4. A열 & 200,000 // ")
orchestra_type1.create_seat("5. S석 & 300,000 // ")
orchestra_type1.create_seat("6. VIP석 & 400,000 // ")
orchestra_type1.create_seat("7. VVIP석 & 500,000")

orchestra_type2.create_seat("4. A열 & 200,000 // ")
orchestra_type2.create_seat("5. S석 & 300,000 // ")
orchestra_type2.create_seat("6. VIP석 & 400,000 // ")
orchestra_type2.create_seat("7. VVIP석 & 500,000")

orchestra_type3.create_seat("4. A열 & 200,000 // ")
orchestra_type3.create_seat("5. S석 & 300,000 // ")
orchestra_type3.create_seat("6. VIP석 & 400,000 // ")
orchestra_type3.create_seat("7. VVIP석 & 500,000")

# o_type_all 저장소에 클래스 내 저장된 오케스트라 타입을 리스트로 저장
o_type_all = [orchestra_type1, orchestra_type2, orchestra_type3]

print()
print("관람 가능한 연주회를 확인해주세요.")
print()
print("=======================================")
print(orchestra_type1.type)
print(orchestra_type2.type)
print(orchestra_type3.type)
print("=======================================")
print()


o_type1 = input("오케스트라(실내악) 목록을 확인 후 관람권을 선택해주세요. > ")
o_type1 = int(o_type1)
 
if 1 <= o_type1 <= 3:
    selected_orchestra = o_type_all[o_type1 -1]
    seat_type1 = select_seat(selected_orchestra.type, selected_orchestra.type_all)
else:
    print("ㄴ 선택 가능한 연주회는 '1 ~ 3'입니다.")
    print()
    retry = 1
    while True:
        retry = retry + 1
        input_text = input(">> 연주회 선택을 종료합니다.(Y/N)? ")
        print()
        if input_text in ["Y", "y", "ㅛ"]:
            print("[End] 관람권 선택을 종료합니다.")
            break
        else:
            print()
            print("연주회 선택을 다시 시작합니다.")
            o_type2 = input("[Retry] 오케스트라(실내악) 관람권 선택을 다시 시작합니다. 관람권을 선택해주세요. >>>>> ")
            o_type2 = int(o_type2)
            if 1 <= o_type2 <= 3:
                selected_orchestra = o_type_all[o_type2 -1] # -1 값을 넣은 이유는 o_type1을 불러오기 위해서(=저장된 오케스트라에서 불러오려고 사용)
                seat_type1 = select_seat(selected_orchestra.type, selected_orchestra.type_all)
            else:
                print("{0}회 선택 잘못하였습니다. 연주회 선택을 종료합니다.".format(retry))
        break