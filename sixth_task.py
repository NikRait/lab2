print("Temperature converter. 1 - Celsius to Fahrenheit, 2 - Fahrenheit to Celsius")

choice = int(input())

if choice == 1:
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = celsius * 9/5 + 32 # Converting to fahrenheit
    print(f"{celsius:.1f}C = {fahrenheit:.1f}F") # :.1f means one number after comma
elif choice == 2:
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9 # Converting to celsius
    print(f"{fahrenheit:.1f}F = {celsius:.1f}C") 
else:
    print("Wrong value") # break if not 1 or 2