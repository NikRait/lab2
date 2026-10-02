Number = 1234321
num = Number
count = 0
while num > 0:
    num //= 10
    count += 1
for i in range(count):
    first = Number // 10 ** (count - i - 1) # First digit
    sec = Number % 10 # Last digit
    Number -= first * 10 ** (count - i - 1) # Removing first digit
    Number //= 10 # Removing last digit
    count -= 1
    if first != sec:
        print("Не пaлиндром")
        break
else:
    print("Палиндром")

print("END")
