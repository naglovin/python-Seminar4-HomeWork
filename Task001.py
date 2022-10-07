# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988
from decimal import Decimal                    # из модуля десимал берем десимал)
def accuracu (a, b):
    num = Decimal(f"{a}")                      # (f"{a}")  форматирование в строку
    return num.quantize(Decimal(f"{b}"))
print(accuracu(8.98785, 0.001))




