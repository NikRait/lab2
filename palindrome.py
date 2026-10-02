Number = int(input())
num = Number
count = 0
while num > 0:
    num //= 10
    count += 1
for i in range(1, count, 2):
    first = Number // 10 ** (count - i)  # First digit
    sec = Number % 10  # Last digit
    Number -= first * 10 ** (count - i)  # Removing first digit
    Number //= 10  # Removing last digit
    if first != sec:
        print("Не пaлиндром")
        break
else:
    print("Палиндром")

print("END")
