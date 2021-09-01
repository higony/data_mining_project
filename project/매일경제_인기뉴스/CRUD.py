# 스크래핑과 관련 없는, CRUD와 관련된 함수들

# 모든 기사 결과 출력
def news_print(li):
    for idx, elem in enumerate(li):
        print(f"{idx+1}) {elem[0]}")

        for k in range(len(elem[1])):
            print(f"  {k+1}. {elem[1][k]}")
            print(f"  링크: {elem[2][k]}")
            print()
        print("-"*50, end="\n\n")

# 1.0.1 즐겨찾기 추가 기능: 전체 언론사 나열 기능, 언론사 검색 알고리즘 구현
def favorite_add(press_list, filename):
    print("\n즐겨찾기 기능을 선택해주세요")
    while True:
        print("1. 전체 언론사 보기")
        print("2. 검색하기")
        print("0. 종료")
        selection = int(input("\n 기능선택 >>>>>> "))

        if selection == 0:
            break
        
        elif selection == 1:
            print("\n전체 언론사 목록입니다.\n")
            print(", ".join(press_list))
            selection = 2

        if selection == 2:
            result_list = []
            press = input("\n검색하고자 하는 언론사를 입력해주세요. ")
            
            for elem in press_list:
                if press in elem:
                    result_list.append(elem)
            
            if len(result_list) == 0:
                print("검색 결과가 없습니다.")
                continue
            
            print(f"총 {len(result_list)}개의 검색 결과가 있습니다.")
            for idx, elem in enumerate(result_list):
                print(f"{idx+1}. {elem}")
            print("\n추가하고자 하는 언론사의 번호를 입력해주세요.")
            selection = int(input("언론사 선택 >>>> "))

            try:
                with open(filename, "a") as f:
                    f.write(f"{result_list[selection-1]}\n")
                print("성공적으로 즐겨찾기에 저장되었습니다.")
            except:
                print("잘못된 번호를 입력하셨습니다.")
                continue

# 1.0.1 즐겨찾기 조회 기능
def favorite_read(filename):
    try:
        with open(filename, "r") as f:
            li = sorted(list(set(f.readlines())))
            if len(li) == 0:
                print("즐겨찾기한 언론사가 없습니다.\n")
            else:
                print("\n즐겨찾는 언론사 목록")
                for idx, elem in enumerate(li):
                    print(f"{idx+1}. {elem}", end="")
    except:
        print("즐겨찾기한 언론사가 없거나, 파일이 손상되었습니다..\n")

# 1.0.1 즐겨찾기 삭제 기능
def favorite_delete(filename):
    try:
        with open(filename, "r") as f:
            li = sorted(list(set(f.readlines())))
        while True:
            if len(li) == 0:
                print("현재 즐겨찾기 목록이 없습니다.")
                break

            print("현재 즐겨찾기 한 언론사 목록입니다.")
            for idx, elem in enumerate(li):
                print(f"{idx+1}. {elem}", end="")
            selection = int(input("\n삭제를 원하시는 언론사의 번호를 입력해주세요. 종료를 원하시면 0을 입력해주세요. : "))
            if selection == 0:
                break
            print(f"{li[selection-1]} 언론사를 즐겨찾기에서 제외합니다.")
            del li[selection-1]

        with open(filename, "w") as f:
            for elem in li:
                f.write(f"{elem}\n")
            print("즐겨찾기 수정이 반영되었습니다.\n")
    except:
        print("즐겨찾기한 언론사가 없거나, 잘못된 입력을 하셨습니다.\n")