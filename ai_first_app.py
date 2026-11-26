from datetime import datetime

name = input("Як тебе звати? ")
hour = datetime.now().hour

if hour < 12:
	greeting = "Доброго ранку"
elif hour < 18:
	greeting = "Доброго дня"
else:
	greeting = "Доброго вечора"

print(f"{greeting}, {name}! Ласкаво просимо у світ Python 🐍")
