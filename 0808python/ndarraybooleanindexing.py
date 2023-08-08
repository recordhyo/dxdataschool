import numpy as np

print(bool([])) #False
print(bool([1,2,3])) #True


#boolean indexing : array의 인덱스에 bool 배열 대입해서 True 인 데이터만 골라내기
ar = np.array([1,2,3,4,5,6,7])

result = ar[[True, False, True, True, False, True, False]]
print(result)

br = np.array([10,20,30,40,50,60,70])
result = ar[br >= 50]
print(result)

#다중 조건들은 & | 으로 묶어야함 (and와 or는 안됨) 
result = ar[(br >= 30) & (br <=60)]
print(result)