totalSeconds = int(input("Enter seconds: "))

hours = totalSeconds // 3600
minutes = (totalSeconds % 3600) // 60
seconds = totalSeconds % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}") # :02d makes it at least two numbers and replaces blank fields with zero
