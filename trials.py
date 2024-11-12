# name = input("What is your name?\n")
# color = input("What is your favorite color?\n")

# print("Hello %s, your favorite color, %s, is awesome!"% (name, color))

# print(f"Hello {name} and your color is {color}")

# numbers = [10, 15, 17, 25]

# numbers.append(40)
# print(numbers)

# even_numbers = [2, 4, 6, 8]
# numbers.extend(even_numbers)
# print("This is the full list: ", numbers)

# languages = ['English', 'Python', 'Java']

# languages[1] = 'Html'

# print(languages)

# for language in languages:
#     print(language)

# This prints up  the square of numbers from 1 to 5
# numbers = [number*number for number in range(1,6)]
# print(numbers)

# numbers = {1 : 'one', 2 : 'two'}
# print(numbers)

capital_city = {"Kenya": "Nairobi", "Uganda": "Kampala"}

print("Initial dictionaries: ", capital_city)

capital_city["Tanzania"] = "Dar es Salaam"

print("Updated dictionaries: ", capital_city)

print(capital_city["Uganda"])