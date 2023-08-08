import numpy as np

#random
np.random.seed(seed=42) #seed를 고정

cards = np.array(range(1,49))

#배열을 섞어서 리턴을 함 
result = np.random.permutation(cards) 
print(result)

np.random.shuffle(cards) #카드를 바꿈
print(cards)


# ------------------------------------------------------

# 기본 통계 함수
matrix = np.array([[10,20],[30,40],[50,60]])

print(matrix.sum())
print(matrix.std()) #표준 편차
print(matrix.std(ddof=1)) #표준 편차 - 자유도 1적용
print(np.percentile(matrix,75)) #75프로에 해당하는 값

#행단위와 열단위 통계
print(matrix.sum(axis=0)) #열단위
print(matrix.sum(axis=1)) #행단위
print(matrix.sum(axis=1, keepdims=True)) #matrix와 동일 차원으로 리턴 