from decimal import Decimal

#실수 표현의 한계로 연산 결과가 다르게 나옴
print((Decimal('1234.567') + Decimal('45.67844')) + Decimal('0.0004'))
print(Decimal('1234.567') + (Decimal('45.67844') + Decimal('0.0004')))