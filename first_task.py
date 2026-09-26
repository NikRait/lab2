# Input
integer = int(input("Enter integer: "))
decimal = float(input("Enter decimal: "))
text = input("Enter string: ")

# Output
print(f"Number: {integer}, type: {type(integer).__name__}")
print(f"Number: {decimal}, type: {type(decimal).__name__}")
print(f"Text: {text}, type: {type(text).__name__}")
