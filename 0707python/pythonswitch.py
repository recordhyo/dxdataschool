#0일1월2화3수4목5금6토

switch = {
    0 : "일요일",
    1 : "월요일",
    2 : "화요일",
    3 : "수요일",
    4 : "목요일",
    5 : "금요일",
    6 : "토요일"
}

print(switch.get(3, "알 수 없는 요일"))
#get은 일치하는 키 있으면 그 값을 가져오고
#없으면 두번째 매개변수의 값을 리턴 -> default 처럼 사용 가능